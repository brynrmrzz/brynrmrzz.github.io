## The purpose of this was really to follow along and get a general introduction with Tkinter as I had never used it before, 
## The calculator's functionality is laughable but overall I was able to abstract the functions from it that I needed
## With what I gathered from this I'm a bit closer to being able to put together some other ideas that I have. 

#Import from tkinter everything
from tkinter import *

#Here we are definining our root widget or our main window essentially
root = Tk()

#Here we are call our main widget it and then apply the title
root.title('Calculator')
#we can then just call our geometry object to make our border. I wrapped it in int() because the float result was causing an error. 
root.geometry('250x300')
# and then we added some color for fun 
root.config(bg='green')

#This is creating our input widget(or text box)
entered = Entry(root, width = 29, borderwidth = 4)

#Defining our click function 
def button_click(string):    
    #We're storing any numbers already present in our entered widget
    current_number = entered.get()
    #We then delete everything in the widget
    entered.delete(0, END)
    #Here we are taking out stored value and concatting it with the new value
    entered.insert(0, str(current_number)+str(string))
    
def convert_negative():
    current_value = entered.get()
    if '-' in current_value:
        return
    else:
        entered.insert(0, '-')

def button_add():
    #initializing our first number globally 
    global first_num
    #initializing our operator variable gobally
    global operator
    #store our current number as our first number
    first_num = float(entered.get())
    # storing our operator as addition
    operator = '+'
    #erase the number so that other numbers can now be entered
    entered.delete(0, END)
    
def button_sub():
    #initializing our first number globally 
    global first_num
    #initializing our operator variable gobally
    global operator
    #store our current number as our first number
    first_num = float(entered.get())
    # storing our operator as addition
    operator = '-'
    #erase the number so that other numbers can now be entered
    entered.delete(0, END)

def button_multi():
    #initializing our first number globally 
    global first_num
    #initializing our operator variable gobally
    global operator
    #store our current number as our first number
    first_num = float(entered.get())
    # storing our operator as addition
    operator = '*'
    #erase the number so that other numbers can now be entered
    entered.delete(0, END)


def button_divide():
    #initializing our first number globally 
    global first_num
    #initializing our operator variable gobally
    global operator
    #store our current number as our first number
    first_num = float(entered.get())
    # storing our operator as addition
    operator = '\ '
    #erase the number so that other numbers can now be entered
    entered.delete(0, END)

def button_equal():

    #check if length is less than 1 
    if len(entered.get()) < 1 or len(str(first_num)) < 1:
        entered.delete(0,END)
        #if the length is less than 1 make it 0 because that means it's undefined
        entered.insert(0, first_num)
        return
    else:
        second_num = float(entered.get())
    #then delete the value so it is not displayed alongside new values
    entered.delete(0, END)
    # check our operator for which method to apply
    if operator == '+' :
        #add and assign to a variable
        total = first_num + second_num
        #insert our total into our text box so that it is displayed
        entered.insert(0, str(total))
    #instead if operator is subtraction
    elif operator == '-':
        #subtract and assign to total
        total = first_num - second_num
        #display our total
        entered.insert(0, str(total))   
    #instead if operator is multiplication
    elif operator == '*':
        #multiply and assign to total
        total = first_num * second_num
        #display our total
        entered.insert(0, str(total))   
    #instead if operator is division
    elif operator == '\ ':
        #divide and assign to total
        total = first_num / second_num
        #display our total
        entered.insert(0, str(total))
    #here we have a our final else case meaning operator was never defined 
    else:
        entered.insert(0, int(first_num))
        

def button_clear():
    #Clearing our text box entirely for new input
    entered.delete(0, END)
    
#Here is the creation and visualization of our buttons widgets
button_1 = Button(root, text = '1', padx = 30, pady = 10, command = lambda : button_click(1))
button_2 = Button(root, text = '2', padx = 30, pady = 10, command = lambda : button_click(2))
button_3 = Button(root, text = '3', padx = 30, pady = 10, command = lambda : button_click(3))
#This white space helps me group them logically for legibility 
button_4 = Button(root, text = '4', padx = 30, pady = 10, command = lambda : button_click(4))
button_5 = Button(root, text = '5', padx = 30, pady = 10, command = lambda : button_click(5))
button_6 = Button(root, text = '6', padx = 30, pady = 10, command = lambda : button_click(6))
#We call the number in a lambda function so that we may enter a integer with our function
button_7 = Button(root, text = '7', padx = 30, pady = 10, command = lambda : button_click(7))
button_8 = Button(root, text = '8', padx = 30, pady = 10, command = lambda : button_click(8))
button_9 = Button(root, text = '9', padx = 30, pady = 10, command = lambda : button_click(9))
#These functions were added in to test my understanding of the material 
button_negative = Button(root, text = '-/+', padx = 25, pady = 10, command = convert_negative)
button_0 = Button(root, text = '0', padx = 30, pady = 10, command = lambda : button_click(0))
button_dec = Button(root, text = ' . ', padx = 30, pady = 10, command = lambda : button_click('.'))
#these were included in the tutorial but I edited their appearance to fit with my new buttons
button_sub = Button(root, text = ' -' , padx = 30, pady = 10, command = button_sub)
button_multi = Button(root, text = '*' , padx = 30, pady = 10, command = button_multi)
button_divide = Button(root, text = '\ ' , padx = 30, pady = 10, command = button_divide)
#Again we initialize our buttons assigning them visual properties and defining their function
button_plus = Button(root, text = '+', padx = 30, pady = 10, command = button_add)
button_equal = Button(root, text = '=', padx = 30, pady = 10, command = button_equal)
button_clear = Button(root, text = 'Clear', padx = 20, pady = 10, command = button_clear)

# Here we begin actually displaying our graphics first with our text box
entered.grid(row = 0, column = 0, padx = 1, pady = 1, columnspan = 3)
#our first row of buttons and respective colums
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
#our second row of buttons and respective colums
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
#our third row of buttons and respective colums
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
#our fourth row of buttons and respective colums
button_negative.grid(row = 4 , column = 0)
button_0.grid(row = 4 , column = 1)
button_dec.grid(row = 4 , column = 2)
#our fifth row of buttons and respective colums
button_sub.grid(row = 5 , column = 0)
button_multi.grid(row = 5, column = 1)
button_divide.grid(row = 5, column = 2)
#our sixth row of buttons and respective colums
button_plus.grid(row = 6, column = 2)
button_equal.grid(row = 6, column = 1)
button_clear.grid(row = 6, column = 0)

# lastly, we run our root and all its main functions 
root.mainloop()
