import openai
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import random
root = ThemedTk(theme="yaru")
root.geometry("700x700")
key ="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"
openai.api_key = key

def make_excuse():
    temp = random.uniform(0.9,1.5)
    seed = random.randint(0,1000)
    response = openai.Completion.create(model="text-davinci-003", prompt=f"Using the seed {seed}, generate an excuse without mentioning the seed;", temperature=temp, max_tokens=256)
    choices=response["choices"]
    choices_dict=choices[0]
    return choices_dict["text"]
excuse = ttk.Label(text="",wraplength=400,justify="center")

def command():
    excuse.config(text=make_excuse())
    excuse.pack()
generate = ttk.Button(text="Generate random excuse",command=command)
generate.place(anchor="center",relx=0.5,rely=0.8)

root.mainloop()