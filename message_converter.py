"""
Takes a text file with a subject and message and converts it to readable string.s
    Parameter:
    msg_file: File with given subject and message
"""
def convert_message_file(msg_file):

    subject = ""
    message = ""

    with open(msg_file) as file:

        subject = file.readline().strip()

        for line in file:
            message += line

        return subject, message
            