from anki.hooks import addHook
from aqt import mw
from aqt.qt import *
from aqt.editor import Editor
from aqt.gui_hooks import editor_will_load_note
from aqt.gui_hooks import browser_will_show_note
from aqt.webview import AnkiWebView
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
import os

class ChemPaintAnki:
    def __init__(self, addon_path):
        self.addon_path = addon_path
        self.webview = None

        addHook("unloadProfile", self.unload)

    def unload(self):
        if self.webview:
            self.webview.setParent(None)
            self.webview = None

    def jcp(self):
        # Load the JChemPaint applet files
        applet_core = os.path.join(self.addon_path, "web", "jchempaint-applet-core.jar")
        applet_editor = os.path.join(self.addon_path, "web", "jchempaint-applet-editor.jar")

        # Create a new dialog window
        dialog = QDialog(mw)
        dialog.setWindowTitle("JChemPaint Applet")
        dialog.setWindowModality(Qt.ApplicationModal)

        # Create a layout to hold the webview and a close button
        layout = QVBoxLayout(dialog)

        # Create a webview to display the JChemPaint applet
        self.webview = AnkiWebView(dialog)
        # self.webview.stdHtml("", js=[
        #     f"loadApplet('{applet_core}', '{applet_editor}');",
        # ])
		self.webview.stdHtml("", js=[
		    "<script src='web/jcp.js'></script>",  # include the JChemPaint library
		    "<script>loadApplet('web/jchempaint-applet-core.jar', 'web/jchempaint-applet-editor.jar');</script>",  # call the loadApplet function
		])

        layout.addWidget(self.webview)

        # Create a button to close the dialog
        button = QPushButton("Close", dialog)
        button.clicked.connect(dialog.reject)
        layout.addWidget(button)

        # Show the dialog
        dialog.exec_()

        # Clean up the webview
        self.webview.setParent(None)
        self.webview = None

    def add_button(self, editor):
        button = QAction(QIcon(os.path.join(self.addon_path, "icons", "jcp_icon.jpeg")), "JChemPaint", editor)
        button.triggered.connect(lambda _, ed=editor: self.on_button_clicked(ed))
        editor.toolbar.addSeparator()
        editor.toolbar.addAction(button)

    def on_button_clicked(self, editor):
        # Load the JChemPaint applet files
        applet_core = os.path.join(self.addon_path, "web", "jchempaint-applet-core.jar")
        applet_editor = os.path.join(self.addon_path, "web", "jchempaint-applet-editor.jar")

        # Create a new dialog window
        dialog = QDialog(mw)
        dialog.setWindowTitle("JChemPaint Applet")
        dialog.setWindowModality(Qt.ApplicationModal)

        # Create a layout to hold the webview and a close button
        layout = QVBoxLayout(dialog)

        # Create a webview to display the JChemPaint applet
        self.webview = AnkiWebView(dialog)
        self.webview.stdHtml("", js=[
            "<script src='web/jcp.js'></script>",  # include the JChemPaint library
            "<script>loadApplet('web/jchempaint-applet-core.jar', 'web/jchempaint-applet-editor.jar');</script>",  # call the loadApplet function
        ])

        layout.addWidget(self.webview)

        # Create a button to close the dialog
        button = QPushButton("Close", dialog)
        button.clicked.connect(dialog.reject)
        layout.addWidget(button)

        # Show the dialog
        dialog.exec_()

        # Clean up the webview
        self.webview.setParent(None)
        self.webview = None

    def browser_will_show_note_browser(web_engine, note, editor, addon_path):
	    if "JChemPaint" in note.model()["name"]:
	        applet_core = os.path.join(addon_path, "web", "jchempaint-applet-core.jar")
	        applet_editor = os.path.join(addon_path, "web", "jchempaint-applet-editor.jar")
	        web_engine.stdHtml("", js=[
	            "<script src='web/jcp.js'></script>",
	            "<script>loadApplet('web/jchempaint-applet-core.jar', 'web/jchempaint-applet-editor.jar');</script>",
	        ])	

chempaint_anki = ChemPaintAnki(os.path.dirname(os.path.abspath(__file__)))

def editor_will_load_note_editor(web_engine, editor, note):
    chempaint_anki.add_button(editor)

def browser_will_show_note_browser_wrapper(web_engine, note, editor):
    browser_will_show_note_browser(web_engine, note, editor, os.path.dirname(os.path.abspath(__file__)))

browser_will_show_note.append(browser_will_show_note_browser_wrapper)

editor_will_load_note.append(editor_will_load_note_editor)
# browser_will_show_note.append(browser_will_show_note_browser) #not sure if we still need this call?

addHook("browser_will_show_note", browser_will_show_note_browser)

