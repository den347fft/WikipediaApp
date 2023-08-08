from tkinter import *
from tkinter import messagebox
import wikipedia
import pyperclip

root = Tk()
root["bg"] = "black"
root.geometry('600x400')
root.title("WikiApp by _sineD_0")

search_value = StringVar()
lang = StringVar()
lang.set("en")

def search():
    try:
        search_answer = wikipedia.summary(search_value.get())
        wikipedia.set_lang(lang.get())
        search_result["text"] = search_answer
        messagebox.showinfo("INFO",f"{search_answer}")
    except Exception:
        messagebox.showerror("ERROR",f"по запросу:{search_value.get()} ,ничего не найдено")
        search_result["text"] = ""
def copy_text():
    text = search_result["text"]
    pyperclip.copy(text)
    messagebox.showinfo("INFO", "Text copied to clipboard")
optionmenu = OptionMenu(root, lang, "en", "ru","uk","pl")
optionmenu.config(bg="black", fg="white",border=7)
optionmenu["menu"].config(bg="black", fg="white")
optionmenu.pack(side=BOTTOM)
h2 = Label(bg="black",text="WikiApp",fg="White",font="10").pack()
search_input =  Entry(textvariable=search_value,bg="grey",fg="White").pack()
search_button = Button(bg="black",fg="White",text="Search",command=search).pack()
search_result = Label(bg="Black",fg="White",text="")
search_result.pack()
copy_button = Button(bg="black", fg="white", text="Copy", command=copy_text)
copy_button.pack()

root.mainloop()