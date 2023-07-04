import wasp

class MyApp():
    """A hello world application for wasp-os."""
    NAME = "Hello"

    def __init__(self, msg="notification sent"):
        self.msg = msg

    def foreground(self):
        notes = wasp.system.notifications
        uzi = {'title': 'parancs', 'body': 'Move robot.'}
        notes.__setitem__(1, uzi)
        watch.vibrator.pulse(1)
        self._draw()

    def _draw(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string(self.msg, 0, 108, width=240)

