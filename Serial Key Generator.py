import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

Alphabet = "BCDFGHJKMNPQRTVWXY2346789"

def key(keyLength=25):
    chars = []

    for i in range(keyLength):
        chars.append(Alphabet[random.randrange(len(Alphabet))])
    return "".join(chars)

print("Serial Key Generator v1.0.0 By suiken-Developer\n\nYour Serial Key:\n" + key())
