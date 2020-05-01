# -*- coding: utf-8 -*-
#!python

"""
Python script for ocr images using pytesseract library 
by: Iago Vargas

"""

import cv2
import pytesseract
import json
from pytesseract import Output

parse = argparse.ArgumentParser(description='OCR')
parse.add_argument('--f', type=str, required= True,  help='Input the image directory')
args = parse.parse_args()

archieve = args.f

img = cv2.imread(archieve)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

text = []

for i in d['text']:
    if i != '':
        text.append(i)

with open('text.json', 'w') as json_file:
    json.dump(text, json_file)

print('---------------Successfully-----------------')



__author__ = 'Iago Vargas'
__version__ = '0.0.1'
__maintener__ = 'Iago Vargas'
__email__ = 'iago.g.vargas@gmail.com'