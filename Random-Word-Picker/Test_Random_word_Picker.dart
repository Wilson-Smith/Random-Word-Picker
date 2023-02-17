# Libraries are here
from tkinter import *
import random
import requests
import os

#include <string>

void DictionaryAccess():
    // Open the dictionary file
    with open('C:\\Users\\utente\\Desktop\\Random-Word-Generator\\dictionary.txt', 'r') as f:
        # Read all the lines from the file
        lines = f.readlines()
    return lines
        
def WordPicker(lines):
    // Choose a random line from the file
    random_line = random.choice(lines)

    // Split the line by whitespace to get the word
    random_word = random_line.split()[0]
    return random_word

def Url(word):
    // Creation of the link
    url = 'https://www.urbandictionary.com/define.php?term=' + word + '/'
    return url

def button():
    while true:
        string lines = DictionaryAccess()
        word = WordPicker(lines)

        url = Url(word)
        r = requests.get(url)

        // Launching Chrome if there is a real hentai
        if r.status_code != 404:
            os.system('start chrome --incognito '+'"' + url + '"')
            break

