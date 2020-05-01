# Language Detection from Receipts' images

This is a simple python script to detect in which language the recipe images were written in. The process consists of two steps: the first is to transform the image into a text file, for this purpose the “pytesseract” library was used. The second step is to identify in which language the text was written, for this step the python library “langdetect” was used. 

## Getting Started

To use this script clone this repository on your local machine and execute the following commands into the directory:

```
python ocr_document.py --f "[Insert here the image path]"
```
The above command will transform the image in a ".json" file containing the recognized text.
Use the ".json" file generated in the previous step in the follow command:

```
python lang_detect.py --f "[Insert here the '.json' file path]"

```
The output will be a string with the language detected in the text, as in the example below:
```
Your text is write in 'en'.
```




