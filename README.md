# 🔐 Password Strength Checker

## 📌 Overview
This project is a Python-based password strength checker that evaluates the security of a password using multiple criteria. It also detects whether the password exists in a common password list (`rockyou.txt`), simulating a basic dictionary attack.

---

## 🚀 Features
- Checks password strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Detects **common/weak passwords** using `rockyou.txt`
- Provides **suggestions** to improve weak passwords
- Fast lookup using optimized data structures (set)

---

## 🛠️ Technologies Used
- Python 3
- Regular Expressions (re module)
- Wordlist analysis (rockyou.txt)

---

## 📂 Project Structure

password-strength-checker/
│── checker.py
│── README.md
│── rockyou.txt (not included)


---

## ⚠️ Important Note
The `rockyou.txt` file is **not included** in this repository due to its large size.

### 📥 How to get it:
If you are using Kali Linux:
```bash
cp /usr/share/wordlists/rockyou.txt .
