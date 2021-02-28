# PYRESWATER

> A simple python command-line utility to resize and watermarking images.


### Virtualenv

Dependencies are specified in the `requirements.txt` file as usual.


## Usage examples

The logo for the watermark has to be a `png` file with trasparency (otherwise
the result would not be so good...but it's you choice).

To start use `Pyreswater` go inside the `watermark` folder and:


- Resize all pictures inside the `images` folder to a maximum of 1800 pixels
  and with no watermark:

    `python watermark.py -n -r -m 1800 images`


- Resize all pictures inside the `images` folder to a maximum of 2100 pixels,
  at 300dpi, with white watermark:

    `python watermark.py -p -r -m 2100 images`


- Resize the file `ciccibalicci.jpg` to a maximum of 2000 pixels and append the
  string `res` to the output file:

    `python watermark.py -s res -r -m 2000 ciccibalicci.jpg`


- Resize the file `ciccibalicci.jpg` to a maximum of 2100 pixels using the png
  at the specified path:

    `python watermark.py -r -m 2100 -l "images/logo/Custom_Logo.png" ciccibalicci.jpg`


Just use `python watermark.py -h` to show the help text.


Right now, all the processed images go inside the `watermarked` folder. In the
future it will be possibile to save them beside the original.


### DPI

If you don't specify the `-p` flag, all the processed images will be
scaled to 150dpi. If you use `-p` (as in "print") they will be at 300dpi.


## Other resources and/or licenses

- Roboto Font: https://github.com/google/fonts/tree/main/apache/roboto


#### Notes

This software grew up as a personal command-line tool to help me in my workflow
with my photos. It does what it's supposed to do.
Right now is quite versatile (for a side project with no time dedicated to it)
but has some limitations.

Feel free to try it. I may enhance it when the time comes...

If you have any requests, open an issue (or make a pull request).
