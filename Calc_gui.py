import tkinter as tk
import clipboard as cl


win=tk.Tk()
win.resizable(width=False,height=False)
win.geometry("270x270")
win.title("Calc")


def decrement(event):
    #text_widget.see("end")
    number=int(text_widget1.get("1.0", "end-1c"))
    text_widget1.delete("1.0", "end")
    text_widget1.insert("1.0",f"{number-1}")


def minus_3_percent(event):
    number=text_widget.get("1.0", "end-1c")
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0",f"{number}-{int(number)*3/100}={int(number)-int(number)*3/100}")

text=""
number=0

def adding():
    global text
    global number
    number=int(text_widget1.get("1.0", "end-1c"))
    text = f"{number}+"
    label1.config(text=text)
    text_widget1.delete("1.0", "end")
    
def multiply():
    global text
    global number
    number=int(text_widget1.get("1.0", "end-1c"))
    text = f"{number}*"
    label1.config(text=text)
    text_widget1.delete("1.0", "end")
    
def clear():
    label1.config(text="")
    text_widget1.delete("1.0", "end")
    
    
def substraction():
    global text
    global number
    number=int(text_widget1.get("1.0", "end-1c"))
    text = f"{number}-"
    label1.config(text=text)
    text_widget1.delete("1.0", "end")

def division():
    global text
    global number
    number=int(text_widget1.get("1.0", "end-1c"))
    text = f"{number}/"
    label1.config(text=text)
    text_widget1.delete("1.0", "end")
    
    
def equals_on_enter(event):
    global text
    global number
    result=0
    second_number=int(text_widget1.get("1.0", "end-1c"))
    if text[-1]=="+":
        label1.config(text=f"{number}+{second_number} ={number+second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number+second_number)
    elif text[-1]=="-":
        label1.config(text=f"{number}-{second_number} ={number-second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number-second_number)
    elif text[-1]=="*":
        result=number-second_number
        label1.config(text=f"{number}*{second_number} ={number*second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number*second_number)
    elif text[-1]=="/":
        result=number/second_number
        label1.config(text=f"{number}/{second_number} ={number/second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number/second_number)    

      
def equals_on_button():
    global text
    global number
    second_number=int(text_widget1.get("1.0", "end-1c"))
    if text[-1]=="+":
        label1.config(text=f"{number}+{second_number} ={number+second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number+second_number)
    elif text[-1]=="-":
        label1.config(text=f"{number}-{second_number} ={number-second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number-second_number)
    elif text[-1]=="*":
        label1.config(text=f"{number}*{second_number} ={number*second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number*second_number)   
    elif text[-1]=="/":
        label1.config(text=f"{number}/{second_number} ={number/second_number}")
        text_widget1.delete("1.0", "end")
        text_widget1.insert("1.0",number/second_number)   
    
label = tk.Label(win, text="Введіть суму для виведення 3% (Ctrl+x)")
label.place(x=10,y=25)

text_widget = tk.Text(win)
text_widget.place(x=10,y=50,width=200,height=20)
text_widget.bind("<Control-x>",minus_3_percent)
text_widget.bind("<Control-z>",decrement)


#<Control-x>
label1 = tk.Label(win, text="")
label1.place(x=10,y=75)



text_widget1=tk.Text(win)
text_widget1.place(x=10,y=100,width=200,height=20)
text_widget1.bind("<Control-x>",minus_3_percent)
text_widget1.bind("<Control-z>",decrement)
text_widget1.bind("<Return>",equals_on_enter)

button_font = ("Arial", 30)

button_plus = tk.Button(win, text="+",command=adding,font=button_font)
button_plus.place(x=10,y=125,width=50,height=50)

button_equal= tk.Button(win, text="=",command=equals_on_button,font=button_font)
button_equal.place(x=130,y=185,width=50,height=50)


button_minus=tk.Button(win, text="-",command=substraction,font=button_font)
button_minus.place(x=70,y=125,width=50,height=50)

button_mult=tk.Button(win, text="*",command=multiply,font=button_font)
button_mult.place(x=130,y=125,width=50,height=50)

button_div=tk.Button(win, text="/",command=division,font=button_font)
button_div.place(x=70,y=185,width=50,height=50)

button_clear=tk.Button(win, text="C",command=clear,font=button_font)
button_clear.place(x=10,y=185,width=50,height=50)


button_to_clip=tk.Button(win,text="Copy")
button_to_clip.place(x=220,y=100)

win.mainloop()