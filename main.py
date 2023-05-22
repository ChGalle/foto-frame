import os
import argparse
from PIL import Image, ImageOps, UnidentifiedImageError

# Preset Werte (längste Seite, Rahmenfarbe, Rahmengröße, Beibehaltung der EXIF-Daten)
preset_values = {
    'flickr': {
        'max_size': 2048,
        'frame_color': 'w',
        'frame_size': 50,
        'keep_exif': True,
        'quality': 95
    },
    'insta': {
        'max_size': 1080,
        'frame_color': 'w',
        'frame_size': 50,
        'keep_exif': False,
        'quality': 90
    },
    'print13': {
        'max_size': 2126,
        'frame_color': None,
        'frame_size': None,
        'keep_exif': False,
        'quality': 100
    }
}

def add_frame_and_resize(input_folder, output_folder, preset=None):
    # Überprüfe, ob ein gültiges Preset angegeben wurde
    if preset and preset not in preset_values:
        raise ValueError("Ungültiges Preset. Verwenden Sie 'flickr', 'insta' oder 'custom'.")

    # Lese die Werte aus dem Preset oder verwende Standardwerte
    if preset:
        params = preset_values[preset]
        max_size = params['max_size']
        frame_color = params['frame_color']
        frame_size = params['frame_size']
        keep_exif = params['keep_exif']
        quality_set = params['quality']
    else:
        # Verwende hier Standardwerte, wenn kein Preset angegeben wurde
        max_size = None
        frame_color = None
        frame_size = None
        keep_exif = True
        quality_set = 100

    color_map = {"w": (255, 255, 255), "b": (0, 0, 0)}

    # Erstelle das Ausgabeverzeichnis, wenn es noch nicht existiert
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Durchsuche alle Dateien im Eingangsordner
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            print(f"Verarbeite {filename}...")
            image_path = os.path.join(input_folder, filename)
            try:
                # Öffne das Bild
                image = Image.open(image_path)
                image = ImageOps.exif_transpose(image)

                # Behalte die EXIF-Daten bei, wenn gewünscht
                exif = None
                if keep_exif and "exif" in image.info:
                    exif = image.info["exif"]

                # Füge einen Rahmen hinzu, wenn gewünscht
                if frame_size is not None and frame_color is not None:
                    if frame_color.lower() not in color_map:
                        raise ValueError("Ungültiger Farbkürzel. Verwenden Sie 'w' für weiß oder 'b' für schwarz.")
                    frame_color_rgb = color_map[frame_color.lower()]
                    image = ImageOps.expand(image, border=frame_size, fill=frame_color_rgb)

                # Skaliere das Bild, wenn eine maximale Größe angegeben ist
                if max_size is not None:
                    image.thumbnail((max_size, max_size), Image.LANCZOS)

                # Speichere das bearbeitete Bild
                output_path = os.path.join(output_folder, (f"{preset}_")+filename)
                if keep_exif and exif is not None:
                    image.save(output_path, "JPEG", quality=quality_set, exif=exif)
                else:
                    image.save(output_path, "JPEG", quality=quality_set)

            except (IOError, UnidentifiedImageError):
                print(f"Kann {filename} nicht öffnen. Überspringe diese Datei.")
                continue

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Fügt einen Rahmen zu allen JPEG-Bildern in einem Ordner hinzu und skaliert sie entsprechend einem ausgewählten Preset.')
    parser.add_argument('input_folder', type=str, help='Pfad zum Eingangsordner')
    parser.add_argument('output_folder', type=str, help='Pfad zum Ausgabeordner')
    parser.add_argument('-preset', type=str, default=None, help="Optional: Preset für die Skalierung und Rahmenoptionen. Verwenden Sie 'flickr', 'insta' oder 'custom'.")
    args = parser.parse_args()
    add_frame_and_resize(args.input_folder, args.output_folder, args.preset)
