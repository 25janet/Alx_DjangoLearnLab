## 📌 Overview
This project is part of the **Alx Django Learn Lab** and implements a **secure authentication system** using Django's built-in authentication framework.  
It includes functionality for **user registration**, **login**, **logout**, and **profile management** with security best practices such as CSRF protection and password hashing.

---

## ⚙️ Features
- **Register** new users with hashed passwords.
- **Log in** using Django's `authenticate()` function.
- **Log out** securely and end user sessions.
- **Profile management** for authenticated users.
- **CSRF protection** for all POST requests.
- **Access control** to restrict profile and sensitive pages.

---

## 🔗 URLs
| Path                  | Description             | View Function   |
|-----------------------|-------------------------|-----------------|
| `/users/register/`    | Register a new account | `register_view` |
| `/users/login/`       | Log in to the system   | `login_view`    |
| `/users/logout/`      | Log out                | `logout_view`   |
| `/users/profile/`     | View/Edit profile      | `profile_view`  |

---

## 🛠️ How It Works
1. **Registration**
   - User fills in username, email, and password.
   - Password is hashed automatically by Django.
2. **Login**
   - Credentials are validated using `authenticate()`.
   - Django session is created on success.
3. **Logout**
   - Ends user session securely.
4. **Profile**
   - Authenticated users can view and update their details.
   - Protected with `@login_required`.

---

## 🔒 Security
- **Password Hashing** – Uses Django’s built-in secure password storage.
- **CSRF Tokens** – All forms include `{% csrf_token %}`.
- **Access Control** – Restricted views require login.

---

## 🧪 Testing Instructions
1. **Registration**
   - Visit `/users/register/` and create a new account.
2. **Login**
   - Visit `/users/login/`, enter valid credentials.
3. **Logout**
   - Visit `/users/logout/` and confirm session ends.
4. **Profile**
   - While logged in, visit `/users/profile/` and update details.
5. **Access Restriction**
   - Log out and try `/users/profile/` → should redirect to login.

---

## 📝 Requirements
- Python 3.x
- Django 4.x or higher
- Browser with cookies enabled

---

