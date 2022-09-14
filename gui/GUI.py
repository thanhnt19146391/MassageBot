from tkinter import *
import tkinter.font as font
from tkinter import scrolledtext

class gui(Tk):
    def __init__(self):
        super().__init__()
        # Set the background colour of GUI window
        self.configure(background = "white")
        # Set the title of GUI window
        self.title("Massage Bot")
        # Set the configuration of GUI window
        self.geometry("1600x900+0+0")
        self.state('zoomed')
        # Create a label to show the Video frames
        self.video_label = Label(self)
        self.video_label.place(
            relx = .01,
            rely = .01,
            anchor = 'nw')  
        # Label to show captured frame:
        self.cap_label = Label(self)
        self.cap_label.place(
            relx = .4,
            rely = .01,
            anchor = 'nw')
        # Create a Button
        my_font = font.Font(family='Helvitica', size=20)
        self.reset_btn = Button(
            self, 
            text = 'Reset',     
            bg='cornflowerblue',
            fg='black',
            bd=0,
            font= my_font,
            height = 2,
            width = 15,
        )
        self.reset_btn.place(
            relx = .5,
            rely = .86,
            anchor = 'center'
        ) 
        self.run_btn = Button(
            self, 
            text = 'Run',     
            bg='cornflowerblue',
            fg='black',
            bd=0,
            font= my_font,
            height = 2,
            width = 15,
            # command = Run_Kinect
        )
        self.run_btn.place(relx = .5, rely = .7, anchor = 'center') 
        self.pos_label = Label(
            self,
            text = ' Position: (..., ...)\nDepth: ...',     
            anchor = 'w',
            bg = 'darkolivegreen1',
            fg = 'black',
            bd = 0,
            font = my_font,
            height = 3,
            width = 15
        )
        self.pos_label.place(
            relx = .01,
            rely = .01,
            anchor = 'nw'
        )   

        # Creating scrolled text 
        self.text_area = scrolledtext.ScrolledText(
            self, 
            wrap = WORD, 
            width = 22, 
            height = 30, 
            font = (my_font, 15))
        self.text_area.grid(column = 0, pady = 10, padx = 10)
        self.text_area.place(
            relx = 0.82,
            rely = .01,
            anchor = 'nw'
        )
        

