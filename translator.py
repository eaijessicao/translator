from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import textblob

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c, font="Roboto 12 bold", width=12, bd=3, fg= '#D1C3FA', relief=GROOVE)
    label2.configure(text=c1, font="Roboto 12 bold", width=12, bd=3, relief=GROOVE)
    root.after(1000, label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            translator = Translator()
            lan = translator.detect(text_).lang
            for i, j in language.items():
                if j == c3:
                    lan_ = i
            words = translator.translate(text_, src=lan, dest=str(lan_)).text
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror('Googletrans', f'Error: {e}')

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

# Icon
image_icon = PhotoImage(file='google.png')
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font='Montserrat 12', state='readonly')
combo1.place(relx=0.05, rely=0.05, relwidth=0.2)
combo1.set('ENGLISH')

label1 = Label(root, text="ENGLISH", font="bold", bg="white",fg= '#D1C3FA', width=12, bd=3, relief=GROOVE)
label1.place(relx=0.05, rely=0.15)

f = Frame(root, bg='#D1C3FA', bd=5)
f.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)

text1 = Text(f, font='Montserrat 12',fg= '#D1C3FA', bg='white', relief=GROOVE, wrap=WORD)
text1.place(relwidth=1, relheight=1)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side='right', fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Arrow
# arrow_image = PhotoImage(file='arrow.png')
# image_label = Label(root, image=arrow_image)
# image_label.place(relx=0.45, rely=0.15, relwidth=0.1, relheight=0.1)

combo2 = ttk.Combobox(root, values=languageV, font='Montserrat 12', state='readonly')
combo2.place(relx=0.55, rely=0.05, relwidth=0.2)
combo2.set('SELECT')

label2 = Label(root, text="ENGLISH", font="bold", bg="white", width=12, bd=2, fg= '#D1C3FA',relief=GROOVE)
label2.place(relx=0.55, rely=0.15)

f1 = Frame(root, bg='#D1C3FA', bd=5)
f1.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.5)

text2 = Text(f1, font='Montserrat 12',fg= '#D1C3FA',bg='white', relief=GROOVE, wrap=WORD)
text2.place(relwidth=1, relheight=1)
scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side='right', fill='y')

scrollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scrollbar2.set)

# Translator button
translate = Button(root, text='TRANSLATE', fg='#D1C3FA', bg='white', font='Roboto 12 bold', activebackground='#D1C3FA', cursor='hand2', bd=3, command=translate_now)
translate.place(relx=0.45, rely=0.85, relwidth=0.1)

label_change()

root.configure(bg="#845ac0")
root.mainloop()
