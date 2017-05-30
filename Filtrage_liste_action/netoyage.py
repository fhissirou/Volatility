#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys



fichier = open("actions_a_traiter.csv", "r")

inlistes= fichier.readlines()
liste_propre=[]
lnom1=[]
lnom2=[]
for line in inlistes:
	tab_lines=line.split(',')
	lnom1.append(tab_lines[0])
	lnom2.append(tab_lines[5].replace('\n',""))

file_save= open("save_action.csv", "w+")
for line in inlistes:
	tab_lines=line.split(',')
	nom = tab_lines[0]
	if nom in lnom2:
		file_save.write(str(tab_lines[0])+",")
		file_save.write(str(tab_lines[1])+",")
		file_save.write(str(tab_lines[2])+",")
		file_save.write(str(tab_lines[3])+",")
		file_save.write(str(tab_lines[4])+"\n")


file_save.close()
fichier.close()

