# 🔐 Django JWT Authentication API

A production-ready authentication API built using **Django**, **Django REST Framework**, and **JWT (SimpleJWT)**.

This project implements a fully custom user model with email-based authentication, secure JWT login, and password reset via email.

---

## 🚀 Features

- ✅ Custom User Model (Email as username)
- ✅ User Registration API
- ✅ JWT Login (Access + Refresh Tokens)
- ✅ Protected Profile Endpoint
- ✅ Password Reset via Email (Token-based)
- ✅ Gmail SMTP Integration
- ✅ Admin Panel Support

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT
- Gmail SMTP

---

## 📌 API Endpoints

### 🔹 Register User
```
POST /api/user/register/
```

### 🔹 Login User (JWT)
```
POST /api/user/login/
```

### 🔹 Refresh Token
```
POST /api/user/token/refresh/
```

### 🔹 Get Profile (Protected)
```
GET /api/user/profile/
Authorization: Bearer <access_token>
```

### 🔹 Send Password Reset Email
```
POST /api/user/send-reset-password-email/
```

### 🔹 Reset Password
```
POST /api/user/reset-password/<uid>/<token>/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ajumishra5/django-jwt-auth-api.git
cd django-jwt-auth-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables (.env)

Create a `.env` file:

```
EMAIL_USER=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

### 6️⃣ Start Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication Flow

1. User registers
2. User logs in → receives JWT access & refresh tokens
3. Access token used to access protected routes
4. Password reset uses Django token generator + uid encoding

---

## 🧠 Key Learning Outcomes

- Implemented a fully custom user model using `AbstractBaseUser`
- Overrode serializer `create()` method for secure password handling
- Implemented token-based authentication
- Integrated SMTP email system
- Debugged real-world email delivery issues

---

## 📂 Project Structure

```
account/
config/
manage.py
```

---

## 📈 Future Improvements

- Docker Support
- PostgreSQL integration
- Token Blacklisting
- HTML Email Templates
- Unit Tests

---

## 👨‍💻 Author

Ajay Mishra  
Backend Developer | Django & DRF  
Open to backend opportunities

GitHub: https://github.com/ajumishra5
