#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class App:
	def run (self):
		window = Gtk.Window()
		window.resize(800, 600)
		window.connect('delete-event', Gtk.main_quit)

		drawing_area = Gtk.DrawingArea()
		window.add(drawing_area)
		window.show_all()

		wid = drawing_area.get_property('window').get_xid()
		print('wid:', wid)

		Gtk.main()

if __name__ == '__main__':
	App().run()
