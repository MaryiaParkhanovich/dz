import random
import tkinter as tk
from tkinter import *

def space(number):
    num = [n for n in range(1, number+5)]
    num2 = []
    while len(num2) < 5:
        n = random.choice(num)
        num.pop(num.index(n))
        ask = True
        if num2 != []:
            for k in range(len(num2)):
                if (num2[k] + 1 == n) or (num2[k] - 1 == n) or num2[k] == n:
                    ask = False
                    break
            if ask:
                num2.append(n)
        else:
            num2.append(n)
    return num2

def words_window():
    number = int(length.get())
    root.geometry("400x300")
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, font=('Arial', 12, "bold"), bg="lightpink", text=words(number),wraplength=400)
    label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def words(number):
    alphabet = [chr(i) for i in range(97, 123)]
    words = []
    while True:
        for n in range(number+5):
            sumbol = random.choice(alphabet)
            words.append(sumbol)
        for n in space(number):
            words[n] = " "
        ans = "".join(words)
        break
    return ans


def start():
    global root
    root = Tk(className="zapocet")
    root.configure(bg="lightpink")
    words_label = tk.Frame(root)
    words_label.pack()
    label = tk.Label(root, font=('Arial', 12, "bold"), bg="lightpink",
                     text="""   Programovacie techniky
             Maryia Parkhanovich
                    Vygenerujte 30 náhodných písmen z ktorých poskladáte náhodnú vetu z 6-tich slov aj s medzerami""")
    root.geometry("1000x400")
    label.pack()
    global length
    length = Spinbox(root, from_=30, to_=70)
    length.pack(pady=20)
    button = Button(root, text="start", bg="purple", fg="white", font=('Arial', 12, "bold"), width=20, command=words_window)
    button.pack(pady=20)
    root.mainloop()



start()