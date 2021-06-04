# import emoji
import tkinter.messagebox
from tkinter import *
from random import *
import pyperclip
import os
#from termcolor import colored


# Types definition
numeric = "0123456789"
alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphanumeric_and_special = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:;!?-_&=+#@$%"


def pass_creation():

    # Choice :
    chaine = string_choice.get()

    # In case of empty choice !
    if chaine == "" :
        text_Field.delete(0.0, END)
        text_Field.insert(END, "\n Select the type you would like to use !")

    length = int(pass_length.get())


    # Definition of list that will contain random password :
    M = []

    # Characters are picked randomly
    for i in range(length) :
        M.append(choice(chaine))

    # Converting the List into String using -->Join
    password = "".join(M)

    # Now we copy the password into the clipboard
    pyperclip.copy(password)


    # Here we display the message

    #passwd = colored(password, "green")

    #if length <= 90 :
    text = "\n *** your password is : [ "+password+" ]\t *** \n\n This password has been copied to the clipboard"
    #else :
    #text = " *** your password is : " + password + "\n This password has been copied to the clipboard "


    # Display of the result !
    text_Field.delete(0.0, END)
    text_Field.insert(END, text)



# Designing the GUI using Tkinter

window = Tk()
window.title("Laspeed Password Generator")
window.geometry("850x500")

tkinter.messagebox.showinfo("Laspeed Coding","---> Welcome to my password Generator <---")
# Welcoming message :
#  emo=print(emoji.emojize("RANDOM PASSWORD GENERATOR :sunglasses:" , use_aliases=True))
ProgName = Label(window,font=('times', 15, 'bold'), text = "RANDOM PASSWORD REGENERATOR (^_^)",fg="red",)
ProgName.grid(row=1, column=3, padx=230, pady=19)


# Here is where you chose the type of random password to get generated !
TypeChoice = Label(window, text = "Choose a type among the 3 :")
TypeChoice.grid(row=2, column=3, pady=9)

# Using radio button to make sure the user picks only one type

string_choice = StringVar()

numeric_choice = Radiobutton(window, text = "numeric", variable = string_choice, value=numeric)
alphanumeric_choice = Radiobutton(window, text = "alphanumeric", variable = string_choice, value=alphanumeric)
alphanumeric_choice_and_special = Radiobutton(window, text = "alphanumeric and specials", variable = string_choice, value=alphanumeric_and_special)

numeric_choice.grid(row=3, column=3)
alphanumeric_choice.grid(row=4, column=3)
alphanumeric_choice_and_special.grid(row=5, column=3)


# Here is where user defines the password length

TypeChoice = Label(window, text = "\n Define password length :")
TypeChoice.grid(row=6, column=3, pady=1)

# We use a SpinBox to set a minimum value and a maximum value for the password
pass_length = Spinbox(window, from_=8, to=360)
pass_length.grid(row=7, column=3, pady=9)

# --> Here is where we display the result <--

text_Field = Text(window, height=6, width=90, wrap=WORD)
text_Field.grid(row=8, column=3, pady=19)
text_Field.insert(END, "\n Generate the password ! ")


# We finally use command to call the function

generate_button = Button(window, text="Generate", command=pass_creation)
generate_button.grid(row=9, column=3, pady=9)

# Shutting down the program

Exit_button = Button(window, text="Quit", command=window.destroy)
Exit_button.grid(row=10, column=3, pady=19)


window.mainloop()
