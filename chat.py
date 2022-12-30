import openai
import os
import random
import tkinter as tk
from tkinter import *
root = tk.Tk()
key ="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"
openai.api_key = key
generate = tk.Button(text="Generate random excuse",font=('Arial',20))
def make_excuse():
    temp = random.uniform(0.9,1.5)
    seed = random.randint(0,1000)
    response = openai.Completion.create(model="text-davinci-003", prompt=f"Using the seed {seed}, generate an excuse without mentioning the seed;", temperature=temp, max_tokens=256)
    choices=response["choices"]
    choices_dict=choices[0]
    return choices_dict["text"]
make_excuse()
root.mainloop()