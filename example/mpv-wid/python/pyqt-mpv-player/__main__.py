#!/usr/bin/env python3

import os
import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QWidget

class App:
	def run (self):
		application = QApplication(sys.argv)

		window = QWidget()
		window.setWindowTitle('Play Window')
		window.resize(800, 600)
		window.move(200, 200)


		window.show()
		# print(window.winId()) # <sip.voidptr object at 0x7f3c7f122eb8>
		# print(dir(window.winId()))
		#print('wid:', int(window.winId()))
		wid = int(window.winId())
		print(wid)


		self.mpv = subprocess.Popen(('mpv', '--wid={}'.format(wid), os.path.expanduser('~/Videos/test.mp4')))
		self.mpv.poll()


		application.exec()
		#sys.exit(application._exec())

	def quit (self):
		self.mpv.kill()


if __name__ == '__main__':
	App().run()
