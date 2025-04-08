[Setup]
AppName=SigaText
AppVersion=1.0
DefaultDirName={pf}\SigaText
DefaultGroupName=SigaText
OutputDir=.\Instaladores
OutputBaseFilename=instalador

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SigaText"; Filename: "{app}\main.exe"
