# IT6006 — Monke Bookstore (Django)

A simple bookstore web application built for **IT6006 Secure Web Application Development**.  

---

## Features

- **Homepage** with three sections: 
  - **Featured**, 
  - **Best Sellers**, 
  - **Discounts**

- **Books**
  - List and Detail pages (template-based)
  - simple search/filter by title/genre
  
- **Books Details**
  - Details of Selected books
  - Add to cart button
  
- **Cart**
  - Add / remove / update quantity
  - Totals update on page
  
- **Login / Sign Up/ Auth**
  - Django built-in auth for login/logout/signup

- **Admin**
  - Manage Users, Books, Orders, etc. via Django Admin

---

##  Getting Started (Local)

> **Windows CMD/PowerShell** 

### 1) Clone and enter the project
Open your preferred project folder in cmd, make sure the CD is accurate, and then:
```CMD
git clone https://github.com/Kronos6419/IT6006_Monke-Bookstore.git
```
this will clone the project on your device

### 2) Create and activate a virtual environment
```CMD
python -m venv env
env\Scripts\Activate.ps1
```

### 3) Install dependencies
```CMD
pip install -r requirements.txt
```
this will download the packages we need

### 4) Migrate the database
```powershell
python manage.py migrate
```

### 5) Use the superuser 
Provided Super User (Dev) is:
- **Username:** `admin`
- **Password:** `monkeadmin@bookstore123`

### 5.5) Alternatively, Register as a Customer
Alternatively to test the customer version, once the server has been launched
one can navigate to login and Create a customer account and explore the website that way

### 6) Run the server
```CMD
python manage.py runserver
```
Open: http://127.0.0.1:8000/  
Admin: http://127.0.0.1:8000/admin/

---

## Git Workflow (quick reference)

**Bring latest `main` locally:**
```powershell
git checkout main
git fetch origin
git pull --rebase origin main
```
Merging and checking incompatibilities performed on Github
