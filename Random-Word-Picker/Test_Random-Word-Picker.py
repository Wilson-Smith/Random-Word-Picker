# Libraries are here
from tkinter import *
import random
import requests
import os

def DictionaryAccess():
    # Open the dictionary file
    with open('C:\\Users\\utente\\Desktop\\Random-Word-Generator\\dictionary.txt', 'r') as f:
        # Read all the lines from the file
        lines = f.readlines()
    return lines
        
def WordPicker(lines):
    # Choose a random line from the file
    random_line = random.choice(lines)

    # Split the line by whitespace to get the word
    random_word = random_line.split()[0]
    return random_word

def Url(word):
    # Creation of the link
    url = 'https://www.urbandictionary.com/define.php?term=' + word + '/'
    return url

def button():
    while True:
        lines = DictionaryAccess()
        word = WordPicker(lines)

        url = Url(word)
        r = requests.get(url)

        # Launching Chrome if there is a real hentai
        if r.status_code != 404:
            os.system('start chrome --incognito '+'"' + url + '"')
            break

# Create object
root = Tk()

# Adjust window size
root.geometry("500x500")
root.configure(width=500, height=500)

# Set window center
root.eval('tk::PlaceWindow . center')

# Add image file

bg = PhotoImage(file="C:\\Users\\utente\\Desktop\\Random-Word-Generator\\background.png")

# Add icon file
root.iconbitmap('C:\\Users\\utente\\Desktop\\Random-Word-Generator\\icon.ico')

# Title window
root.title("Random Word Picker")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label2 = Label(root, text="...Create your wisdom...")
label2.pack(pady=50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)

#Creating The Button
button1 = Button(root, text="Learn", command=button)
#put on screen
button1.pack()

# move window center
winWidth = root.winfo_reqwidth()
winwHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
root.geometry("+{}+{}".format(posRight, posDown))

# Execute tkinter
root.mainloop()
