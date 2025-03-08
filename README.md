# Message Encryption and Decryption Tool

This project is a Python-based web application for encrypting and decrypting messages using a **substitution cipher technique**. The project is built using **Flask** for backend processing and **HTML, CSS, and JavaScript** for the frontend.

---

## 📌 Table of Contents
- [Features](#features)
- [How it Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Screenshot](#screenshot)
- [License](#license)
- [Author](#author)

---

## 🚀 Features

✔ **Encrypt Messages:** Securely encrypt messages using a user-defined key.  
✔ **Decrypt Messages:** Retrieve original messages using the same key.  
✔ **Simple Web Interface:** User-friendly UI with hacking theme.  
✔ **Custom Key:** Enter any string as an encryption/decryption key.  
✔ **Flask-based API:** Backend processing with Python Flask.  
✔ **Real-time Processing:** Instant message conversion with a single click.  

---

## 🔍 How it Works

🔹 **Encryption:**
   - The message is encoded character by character based on the key.
   - Each character's Unicode value is shifted using the corresponding character from the key.
   - The encoded string is further converted to a **Base64 string** for added security.

🔹 **Decryption:**
   - The Base64 string is decoded.
   - Each character is shifted back to retrieve the original message using the same key.

---

## 💻 Installation

1️⃣ **Clone the Repository**
```bash
   git clone https://github.com/hritikranjan1/message-encryption-decryption.git
```

2️⃣ **Navigate to the Project Directory**
```bash
   cd message-encryption-decryption
```

3️⃣ **Install Dependencies**
```bash
   pip install -r requirements.txt
```

4️⃣ **Run the Flask Application**
```bash
   python app.py
```

5️⃣ **Open in Browser**
```
   http://127.0.0.1:5000/
```

---

## 📜 Usage

1️⃣ **Enter Message:** Type the text you want to encrypt or decrypt.  
2️⃣ **Enter Key:** Input a custom key for encryption/decryption.  
3️⃣ **Select Mode:**
   - Choose **Encrypt** to encode the message.
   - Choose **Decrypt** to decode the message.
4️⃣ **Submit:** Click the **Submit** button to process the message.  
5️⃣ **View Result:** The result will be displayed instantly.  
6️⃣ **Reset:** Click the **Reset** button to clear all fields.  

---

## 🔧 Requirements

- **Python 3.x**
- **Flask**
- **Base64** (Python built-in library)
- **HTML, CSS, JavaScript** (Frontend)

---

## 🖼 Screenshot

![Message Encryption & Decryption Tool](https://github.com/user-attachments/assets/4d165f0a-b46f-4929-a1d2-d3e141125bdb)

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 👨‍💻 Author

- **Name:** Hritik Ranjan
- **GitHub:** [hritikranjan1](https://github.com/hritikranjan1)
- **LinkedIn:** [Hritik Ranjan](https://www.linkedin.com/in/hritik-ranjan-05a835230/)
- **Telegram Community:** [Join Here](https://t.me/codewithluv143)  

🚀 **Happy Encrypting & Decrypting!** 🔒

