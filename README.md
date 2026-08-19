# 🔐 Caesar Cipher 

## 📌 Introduction

The **Caesar Cipher Web Application** is a web-based cryptography project developed using **Python and Flask**. It allows users to encrypt and decrypt text using the Caesar Cipher algorithm through a simple and interactive web interface.

The project demonstrates the practical implementation of a classical encryption technique while providing hands-on experience with **Python, Flask, HTML, CSS, form handling, and web application deployment**.

---

## 🎯 Project Objective

The main objective of this project is to develop an easy-to-use web application that demonstrates how the Caesar Cipher algorithm works.

The project aims to:

* Implement Caesar Cipher encryption and decryption.
* Provide an interactive web-based interface.
* Allow users to enter custom text and shift values.
* Display the encrypted or decrypted result instantly.
* Understand the connection between frontend and backend.
* Deploy the application as a live web application.

---

## ❓ Problem Statement

Cryptography concepts can be difficult to understand when studied only through theoretical examples. Beginners need a practical way to experiment with encryption and decryption.

This project solves this problem by providing an interactive web application where users can enter text, select a shift value, and observe how the Caesar Cipher transforms the message.

---

## 💡 Proposed Solution

The proposed solution is a Flask-based web application that implements the Caesar Cipher algorithm.

The user enters:

1. A message
2. A shift value
3. An operation — Encrypt or Decrypt

The Flask backend processes the input using the Caesar Cipher algorithm and returns the result to the web interface.

---

## ⚙️ How It Works

The application follows this workflow:

```text
User
  ↓
Enter Text
  ↓
Enter Shift Value
  ↓
Select Encrypt / Decrypt
  ↓
HTML Form
  ↓
Flask Backend
  ↓
Caesar Cipher Algorithm
  ↓
Generate Result
  ↓
Display Result
```

### 🔐 Encryption

During encryption, each alphabetic character is shifted forward by the selected number of positions.

Example:

```text
Original Text : HELLO
Shift         : 3
Encrypted Text: KHOOR
```

### 🔓 Decryption

During decryption, each character is shifted backward by the selected number of positions.

Example:

```text
Encrypted Text: KHOOR
Shift         : 3
Decrypted Text: HELLO
```

---

## ✨ Features

* 🔐 Caesar Cipher encryption
* 🔓 Caesar Cipher decryption
* 🔢 Custom shift value
* 📝 User-friendly text input
* ⚡ Fast processing
* 🌐 Web-based interface
* 📱 Responsive design
* 🔄 Supports repeated encryption and decryption
* 🚀 Deployment-ready Flask application

---

## 🛠️ Technologies Used

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Backend programming and cipher logic |
| Flask      | Web application framework            |
| HTML5      | Frontend structure                   |
| CSS3       | User interface styling               |
| Jinja2     | Dynamic result rendering             |
| Git        | Version control                      |
| GitHub     | Source code repository               |
| Gunicorn   | Production server                    |
| Render     | Cloud deployment                     |

---

## 📂 Project Structure

```text
caesar_cipher/
│
├── app.py
├── README.md
├── requirements.txt
├── .python-version
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
    └── caesar-cipher-output.png
```

---

## 🖥️ Project Output

The following screenshot shows the complete working output of the Caesar Cipher Web Application.

![Caesar Cipher  Output](caesar-cipher-output.png)

---

## 🧪 Test Cases

| Test Case | Input       | Shift | Operation | Expected Output |
| --------- | ----------- | ----: | --------- | --------------- |
| 1         | HELLO       |     3 | Encrypt   | KHOOR           |
| 2         | KHOOR       |     3 | Decrypt   | HELLO           |
| 3         | ABC XYZ     |     2 | Encrypt   | CDE ZAB         |
| 4         | Hello World |     5 | Encrypt   | Mjqqt Btwqi     |

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd caesar_cipher
```

### Step 2: Create a Virtual Environment

```powershell
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

```powershell
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Run the Application

```powershell
python app.py
```

### Step 6: Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🌐 Live Demo

**Live Demo:** Add your deployed application URL here.

Example:

```text
https://your-caesar-cipher-app.onrender.com
```

---

## 🚀 Deployment

The application can be deployed as a Python Web Service using platforms such as Render.

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
gunicorn app:app
```

After successful deployment, the generated public URL can be added to the **Live Demo** section.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Flask web development
* Frontend and backend integration
* HTML form handling
* HTTP POST requests
* Jinja2 templates
* Basic cryptography concepts
* Git and GitHub
* Cloud deployment
* Technical documentation

---

## ⚠️ Security Limitation

The Caesar Cipher is a **classical educational encryption technique** and should not be used to protect sensitive or confidential information.

Because the cipher has a very small key space, it can be easily broken using modern cryptographic techniques.

This project is intended primarily for **educational and demonstration purposes**.

---

## 🔮 Future Enhancements

* [ ] Copy-to-clipboard functionality
* [ ] Clear/reset button
* [ ] Dark mode
* [ ] Encryption history
* [ ] Download encrypted text
* [ ] Mobile UI improvements
* [ ] Automated unit testing
* [ ] REST API support
* [ ] User authentication
* [ ] Integration of modern encryption algorithms such as AES

---

## 👩‍💻 Author

**Srilatha Pappu**

B.Tech – Computer Science and Engineering (AI & ML)

---

## 📄 License

This project is developed for **educational, learning, and internship purposes**.
