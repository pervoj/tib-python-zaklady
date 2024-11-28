import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from content import Content

class Window(Adw.ApplicationWindow):
  def __init__(self, application):
    super().__init__(title = "Hello World", application = application)
    self.set_default_size(450, 200)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.set_content(box)

    headerbar = Adw.HeaderBar()
    box.append(headerbar)

    content = Content()
    box.append(content)

  def on_button_clicked(self, button):
    print("Hello World")
