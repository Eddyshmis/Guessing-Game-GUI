#imports the library's we need to run everything
import tkinter as tk
import random

#makes "num" into a number between 1-10

num_wins = 0
num = random.randint(1,10)


#this runs when the button is clicked
def get_num(wins,number):
    #turning the user input into a number (int)
    
    try:
        user_input_int = int(user_input.get())
    except:
        win_label.config(text="NOT A NUMBER")
        return None

    #will check if user input is equal to the random number
    if number == user_input_int:
        global num_wins
        num_wins += 1
        global num
        num = random.randint(1,10)
        print(num)
        user_input.delete(1)
        num_of_wins.config(text=f'Number of wins: {num_wins}')
        win_label.config(text="win")
    else:
        win_label.config(text="Lose")      
        user_input.delete(0)
        





#makes window
root = tk.Tk()

root.title("Guessing game")
root.geometry("250x100")

label = tk.Label(root, text="guess a number between 1-10")
#calling the VAR "label" then ".pack()" will add it to the window
label.pack()


#allows the user to input there number
user_input = tk.Entry(root)
user_input.pack()

#button to sumbit your response, "command" is what it runs when clicked
button = tk.Button(root, text= "submit", command=lambda: get_num(num_wins,num))
button.pack()

num_of_wins = tk.Label(root, text=f'number of wins:{num_wins}')
num_of_wins.pack()

#empty text to change later
win_label = tk.Label(root, text="")
win_label.pack()


#loop
root.mainloop()


