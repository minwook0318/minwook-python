1.
import tkinter as 사

def say_hello():
label.config(text="Hello, World!")

root = tk.Tk()
root.title("Hello World App")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
2.
import tkinter as tk

def greet():
    name = entry.get()  
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("인사 프로그램")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=5)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()
3.
import tkinter as tk

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label.config(text=f"Result: {result}", fg="blue")
    except ValueError:
        label.config(text="숫자를 입력하세요!", fg="red")

root = tk.Tk()
root.title("덧셈 계산기")

entry1 = tk.Entry(root, width=15, justify="center", font=("Arial", 12))
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=15, justify="center", font=("Arial", 12))
entry2.pack(pady=5)

button = tk.Button(
    root, 
    text="Add", 
    command=add,
    bg="lightgreen",
    font=("Arial", 10, "bold")
)
button.pack(pady=10)

label = tk.Label(root, text="", font=("Arial", 12, "bold"))
label.pack(pady=10)

root.mainloop()
4.
import tkinter as tk

def show_selection():
    selections = [ ]
    if var1.get():
        selections.append("옵션 1")
    if var2.get():
        selections.append("옵션 2")
    
    if selections:  
        label.config(text=f"선택된 항목: {', '.join(selections)}", fg="blue")
    else:  
        label.config(text="선택된 항목이 없습니다.", fg="red")

root = tk.Tk()
root.title("체크박스 선택 프로그램")  

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

tk.Checkbutton(root, text="옵션 1", variable=var1, font=("Arial", 10)).pack(pady=5)

tk.Checkbutton( root, text="옵션 2", variable=var2, font=("Arial", 10)).pack(pady=5)

tk.Button(root, text="결과 확인", command=show_selection, bg="lightblue", font=("Arial", 10)).pack(pady=10)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=10) 
root.mainloop()
5.
import tkinter as tk

def change_color():
    root.config(bg=color.get())

root = tk.Tk()
root.title("색상 선택 프로그램")
root.geometry("300x200")

color = tk.StringVar()

tk.Radiobutton(root, text="Red", variable=color, value="red", command=change_color, font=("Arial", 12), fg="red).pack(pady=5)

tk.Radiobutton(root,text="Blue",variable=color,value="blue",command=change_color, font=("Arial", 12),  fg="blue" ).pack(pady=5)

tk.Radiobutton(root,text="Green",variable=color,value="green",command=change_color,font=("Arial", 12), fg="green" ).pack(pady=5)

color.set("")

root.mainloop()
6.
import tkinter as tk

def resize(val):
    label.config(font=("Arial", int(val)))

root = tk.Tk()
scale = tk.Scale(root, from_=10, to=40, orient="horizontal", command=resize)
scale.pack()
label = tk.Label(root, text="Resizable Text")
label.pack()
root.mainloop()
7.
import tkinter as tk

def show_fruit(event):
    selection = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selection}")

root = tk.Tk()

listbox = tk.Listbox(root)

for fruit in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, fruit)

listbox.pack()

listbox.bind("<<ListboxSelect>>", show_fruit)

label = tk.Label(root, text="")

label.pack()
8.
import tkinter as tk

def show_message(msg):
    label.config(text=msg)

root = tk.Tk()

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=lambda: show_message("Open clicked"))
menu.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_message("About clicked"))
menu.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
9.
import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("텍스트 파일", "*.txt"),
                                                        ("모든 파일", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

root = tk.Tk()
root.title("간단 메모장")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both", padx=10, pady=10)

button = tk.Button(root, text="저장", command=save_file)
button.pack(pady=5)

root.mainloop()
10.
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("실시간 시계")

label = tk.Label(root, font=("Arial", 24))
label.pack(padx=50, pady=50)

update_time()

root.mainloop()
