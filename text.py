# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:21:58 2021

@author: o
"""

def revword(word:str) -> str:
    new_word = ''
    for c in reversed(word):
        new_word+=c.lower()
    return new_word

def countword() -> int:
    count = 1
    with open('text.txt', 'r') as f:
        word = f.readline().rstrip()
        for line in f:
            for one_word in line.split(' '):                
                if (revword(one_word).strip() == word):
                    count = count+1
    f.close()
    return count