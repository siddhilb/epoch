import tkinter as tk
from tkinter import *
import requests
import json
import openai
openai.api_key = "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"

openai.Completion.create(
  engine="davinci",
  prompt="Make a list of astronomical observatories:"
)
print(prompt)
root = tk.Tk()
root.geometry("600x600")
root.mainloop()