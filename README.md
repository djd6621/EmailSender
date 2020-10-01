# EmailSender
Python program that can send an email from one email to another or a list of emails.

# How to Use
This program is ran using the command line. You will need to have Python installed to your computer with the PATH configurated. 

From command line run the follow command:
python send_emails.py [1] [2] [3] [4]

The [] are not included in the command!

# Parameters
1 - email_to_send_from
2 - either a txt file of emails on each line or a single email to recieve the email
3 - single OR file dependent upon last paramater
4 - A text file with the first line being the subject text and the rest of the lines being the message. 

# Example - File
emails.txt -> An exmaple file is given.

message.txt -> An exmaple file is given.

Command: python send_emails.py myemail@gmail.com emails.txt file message.txt

# Example - Single
Command: python send_emails.py myemail@gmail.com joe@gmail.com single message.txt
