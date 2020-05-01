# -*- coding: utf-8 -*-
#!python

"""
Python script for language detection from text documents using langdetect library
by: Iago Vargas

"""


import json
from langdetect import detect 

parse = argparse.ArgumentParser(description='Language Detection')
parse.add_argument('--f', type=str, required= True,  help='Input the json file directory')
args = parse.parse_args()

archieve = args.f

file = archieve

def processing(route):
    try:
        archieve_json = open(route, 'r', encoding="utf8")
        data_json = json.load(archieve_json)
        archieve_json.close()
    except Exception as erro:
        print("error occured : {}".format(erro))

    def create_string(archieve_json):
        data = []
        for i in archieve_json:
            data.append(i)
        return data
    
    def listToString(data):
        str1 = " "
        return(str1.join(data))

    def removeUndesired(data_string):
        result = ''.join([i for i in data_string if not i.isdigit()])
        result = result.replace('*',' ').replace('#',' ').replace('%',' ').replace('/',' ').replace(':',' ')
        result = result.lower()
        return result
    
    data = create_string(data_json)
    data_string = listToString(data)
    final_string = removeUndesired(data_string)

    return final_string

text = processing(file)
lg = detect(text)

print('Your text is write in {}'.format(lg))


__author__ = 'Iago Vargas'
__version__ = '0.0.1'
__maintener__ = 'Iago Vargas'
__email__ = 'iago.g.vargas@gmail.com'
