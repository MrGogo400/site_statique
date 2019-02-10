#  Copyright (c) 2019 Hugo Marques
#  Copyright (c) 2012 Trent Mick
#  Copyright (c) 2010 ActiveState Software Inc.
#  Copyright ajouter car markdown2 est sous license MIT


import os
import re
import markdown2
import argparse
import sys

from os.path import splitext

sys.tracebacklimit = 0

link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]


head = "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'>\n<style>body {font-family: 'Open Sans', sans-serif;}</style></head>\n<body>\n"
rainbowhead = "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'>\n<style>body {font-family: 'Open Sans', sans-serif; -webkit-animation: body 3s infinite;} @-webkit-keyframes body{0%{color: orange;} 10%{color: purple;} 20%{color: red;} 30%{color: CadetBlue;} 40%{color: yellow;} 50%{color: coral;} 60%{color: green;} 70%{color: cyan;} 80%{color: DeepPink;} 90%{color: DodgerBlue;} 100%{color: orange;}</style></head>\n<body>\n"
EndHead = "</body>\n</html>"

def convert(md_input, html_output):
    liste = os.listdir(f''+md_input)
    for i in liste:
        f = open(f'{md_input}/{i}', "r")
        html = markdown2.markdown(f.read(), extras=["link-patterns"] ,link_patterns=link_patterns)
        nomdufichier = os.path.splitext(i)[0]
        print(f'Le fichier "{nomdufichier}" été convertie !')
        html_file = open(f'{html_output}/{nomdufichier}.html', 'w')
        html_file.write(head)
        html_file.write(html)
        html_file.write(EndHead)

def convertrainbow(md_input, html_output):
    liste = os.listdir(f''+md_input)
    for i in liste:
        f = open(f'{md_input}/{i}', "r")
        html = markdown2.markdown(f.read(), extras=["link-patterns"] ,link_patterns=link_patterns)
        nomdufichier = os.path.splitext(i)[0]
        print(f'Le fichier "{nomdufichier}" été convertie et en plus il y a tout plein de couleur !')
        html_file = open(f'{html_output}/{nomdufichier}.html', 'w')
        html_file.write(rainbowhead)
        html_file.write(html)
        html_file.write(EndHead)

print('Convertisseur de fichier au format .MD au format .html\n\n')

print('Voici à quoi votre commande doit ressembler : main.py -i chemin_vers_le_dossier_input -o chemin_vers_le_dossier_output\n\n')

print('Un exemple est disponible dans le readme.md\n\n')

parser = argparse.ArgumentParser()

parser.add_argument("-i", '--input_directory',help='Inserer le chemin du fichier .md')
parser.add_argument("-o", '--output_directory',help='Inserer le chemin du fichier .html')
parser.add_argument("-r", '--rainbow',action='store_true',help='Transforme le texte en arc-en-ciel')
args = parser.parse_args()

if args.rainbow is True:
  convertrainbow(args.input_directory, args.output_directory)
else:
  convert(args.input_directory, args.output_directory)

