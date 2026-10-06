# PyInstaller recipe for the Bhrams desktop app.
#   macOS:   pyinstaller packaging/bhrams.spec   -> dist/Bhrams.app
#   Windows: pyinstaller packaging/bhrams.spec   -> dist/Bhrams/Bhrams.exe
import os, sys
# The project folder is the one above this "packaging" folder, wherever PyInstaller is started from.
ROOT = os.path.dirname(os.path.abspath(SPECPATH))
sys.path.insert(0, ROOT)
from config import VERSION
datas = [(os.path.join(ROOT, "templates"), "templates"), (os.path.join(ROOT, "static"), "static")]
hidden = ["app", "auth", "db", "config", "mailer", "payments", "quotes", "finder", "assist", "licensing",
          "reportlab.graphics.barcode.common", "reportlab.graphics.barcode.code128"]
icon = os.path.join(ROOT, "packaging", "bhrams.icns" if sys.platform == "darwin" else "bhrams.ico")

a = Analysis([os.path.join(ROOT, "desktop.py")], pathex=[ROOT], datas=datas, hiddenimports=hidden,
             excludes=["tkinter", "matplotlib", "numpy", "pandas", "PyQt5", "PyQt6", "PySide2", "PySide6", "IPython"],
             noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="Bhrams", console=False, icon=icon,
          upx=False, disable_windowed_traceback=False, argv_emulation=False,
          version=os.path.join(ROOT, "packaging", "version_info.txt") if sys.platform == "win32" else None)
coll = COLLECT(exe, a.binaries, a.datas, name="Bhrams", upx=False)

if sys.platform == "darwin":
    app = BUNDLE(coll, name="Bhrams.app", icon=icon, bundle_identifier="in.bhrams.desktop", version=VERSION,
                 info_plist={
                     "CFBundleName": "Bhrams", "CFBundleDisplayName": "Bhrams",
                     "CFBundleShortVersionString": VERSION, "CFBundleVersion": VERSION,
                     "NSHighResolutionCapable": True, "LSMinimumSystemVersion": "11.0",
                     "LSApplicationCategoryType": "public.app-category.business",
                     "NSHumanReadableCopyright": "© Bhrams",
                     "NSAppTransportSecurity": {"NSAllowsLocalNetworking": True},
                 })
