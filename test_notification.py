notes = wasp.system.notifications
msg= {'title': 'cron Notification', 'body': 'The archiving process ran successfully!'}
notes.__setitem__(1, msg)
watch.vibrator.pulse(1)
