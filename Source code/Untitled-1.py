import pygame 
import tkinter as tk
from tkinter import filedialog, messagebox as mb, ttk
from PIL import ImageTk, Image  
from pathlib import Path
import time

MAX_SLOT = 9
PARENT_DIR = str(Path(__file__).resolve().parent)

def play_music(dir,volume):
    pygame.mixer.music.load(dir)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)

class Entry(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self,parent,height=325,width=500)
        self.dir = PARENT_DIR + '\\img\\pngwing.com.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=250,y=150)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)     
        
        self.lb_info = tk.Label(self,text="Enter your name", font=('calibre',15,'normal'))
        self.lb_info.place_configure(x=150,y=0,width=150,height=50)
        self.name = tk.StringVar()
        self.entry_info = tk.Entry(self,textvariable=self.name)
        self.entry_info.place_configure(x=150,y=100,width=150,height=100)
        self.entry_info.bind('<Return>',self.back)
        
    def back(self,event):
        print(self.name.get())
        self.place_forget()

class Options(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self,parent,height=325,width=500)
        self.dir = PARENT_DIR + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=250,y=150)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)     
        
        self.options = []
        fp = open(PARENT_DIR + '\\scripts\\switch.txt')
        info = fp.readlines()
        x = 200 
        y = 10
        width = 150
        height = 100
        for line_info in info:
            cur = line_info.split('|')
            if parent.cur_scene == cur[0]:
                cur.pop(0)
                for idx in range(len(cur)):
                    sth = cur[idx].split(":")
                    self.options.append(tk.Button(self,text=sth[1], command=lambda id = sth[0]:self.change(parent,id)
                                                    , font=('calibre',15,'normal')))
                    self.options[idx].place_configure(x=x,y=y+idx*(height+50//len(cur)),width = width, height = height)
                break
            print(line_info)
            
        fp.close()

    def change(self, parent, id):
        parent.cur_scene = id
        parent.pos = 0
        fs = open(PARENT_DIR + '\\scripts\\scene' + parent.cur_scene + '.txt','r')
            # if FileNotFoundError:
            #     return
                # stop changing line or scene when end
        parent.scripts = fs.readlines()
        fs.close()
        parent.Continue()
        self.place_forget()
        
class MainScreen(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        self.place(x=0,y=0)

        self.vol_val = 100
        self.sfx_val = 100
        # play music
        dir = PARENT_DIR + '\\music\\dokitheme.mp3'
        play_music(dir,self.vol_val)
        # save load tracking
        try:
            fp = open(PARENT_DIR + '\\data\\save\\status.txt')
        except FileNotFoundError:
            fp = open(PARENT_DIR + '\\data\\save\\status.txt', 'w+')
            fp.write("\n".join(["0|Empty" for i in range(MAX_SLOT)]))

        self.status = fp.readlines()
        fp.close()
        self.status = [value.split('|') for value in self.status]
        self.status = [[int(v1),v2.split('\n')[0]] for v1,v2 in self.status]
        print(self.status)
        self.isLoading = -1

        # import and draw background
        self.dir = PARENT_DIR + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
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
        self.place(x=0,y=0)

        # import and draw background
        # self.create_image(0,0,anchor=tk.NW,image=self.tkimg)    
            
        #  # import and draw character
        # dir = PARENT_DIR + '\\img\\img2.png'
        # image = Image.open(dir)
        # self.tkimg2 = ImageTk.PhotoImage(image)
        self.character = tk.Canvas(self,height=343,width=650)
        self.character.place(x=150,y=100)
        # self.character.create_image(0,0,anchor=tk.NW,image=self.tkimg2) 

        dir = PARENT_DIR + '\\music\\dokigameplay.mp3'
        play_music(dir,parent.vol_val)

        # dialog box
        self.T = tk.Text(self, height = 5, width = 105)
        # self.T.insert('0.1', "Hello! What's your name? ")
        self.T.place_configure(x=30,y=450)

        # create buttons (place holder rn)
        self.btn_back = tk.Button(self, text="Main menu",command=lambda:self.back(parent),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)

        # bind for changing line
        self.bind('<Button-1>',self.ChangeLine)

        # plan: save option, settings, skip (?), probs easter eggs (last priority) 
        self.Game_UI(parent)
        self.Continue()

    # manual click
    def Continue(self):
        self.event_generate('<Button-1>')        
        self.update()    

    def back(self,parent):
        # check if progress is saved? remind if havent
        check = mb.askyesno(title='Back to main menu?',message='Game progress is not saved automatically and will be lost. Do you wanna proceed?')
        if check:
            self.place_forget()
            dir = PARENT_DIR + '\\music\\dokitheme.mp3'
            play_music(dir,parent.vol_val)

    # plan: save/load option, settings, skip, probs easter eggs (last priority) (WIP)
    def Game_UI(self,parent):
        self.cur_scene = '0001'
        self.pos = 0
        if parent.isLoading != -1:
            if parent.status[parent.isLoading][0] == 1:
                fs = open(PARENT_DIR + "\\data\\save\\game_save_" + str(parent.isLoading) + ".txt",'r')
                line = fs.read().split('|')
                self.cur_scene, temp = line 
                self.pos = int(temp)
                fs.close()
                print("Loading...")
            parent.isLoading = -1
        fs = open(PARENT_DIR + '\\scripts\\scene' + self.cur_scene + '.txt','r')
        self.scripts = fs.readlines()
        fs.close()

        self.event_generate('<Button-1>')        
        self.update()
        
        self.btn_save = tk.Button(self, text="Save",command=lambda:Save(self,parent),font=('calibre',15,'normal'))
        self.btn_save.place_configure(x=30,y=580,width=150,height=60)
        self.btn_load = tk.Button(self, text="Load",command=lambda:self.load_file(parent),font=('calibre',15,'normal'))
        self.btn_load.place_configure(x=215,y=580,width=150,height=60)
        self.btn_setting = tk.Button(self, text="Setting",command=lambda:Setting(parent),font=('calibre',15,'normal'))
        self.btn_setting.place_configure(x=400,y=580,width=150,height=60) 
        self.btn_skip = tk.Button(self, text="Skip",command=lambda:self.Skip(),font=('calibre',15,'normal'))
        self.btn_skip.place_configure(x=800,y=580,width=150,height=60)


    def UpdateImage(self, filename):
        dir = PARENT_DIR + '\\img\\' + filename
        image = Image.open(dir)
        return image        

    def ChangeLine(self, event): #config char and/or bg
        # bg    
        if self.pos == len(self.scripts):
            # cs = self.cur_scene[:self.cur_scene.rfind("000")]
            # temp = self.cur_scene.split("000")[1].split(".")[0]
            # temp = str(int(temp) + 1)

            # self.cur_scene = cs + "000" + temp + ".txt"
            
            #     # temporary lim=9 --> how to create 0000 -> 9999 string
            # # self.cur_scene = "\\scripts\\scene0002.txt"

            # self.pos = 0
            # fs = open(PARENT_DIR + self.cur_scene,'r')
            # # if FileNotFoundError:
            # #     return
            #     # stop changing line or scene when end
            # self.scripts = fs.readlines()
            # fs.close()
            Options(self)        
        

        tup = self.scripts[self.pos].split('\n')
        tup = tup[0].split('|')
        print(tup)
        
        self.T.delete('1.0','end')
        self.T.insert('1.0', tup[0])
        
        image = self.UpdateImage(tup[1])
        self.tkimg = ImageTk.PhotoImage(image)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)
        
        image = self.UpdateImage(tup[2])
        self.tkimg2 = ImageTk.PhotoImage(image)
        self.character.create_image(0,0,anchor=tk.NW,image=self.tkimg2)
        self.pos += 1

    def load_file(self,parent):
        Load(parent)
        print("selected")
        self.place_forget()

    def Skip(self): #config char and/or bg
        # bg
        while(self.pos != len(self.scripts)):
            self.Continue()
        
        self.Continue()
        
    # effects on screen canvas?

class Save(tk.Canvas):
    def __init__(self,parent, grand):
        tk.Canvas.__init__(self,grand,height=650,width=1000)
        # import and draw background
        self.dir = PARENT_DIR + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)      

        # plan: several slots to save game progress, probs easter eggs (last priority)  (WIP)
        
        cre = tk.Label(self, text= "Where do you wanna save?", font =("Courier", 15))
        cre.place_configure(x=30,y=120,width=900,height=40)

        self.loadspace = []
        count=0
        for j in range(170,500,150):
            for i in range(30,900,300):
                self.create_rectangle(i,j,i+300,j+150,width=4)
                self.loadspace.append(tk.Button(self, text="Save_" + str(count) + '\n' + grand.status[count][1] ,command=lambda idx = count:self.save_file(parent, grand, idx),font=('calibre',15,'normal')))
                self.loadspace[count].place_configure(x=i,y=j,width=300,height=150)
                count += 1

        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)


    def back(self):
        self.place_forget()

    def save_file(self, parent, grand, slot):
        check = 1
        if grand.status[slot][0] == 0:
            grand.status[slot][0] = 1
        else:
            check = mb.askyesno(title="Override this slot?",message="Progress of this slot will be lost.. :(")

        if check:
            grand.status[slot][1] = time.ctime()
            fp = open(PARENT_DIR + "\\data\\save\\game_save_" + str(slot) + ".txt",'w')
            fp.write(parent.cur_scene + "|" + str(parent.pos-1))
            fp.close()
            mb.showinfo(title=">:D",message="Save successfully!")
            
        fp = open(PARENT_DIR + "\\data\\save\\status.txt",'w')
    
        fp.write("\n".join([str(v1)+'|'+v2 for v1,v2 in grand.status]))
        fp.close()
        Save(parent,grand)
        self.place_forget()                
    

