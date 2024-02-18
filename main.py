""" Specific Email Type Message Sender - Each Sendv (Other Recepient will not know)"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import datetime

msg = []
# ===================================================
PATH = r"C:\Users\tejas\OneDrive\Pictures\Desktop\SEND-MAILS"
os.chdir(PATH)
sender_email = 'tejasjagannatha@gmail.com'  # Replace with the sender's email address
password = 'baqn llbv kndx oajn'


# JD= list(input('if JD paste here'))

# JDS = int(input(f'Enter no of mail to be sent: '))

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {message}\n"

    with open("logfile.txt", "a") as log_file:
        log_file.write(log_entry)


# =============================

resume = int(input('Enter 1- for Main Resume'))

# Testing
# Read the list of recipient emails from the file
with open('C:/Facebook/prof_emails.txt', 'r') as file:
    lines_list = [line.strip() for line in file]

for receiver_email in lines_list:
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    print(receiver_email)
    # --------------------------------------------------------------
    # Main
    if resume == 1:

        message[
            'Subject'] = 'Python Full Stack - Flask/Django | QA Engineer| DevOps | Automation Testing | Cloud | CI/CD '
        file_name = 'Tejas_Jagannatha_CV_FA.docx'
        msg = 'Dear Hiring manager,' + '\n' + '\n' + 'Hope all is well.' + 'I am writing to express my strong interest in the Software Developer/QA/Automation/FullStack jobs. With a proven track record of four years in Python software development, full-stack engineering, and automation, I am confident in my ability to contribute effectively. ' + '\n' + '\n' + 'Is there any choice for you to refer me to internal positions in your project? Having knowledge on also Testing. Used Jmeter for Stress testing used loops, threads, intervals In my previous role, I worked along with cross-functional teams in developing robust and scalable solutions, successfully delivering several end-to-end projects. ' + '\n' + 'My expertise spans the entire software development life cycle, from conceptualization to deployment, with a keen focus on automation to streamline processes and enhance efficiency. My passion is about technologies and building new innovative tools that would be robust and fast and improves cost cutting and need of manual. ' + '\n' + '\n' + 'I have 2 innovative challenge awards from 2 companies where I streamlined the manual procedure into automation reducing the need of manual work by 60% reduction and the efficiency boosted to 85% as discussed in the midterm review. Other would be in developing a website portal using python flask and fastapi where the server related issues was solved by python rest api authentication level hits and the manual procedures of drafting mails which would take atleast 3days for the replies to come back as it was onsite offshore communication as it involved admin level rights as well. This portal that i built was able to solve that challenge with just a button click. For which, the efficiency increased 40% as the servers where running again without a delay of providing their services so Testers could test. Please requesting you to see my profile.'
        JD = input('Enter JD if exist or shoot direct mail:')
        if JD:
            msg = msg + "I am interested in this position: " + JD

        # Add body to email and send
        message.attach(MIMEText(msg, 'plain'))
        # Attach the file
        with open(file_name, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {file_name}')
            message.attach(part)
            # Establish a secure session with the SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                # Send the email
                server.sendmail(sender_email, receiver_email, message.as_string())

    """elif resume == 2:
        file_name = 'Tejas_Jagannatha_Automation.pdf'

        with open("Senr_AutomationManual-CoverLetter.txt", 'r') as file:
            lines_list = file.readlines()

            msg= '\n'.join(lines_list)


        message['Subject'] = 'Automation Testing- Python and Pytest|JavaScript |QA Engineer |Full Stack - Flask/Django|DevOps|Cloud | CI/CD'

    """

