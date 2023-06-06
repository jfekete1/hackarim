import imaplib
import email
import argparse
import hashlib

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

# Read processed checksums from processed.txt
processed_emails = set()
try:
    with open('processed.txt', 'r') as file:
        for line in file:
            processed_emails.add(line.strip())
except FileNotFoundError:
    pass

# Generate checksum for the email
checksum = hashlib.md5(email_message.as_bytes()).hexdigest()

# Check if the email has already been processed
if checksum in processed_emails:
    print("Nothing to see here")
    exit()

# Add the checksum to the processed_emails set
processed_emails.add(checksum)

# Write processed checksums to processed.txt
with open('processed.txt', 'w') as file:
    for checksum in processed_emails:
        file.write(checksum + '\n')

# Continue processing the email
# Get the email subject
subject = email_message['Subject'][:14]  # Retrieve only the first 14 characters
print('Subject:', subject)


# Get the email body
if email_message.is_multipart():
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True).decode('utf-8')
            body = '\n'.join(line for line in body.split('\n') if not line.startswith('>'))
            body = body.replace('\n', ' ').replace('\r', '')
            print('Body:', body)
else:
    body = email_message.get_payload(decode=True).decode('utf-8')
    body = '\n'.join(line for line in body.split('\n') if not line.startswith('>'))
    body = body.replace('\n', ' ').replace('\r', '')
    print('Body:', body)

# Create a notification.py file with email values
notification_script = f"notes = wasp.system.notifications\nmsg = {{'title': '{subject}', 'body': '{body}'}}\nnotes.__setitem__(1, msg)\nwatch.vibrator.pulse(1)\n"

# Write the content to the notification.py file
with open('notification.py', 'w') as file:
    file.write(notification_script)

# Close the mailbox connection
imap.close()
imap.logout()

