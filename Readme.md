# Email Sales Report Automation (Python)

A Python script to automatically send a sales summary Excel report via email.

The script attaches an existing `sales_summary.xlsx` file and sends it using Gmail SMTP with secure TLS authentication.

## Features
- Sends email with Excel attachment
- Uses secure TLS encryption
- Validates file existence before sending
- Simple command-line input interface
- Graceful error handling

## Requirements
- Python 3.x
- A Gmail account with App Password enabled

## Setup (Gmail)
To use this script with Gmail:
1. Enable **2-Step Verification** on your Google account
2. Generate an **App Password**
3. Use the App Password when prompted (not your Gmail password)

## Installation
Clone the repository:

git clone https://github.com/your-username/email-sales-report.git
cd email-sales-report
## Usage
Run the script:
python send_sales_report.py
Provide the required inputs when prompted:

Sender email address

Gmail App password

Receiver email address

Email subject and body

Folder path containing sales_summary.xlsx

##Example

Enter sender email address: example@gmail.com
Enter App password: ************
Enter receiver email address: manager@example.com
Enter Email subject: Monthly Sales Report
Enter Email body: Please find the attached sales summary.
Enter folder path containing sales_summary.xlsx: C:\Users\YourName\Reports