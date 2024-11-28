import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw

from window import Window

class Application(Adw.Application):
  def __init__(self):
    super().__init__()
    self.connect("activate", self.on_activate)
  
  def on_activate(self, app):
    self.win = Window(application = app)
    self.win.present()
