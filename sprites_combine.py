import sys
from PIL import Image
import glob
total_width = 256
max_height = 64
for i in range(1, 1523):
    if i >= 1431 and i <= 1433:
        pass
    else:
        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        im=Image.open('sprites/front/' + str(i) + '.png')
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
        im=Image.open('sprites/front-shiny/' + str(i) + '.png')
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
        im=Image.open('sprites/back/' + str(i) + '.png')
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
        im=Image.open('sprites/back-shiny/' + str(i) + '.png')
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
        new_im.save('sprites/sheets/' + str(i) + '.png')