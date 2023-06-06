import imaplib
import email
import argparse

# IMAP server and login credentials
imap_server = 'mail.dmz.zalaszam.hu'
imap_port = 993
username = 'feketej'

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Retrieve the latest email from a sender.')
parser.add_argument('--sender', required=True, help='Email address of the sender')
parser.add_argument('--password', required=True, help='Mailbox password')
args = parser.parse_args()

# Set the sender_email and password from command-line arguments
sender_email = args.sender
password = args.password

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(imap_server, imap_port)

# Login to the mailbox
imap.login(username, password)

# Select the INBOX mailbox
imap.select('INBOX')

# Search for emails from the specified sender
status, email_ids = imap.search(None, f'(FROM "{sender_email}")')

# Get the latest email id
latest_email_id = email_ids[0].split()[-1]

# Fetch the email with the given id
status, email_data = imap.fetch(latest_email_id, '(RFC822)')

# Parse the email content
raw_email = email_data[0][1]
email_message = email.message_from_bytes(raw_email)

# Print the email subject
subject = email_message['Subject']
print('Subject:', subject)

# Print the email body
if email_message.is_multipart():
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True).decode('utf-8')
            print('Body:', body)
else:
    body = email_message.get_payload(decode=True).decode('utf-8')
    print('Body:', body)

# Close the mailbox connection
imap.close()
imap.logout()

