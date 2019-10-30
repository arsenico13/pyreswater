# PYRESWATER

> A simple python command-line utility to resize and watermarking images.


### Virtualenv

Dependencies are specified in the `requirements.txt` file as usual.


## Usage examples

Go inside the `watermark` folder and:


- Resize all pictures inside the `images` folder to a maximum of 1800 pixels
  and with no watermark:

    python watermark.py -n -r -m 1800 images


- Resize all pictures inside the `images` folder to a maximum of 2100 pixels,
  at 300dpi, with white watermark:

    python watermark.py -p -r -m 2100 images


- Resize the file `ciccibalicci.jpg` to a maximum of 2000 pixels and append the
  string `res` to the output file:

    python watermark.py -s res -r -m 2000 ciccibalicci.jpg


### DPI

If you don't specify the `-p` flag, all the processed images will be
scaled to 150dpi. If you use `-p` they will be at 300dpi.


#### Notes

This software grew up as a personal command-line tool to help me in my workflow
with my photos. It does what it's supposed to do.
Right now is quite versatile (for a side project with no time dedicated to it)
but has some limitations.

Feel free to try it. I may enhance it when the time comes...
