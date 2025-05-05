# Email-Verification-Code-Sender
Email Verification Code Sender With Python

# Email Verification Code Sender

This Python script sends a randomly generated 4-digit verification code to a specified email address using Gmail's SMTP service. It then asks the user to enter the code and verifies whether it matches the sent one.

## Features

- Generates a random 4-digit code
- Sends the code via email using SMTP over SSL
- Verifies user input against the sent code
- Easy to configure and use

## Requirements

- Python 3.x
- An active Gmail account
- Less secure apps access enabled (for Gmail accounts using basic authentication)
- Internet access

## Installation

1. Clone or download this repository.
2. Install required libraries (only built-in libraries are used, no external installations needed).

## Usage

1. Open the script file.
2. Replace the placeholders with your own credentials:
    ```python
    FROM = 'your_email@gmail.com'
    TO = 'recipient_email@example.com'
    keyy_password = 'your_email_app_password'
    ```
3. **Important:** If you use Gmail, generate an [App Password](https://support.google.com/accounts/answer/185833) instead of your actual password.
4. Run the script:
    ```bash
    python Email-Verification-Code.py
    ```
5. Enter the verification code received in your inbox when prompted.


