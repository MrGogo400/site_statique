# Projet générateur de site statique

## Présentation du projet.

La finalité de ce projet était de développer un outil permettant la conversion de fichiers markdown en fichiers HTML.

## La liste des commandes.

Voici les commandes disponibles :

`-i` ou `--input-directory` accompagné du chemin vers le dossier où se trouvent les fichiers .md à convertir.

`-o` ou `--output-directory`  accompagné tu chemin vers le dossier où vous avez choisie de mettre les fichiers converties en .html

`-h` ou `--help`  affiche les aide pour les commandes.

`-r` ou `--rainbow` transforme tout les texte en arc-en-ciel (Référence au "Double Rainbow" https://www.youtube.com/watch?v=MX0D4oZwCsA)


![COMMENT C BO](https://i.makeagif.com/media/11-26-2015/ATqgx3.gif)
## Comment ça marche ?

Ce script est simple d'utilisation.

Dans un terminal/CMD ou la console python et rendez vous dans le dossier ou ce trouve `sitestatique.py`.

Voici la commande a écrire :

    sitestatique.py -i Chemin_du_dossier_input -o Chemin_du_dossier_output
Ou

    sitestatique.py -input-directory Chemin_du_dossier_input -output-directory Chemin_du_dossier_output
Et pour avoir des beau arc-en-ciel il suffit de rajouter `-r` a la fin.

Comme ceci : 

    sitestatique.py -i Chemin_du_dossier_input -o Chemin_du_dossier_output -r

### Maintenant vous pouvez faire semblant d'être un hacker en modifiant des # en balise HTML

![enter image description here](https://i.imgur.com/ye5udHZ.gif)

(Pa
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1MDc4NDY3NiwxNzExNDY2NjM3LC0xMz
g1NDExODk5LDE0NzcwNDUyMzcsMTk2NDIzMDc1XX0=
-->