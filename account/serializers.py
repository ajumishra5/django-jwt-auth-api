from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

     # This field is for confirming the password during registration
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'password2', 'tc')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        # Validate that the two password fields match
    def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password != password2:
                raise serializers.ValidationError("Passwords and confirm password does not match.")
            return attrs
        
    def create(self, validated_data):
            return User.objects.create_user(**validated_data)
        

class UserLoginSerializer(serializers.ModelSerializer):
      email = serializers.EmailField(max_length=255)
      class Meta:
        model = User
        fields = ('email', 'password')
            