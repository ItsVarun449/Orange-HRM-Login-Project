# 🔐 Selenium Login Automation using POM

## 📌 Description

This project is a **Selenium automation framework** built using **Python** and the **Page Object Model (POM)** design pattern.

It automates the login functionality of the OrangeHRM demo website and verifies whether the login is successful.

---

## 🚀 Features

* Page Object Model (POM) structure
* Explicit waits (WebDriverWait)
* Assertion for validation
* Clean and reusable code

---

## 🛠 Technologies Used

* Python
* Selenium WebDriver

---

## 📂 Project Structure

```
project/
│
├── main.py
├── pages/
│   └── login_page.py
├── utilities/
│   └── driver_setup.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Step 1: Install dependencies

```
pip install -r requirements.txt
```

### Step 2: Run the script

```
python main.py
```

---

## ✅ Test Scenario

* Open login page
* Enter valid username and password
* Click login button
* Verify Dashboard page is displayed

---

## 🔍 Assertion

The test checks whether the **Dashboard header** is visible after login to confirm success.

---

## 👨‍💻 Author

Varun Rana
