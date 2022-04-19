from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'
current_card = {}
to_learn ={}

try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ---------------------------- STEP4:  create to_learn file ------------------------------- #

def is_known():
    to_learn.remove(current_card) # get rid of the known card from French words.
    data = pandas.DataFrame(to_learn) # save the remaining card/words to a new file
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()


# ---------------------------- STEP3:  Flip the Cards ------------------------------- #
def flip_card():
    print(current_card['English'])  # must match the column header using capital "E"
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill = 'white')
    canvas.itemconfig(card_background, image = card_back_img)
    window.after(3000, func=flip_card)

# ---------------------------- STEP2: loading french words ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card['French']) # must match the column header using capital "F"
    canvas.itemconfig(card_title, text='French', fill = 'black')
    canvas.itemconfig(card_word, text=current_card["French"], fill = 'black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- STEP1: UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx= 50, pady=50, bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0 )
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400, 150,text="Title", font=(FONT_NAME, 40, "italic"))
card_word =canvas.create_text(400, 263,text = "placeholder", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


#botton
check_img = PhotoImage(file="images/right.png")
check_but = Button(image= check_img, highlightthickness=0, command = is_known)
check_but.grid(column=1, row=1)

cross_img = PhotoImage(file="images/wrong.png")
cross_but = Button(image= cross_img, highlightthickness=0, command= next_card)
cross_but.grid(column=0, row=1)

next_card()


window.mainloop()