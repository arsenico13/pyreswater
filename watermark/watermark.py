# -*- coding: utf-8 -*-

'''

Author    : Giacomo Monari (arsenico13)
Github    : https://github.com/arsenico13
License   : GPLv3


Copyright (c) 2017-2019  - Giacomo Monari (arsenico13)

This file is part of Pyreswater.

Pyreswater is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pyreswater is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pyreswater (see the COPYING file).
If not, see <http://www.gnu.org/licenses/>.

'''

# Usage example:
# Singola immagine con resize settato a 1100:
#   python watermark.py -r -m 1100 images/DSC_9521.jpg
# Cartella con resize di default:
#   python watermark.py images/ -r
# Singola immagine con resize settato a 1400 e logo nero:
#   python watermark.py -r -m 1400 -b images/DSC_1234.jpg
# E' possibile usare questo script anche solo per eseguire un resize di una
# immagine aggiungengo il flag -n/--no-watermark:
#   python watermark.py -n -r -m 1000 images/
# Watermark e resize ottimizzato per la stampa -> MARGINE 150px:
#   python watermark.py -r --print -m 3600 images/

from _colorized.banner import banner
from datetime import datetime as dt
from __init__ import __version__

import argparse
import errno
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont  # noqa
except ImportError:
    exit("This script requires the PIL module.\n"
         "Install with pip install Pillow."
         )


class ScriptConf():
    """
    This class contains all the configuration parameters.

    Args:
        margin (int): la distanza in pixel come margine tra bordo e watermark
        suffix (str): il suffisso che verrà aggiunto al file finale
        dest_path (str): il percorso della cartella in cui salvare i file
        image_quality (int): la qualità in output dell'immagine
        max_size (int): la dimensione massima in pixel del lato più lungo
                        dell'immagine finale processata

    Attributes:
        LOGO (str): il percorso del logo da usare
        DPI (tuple): risoluzione dell'immagine in punti per pollice
        ACCEPTED_EXT (list): elenco delle estensioni di file accettate
    """

    LOGO = ""
    DPI = (300, 300)
    ACCEPTED_EXT = ['.jpg', '.JPG', '.jpeg']
    RESIZE = True
    WATERMARK = True

    def __init__(
            self,
            margin=20,
            suffix="wm",
            dest_path="watermarked/",
            image_quality=95,
            max_size=1700,
            logo_path="images/logo/Arsenico13_White.png",
            ):
        self.margin = margin
        self.suffix = suffix
        self.dest_path = dest_path
        self.image_quality = image_quality
        self.max_size = max_size
        self.LOGO = logo_path

# LOGO_WHITE = "images/logo/Arsenico13_White.png"
# LOGO_BLACK = "images/logo/Arsenico13_Black.png"
# 20px = circa 0,17cm a (300dpi)
# 130px = circa 1,10cm a (300dpi)
# MARGIN = 20     # distanza tra il bordo e l'inizio del watermark in pixel
# SUFFIX = "_wm"  # suffisso che viene 'appeso' al nome del file
# DEST_PATH = "watermarked/"
# IMAGE_QUALITY = 95
# MAX_SIZE_DEFAULT = 1700  # max pixel per ogni lato
# PRINT_DPI = (300, 300) # A tuple of integers representing pixel density (x,y)
# ACCEPTED_EXT = ['.jpg', '.JPG', '.jpeg']  # lista estensioni di file ammesse


def _destination_folder(path):
    """ Questo metodo controlla se il percorso di destinazione esiste.
    In caso contrario, lo crea.
    """

    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def check_watermark_size(photo, watermark):
    """ Questo metodo controlla il rapporto tra le dimensioni della foto
    e il watermark stesso.
    Non deve essere troppo grande rispetto all'immagine finale (direi non oltre
    il 15% della dimensione).
    """

    perc = (100 * watermark.width) / photo.width

    if perc > 13:
        max_width = (13 * photo.width) / 100
        watermark.thumbnail((max_width, max_width), Image.ANTIALIAS)

    return watermark


def watermark_offset(photo, watermark, margin=ScriptConf().margin):
    """ Questo metodo calcola le coordinate a cui inserire il watermark.
    photo e watermark sono due oggetti 'Image' di PIL.
    margin è il margine da lasciare su ogni lato della foto finale.

    Restituisce una tupla (x, y)
    """
    photo_l, photo_h = photo.size
    watermark_l, watermark_h = watermark.size

    y_offset = photo_h - watermark_h - margin
    x_offset = margin

    return x_offset, y_offset


def get_file_name(
        config,
        filename="photo",
        prefix="",
        suffix="_wm",
        date=True,
        ext='.jpg'):
    """ Restituisce una stringa da usare come filename per salvare l'immagine.

    date: specifica se inserire o meno la data (AAAA-MM-DD) nel nome.
    """

    suffix = config.suffix or suffix

    file_name = [
        config.dest_path,
        prefix,
        filename,
        suffix,
    ]

    if date:
        file_name.append('_')
        file_name.append(str(dt.now().day))
        file_name.append('-')
        file_name.append(str(dt.now().month))
        file_name.append('-')
        file_name.append(str(dt.now().year))

    file_name.append(ext)

    return "".join(file_name)


