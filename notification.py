notes = wasp.system.notifications
msg = {'title': 'teszt', 'body': 'teszt '}
notes.__setitem__(1, msg)
watch.vibrator.pulse(1)
