import gi
import RPi.GPIO as GPIO
import threading
from mfrc522 import SimpleMFRC522
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class LoginWindow(Gtk.Dialog):
    studentId=0
    studId = Gtk.Label("tap")

    def login(self):
        reader = SimpleMFRC522()
        try:
            id = reader.read()
            self.studentId = id[0]
            print(id)
        finally:
            self.studId.set_markup("<span font='19' font-weight='bold'>Welcome:</span> <span font='20'>"+str(self.studentId)+"</span>")
            GPIO.cleanup()
            timer = threading.Timer(2.0, self.close)
            timer.start()


    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Please Log In")
        self.set_default_size(1024, 576)
        self.maximize()

        label = Gtk.Label()
        label.set_markup("<span font-weight='bold' font='70'>Please Log In</span>")
        box = self.get_content_area()
        box.add(label)
        box.add(self.studId)
        box.show_all()

        timer = threading.Timer(1.0, self.login)
        timer.start()
