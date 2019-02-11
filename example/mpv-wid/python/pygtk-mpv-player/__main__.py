#!/usr/bin/env python3

import os
import subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class App:
	def run (self):
		window = Gtk.Window()
		window.resize(800, 600)
		window.connect('delete-event', self.quit)

		drawing_area = Gtk.DrawingArea()
		window.add(drawing_area)
		window.show_all()

		wid = drawing_area.get_property('window').get_xid()
		print('wid:', wid)

		self.mpv = subprocess.Popen(('mpv', '--wid={}'.format(wid) , os.path.expanduser('~/Videos/test.mp4')))
		self.mpv.poll()

		Gtk.main()

	def quit (self, widget, event):
		self.mpv.kill()
		Gtk.main_quit()

if __name__ == '__main__':
	App().run()
