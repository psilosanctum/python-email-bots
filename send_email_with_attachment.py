import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

# Login information for email sender
sender = ''
password = ''

# Email recipient(s)
recipients = ['', '']

# Create email subject and body
subject = "Monthly Transaction Report"
html = """\
    <html>
        <head></head>
        <body>
            <p> Howdy! <br>
                <div style="align-items: center;">
                    Please see the attached PDF detailing the prior month's transaction data. Contact management to discuss any comments or questions.
                </div>
            </p>
            <div style="margin-top: 25px">
                Yours truly, <br>
                Bot X-145
            </div>   
        </body>
    </html>

        """

# PDF file
file_location = 'transaction_growth.pdf'

# Create the attachment file 
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Connect and login to the email server

# Outlook Example
# server = smtplib.SMTP('smtp-mail.outlook.com', 587)

# Gmail Example
server = smtplib.SMTP('smtp.gmail.com', 587)

# Login to your email
server.starttls()
server.login(sender, password)

# Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(html, 'html'))

# Attach the attachment file
msg.attach(part)

# Send the email to this specific email address
server.send_message(msg)


# Quit the email server when everything is done
server.quit()
