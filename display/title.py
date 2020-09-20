#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
#import traceback
import sys

title = sys.argv[1]

epd = epd2in13.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)
    
image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)    

# Drawing on the image
draw.text((20, 20), title, fill = 0)
epd.display(epd.getbuffer(image))
time.sleep(2)