import tkinter as tk
from tkinter import filedialog, messagebox as mb, ttk
from PIL import ImageTk, Image  
from pathlib import Path

#Something...
class MainScreen(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        self.vol_val = 100
        self.sfx_val = 100
        # import and draw background
        self.dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)
        # create buttons
        self.btn_start = tk.Button(self, text="Start",command=lambda:Start(self),font=('calibre',15,'normal'))
        self.btn_start.place_configure(x=400,y=250,width=150,height=60)
        
        self.btn_load = tk.Button(self, text="Load",command=lambda:Load(self),font=('calibre',15,'normal'))
        self.btn_load.place_configure(x=400,y=320,width=150,height=60)

        self.btn_setting = tk.Button(self, text="Setting",command=lambda:Setting(self),font=('calibre',15,'normal'))
        self.btn_setting.place_configure(x=400,y=390,width=150,height=60)

        self.btn_credit = tk.Button(self, text="Credit",command=lambda:Credit(self),font=('calibre',15,'normal'))
        self.btn_credit.place_configure(x=400,y=460,width=150,height=60)
        
        self.btn_quit = tk.Button(self, text="Quit",command=lambda:self.Quit(parent),font=('calibre',15,'normal'))
        self.btn_quit.place_configure(x=400,y=530,width=150,height=60)

        
    def Quit(self, master):
            # ask if wanna quit
            check = mb.askyesno(title='Quitting?',message='Are you sure about that?')
            if check:
                check = mb.askyesno(title='Really?!?',message='ARE YOU SURE?!?!?!???')
                if check:
                    master.destroy()         


class Start(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        image = Image.open(dir)
        self.tkimg = ImageTk.PhotoImage(image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)    

         # import and draw character
        dir = str(Path(__file__).resolve().parent) + '\\img\\img2.png'
        image = Image.open(dir)
        self.tkimg2 = ImageTk.PhotoImage(image)
        self.character = tk.Canvas(self,height=343,width=650)
        self.character.place(x=150,y=100)
        self.character.create_image(0,0,anchor=tk.NW,image=self.tkimg2) 

        # dialog box
        self.T = tk.Text(self, height = 5, width = 105)
        self.T.insert('0.1', "Hello! What's your name? ")
        self.T.place_configure(x=30,y=450)

        # create buttons (place holder rn)
        self.btn_back = tk.Button(self, text="Main menu",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)

        # plan: save option, settings, skip (?), probs easter eggs (last priority) 
        self.Game_UI(parent)
        # bind in case of skipping a lot (WIP)
        self.bind('<Button-1>',self.ChangeScene)

    def back(self):
        # check if progress is saved? remind if havent
        check = mb.askyesno(title='Back to main menu?',message='Game progress is not saved automatically and will be lost. Do you wanna proceed?')
        if check:
            self.place_forget()

    # plan: save/load option, settings, skip (?), probs easter eggs (last priority) (WIP)
    def Game_UI(self,parent):
        fs = open(str(Path(__file__).resolve().parent) + '\\scripts\\scene0001.txt')
        self.scripts = fs.readlines()
        self.pos = 0

        self.btn_save = tk.Button(self, text="Save",command=lambda:Save(parent),font=('calibre',15,'normal'))
        self.btn_save.place_configure(x=30,y=580,width=150,height=60)
        self.btn_load = tk.Button(self, text="Load",command=lambda:Load(parent),font=('calibre',15,'normal'))
        self.btn_load.place_configure(x=215,y=580,width=150,height=60)
        self.btn_setting = tk.Button(self, text="Setting",command=lambda:Setting(parent),font=('calibre',15,'normal'))
        self.btn_setting.place_configure(x=400,y=580,width=150,height=60) 
        self.btn_skip = tk.Button(self, text="Skip",command=lambda:self.Skip(),font=('calibre',15,'normal'))
        self.btn_skip.place_configure(x=800,y=580,width=150,height=60)    

    def UpdateImage(self, filename):
        dir = str(Path(__file__).resolve().parent) + '\\img\\' + filename
        image = Image.open(dir)
        return image        

    def ChangeScene(self, event): #config char and/or bg
        # bg    
        tup = self.scripts[self.pos].split('\n')
        tup = tup[0].split('|')
        print(tup)
        if len(tup) >= 1:
            self.T.delete('1.0','end')
            self.T.insert('1.0', tup[0])
        if len(tup) >= 2:
            image = self.UpdateImage(tup[1])
            self.tkimg = ImageTk.PhotoImage(image)
            self.create_image(0,0,anchor=tk.NW,image=self.tkimg)
        if len(tup) == 3:
            image = self.UpdateImage(tup[2])
            self.tkimg2 = ImageTk.PhotoImage(image)
            self.character = tk.Canvas(self,height=343,width=650)
            self.character.place(x=150,y=100)
            self.character.create_image(0,0,anchor=tk.NW,image=self.tkimg2)

        self.pos += 1


    def Skip(self): #config char and/or bg
        # bg
        image = self.UpdateImage('img4.png')
        self.tkimg = ImageTk.PhotoImage(image)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)
        #char
        image = self.UpdateImage('img3.png')
        self.tkimg2 = ImageTk.PhotoImage(image)
        self.character = tk.Canvas(self,height=343,width=650)
        self.character.place(x=150,y=100)
        self.character.create_image(0,0,anchor=tk.NW,image=self.tkimg2)
        #dialog
        self.T.insert('1.0', "Oh? Are you skipping? ")
        #char

        #dialog
        

    # change screen
    # change dialog
    # effects on screen canvas?


