function loadApplet(coreJarUrl, editorJarUrl) {
  // Set up the applet parameters
  var appletParams = {
    codebase: "web/",
    archive: coreJarUrl + "," + editorJarUrl,
    code: "org.jmol.applet.JChemPaintApplet.class",
    name: "jcp",
    width: "100%",
    height: "100%",
    mayscript: "true"
  };

  // Embed the applet in the webview
  var appletContainer = document.createElement("div");
  appletContainer.style.width = "100%";
  appletContainer.style.height = "100%";
  document.body.appendChild(appletContainer);
  new Jmol._Applet("jcp", appletParams, appletContainer);
}
