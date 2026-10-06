; Inno Setup script: turns dist\Bhrams into a normal Windows installer (BhramsSetup.exe).
; Build with:  iscc packaging\installer.iss
#define AppVersion "1.0.0"
[Setup]
AppId={{6B1E3C2A-9D4F-4E7A-B369-369036903690}
AppName=Bhrams
AppVersion={#AppVersion}
AppPublisher=Bhrams
DefaultDirName={autopf}\Bhrams
DefaultGroupName=Bhrams
UninstallDisplayIcon={app}\Bhrams.exe
OutputDir=..\dist
OutputBaseFilename=BhramsSetup-{#AppVersion}
SetupIconFile=bhrams.ico
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesInstallIn64BitMode=x64compatible

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Shortcuts:"

[Files]
Source: "..\dist\Bhrams\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Bhrams"; Filename: "{app}\Bhrams.exe"
Name: "{autodesktop}\Bhrams"; Filename: "{app}\Bhrams.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Bhrams.exe"; Description: "Open Bhrams now"; Flags: nowait postinstall skipifsilent
