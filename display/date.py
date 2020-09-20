#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import datetime

timestring = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

try:
    epd = epd2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
    image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)    
    # Drawing on the image
    draw.text((110, 60), timestring, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    
    #epd.Clear(0xFF)
#     image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
#     draw = ImageDraw.Draw(image)
#     draw.text((110, 60), 'This', fill = 0)
#     epd.display(epd.getbuffer(image))
        
except Exception, e:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

