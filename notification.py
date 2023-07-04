notes = wasp.system.notifications
msg = {'title': 'notification', 'body': 'System started.'}
notes.__setitem__(1, msg)
watch.vibrator.pulse(1)
