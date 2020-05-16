<<<<<<< HEAD
#!/usr/bin/env python2

from __future__ import print_function

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from os import path


def filechooser(pathname):
    dialog = Gtk.FileChooserDialog("Open ...", None,
                                   Gtk.FileChooserAction.OPEN,
                                   (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                    Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

    dialog.set_default_response(Gtk.ResponseType.OK)
    dialog.set_current_folder(pathname)

    filter = Gtk.FileFilter()
=======
#!/usr/bin/env python

from __future__ import print_function

import gtk
from os import path


if gtk.pygtk_version < (2, 3, 90):
    print("Please upgrade your pygtk")
    raise SystemExit


def filechooser(pathname):
    dialog = gtk.FileChooserDialog("Open ...", None,
                                   gtk.FILE_CHOOSER_ACTION_OPEN,
                                   (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                    gtk.STOCK_OPEN, gtk.RESPONSE_OK))

    dialog.set_default_response(gtk.RESPONSE_OK)
    dialog.set_current_folder(pathname)

    filter = gtk.FileFilter()
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
    filter.set_name("Airframe File")
    filter.add_pattern("*.xml")
    dialog.add_filter(filter)

    response = dialog.run()
    filename = ""
<<<<<<< HEAD
    if response == Gtk.ResponseType.OK:
        filename = dialog.get_filename()
    elif response == Gtk.ResponseType.CANCEL:
=======
    if response == gtk.RESPONSE_OK:
        filename = dialog.get_filename()
    elif response == gtk.RESPONSE_CANCEL:
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
        print("No file selected")

    dialog.destroy()
    return filename


def error_loading_xml(s):
<<<<<<< HEAD
    err_msg = Gtk.MessageDialog(None, Gtk.DIALOG_DESTROY_WITH_PARENT,
                                Gtk.MESSAGE_ERROR, Gtk.BUTTONS_CLOSE,
=======
    err_msg = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT,
                                gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE,
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
                                "Error Loading XML: " + s)
    err_msg.run()
    err_msg.destroy()


def about(home):
<<<<<<< HEAD
    about_d = Gtk.AboutDialog()
=======
    about_d = gtk.AboutDialog()
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
    about_d.set_program_name("Paparazzi Airframe Editor")
    about_d.set_version("0.1")
    about_d.set_copyright("(c) GPL v2")
    about_d.set_comments("Airframe Editor")
    about_d.set_website("http://paparazzi.github.io")
<<<<<<< HEAD
    about_d.set_logo(GdkPixbuf.Pixbuf.new_from_file(path.join(home, "data/pictures/penguin_icon.png")))
=======
    about_d.set_logo(gtk.gdk.pixbuf_new_from_file(path.join(home, "data/pictures/penguin_icon.png")))
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
    about_d.run()
    about_d.destroy()

