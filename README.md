# Smart FAQ Chatbot using Flask & Gemini AI

## Overview

The Smart FAQ Chatbot is a web-based application developed using Flask, SQLite, and Google's Gemini AI API. It provides instant responses to frequently asked questions (FAQs) and automatically generates AI-powered answers when a matching FAQ is not available.

The chatbot includes user authentication, chat history management, an admin panel, and an interactive chat interface, making it suitable for educational purposes and internship projects.

---

## Features

* User Registration and Login
* Secure Session Management
* FAQ-Based Question Answering
* AI-Powered Responses using Gemini API
* Chat History Storage with SQLite
* Admin Panel
* Responsive User Interface
* Typing Animation
* Markdown Response Support
* Logout Functionality

---

## Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3
* JavaScript
* Google Gemini API
* python-dotenv

---

## Project Structure

```
faq-chatbot/
│
├── app.py
├── ai.py
├── chatbot.db
├── faq_data.json
├── requirements.txt
├── .env
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── admin.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd faq-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project folder.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Working

1. Register a new account.
2. Login using your credentials.
3. Ask a question.
4. The chatbot first searches the FAQ database.
5. If no matching FAQ is found, Gemini AI generates a response.
6. All conversations are stored in the database for future reference.

---

## Future Enhancements

* Voice Input
* Speech Output
* Multi-language Support
* File Upload Support
* AI Response Streaming
* Dark Mode
* User Dashboard
* Analytics for Admin

---

## Author

**Sakshi Karle**

---

## License

This project is developed for educational and internship purposes.
