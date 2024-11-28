# Github https://github.com/Heycan59/scissors-rock-paper

import random
import tkinter as tk
from tkinter import messagebox

def rd():
    mora={1:'剪刀', 2:'石頭', 3:'布'}
    Com_mora=random.randint(1,3)
    bot = mora[Com_mora]
    return Com_mora, bot

def cut():
    Com_mora, bot = rd()
    e = f"你出的拳是 剪刀\n電腦出 {bot}\n"
    if Com_mora == 1:
        messagebox.showinfo("資訊", f"{e}平手!")
    if Com_mora == 2:
        messagebox.showinfo("資訊", f"{e}你輸了!")
    if Com_mora == 3:
        messagebox.showinfo("資訊", f"{e}你贏了!")

def stone():
    Com_mora, bot = rd()
    e = f"你出的拳是 石頭\n電腦出 {bot}\n"
    if Com_mora == 1:
        messagebox.showinfo("資訊", f"{e}你贏了!")
    if Com_mora == 2:
        messagebox.showinfo("資訊", f"{e}平手!")
    if Com_mora == 3:
        messagebox.showinfo("資訊", f"{e}你輸了!")

def cloth():
    Com_mora, bot = rd()
    e = f"你出的拳是 布\n電腦出 {bot}\n"
    if Com_mora == 1:
        messagebox.showinfo("資訊", f"{e}你輸了!")
    if Com_mora == 2:
        messagebox.showinfo("資訊", f"{e}你贏了!")
    if Com_mora == 3:
        messagebox.showinfo("資訊", f"{e}平手!")

root = tk.Tk()
root.title('剪刀石頭布')
root.resizable(width=False, height=False)
root.geometry("400x250")

label = tk.Label(root, text="點選要猜的拳")
label.pack(pady=10)

剪刀 = tk.Button(root, text="剪刀", width=15, command=cut)
剪刀.pack(pady=10)

石頭 = tk.Button(root, text="石頭", width=15, command=stone)
石頭.pack(pady=10)

布 = tk.Button(root, text="布", width=15, command=cloth)
布.pack(pady=10)

離開 = tk.Button(root, text="離開", width=15, command=root.destroy)
離開.pack(pady=10)

root.mainloop()
