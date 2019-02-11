
## How to test

run

``` sh
$ ./__main__.py
```


## Reference

* man [mpv](http://manpages.ubuntu.com/manpages/bionic/en/man1/mpv.1.html#options)
* mpv / Manual / Options / Window / [--wid](https://mpv.io/manual/master/#options-wid)
* https://docs.python.org/3/library/functions.html#int
* https://doc.qt.io/qt-5/reference-overview.html
* https://doc.qt.io/qt-5/qwidget.html#winId
* https://doc.qt.io/qt-5/qtglobal.html#quint64-typedef
* https://doc.qt.io/qt-5/qtglobal.html#quintptr-typedef
* https://doc.qt.io/qt-5/qcoreapplication.html#aboutToQuit
* http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html


## Explore

run

``` sh
$ dpkg -L qtbase5-dev | grep qwindowdefs.h
```

show

```
/usr/include/x86_64-linux-gnu/qt5/QtGui/qwindowdefs.h
```

run

``` sh
$ dpkg -L qtbase5-dev | grep qglobal.h
```

show

```
/usr/include/x86_64-linux-gnu/qt5/QtCore/qglobal.h
```

run

``` sh
$ apt-get source qtbase5-dev
```

then find

* qtbase-opensource-src-5.9.5+dfsg/src/gui/kernel/qwindowdefs.h
* qtbase-opensource-src-5.9.5+dfsg/src/corelib/global/qglobal.h


## Related

* [pyqt-wid](../pyqt-wid)
