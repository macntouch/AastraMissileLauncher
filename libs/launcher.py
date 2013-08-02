__author__ = 'amucci'
import usb.core
import usb.util
import time

class Thunder(object):
    duration_time = 250
    DOWN = 0x01
    UP = 0x02
    LEFT = 0x04
    RIGHT = 0x08
    FIRE = 0x10
    STOP = 0x20

    def connect(self):

        self.device = usb.core.find(idVendor=0x2123, idProduct=0x1010)
        if self.device is None:
            raise ValueError('Missile device not found')
        else:
            self.device_type = "Thunder"
        self.device.set_configuration()

    def _send_command(self, cmd):
        self.device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, cmd, 0x00,0x00,0x00,0x00,0x00,0x00])

    def led(self, cmd):
        if cmd == "on":
            status_led = 0x01
        else:
            status_led = 0x00
        self.device.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, status_led, 0x00,0x00,0x00,0x00,0x00,0x00])

    def send_actions(self, cmd):
        dur_time = self.duration_time
        if cmd == "left":
            command = self.LEFT
        if cmd == "right":
            command = self.RIGHT
        if cmd == "down":
            dur_time = 100
            command = self.DOWN
        if cmd == "up":
            dur_time = 100
            command = self.UP
        if cmd == "fire":
            command = self.FIRE

        self._send_command(command)
        time.sleep(dur_time / 1000.0)
        self._send_command(self.STOP)

    def fire(self):
        time.sleep(0.5)
        self._send_command(self.FIRE)
        time.sleep(4.5)