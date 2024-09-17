# 🕵️‍♂️ WADark - WhatsApp Phishing Tool via OTP Code

WADark is a phishing tool designed to capture OTP codes from WhatsApp web sessions. This tool leverages Selenium for web automation, Flask for the web interface, and Tesseract for Optical Character Recognition (OCR) to extract OTP codes from the screenshots captured during the WhatsApp web login process.

> ⚠️ **Warning:** This tool is intended for educational purposes only. Unauthorized use of this tool to access someone's account without permission is illegal and unethical. Use responsibly.

```bash
Dev: LSDeep - v1.0.0
www.htdark.com
Contact: https://t.me/lsd33p
```
## ✨ Features

- 🛡️ **Phishing via OTP**: Capture OTP codes during the WhatsApp web login process.
- 🤖 **Web Automation**: Uses Selenium WebDriver for automating interactions with the WhatsApp web interface.
- 🔍 **OCR Integration**: Extracts text from images using Tesseract OCR for accurate OTP retrieval.
- 🌐 **Flask Web Interface**: Simple, intuitive web UI for user interaction.
- 📝 **Data Logging**: Captures user details including IP, User-Agent, and location information.

## 📋 Prerequisites

- 🐍 **Python 3.7+**: Ensure Python is installed on your machine.
- 🌐 **Ngrok**: Required to expose the Flask application to the internet.
- 🖥️ **ChromeDriver**: Compatible version of ChromeDriver to run Selenium WebDriver.
- 🔠 **Tesseract OCR**: Install Tesseract and update the path in the script. [Tesseract OCR Installation Guide](https://github.com/UB-Mannheim/tesseract/wiki)

## 🛠️ Installation

1. **Clone the Repository** 📂
   ```bash
   git clone [https://github.com/cyb3rhex/WADark.git](https://github.com/cyb3rhex/WADark)
   cd WADark
   ```
   
2. **Set Up Virtual Environment 🌐**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies 📦**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Configure Tesseract OCR Path ⚙️**
   - Update NGROK Authkey
   - Update the pytesseract.pytesseract.tesseract_cmd path in the script to match your local installation of Tesseract.

## 🚀 Usage
Run the tool using the command:
   ```bash
   python3 WADark.py
   ```

## 🛡️ How It Works

1. 📝 Phishing Page: Users are prompted to enter their phone number on the web page.
2. 🤖 WhatsApp Web Automation: The tool uses Selenium to navigate through the WhatsApp web interface.
3. 🔍 OTP Extraction: A screenshot of the OTP area is taken, and the OTP is extracted using Tesseract OCR.
4. 📊 Data Logging: User details, OTP code, and other information are logged to a text file for analysis.

## Demo
https://github.com/user-attachments/assets/51e68c86-76bf-4384-a7a3-5e9d05e0a67e

## 🤝 Contribution
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.
