# Foto-Frame Python Skript

## Beschreibung
Das Foto-Frame Python Skript ist ein einfaches, aber effektives Werkzeug zur Bearbeitung von JPEG-Bildern. Es ermöglicht dir, Bilder zu skalieren, einen Rahmen hinzuzufügen und EXIF-Daten beizubehalten. Es gibt auch einige vordefinierte Einstellungen (Presets), die für verschiedene Anwendungsfälle optimiert sind.

## Features
* Bilder skalieren
* Rahmen zu Bildern hinzufügen
* EXIF-Daten beibehalten
* Verschiedene voreingestellte Optionen: 'flickr', 'insta', 'print13'
* Benutzerdefinierte Einstellungen

## Anforderungen
* Python 3
* Pillow

## Installation der Abhängigkeiten
Um das Skript ausführen zu können, musst du sicherstellen, dass du Python 3 auf deinem Computer installiert hast. Außerdem benötigst du die Python-Bibliothek `Pillow`. Um diese Abhängigkeiten zu installieren, befolge bitte die unten stehenden Anweisungen.

### Windows:
1. Download und Installation von Python: Gehe zu https://www.python.org/downloads/windows/ und lade die neueste Version von Python herunter. Führe die Installationsdatei aus und folge den Anweisungen auf dem Bildschirm.

2. Installation von Pillow: Öffne die Windows-Befehlszeile (cmd) und gebe den folgenden Befehl ein: `pip install pillow`

### MacOS:
1. Download und Installation von Python: Gehe zu https://www.python.org/downloads/mac-osx/ und lade die neueste Version von Python herunter. Führe die Installationsdatei aus und folge den Anweisungen auf dem Bildschirm.

2. Installation von Pillow: Öffne das Terminal und gebe den folgenden Befehl ein: `pip3 install pillow`

## Verwendung
Navigiere in der Befehlszeile oder im Terminal zu dem Verzeichnis, in dem das Skript `main.py` gespeichert ist. 

Gib den folgenden Befehl ein, um das Skript auszuführen:

`python main.py <input_folder> <output_folder> -preset <preset>`

Ersetze `<input_folder>` durch den Pfad zum Ordner, der die zu bearbeitenden Bilder enthält. Ersetze `<output_folder>` durch den Pfad zum Ordner, in den die bearbeiteten Bilder gespeichert werden sollen. Ersetze `<preset>` mit dem Namen des Presets, das du verwenden möchtest ('flickr', 'insta' oder 'print13'). 

Beispiel:

`python main.py /Users/meinname/Desktop/orig /Users/meinname/Desktop/framed -preset flickr`

## Support
Wenn du Hilfe benötigst oder einen Fehler findest, erstelle bitte ein neues Issue in diesem Repository.

---

# Foto-Frame Python Script

## Description
The Foto-Frame Python script is a simple yet effective tool for editing JPEG images. It allows you to scale images, add a frame, and retain EXIF data. There are also several predefined settings (presets) that are optimized for different use cases.

## Features
* Scale images
* Add frame to images
* Keep EXIF data
* Various preset options: 'flickr', 'insta', 'print13'
* Custom settings

## Requirements
* Python 3
* Pillow



## Installing Dependencies
To run the script, you need to ensure that you have Python 3 installed on your computer. You will also need the Python library `Pillow`. To install these dependencies, please follow the instructions below.

### Windows:
1. Download and Install Python: Go to https://www.python.org/downloads/windows/ and download the latest version of Python. Run the installer and follow the on-screen instructions.

2. Install Pillow: Open the Windows Command Prompt (cmd) and enter the following command: `pip install pillow`

### MacOS:
1. Download and Install Python: Go to https://www.python.org/downloads/mac-osx/ and download the latest version of Python. Run the installer and follow the on-screen instructions.

2. Install Pillow: Open the Terminal and enter the following command: `pip3 install pillow`

## Usage
Navigate to the directory containing the `main.py` script in the command line or Terminal. 

Enter the following command to run the script:

`python main.py <input_folder> <output_folder> -preset <preset>`

Replace `<input_folder>` with the path to the folder containing the images to be edited. Replace `<output_folder>` with the path to the folder where the edited images should be saved. Replace `<preset>` with the name of the preset you want to use ('flickr', 'insta' or 'print13'). 

Example:

`python main.py /Users/myname/Desktop/orig /Users/myname/Desktop/framed -preset flickr`

## Support
If you need help or find a bug, please create a new issue in this repository.