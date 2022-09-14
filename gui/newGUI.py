from tkinter import * 
from PIL import Image, ImageTk

class gui(Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = Frame(self) 
        # container.pack()
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Page0, Page1, Page2, Page3):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        # Set the title of GUI window
        self.title("Massage Bot")
        # Set the configuration of GUI window
        self.attributes('-fullscreen', True)
        # self.state('zoomed')

        self.show_frame(Page0)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class Page0(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Set the background colour of GUI window
        BG = "white"
        self.configure(background = BG)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(0, weight = 2)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        
        self.card_bg = canvas = Canvas(
            self,
            height = 600,
            width = 750
            )
        self.card_bg.place(
            relx = .5,
            rely = .45,
            anchor = 'center')  
        
        # Create an object of tkinter ImageTk
        self.welcome_img = ImageTk.PhotoImage(Image.open("./icon/welcome.png").resize((250, 250)))

        # Create a Label Widget to display the text or Image
        self.welcome_label = Label(
            self,
            image = self.welcome_img)

        self.welcome_label.grid(
            row = 0, 
            column = 0,
            sticky = 'S',
            columnspan = 3) 
        
        self.name_label = Label(
            self,
            text = "MASSAGE BOT",
            font = ('Helvitica', 25, "bold"))
        self.name_label.grid(
            row = 1,
            column = 0,
            sticky = 'N', 
            columnspan = 3)


        self.start_icon = ImageTk.PhotoImage(
            Image.open("./icon/play.png").resize((100, 100)))
        self.start_button = Button(
            self, 
            bd = 0,
            image = self.start_icon,
            command = lambda : controller.show_frame(Page1))
        self.start_button.grid(
            row = 2, 
            column = 0,
            sticky = 'N',
            padx = 0, 
            pady = 0,
            columnspan = 3)

        self.close_icon = ImageTk.PhotoImage(
            Image.open("./icon/close.png").resize((50, 50)))
        self.close_button = Button(
            self, 
            bd = 0,
            image = self.close_icon,
            background = BG,
            command=self.quit)
        self.close_button.grid(
            row = 3, 
            column = 2,
            sticky= 'ES',
            padx = 20, 
            pady = 30)          
  
  
# second window frame page1
class Page1(Frame):
     
    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        BG = "white"
        self.configure(background = BG)

        card_bg = Canvas(
            self,
            height = 450,
            width = 1140)
        card_bg.place(
            relx = .5,
            rely = .35,
            anchor = 'center')  

        card_bg = Canvas(
            self,
            height = 440,
            width = 1130,
            bg = BG)
        card_bg.place(
            relx = .5,
            rely = .35,
            anchor = 'center')  

        self.close_icon = ImageTk.PhotoImage(
            Image.open("./icon/close.png").resize((50, 50)))
        close_button = Button(
            self, 
            bd = 0,
            image = self.close_icon,
            background = BG,
            command=self.quit)
        close_button.place(
            relx = .98,
            rely = .05,
            anchor = 'ne')  
        
        img = Image.open("./img/img2.png").resize((200, 250))
        self.back_img = ImageTk.PhotoImage(img)
        self.personBack= Label(
            self,
            image = self.back_img,
            bg = BG,
            highlightthickness=0
            )

        self.personBack.place(
            relx = .75,
            rely = .35,
            anchor = 'center')

        self.back_icon = ImageTk.PhotoImage(
            Image.open("./btn/backButton.png").resize((150, 60)))
        back_button = Button(
            self, 
            image = self.back_icon,
            bg = BG,
            bd = 0,
            command = lambda : controller.show_frame(Page0))
        
        back_button.place(
            relx = .02,
            rely = .9,
            anchor = 'w')
        
        self.select_icon = ImageTk.PhotoImage(
            Image.open("./btn/selectButton.png").resize((150, 60)))
        next_button = Button(
            self,
            image = self.select_icon,
            compound = "right",
            bg = BG,
            bd = 0,
            command = lambda : controller.show_frame(Page2))
        next_button.place(
            relx = .98,
            rely = .9,
            anchor = 'e')

        # card_bg = Canvas(
        #     self,
        #     height = 60,
        #     width = 150,
        #     bg = 'black')
        
        # card_bg.place(
        #     relx = .7,
        #     rely = .9,
        #     anchor = 'center')
     
        
        
class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        BG = "white"
        self.configure(background = BG)
        
        card_bg = Canvas(
            self,
            height = 600,
            width = 1140)
        card_bg.place(
            relx = .5,
            rely = .4,
            anchor = 'center')  

        title = Label(
            self, 
            text = "Select the soundtrack for this session",
            font = ('Helvitica', 22))
        title.place(
            relx = .5,
            rely = .15,
            anchor = 'center'
        )
        
        self.close_icon = ImageTk.PhotoImage(
            Image.open("./icon/close.png").resize((50, 50)))
        close_button = Button(
            self, 
            bd = 0,
            image = self.close_icon,
            background = BG,
            command=self.quit)
        close_button.place(
            relx = .98,
            rely = .05,
            anchor = 'ne')  

        self.back_icon = ImageTk.PhotoImage(
            Image.open("./btn/backButton.png").resize((150, 60)))
        back_button = Button(
            self, 
            image = self.back_icon,
            bg = BG,
            bd = 0,
            command = lambda : controller.show_frame(Page1))
        
        back_button.place(
            relx = .02,
            rely = .9,
            anchor = 'w')
        
        self.select_icon = ImageTk.PhotoImage(
            Image.open("./btn/selectButton.png").resize((150, 60)))
        next_button = Button(
            self,
            image = self.select_icon,
            compound = "right",
            bg = BG,
            bd = 0,
            command = lambda : controller.show_frame(Page3))
        next_button.place(
            relx = .98,
            rely = .9,
            anchor = 'e')
        
class Page3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        BG = "white"
        self.configure(background = BG)

        self.close_icon = ImageTk.PhotoImage(
            Image.open("./icon/close.png").resize((50, 50)))
        close_button = Button(
            self, 
            bd = 0,
            image = self.close_icon,
            background = BG,
            command=self.quit)
        close_button.place(
            relx = .98,
            rely = .05,
            anchor = 'ne')  
  
  
# Driver Code
app = gui()
app.mainloop()