from tkinter import *
from PIL import ImageTk
from random import randint

words = []
letters = []

with open('hang_game.txt', 'r') as file:
    words_2 = file.read()
    for x in words_2.split(','):
        words.append(x)

randomicNumber = randint(0, len(words))

#creating a label widget
root = Tk()
root.title('Hang Game')
canvas = Canvas(root, width=300, height=300)
canvas.pack()

img = ImageTk.PhotoImage(Image('knights.png'))
canvas.create_image(40, 40 , img)


#creating a function for buttons
def myButton():
    """Creates a simple button"""
    mylabel = Label(root, text='look i clicked this button!')
    mylabel.pack()

def button_add(letter):
    letters.append(letter)

button_a = Button(root, text='A', fg='black',padx=40, pady=20, command=lambda: button_add('A')).grid(row=2, column=1)
button_b = Button(root, text='B', fg='black',padx=40, pady=20, command=lambda: button_add('B')).grid(row=3, column=5)
button_c = Button(root, text='C', fg='black',padx=40, pady=20, command=lambda: button_add('C')).grid(row=3, column=3)
button_d = Button(root, text='D', fg='black',padx=40, pady=20, command=lambda: button_add('D')).grid(row=2, column=3)
button_e = Button(root, text='E', fg='black',padx=40, pady=20, command=lambda: button_add('E')).grid(row=1, column=3)
button_f = Button(root, text='F', fg='black',padx=40, pady=20, command=lambda: button_add('F')).grid(row=2, column=4)
button_g = Button(root, text='G', fg='black',padx=40, pady=20, command=lambda: button_add('G')).grid(row=2, column=5)
button_h = Button(root, text='H', fg='black',padx=40, pady=20, command=lambda: button_add('H')).grid(row=2, column=6)
button_i = Button(root, text='I', fg='black',padx=40, pady=20, command=lambda: button_add('I')).grid(row=1, column=8)
button_j = Button(root, text='J', fg='black',padx=40, pady=20, command=lambda: button_add('J')).grid(row=2, column=7)
button_k = Button(root, text='K', fg='black',padx=40, pady=20, command=lambda: button_add('K')).grid(row=2, column=8)
button_l = Button(root, text='L', fg='black',padx=40, pady=20, command=lambda: button_add('L')).grid(row=2, column=9)
button_m = Button(root, text='M', fg='black',padx=40, pady=20, command=lambda: button_add('M')).grid(row=3, column=7)
button_n = Button(root, text='N', fg='black',padx=40, pady=20, command=lambda: button_add('N')).grid(row=3, column=6)
button_o = Button(root, text='O', fg='black',padx=40, pady=20, command=lambda: button_add('O')).grid(row=1, column=9)
button_p = Button(root, text='P', fg='black',padx=40, pady=20, command=lambda: button_add('P')).grid(row=1, column=10)
button_q = Button(root, text='Q', fg='black',padx=40, pady=20, command=lambda: button_add('Q')).grid(row=1, column=1)
button_r = Button(root, text='R', fg='black',padx=40, pady=20, command=lambda: button_add('R')).grid(row=1, column=4)
button_s = Button(root, text='S', fg='black',padx=40, pady=20, command=lambda: button_add('S')).grid(row=2, column=2)
button_t = Button(root, text='T', fg='black',padx=40, pady=20, command=lambda: button_add('T')).grid(row=1, column=5)
button_u = Button(root, text='U', fg='black',padx=40, pady=20, command=lambda: button_add('U')).grid(row=1, column=7)
button_v = Button(root, text='V', fg='black',padx=40, pady=20, command=lambda: button_add('V')).grid(row=3, column=4)
button_w = Button(root, text='W', fg='black',padx=40, pady=20, command=lambda: button_add('W')).grid(row=1, column=2)
button_x = Button(root, text='X', fg='black',padx=40, pady=20, command=lambda: button_add('X')).grid(row=3, column=2)
button_y = Button(root, text='Y', fg='black',padx=40, pady=20, command=lambda: button_add('Y')).grid(row=1, column=6)
button_z = Button(root, text='Z', fg='black',padx=40, pady=20, command=lambda: button_add('Z')).grid(row=3, column=1)
button_ç = Button(root, text='Ç', fg='black', padx=40,pady=20, command=lambda: button_add('Ç')).grid(row=2, column=10)
myLabel = Label(root, text='Hang Game ')

#shoving it onto the screen



root.mainloop()

print(letters)
print(words)
