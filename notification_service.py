import time
import subprocess

def check_notifications():
    # Execute the command and capture the output
    command = "/home/feketej/wasp-os/tools/wasptool --device D3:7D:50:55:E4:90 --exec /home/feketej/hackarim/check_notification.py"

    try:
        output = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    robot_script = '/home/feketej/pydobot/basic_example.py'

    if "Success" in output:
        print("Starting robot!")
        subprocess.run(['python3', robot_script])

while True:
    check_notifications()
    time.sleep(10)

