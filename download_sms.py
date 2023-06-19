import sqlite3
from datetime import datetime
import subprocess

# Path to the SQLite database file
db_path = "/home/mobian/.purple/chatty/db/chatty-history.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Retrieve the last message from the messages table
cursor.execute("SELECT time, body FROM messages ORDER BY id DESC LIMIT 1")
result = cursor.fetchone()

if result:
    timestamp = result[0]
    body = result[1]
    
    # Convert timestamp to human-readable format
    timestamp_formatted = datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d %H:%M:%S")

    # Print the timestamp and message body
    print("Timestamp:", timestamp_formatted)
    print("Message Body:", body)
    
    # Run the shell command
    subprocess.run([
        "/home/mobian/wasp-os/tools/wasptool",
        "--send-notification",
        "--title",
        timestamp_formatted,
        "--body",
        body
    ])
else:
    print("No messages found.")

# Close the database connection
cursor.close()
conn.close()

