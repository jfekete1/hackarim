notes = wasp.system.notifications
msg = {'title': 'fontos level', 'body': 'Szia ez egy fontos teszt levél !! '}
notes.__setitem__(1, msg)
watch.vibrator.pulse(1)
