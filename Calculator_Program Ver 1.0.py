
from tkinter import *
 

expression = "" 
 
 

def press(num): 
    
    global expression 
 
    
    expression = expression + str(num) 
 
  
    equation.set(expression) 
 
 

def equalpress(): 
  
    try: 
 
        global expression 
 
        
        total = str(eval(expression)) 
 
        equation.set(total) 
 
        
        expression = "" 
 
   
    except: 
 
        equation.set(" error ") 
        expression = "" 
 
 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
 

if __name__ == "__main__": 
    
    root = Tk() 
 
    root.configure(background="white") 
 
    
    root.title("Calculator by Fatima") 
 
     
    root.geometry("293x150") 
 
    
    equation = StringVar() 
 
    
    expression_field = Entry(root, textvariable=equation) 
 
    
    expression_field.grid(columnspan=10, ipadx=85)
 
     
    button1 = Button(root, text=' 1 ', fg='black', bg='lightgray',command=lambda: press(1), height=1, width=9) 
    button1.grid(row=5, column=0) 
 
    button2 = Button(root, text=' 2 ', fg='black', bg='lightgray', command=lambda: press(2), height=1, width=9)
    button2.grid(row=5, column=1) 
 
    button3 = Button(root, text=' 3 ', fg='black', bg='lightgray', 
                    command=lambda: press(3), height=1, width=9)
    button3.grid(row=5, column=2) 
 
    button4 = Button(root, text=' 4 ', fg='black', bg='lightgray', 
                    command=lambda: press(4), height=1, width=9) 
    button4.grid(row=4, column=0) 
 
    button5 = Button(root, text=' 5 ', fg='black', bg='lightgray', 
                    command=lambda: press(5), height=1, width=9)
    button5.grid(row=4, column=1) 
 
    button6 = Button(root, text=' 6 ', fg='black', bg='lightgray', 
                    command=lambda: press(6), height=1, width=9)
    button6.grid(row=4, column=2) 
 
    button7 = Button(root, text=' 7 ', fg='black', bg='lightgray',
                     command=lambda: press(7), height=1, width=9)
    button7.grid(row=3, column=0) 
 
    button8 = Button(root, text=' 8 ', fg='black', bg='lightgray', 
                    command=lambda: press(8), height=1, width=9)
    button8.grid(row=3, column=1) 
 
    button9 = Button(root, text=' 9 ', fg='black', bg='lightgray', 
                    command=lambda: press(9), height=1, width=9)
    button9.grid(row=3, column=2) 
 
    button0 = Button(root, text=' 0 ', fg='black', bg='lightgray', 
                    command=lambda: press(0), height=1, width=9)
    button0.grid(row=6, column=1) 
 
    plus = Button(root, text=' + ', fg='black', bg='lightgray', 
                command=lambda: press("+"), height=1, width=9)

    plus.grid(row=2, column=3) 
 
    minus = Button(root, text=' - ', fg='black', bg='lightgray', 
                command=lambda: press("-"), height=1, width=9)
    minus.grid(row=3, column=3) 
 
    multiply = Button(root, text=' * ', fg='black', bg='lightgray', 
                    command=lambda: press("*"), height=1, width=9) 
    multiply.grid(row=4, column=3) 
 

         

    divide = Button(root, text=' / ', fg='black', bg='lightgray', 
                    command=lambda: press("/"), height=1, width=9) 
    divide.grid(row=5, column=3)

    power = Button(root, text=' ^ ', fg='black', bg='lightgray', 
                    command=lambda: press("**"), height=1, width=9) 

    power.grid(row=6, column=2)

    sqrt=Button(root, text=' sqrt ', fg='black', bg='lightgray', 
                command=lambda: press("**.5"), height=1, width=9)
    
    sqrt.grid(row=6, column=2)

    closedparenth=Button(root, text=' ) ', fg='black', bg='lightgray', 
                command=lambda: press(")"), height=1, width=9)

    closedparenth.grid(row=2, column=2)

    openparenth= Button(root, text=' ( ', fg='black', bg='lightgray', 
                    command=lambda: press("("), height=1, width=9) 
    openparenth.grid(row=2, column=1)

    
    equal = Button(root, text=' = ', fg='black', bg='lightgray',
                command=equalpress, height=1, width=9) 
    equal.grid(row=6, column=3)
    clear = Button(root, text='Clear', fg='black', bg='lightgray', 
                command=clear, height=1, width=9) 
    clear.grid(row=2, column='0') 
 
    Decimal= Button(root, text='.', fg='black', bg='lightgray', 
                    command=lambda: press('.'), height=1, width=9) 
    Decimal.grid(row=6, column=0)

    mainloop()
    # start the ROOT