def watermark_photo(
        photo_path,
        config,
        ):
    """ Funzione principale che mette il watermark su una foto.
    """
    photo = Image.open(photo_path)
    watermark = Image.open(config.LOGO)

    if config.RESIZE:
        max_size = (config.max_size, config.max_size)
        photo.thumbnail(max_size, Image.ANTIALIAS)

    if config.WATERMARK:
        # Eseguiamo il watermark solo se vogliamo
        watermark = check_watermark_size(photo, watermark)
        wm_offset = watermark_offset(photo, watermark, margin=config.margin)

        photo.paste(watermark, wm_offset, watermark)

    cwd = os.getcwd()
    filepath, complete_file_name = os.path.split(photo_path)
    file_name = os.path.splitext(complete_file_name)
    destination_path = os.path.join(
        cwd,
        get_file_name(
            config,
            filename=file_name[0],
            date=False,
        ),
    )

    photo.save(
        destination_path,
        quality=config.image_quality,
        optimize=False,
        dpi=config.DPI,
    )

    sys.stdout.write("Watermarked image: {}\n".format(destination_path))


def main():
    # Arguments
    version = "%(prog)s {version}".format(version=__version__)
    description = 'Tool per applicare watermark a delle foto.'
    parser = argparse.ArgumentParser(
        description=description,
        conflict_handler="resolve")
    parser.add_argument('image', help="image or a folder", type=str)

    general = parser.add_argument_group("General")

    parser.add_argument(
        "-a",
        "--margin",
        help="Margin for the watermark (pixel).",
        type=int,
        )
    parser.add_argument(
        "-b",
        "--black",
        help="Use the black logo instead of " \
             "the white one (which is the default)",
        action="store_true",
        )

    general.add_argument(
        '-h', '--help',
        action='help',
        help="Shows the help.")
    parser.add_argument(
        "-m",
        "--max-size",
        help="Specify max pixel size of the watermarked image. Requires the -r"
             " option.",
        type=int,
        )
    parser.add_argument(
        "-n",
        "--no-watermark",
        help="Flag. Just resize the images without the watermark. Requires -r",
        action="store_true",
        )
    parser.add_argument(
        "-p",
        "--print-size",
        help="Flag. Set the DPI to 300 even when resizing the image.",
        action="store_true",
        )
    parser.add_argument(
        "-r",
        "--resize",
        help="Flag. Resize the watermarked image.",
        action="store_true",
        )

    parser.add_argument(
        '-s',
        "--suffix",
        help="String. Text to append at the end of the processed image.",
        type=str
    )

    parser.add_argument(
        '-l',
        "--logo",
        help="String. The path for the watermark png file.",
        type=str
    )

    args = parser.parse_args()

    suffix = "".join(["_", args.suffix]) if args.suffix else "_wm"

    print(f"Suffisso file in uscita: {suffix}")

    if args.margin:
        conf = ScriptConf(margin=args.margin, suffix=suffix)
    else:
        conf = ScriptConf(suffix=suffix)

    if args.no_watermark and not args.resize:
        raise argparse.ArgumentError(
            argument=None,
            message="If you specify the no-watermark option, -r is required!")
    else:
        conf.WATERMARK = not args.no_watermark

    if args.resize:
        conf.RESIZE = True
        if not args.print_size:
            conf.DPI = (150, 150)
        if args.max_size:
            conf.max_size = args.max_size
            print("Dimensione max finale: {}".format(args.max_size))
        else:
            print("e allora dimensione standard...{}".format(conf.max_size))
    else:
        conf.RESIZE = False

    image = args.image

    if args.logo:
        print(args.logo)
        conf.LOGO = args.logo

    if args.black:
        conf.LOGO = "images/logo/Arsenico13_Black.png"

    if os.path.isfile(image):
        # Watermark di una singola immagine
        filename, file_extension = os.path.splitext(image)
        if file_extension in conf.ACCEPTED_EXT:
            watermark_photo(
                args.image,
                config=conf,
            )
        else:
            print("Devi specificare un'immagine.")
            print("Estesioni di file consentite: {}".format(conf.ACCEPTED_EXT))
    elif os.path.isdir(image):
        # E' stata specificata una cartella. Non andiamo ricorsivamente ma
        # cerchiamo solo i file che hanno una certa estensione.
        for fileobj in os.listdir(image):
            filename, file_extension = os.path.splitext(fileobj)
            if file_extension in conf.ACCEPTED_EXT:
                print("Trovato file immagine: {}".format(fileobj))
                watermark_photo(
                    os.path.join(os.path.abspath(image), fileobj),
                    config=conf,
                )
    else:
        raise


if __name__ == '__main__':
    sys.stdout.write(banner(__version__))
    main()
