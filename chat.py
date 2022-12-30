import openai
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

import os
import random
root = ThemedTk(theme="adapta")
root.geometry("700x400")
key ="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"
openai.api_key = key
what = ttk.Entry()
photo = ImageTk.PhotoImage(file = "icon.png")
noun = openai.Completion.create(model="text-davinci-003", prompt="Generate a noun of a living thing without punctuation:", temperature=0.8, max_tokens=10)
noun2 = noun["choices"]
nounreal=noun2[0]
root.iconphoto(False, photo)
what.insert(0, nounreal["text"].strip())
what.config(foreground="gray")
root.bind("<Key>", key)

def mouseclick(hello):
    what.config(foreground="gray")
    what.delete(0,"end")
root.bind("<Button-1>", mouseclick)


root.title("Random Excuse Generator")
def make_excuse(who):
    temp = random.uniform(0.9,1.2)
    seed = random.randint(0,1000)
    prompt=f"Using the seed {seed}, generate an excuse assuming you are {who} without mentioning the seed;"
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=temp, max_tokens=256)
    choices=response["choices"]
    choices_dict=choices[0]
    return choices_dict["text"]

excuse = ttk.Label(text="",wraplength=400,justify="center")

def command():
    what.delete(0,"end")
    who=what.get()
    noun = openai.Completion.create(model="text-davinci-003", prompt="Generate a noun of a living thing without punctuation:", temperature=0.8, max_tokens=10)
    noun2 = noun["choices"]
    nounreal=noun2[0]
    what.insert(0, nounreal["text"].strip())
    what.config(foreground="gray")
    excuse.config(text=make_excuse(who))
    excuse.place(anchor="center",relx=0.5,rely=0.3)
generate = ttk.Button(text="Generate random excuse",command=command)
generate.place(anchor="center",relx=0.5,rely=0.7)
ttk.Label(text="Who are you? Enter below.").place(anchor="center",relx=0.5,rely=0.85)
what.place(anchor="center",relx=0.5,rely=0.95)
root.configure(background='white')

root.mainloop()