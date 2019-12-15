import gi
import threading
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

loggedIn = False
studId = Gtk.Label()

class POSWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="AlkanSHAP Client POS")
        self.set_default_size(1600, 900)
        box = Gtk.VBox(spacing=10)
        self.add(box)
        self.maximize()

        txt_Title = Gtk.Label()
        txt_Title.set_markup("<span font_weight='bold' font='50'>AlkanSHAP Student Portal</span>")
        txt_Title.set_margin_bottom(10)
        txt_Welcome = Gtk.Label()
        txt_Welcome.set_markup("<span font_weight='light' font='30'>Welcome!</span>")

        btn_Balance = Gtk.Button("Balance")
        btn_Balance.connect("clicked", self.on_balance_clicked)
        btn_Balance.set_margin_left(500)
        btn_Balance.set_margin_right(500)

        btn_Withdraw = Gtk.Button("Withdraw")
        btn_Withdraw.set_margin_left(500)
        btn_Withdraw.set_margin_right(500)
        btn_Withdraw.connect("clicked", self.on_withdraw_clicked)

        btn_Deposit = Gtk.Button("Deposit")
        btn_Deposit.set_margin_left(500)
        btn_Deposit.set_margin_right(500)
        btn_Deposit.connect("clicked", self.on_deposit_clicked)

        btn_Logout = Gtk.Button("Logout")
        btn_Logout.set_margin_left(500)
        btn_Logout.set_margin_right(500)
        btn_Logout.connect("clicked", self.on_logout_clicked)

        box.add(txt_Title)
        box.add(txt_Welcome)
        box.add(btn_Balance)
        box.add(btn_Withdraw)
        box.add(btn_Deposit)
        box.add(btn_Logout)

        box.set_margin_bottom(30)

    def on_balance_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Balance")
        dialog.set_default_size(600, 300);
        dialog.format_secondary_text("broke boy")
        dialog.run()
        print ("done checking balance")
        dialog.destroy()

    def on_withdraw_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Withdraw")
        dialog.set_default_size(600, 300);
        dialog.format_secondary_text("broke boy")
        dialog.run()
        print ("done checking balance")
        dialog.destroy()

    def on_deposit_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Deposit")
        dialog.format_secondary_text("broke boy")
        dialog.run()
        print ("done checking balance")
        dialog.destroy()

    def on_logout_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Logout")
        dialog.set_default_size(600, 300);
        dialog.format_secondary_text("broke boy")
        dialog.run()
        print ("done checking balance")
        dialog.destroy()