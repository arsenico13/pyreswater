# Watermark python jack


## Link utili:

- Ridimensionare una immagine mantenendo il rapporto giusto - resize imagine maintaining ratio - https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio#273962
- Ridimensionare, molto più chiara come spiegazione: https://stackoverflow.com/questions/24745857/python-pillow-how-to-scale-an-image

    Define a maximum size.
    Then, compute a resize ratio by taking min(maxwidth/width, maxheight/height).
    The proper size is oldsize*ratio.