class Load(tk.Canvas): #similar to read file, do after Save to know file (WIP)
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = PARENT_DIR + '\\img\\img1.png'
        self.image = Image.open(self.dir)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.place(x=0,y=0)
        self.create_image(0,0,anchor=tk.NW,image=self.tkimg)     

        # plan: several slots to load game progress, probs easter eggs (last priority)  (WIP)
        cre = tk.Label(self, text= "Where do you wanna continue from?", font =("Courier", 15))
        cre.place_configure(x=30,y=120,width=900,height=40)
        
        self.loadspace = []
        count=0
        for j in range(170,500,150):
            for i in range(30,900,300):
                self.create_rectangle(i,j,i+300,j+150,width=4)
                self.loadspace.append(tk.Button(self, 
                    text="Load_" + str(count) + '\n' + parent.status[count][1],
                    command=lambda idx = count:self.load_file(parent, idx),
                    font=('calibre',15,'normal')))
                self.loadspace[count].place_configure(x=i,y=j,width=300,height=150)
                count += 1
        # create buttons
        self.btn_back = tk.Button(self, text="Back",command=lambda:self.back(),font=('calibre',15,'normal'))
        self.btn_back.place_configure(x=30,y=30,width=150,height=60)


    def back(self):
        self.place_forget()

    def load_file(self,parent, slot):
        parent.isLoading = slot
        Start(parent)

class Setting(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = PARENT_DIR + '\\img\\img1.png'
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
        val = int(self.vol_slider.get())
        self.vol_val.config(text=val)
        pygame.mixer.music.set_volume(val/100)


    def sfx_slider_changed(self, *args):  
        val = int(self.sfx_slider.get())
        self.sfx_val.config(text=val)
        pygame.mixer.music.set_volume(val/100)

class Credit(tk.Canvas):
    def __init__(self,parent):
        tk.Canvas.__init__(self,parent,height=650,width=1000)
        # import and draw background
        self.dir = PARENT_DIR + '\\img\\img1.png'
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
    #initialize pygame.mixer    
    pygame.mixer.init()
    root.title("VISUAL NOVEL")
    root.geometry("1000x650+30+30")
    root.resizable(False,False)
    
    ms = MainScreen(root)
    root.protocol("WM_DELETE_WINDOW",lambda:ms.Quit(root))
    
    # root2 = tk.Tk()
    # root2.attributes('-alpha',0.5)
    # root2.geometry("400x200+35+35")
    root.mainloop()
    # root2.mainloop()

if __name__ == "__main__":
    main()