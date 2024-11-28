import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

class Content(Adw.Bin):
  def __init__(self):
    super().__init__()

    main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 12)
    self.set_child(main_box)
    main_box.set_halign(Gtk.Align.CENTER)
    main_box.set_valign(Gtk.Align.CENTER)
    main_box.set_vexpand(True)

    input_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 8)
    main_box.append(input_box)

    input_a = Gtk.Entry()
    input_box.append(input_a)

    select_options = ["+", "-", "*", "/"]
    select = Gtk.DropDown.new_from_strings(select_options)
    input_box.append(select)

    input_b = Gtk.Entry()
    input_box.append(input_b)

    button = Gtk.Button(label = "Vypočítat")
    main_box.append(button)
    button.set_halign(Gtk.Align.CENTER)

    label = Gtk.Label(label = "Výsledek: ")
    main_box.append(label)

    def on_clicked(button):
      try:
        value_a = int(input_a.get_text())
        value_b = int(input_b.get_text())
        operation = select_options[select.get_selected()]
        
        if operation == "+":
          result = str(value_a + value_b)
        elif operation == "-":
          result = str(value_a - value_b)
        elif operation == "*":
          result = str(value_a * value_b)
        elif operation == "/":
          if value_b == 0:
            result = "chyba"
          else:
            result = str(value_a / value_b)

        label.set_text(f"Výsledek: {result}")
      except ValueError:
        pass

    button.connect("clicked", on_clicked)