class Save(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)      

        # plan: several slots to save game progress, probs easter eggs (last priority)  (WIP)
        cre = tk.Label(self, text= "Where do you wanna save?", font =("Courier", 15))
        cre.place_configure(x=30,y=120,width=900,height=40)

        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)


    def back(self):
        self.place_forget()


class Load(tk.Canvas): #similar to read file, do after Save to know file (WIP)
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)     

        # plan: several slots to load game progress, probs easter eggs (last priority)  (WIP)
        cre = tk.Label(self, text= "Where do you wanna continue from?", font =("Courier", 15))
        cre.place_configure(x=30,y=120,width=900,height=40)

        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)


    def back(self):
        self.place_forget()


class Setting(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)      

        # plan: volume slider, sfx slider, dialog text size options (?), probs easter eggs (last priority) (WIP)

        # create sliders
        slider_label1 = ttk.Label(self,text='Volume:',font=('calibre',15,'normal'))
        slider_label2 = ttk.Label(self,text='Sfx:',font=('calibre',15,'normal'))

        slider_label1.place_configure(x=250,y=350)
        slider_label2.place_configure(x=250,y=400)

        curr_val1 = tk.IntVar(self,value=parent.vol_val)
        curr_val2 = tk.IntVar(self,value=parent.sfx_val)
        self.vol_slider = ttk.Scale(self,from_=0,to=100,orient='horizontal',variable=curr_val1,command=self.vol_slider_changed)
        self.sfx_slider = ttk.Scale(self,from_=0,to=100,orient='horizontal',variable=curr_val2,command=self.sfx_slider_changed)
        
        self.vol_slider.place_configure(x=350,y=350,width=200,height=30)
        self.sfx_slider.place_configure(x=350,y=400,width=200,height=30)

        self.vol_val = ttk.Label(self,text=int(self.vol_slider.get()))
        self.vol_val.place_configure(x=550,y=355)
        self.sfx_val = ttk.Label(self,text=int(self.sfx_slider.get()))
        self.sfx_val.place_configure(x=550,y=405)

        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(parent),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60) 

    def back(self,parent):
        self.place_forget()
        parent.vol_val=int(self.vol_slider.get())
        parent.sfx_val=int(self.sfx_slider.get())


    def vol_slider_changed(self, *args): 
        self.vol_val.config(text=int(self.vol_slider.get()))

    def sfx_slider_changed(self, *args):  
        self.sfx_val.config(text=int(self.sfx_slider.get()))

class Credit(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = str(Path(__file__).resolve().parent) + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)      
        
        # create label note: check
        cre = tk.Label(self, text= "Team GAYM", font =("Courier", 20))
        cre.place_configure(x=30,y=130,width=900,height=40)

        # create text or sth for full credit here (WIP)

        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)


    def back(self):
        self.place_forget()
        return

#####################################################################################            

def main():
    # create window
    root = tk.Tk()
    root.title("VISUAL NOVEL")
    root.geometry("1000x650+30+30")
    root.resizable(False,False)

    ms = MainScreen(root)
    root.protocol("WM_DELETE_WINDOW",lambda:ms.Quit(root))
    root.mainloop()

if __name__ == "__main__":
    main()