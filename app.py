# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# sender_email = "mohd.madani.02@gmail.com"
# recipient_email = "ahmedqudsi786@gmail.com"
# password = "wvla enyv kqox fmfs"

# subject = "Automated Email from Python"
# body = "Hello! This is an automated email sent using Python."
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = recipient_email 
# msg['Subject'] = subject
# msg.attach(MIMEText(body, 'plain'))

# try:
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.send_message(msg)
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")





# import smtplib
# import time
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# sender_email = "mohd.madani.02@gmail.com"
# password = "wvla enyv kqox fmfs"

# recipients = [
#     "ahmedqudsi786@gmail.com",
#     "mr.khans00966@gmail.com",
#     "qadriasma3@gmail.com",
#     "mohd.madani.02@gmail.com"
# ]

# subject = "Application for Potential Opportunities"

# body = """Dear Hiring Team,

# I hope this message finds you well. I am reaching out to explore potential opportunities.
# Please find my resume attached for your consideration.

# Warm regards,
# Ahmed
# """


# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.ehlo()
#     server.starttls()
#     server.login(sender_email, password)

#     for email in recipients:
#         msg = MIMEMultipart()
#         msg["From"] = sender_email
#         msg["To"] = email
#         msg["Subject"] = subject
#         msg.attach(MIMEText(body, "plain"))
          
        
#         server.sendmail(sender_email, email, msg.as_string())
#         print(f"Sent to {email}")

#         time.sleep(10)  # IMPORTANT: delay to avoid spam/blocks

# print("All emails sent individually.")



import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

sender_email = "mohd.madani.02@gmail.com"
password = "wvla enyv kqox fmfs"

recipients = [
    "ahmedqudsi786@gmail.com",
    "mr.khans00966@gmail.com",
    "qadriasma3@gmail.com",
    "mohd.madani.02@gmail.com"
]

subject = "Application for Potential Opportunities"

body = """Dear Hiring Team,

I hope this message finds you well. Please find my resume attached for your review.

Warm regards,
Ahmed
"""

# 📎 Path to the file you want to attach
file_path = "C:\\Users\\Younus\\Downloads\\Madani DXB R.pdf"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)

    for email in recipients:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject

        # Email body
        msg.attach(MIMEText(body, "plain"))

        # Attachment
        if os.path.exists(file_path):
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{os.path.basename(file_path)}"'
            )
            msg.attach(part)
        else:
            print(f"Attachment not found: {file_path}")
            continue

        server.sendmail(sender_email, email, msg.as_string())
        print(f"Sent to {email}")

        time.sleep(10)  # ⏳ delay to stay safe

print("All emails sent individually with attachment.")
