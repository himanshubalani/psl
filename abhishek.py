# import all functions / classes from the tkinter
from os import name
from tkinter import *

from textblob import TextBlob
def check_spelling():
    a=TextBlob(spell_check.get())
    spell=Label(window,text="the correct spelling is :",font=("Arial",30,"bold"),bg="gray")
    spell.pack()
    correct_text=Label(window,text=str(a.correct()),font=("Arial",45,"bold"),bg="lightpink")
    correct_text.pack()
    
window=Tk()
window.title("y spelling checker")
window.geometry("800x600")
window.config(background="lightgreen")
text_headings=Label(window,text="Spelling checker",font=("Arial",50,"bold"),bg="black",fg="lightpink")
text_headings.pack()
text_check=Label(window,text="Enter the spelling",font=("Arial",35,"bold"),bg="yellow",fg="red")
text_check.pack()
spell_check=Entry(window,font=("Arial",45,"bold"),width="500",bg="lightblue")
spell_check.pack()
check_button=Button(window,text="check!!",font=("Arial",30,"bold"),fg="white",bg="red",command=check_spelling)
check_button.pack()
window.mainloop()