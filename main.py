#!/usr/bin/python3

import gi
import RPi.GPIO as GPIO
import threading
from mfrc522 import SimpleMFRC522
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import POSWindow as window
import LoginWindow as login

loggedIn = False

class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

        log = login.LoginWindow(self)
        log.run()
        loggedIn = True

        if (loggedIn == True):
            win = window.POSWindow()
            win.connect("destroy", Gtk.main_quit)
            win.show_all()

app = App()
Gtk.main()