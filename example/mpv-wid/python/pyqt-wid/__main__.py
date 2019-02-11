#!/usr/bin/env python3

import sys

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
		print('wid:', int(window.winId()))


		application.exec()
		#sys.exit(application._exec())


if __name__ == '__main__':
	App().run()
