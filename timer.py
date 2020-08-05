import tkinter
def button_countdown(i, label):
       if i > 0:
           i=i-1
           label.set(i)
           window.after(1000, lambda:button_countdown(i,label))
       else:
           close()

def close():
       window.destroy()

window = tkinter.Tk()

counter = 10
button_label = tkinter.StringVar()
button_label.set(counter)
tkinter.Label(window, textvariable=button_label,font=("標楷體", 16)).pack()
button_countdown(counter, button_label)


              
