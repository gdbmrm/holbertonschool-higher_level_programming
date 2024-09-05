#!/usr/bin/python3
import sys
sys.path.append('/tmp')
import hidden_4
if __name__ == "__main__":
    fichier = dir(hidden_4)
    nb_module = len(fichier)
    for i in range(0, nb_module):
        if fichier[:1] != "_":
            print(fichier[i])