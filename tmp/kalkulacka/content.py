import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

class Content(Adw.Bin):
    def __init__(self):
        super().__init__()

        main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 12)
        self.set_child(main_box)
        main_box.set_vexpand(True)
        main_box.set_valign(Gtk.Align.CENTER)
        main_box.set_halign(Gtk.Align.CENTER)


        input_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 8)
        main_box.append(input_box)
