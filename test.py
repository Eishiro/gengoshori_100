#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:53:18 2020

@author: Eishiro
"""


import json
import re

with open('england_wiki.txt') as f:
    data = f.read()
    # the start of the line  is a bar ^|
    template = re.findall(r'^|(.*)\s=\s(.*)', data)

#    dict_template = {} #{field, data}
#    for i in range(len(template)):
#        dict_template[template[i][0]] = template[i][1]
    
    
    dict_template = {} #{field, data}
    for field in template:
        dict_template[field[i][0]] = template[i][1]


    dict_template = {}
    for field in template:
        if field[0] not in dict_template:
            dict_template[field[0]] = []
        dict_template[field[0]].append(field[1:])    