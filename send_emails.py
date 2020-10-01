import smtplib, ssl
from email.message import EmailMessage
import sys
import message_converter


# opens port to connect to SSL and server email.
port = 465
smpt_server = "smtp.gmail.com"


# creates a secure socket layer
context = ssl.create_default_context()


"""
Sends a message to each email in a file.
    Paramters:
    email: email sending message
    reciever: email recieving message.
    subject: Subject text for email
    msg: Text to send as message.
"""
def file_emails(email, password, file, subject, msg):

    emails = []
    
    try:

        with open("emails.txt") as file:
            for line in file:
                line = line.strip()
                emails.append(line)
    except FileNotFoundError:
        print("Email file not found.")

    print("Sending message to emails in file...")
    for i in range(len(emails)):
        single_email(email, password, emails[i], subject, msg)    


"""
Sends a message to a single given email.
    Paramters:
    email: email sending message
    reciever: email recieving message.
    subject: Subject text for email
    msg: Text to send as message.
"""
def single_email(email, password, reciever, subject, msg):

    print("Sending email...")
    try:

        with smtplib.SMTP_SSL(smpt_server, port, context=context) as server:
            server.login(email, password)
            msg = message_creation(email, reciever, subject, msg)
            server.send_message(msg)
            print("Email sent to {0}".format(reciever))
    except:
        print("Error occurred attempting to send email. Attempt to fix email, password, or reciever.")

        

"""
Creates a sendable message.
    Parameters:
    email: email sending message
    reciever: email recieving message.
    subject: Subject text for email
    msg: Text to send as message.
"""
def message_creation(email, reciever, subject, msg):

    message = EmailMessage()
    message.set_content(msg)
    message['Subject'] = subject
    message['From'] = email
    message['To'] = reciever  
    
    return message


def main():
    # System Args. 1 = email 2 = file/reciever email 3 = file emails or single email 4 = msg.txt 

    # gets email address and password of sender
    email_address = sys.argv[1]
    password = input("Enter your email password: ")
    
    # Grabs the message file and converts it to a subject and message text.
    msg = sys.argv[4]
    subject, message = message_converter.convert_message_file(msg)

    # Gets the single email or file full of emails.
    reciever = sys.argv[2]


    # determines if user sending to single email or a file of emails.
    if sys.argv[3] == "single":
        single_email(email_address, password, reciever, subject, message)
    elif sys.argv[3] == 'file':
        file_emails(email_address, password, reciever, subject,  message)
    else:
        print("Invalid third argument. Try again.")



if __name__ == "__main__":
    main()