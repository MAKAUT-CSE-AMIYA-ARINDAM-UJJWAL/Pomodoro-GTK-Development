import gi
counter = 0

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]
import time
import sys

class GTK_Project(Gtk.Window):
	def __init__(self):
		super().__init__(title="Pomodoro")
		self.set_border_width(100)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		vbox.set_homogeneous(False)
		hbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		hbox_left.set_homogeneous(False)
		hbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		hbox_right.set_homogeneous(False)
		
		vbox.pack_start(hbox_left, True, True, 0)
		vbox.pack_start(hbox_right, True, True, 0)
		
		#Adding Icons
		liststore = Gtk.ListStore(Pixbuf, str)
		iconview = Gtk.IconView.new()
		iconview.set_model(liststore)
		iconview.set_pixbuf_column(0)
		iconview.set_text_column(1)        
		
		# Adding UserInfo
		label = Gtk.Label(label="               Hi! Welcome to Pomodoro!\n  Start your innovative work with Pomodoro.\nAnd complete your work timely and effectively.\n")        
		hbox_left.pack_start(label, True, True, 0)        
				
		self.add(vbox)        
		

		stack = Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(600)

		#checkbutton = Gtk.CheckButton(label="Click me!")
		#stack.add_titled(checkbutton, "check", "Check Button")
		
		# Section for Time Window Selection
		button = Gtk.Button.new_with_label("Select")
		button.connect("clicked", self.style_selector)
		stack.add_titled(button, "select-option", "Time Window Style Selection")

		# Section for Go-To Button       
		openbutton = Gtk.Button.new_with_label("Select")
		openbutton.connect("clicked", self.open_pomodoro)
		stack.add_titled(openbutton, "open-pomodoro-option", "Open Pomodoro")       
		
		
		# Section for Quit Button
		exitbutton = Gtk.Button.new_with_label("Select")
		exitbutton.connect("clicked", self.quit)
		stack.add_titled(exitbutton, "quit-option", "Exit")
		
		

		stack_switcher = Gtk.StackSwitcher()
		stack_switcher.set_stack(stack)
		vbox.pack_start(stack_switcher, True, True, 0)
		vbox.pack_start(stack, True, True, 0)
	
	def style_selector(self, button):
		print("Opening Time-Window Settings")
	
	def quit(self,exitbutton):
		print("Terminating Session")
		sys.exit()
		
	def open_pomodoro(self,openbutton):
		global counter
		print("Opening Pomodoro")    
		print("ID",counter)    
		if(counter==0):
			import todo
			todo.mymain()
			counter=1
		else:
			print("ELSE")
			#counter=0        
		



win = GTK_Project()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
