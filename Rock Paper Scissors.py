#import libraries
from tkinter import * #tkinter library
from random import randint #random library - randint is random integer
from PIL import ImageTk, Image #images library - without it, we wouldn't be able to implement images in our coude

class MainGame: #a class is sort of like a blueprint and MainGame is the name of the class

    def __init__(self, window): #a function I created

        #GAME TITLE AND BACKGROUND COLOUR
        self.main = window #creates window
        self.main.title("Rock, Paper, Scissors!") #title of window
        self.main.configure(bg = "navajo white") #background colour

        #GAME HEADER AND GAME TITLE 
        self.header = Frame(window, borderwidth = 15, relief = RAISED, bg = "thistle1") #creates header window
        
        self.header_img = ImageTk.PhotoImage(Image.open("header_rps.png").resize((100, 100))) #header image, resized to fit
        Label(self.header, image = self.header_img).grid(row = 0, column = 0) #header image position
        Label(self.header, text = "A Game of Rock, Paper, Scissors!", bg = "PaleVioletRed1", fg = "white", font  = ("Verdana, 32")).grid(row = 0, column = 2)
        #game title, fg is the font colour, bg is the background colour, font is set to Verdana and its size to 32, .grid positions it next to the header image

        self.header.pack(pady = 10, padx = 10) #whole header padded on both x and y axis'
        
        #USER WINDOW
        self.player = Frame(window, borderwidth = 10, relief = RAISED, bg = "thistle1")

        self.player_img = ImageTk.PhotoImage(Image.open("human.jpg").resize((90, 90))) 
        Label(self.player, image = self.player_img).grid(row = 1, column = 0) 
        Label(self.player, text = "SILLY HUMAN", fg = "white", bg = "PaleVioletRed1", font = ("Verdana, 12")).grid(row = 2, column = 0, padx = 10, pady =  10)

        self.player.pack(pady = 10, padx = 10, side = LEFT) #unpacking the widget and putting in the same 'block', padding on x and y axis, and positioning it to the left


        #CHOOSE WIDGET
        self.rps_buttons = Frame(window, borderwidth = 10, relief = RAISED, bg = "thistle1") #rock, paper, scissors widget window

        self.choose_label = Label(self.rps_buttons, text = "Choose:", fg = "white", bg = "PaleVioletRed1", font = "Verdana, 22")
        self.choose_label.grid(row = 0, column = 0, pady = 10)
        self.rock_btn = Button(self.rps_buttons, text = "Rock", font = "Verdana", bg = "PaleVioletRed1", fg = "white", command = self.press_rock)
        #rock button; a call to a function called self.press_rock; when said button is pressed, the function will be executed
        self.rock_btn.grid(row = 2, column = 0, padx = 5, pady = 10)
        self.paper_btn = Button(self.rps_buttons, text = "Paper", font = "Verdana", bg = "PaleVioletRed1", fg = "white", command = self.press_paper)
        #paper button; a call to a function called self.press_paper
        self.paper_btn.grid(row = 3, column = 0, padx = 5, pady = 0)
        self.scissors_btn = Button(self.rps_buttons, text = "Scissors", font = "Verdana", bg = "PaleVioletRed1", fg = "white", command = self.press_scissors)
        #scissors button; call to a function called self.press_scissors
        self.scissors_btn.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.rps_buttons.pack(padx = 10, pady = 10, side = LEFT)


        #AI WINDOW
        self.ai = Frame(window, borderwidth = 15, relief = RAISED, bg = "thistle1")
        
        self.ai_img = ImageTk.PhotoImage(Image.open("robot.png").resize((90, 90)))
        Label(self.ai, image = self.ai_img).grid(row = 1, column = 0)
        Label(self.ai, text = "OVERPOWERED AI", fg = "white", bg = "PaleVioletRed1", font = ("Verdana, 12")).grid(row = 2, column = 0, padx = 10, pady = 10)

        self.ai.pack(pady = 10, padx = 10, side = RIGHT)
        
        #QUESTION MARK NEXT TO AI
        self.question = Frame(window, borderwidth = 10, relief = RAISED, bg = "thistle1")

        self.question_img = ImageTk.PhotoImage(Image.open("question_mark.png").resize ((100, 100)))
        self.qi = Label(self.question, image = self.question_img)
        self.qi.grid(row = 0, column = 0)

        self.question.pack(padx = 20, pady = 20, side = RIGHT)

        #COUNTERS WIDGET
        self.game_count = Frame (window, borderwidth = 20, relief = RAISED)
        
        self.turns_left = IntVar() #tab to keep score of how many turns are left which is a variable integer
        self.tl1 = Label(self.game_count, text = "Turns left: ", font = "Verdana, 10", fg = "white", bg = "PaleVioletRed1")
        self.tl1.grid(row = 1, column = 0)
        self.tl2 = Label(self.game_count, textvariable = self.turns_left, bg = "PaleVioletRed1")
        self.tl2.grid(row = 1, column = 1)

        self.sillyhuman_score = IntVar()
        self.shs1 = Label(self.game_count, text = "Silly human score: ", font = "Verdana, 10", fg = "white", bg = "PaleVioletRed1")
        self.shs1.grid(row = 2, column = 0)
        self.shs2 = Label(self.game_count, textvariable = self.sillyhuman_score, bg = "PaleVioletRed1")
        self.shs2.grid(row = 2, column = 1)

        self.overpoweredai_score = IntVar()
        self.oas1 = Label(self.game_count, text = "Overpoweredd AI score: ", font = "Verdanam 10", fg = "white", bg = "PaleVioletRed1")
        self.oas1.grid(row = 3, column = 0, padx = 10, pady = 0)
        self.oas2 = Label(self.game_count, textvariable = self.overpoweredai_score, bg = "PaleVioletRed1")
        self.oas2.grid(row = 3, column = 1)

        self.game_count.pack(padx = 10, pady = 10, side = LEFT)
        

        #FIGHT BUTTON
        self.screen = Frame(window, borderwidth = 2, relief = RAISED, bg = "thistle1")
        
        self.screen_text = Label(self.screen, text = "FIGHT!", font = "Verdana", fg = "black", bg = "PaleVioletRed1")
        self.screen_text.grid(row = 4, column = 2, padx = 10, pady = 10)

        self.screen.pack()


    def press_rock(self): #function called press_rock
        ui = randint(0, 2) #UI will be assigned randomly either 0, 1 or 2
        if ui == 0: #if UI is assigned 0
            self.screen_text.configure(text = "TIE!") #fight button changes to TIE!
            new_img = ImageTk.PhotoImage(Image.open("rock.png").resize ((100, 100))) #image next to UI changes to a picture of a hand rock
        elif ui == 1: #if UI is assigned 1
            self.screen_text.configure(text = "You lose!") #fight button changes to You lose!
            new_img = ImageTk.PhotoImage(Image.open("paper.png").resize ((100, 100))) #image next to UI changed to a picture of hand paper
        elif ui == 2: #if UI is assigned 2
            self.screen_text.configure(text = "You win!") #fight button changes to You win!
            new_img = ImageTk.PhotoImage(Image.open("scissors.png").resize ((100, 100))) #image next to UI changed to a picture of hand scissors
            
        self.qi.configure(image = new_img) #image next to UIchange
        self.question_img = new_img #without this step, image won't change
        self.turns_left.set(self.turns_left.get() +1) #turns_left counter gets 1 added


    def press_paper(self): #function called press_paper
        ui = randint(0, 2)
        if ui == 0:
            self.screen_text.configure(text = "You win!")
            new_img = ImageTk.PhotoImage(Image.open("rock.png").resize ((100, 100)))
        elif ui == 1:
            self.screen_text.configure(text = "TIE!")
            new_img = ImageTk.PhotoImage(Image.open("paper.png").resize ((100, 100)))
        elif ui == 2:
            self.screen_text.configure(text = "You lose!")
            new_img = ImageTk.PhotoImage(Image.open("scissors.png").resize ((100, 100)))
        self.qi.configure(image = new_img)
        self.question_img = new_img
        self.sillyhuman_score.set(self.sillyhuman_score.get() +1) 

        
    def press_scissors(self): #function called press_paper
        ui = randint(0, 2)
        if ui == 0:
            self.screen_text.configure(text = "You lose!")
            new_img = ImageTk.PhotoImage(Image.open("rock.png").resize ((100, 100)))
        elif ui == 1:
            self.screen_text.configure(text = "You win!")
            new_img = ImageTk.PhotoImage(Image.open("paper.png").resize ((100, 100)))
        elif ui == 2:
            self.screen_text.configure(text = "TIE!")
            new_img = ImageTk.PhotoImage(Image.open("scissors.png").resize ((100, 100)))
        self.qi.configure(image = new_img)
        self.question_img = new_img
        self.overpoweredai_score.set(self.overpoweredai_score.get() +1)    
                                                                            
                                                                        
#executes the class
root = Tk()
rps = MainGame(root)
root.mainloop()


##COMMENTS##
#I know how to do the 5 wins but only in theory. I've tried a couple of different ways and couldn't figure out how to implement it.
#Even though it's not the most representable game of rock, paper, scissors, the mechanics of it do work!
