import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
icons = ["edit-cut", "edit-paste", "edit-copy"]

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
