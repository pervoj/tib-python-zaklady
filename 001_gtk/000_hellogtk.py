import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

class Window(Adw.ApplicationWindow):
  def __init__(self, application):
    super().__init__(title = "Hello World", application = application)
    self.set_default_size(400, 300)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.set_content(box)

    headerbar = Adw.HeaderBar()
    box.append(headerbar)

    button = Gtk.Button(label = "Click Me")
    button.connect("clicked", self.on_button_clicked)
    button.set_halign(Gtk.Align.CENTER)
    button.set_valign(Gtk.Align.CENTER)
    button.set_vexpand(True)
    box.append(button)

  def on_button_clicked(self, button):
    print("Hello World")

class Application(Adw.Application):
  def __init__(self):
    super().__init__()
    self.connect("activate", self.on_activate)
  
  def on_activate(self, app):
    self.win = Window(application = app)
    self.win.present()

app = Application()
app.run()