#! /usr/bin/env python3
# to execute the program, set the env variable KEY

import openai
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import os
import random

root = ThemedTk(theme="adapta")
root.geometry("700x400")
key = os.environ["KEY"]
openai.api_key = key
what = ttk.Entry()
photo = ImageTk.PhotoImage(file="icon.png")
noun = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate a noun of a living thing that needs an excuse, including the reason it needs one:",
    temperature=0.8,
    max_tokens=10,
)
noun2 = noun["choices"]
nounreal = noun2[0]
root.iconphoto(False, photo)
what.insert(0, nounreal["text"].strip())
what.config(foreground="gray")
autotext = True


def mouseclick(hello):
    global autotext
    autotext = False
    what.config(foreground="black")
    what.delete(0, "end")


what.bind("<Button-1>", mouseclick)


root.title("Random Excuse Generator")


def make_excuse(who, what2):
    temp = random.uniform(0.9, 1.2)
    seed = random.randint(0, 1000)
    prompt = f"Using the seed {seed}, generate an excuse using {what}, assuming you are {who} without mentioning the seed;"
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=temp, max_tokens=256
    )
    choices = response["choices"]
    choices_dict = choices[0]
    return choices_dict["text"]


excuse = ttk.Label(text="", wraplength=400, justify="center")


def command():
    global autotext
    who = what.get()
    what2 = what.get()
    if autotext:
        what.delete(0, "end")
    if what.get().strip() == "":
        noun = openai.Completion.create(
            model="text-davinci-003",
            prompt="Generate a noun of a living thing that needs an excuse, including the reason it needs one:",
            temperature=0.8,
            max_tokens=10,
        )
        noun2 = noun["choices"]
        nounreal = noun2[0]
        what.insert(0, nounreal["text"].strip())
        autotext = True
        what.config(foreground="gray")
        who = what.get()

    excuse.config(text=make_excuse(who, what2))
    excuse.place(anchor="center", relx=0.5, rely=0.3)


ttk.Label(text="Who are you? What did you do? Enter below.").place(
    anchor="center", relx=0.5, rely=0.65
)
generate = ttk.Button(text="Generate random excuse", command=command)
generate.place(anchor="center", relx=0.5, rely=0.92)

what.place(anchor="center", relx=0.5, rely=0.75)
root.configure(background="white")

root.mainloop()
