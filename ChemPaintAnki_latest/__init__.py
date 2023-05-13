from aqt import mw
from aqt.editor import EditorWebView
from aqt.qt import Qt
from aqt import QAction
from aqt.utils import showInfo

def launch_chempaint_editor():
    web = EditorWebView(mw)
    web.setWindowTitle("ChemPaintAnki")
    web.resize(800, 600)
    web.show()

    applet_code = "org.openscience.jchempaint.applet.JChemPaintEditorApplet"
    applet_archive = "_addons/ChemPaintAnki/web/jchempaint-applet-core.jar," \
                     "_addons/ChemPaintAnki/web/jchempaint-applet-editor.jar"
    applet_name = "JChemPaintEditorApplet"
    applet_params = {
        "codebase_lookup": "false",
        "implicitHs": "true",
        "boxBorder": "false",
        "language": "en",
    }

    html = f"""
        <html>
            <head>
                <title>ChemPaintAnki</title>
            </head>
            <body>
                <applet code="{applet_code}" archive="{applet_archive}" name="{applet_name}"
                        width="100%" height="100%" align="middle">
                    <param name="codebase_lookup" value="{applet_params['codebase_lookup']}">
                    <param name="implicitHs" value="{applet_params['implicitHs']}">
                    <param name="boxBorder" value="{applet_params['boxBorder']}">
                    <param name="language" value="{applet_params['language']}">
                </applet>
            </body>
        </html>
    """

    web.stdHtml(html)
    web.eval_("document.applets[0].resize(document.body.clientWidth, document.body.clientHeight);")
    web.eval_("document.applets[0].init();")

def setup():
    action = QAction("Launch ChemPaint Editor", mw)
    action.triggered.connect(launch_chempaint_editor)
    mw.form.menuTools.addAction(action)
