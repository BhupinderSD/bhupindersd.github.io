#Bhupinder Dhoofer GUI

import sys
import sqlite3
import pandas
from tkinter import messagebox as tkMessageBox
from tkinter import *
import tkinter.ttk as ttk

def start_gui():
    global root
    root = Tk()
    top = TopWindow (root)
    root.mainloop()

class TopWindow:
    def __init__(self, top=None):
        _bgcolor = '#0B0C10'   # Background colour for the widget
        _fgcolor = '#c5c6c7'   # Foreground color for the widget (tab text)
        _compcolor = '#66FCF1' # Current Tab Background colour 
        _ana2color = '#45A29E' # Active Background colour for tabs
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1920x1027+-1+-19")
        top.title("PC Building Toolkit")
        top.configure(background="#0B0C10")

        root.option_add("*Font", "helvetica 20")#Large

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.AllTabs = ttk.Notebook(top)
        self.AllTabs.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.AllTabs.configure(width=1894)
        self.Page1 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page1, padding=3)
        self.AllTabs.tab(0, text="Home Page",underline="-1",)
        self.Page2 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page2, padding=3)
        self.AllTabs.tab(1, text="Components Page",underline="-1",)
        self.Page3 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page3, padding=3)
        self.AllTabs.tab(2, text="Item Page",underline="-1",)
        self.Page4 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page4, padding=3)
        self.AllTabs.tab(3, text="Current Parts Page",underline="-1",)
        self.Page5 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page5, padding=3)
        self.AllTabs.tab(4, text="Final Build Page",underline="-1",)
        self.Page6 = ttk.Frame(self.AllTabs)
        self.AllTabs.add(self.Page6, padding=3)
        self.AllTabs.tab(5, text="End Page",underline="-1",)

        def theme(widget):
            widget.configure(activebackground="#66FCF1")        #Cyan, Active Background colour
            widget.configure(activeforeground="#0B0C10")        #Black, Active Foreground colour
            widget.configure(background="#0B0C10")              #Black, Background colour
            widget.configure(foreground="#c5c6c7")              #Gray, Foreground colour

        self.P1L1 = Label(self.Page1)
        self.P1L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P1L1.configure(background="#0B0C10")               
        self.P1L1.configure(foreground="#c5c6c7")
        self.P1L1.configure(text='''PC Building Toolkit''')

        self.P1B1 = Button(self.Page1)
        self.P1B1.place(relx=0.01, rely=0.35, height=315, width=1876)
        self.P1B1.configure(text='''Build a PC!''')
        self.P1B1.configure(command = lambda : [self.AllTabs.select(self.Page2), UserName(self.P1E1.get())])
        
        self.P1B2 = Button(self.Page1)
        self.P1B2.place(relx=0.01, rely=0.72, height=85, width=1876)
        self.P1B2.configure(text='''Build a PC - Advanced Mode''')
        self.P1B2.configure(command = lambda : [self.AllTabs.select(self.Page2), UserName(self.P1E1.get()), AdvancedMode()])

        def AdvancedMode():
            global AdvancedMode
            AdvancedMode = True     #Turns boolean True
            
        self.P1L2 = ttk.Label(self.Page1)
        self.P1L2.place(relx=0.01, rely=0.83, height=139, width=1866)
        self.P1L2.configure(background="#0B0C10")
        self.P1L2.configure(foreground="#c5c6c7")
        self.P1L2.configure(relief=FLAT)
        self.P1L2.configure(text='''What is the difference?

When using "Build a PC!", we will run a compatibility check to ensure that all of your parts will work together. 
By using "Advanced Mode", we will not run the compatibility checker.''')

        self.P1E1 = Entry(self.Page1)
        self.P1E1.place(relx=0.32, rely=0.24, relheight=0.08, relwidth=0.67)
        self.P1E1.configure(background="#0B0C10")
        self.P1E1.configure(font=font10)
        self.P1E1.configure(foreground="#c5c6c7")
        self.P1E1.configure(insertbackground="black")

        self.P1L3 = Label(self.Page1)
        self.P1L3.place(relx=0.03, rely=0.24, height=71, width=544)
        self.P1L3.configure(background="#0B0C10")
        self.P1L3.configure(foreground="#c5c6c7")
        self.P1L3.configure(text='''What is your name? 
This will be used as the file name''')
        self.P1L3.configure(justify=RIGHT)

        self.P2L1 = Label(self.Page2)
        self.P2L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P2L1.configure(activebackground="#f9f9f9")
        self.P2L1.configure(activeforeground="black")
        self.P2L1.configure(background="#0B0C10")
        self.P2L1.configure(foreground="#c5c6c7")
        self.P2L1.configure(text='''Choose the component to configure''')

        self.P2BB = Button(self.Page2)
        self.P2BB.place(relx=-0.01, rely=0.93, height=75, width=966)
        self.P2BB.configure(text='''Back''')
        self.P2BB.configure(command = lambda : self.AllTabs.select(self.Page1))


        self.P2B1 = Button(self.Page2)
        self.P2B1.place(relx=0.01, rely=0.2, height=74, width=1907)
        self.P2B1.configure(pady="0")
        self.P2B1.configure(text='''CPU''')
        self.P2B1.configure(width=1907)
        self.P2B1.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(1)])

        self.P2B2 = Button(self.Page2)
        self.P2B2.place(relx=0.01, rely=0.29, height=74, width=1907)
        self.P2B2.configure(pady="0")
        self.P2B2.configure(text='''Motherboard''')
        self.P2B2.configure(width=1907)
        self.P2B2.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(2)])

        self.P2B3 = Button(self.Page2)
        self.P2B3.place(relx=0.01, rely=0.38, height=74, width=1907)
        self.P2B3.configure(pady="0")
        self.P2B3.configure(text='''Memory''')
        self.P2B3.configure(width=1907)
        self.P2B3.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(3)])

        self.P2B4 = Button(self.Page2)
        self.P2B4.place(relx=0.01, rely=0.47, height=74, width=1907)
        self.P2B4.configure(pady="0")
        self.P2B4.configure(text='''Storage''')
        self.P2B4.configure(width=1907)
        self.P2B4.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(4)])

        self.P2B5 = Button(self.Page2)
        self.P2B5.place(relx=0.01, rely=0.56, height=74, width=1907)
        self.P2B5.configure(pady="0")
        self.P2B5.configure(text='''Video Card''')
        self.P2B5.configure(width=1907)
        self.P2B5.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(5)])

        self.P2B6 = Button(self.Page2)
        self.P2B6.place(relx=0.01, rely=0.65, height=74, width=1907)
        self.P2B6.configure(pady="0")
        self.P2B6.configure(text='''Power Supply''')
        self.P2B6.configure(width=1907)
        self.P2B6.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(6)])

        self.P2B7 = Button(self.Page2)
        self.P2B7.place(relx=0.01, rely=0.74, height=74, width=1907)
        self.P2B7.configure(pady="0")
        self.P2B7.configure(text='''Case''')
        self.P2B7.configure(width=1907)
        self.P2B7.configure(command = lambda : [self.AllTabs.select(self.Page3), ItemSelection(7)])

        self.P2FB = Button(self.Page2)
        self.P2FB.place(relx=0.51, rely=0.93, height=75, width=956)
        self.P2FB.configure(text='''Skip''')
        self.P2FB.configure(command = lambda : self.AllTabs.select(self.Page3))

        self.P3L1 = Label(self.Page3)
        self.P3L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P3L1.configure(activebackground="#f9f9f9")
        self.P3L1.configure(activeforeground="black")
        self.P3L1.configure(background="#0B0C10")
        self.P3L1.configure(foreground="#c5c6c7")
        self.P3L1.configure(text='''Please select a component from the previous page''')

        self.P3BB = Button(self.Page3)
        self.P3BB.place(relx=-0.01, rely=0.93, height=75, width=966)
        self.P3BB.configure(text='''Back''')
        self.P3BB.configure(command = lambda : self.AllTabs.select(self.Page2))

        self.P3L2 = Label(self.Page3)
        self.P3L2.place(relx=0.01, rely=0.18, relheight=0.71, relwidth=0.99)
        self.P3L2.configure(background="#0B0C10")
        self.P3L2.configure(foreground="#c5c6c7")
        self.P3L2.configure(text='''The list of items will show here''')
        self.P3L2.configure(width=1890)

        self.P3E1 = Entry(self.Page3)
        self.P3E1.place(relx=0.51, rely=0.93, relheight=0.07, relwidth=0.24)
        self.P3E1.configure(background="#0B0C10")
        self.P3E1.configure(font=font10)
        self.P3E1.configure(foreground="#c5c6c7")
        self.P3E1.configure(insertbackground="black")
        self.P3E1.configure(selectbackground="#c4c4c4")
        self.P3E1.configure(selectforeground="black")
        self.P3E1.configure(width=464)

        self.P3FB = Button(self.Page3)	
        self.P3FB.place(relx=0.75, rely=0.93, height=75, width=486)
        self.P3FB.configure(text='''Next''')	
        self.P3FB.configure(width=486)
        self.P3FB.configure(command = lambda : [self.AllTabs.select(self.Page4),ItemSave(self.P3E1.get()),UserComponents()])

        self.P4L1 = Label(self.Page4)
        self.P4L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P4L1.configure(activebackground="#f9f9f9")
        self.P4L1.configure(activeforeground="black")
        self.P4L1.configure(background="#0B0C10")
        self.P4L1.configure(foreground="#c5c6c7")
        self.P4L1.configure(text='''Current Part List''')

        self.P4BB = Button(self.Page4)
        self.P4BB.place(relx=-0.01, rely=0.93, height=75, width=966)
        self.P4BB.configure(text='''Back''')
        self.P4BB.configure(command = lambda : self.AllTabs.select(self.Page3))

        self.P4L1 = Label(self.Page4)
        self.P4L1.place(relx=0.01, rely=0.23, height=411, width=1874)
        self.P4L1.configure(activebackground="#f9f9f9")
        self.P4L1.configure(activeforeground="black")
        self.P4L1.configure(background="#0B0C10")
        self.P4L1.configure(foreground="#c5c6c7")

        self.P4B1 = Button(self.Page4)
        self.P4B1.place(relx=0.01, rely=0.66, height=145, width=1886)
        self.P4B1.configure(text='''Add another component...''')
        self.P4B1.configure(command = lambda : self.AllTabs.select(self.Page2))

        self.P4B2 = Button(self.Page4)
        self.P4B2.place(relx=0.5, rely=0.93, height=75, width=956)
        self.P4B2.configure(text='''Finish''')
        self.P4B2.configure(command = lambda : [self.AllTabs.select(self.Page5), ModeSelection()])

        def ModeSelection():
            global AdvancedMode
            if AdvancedMode == True:        #Checks boolean status
                pass                        #Ignores the check if True
            else:
                BasicMode()                 #Else it will run it
        
        self.P5L1 = Label(self.Page5)
        self.P5L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P5L1.configure(activebackground="#f9f9f9")
        self.P5L1.configure(activeforeground="black")
        self.P5L1.configure(background="#0B0C10")
        self.P5L1.configure(foreground="#c5c6c7")
        self.P5L1.configure(text='''Here is your build''')

        self.P5BB = Button(self.Page5)
        self.P5BB.place(relx=-0.01, rely=0.93, height=75, width=966)
        self.P5BB.configure(text='''Back''')
        self.P5BB.configure(command = lambda : self.AllTabs.select(self.Page4))

        self.P5L2 = Label(self.Page5)
        self.P5L2.place(relx=0.01, rely=0.21, height=461, width=1874)
        self.P5L2.configure(activebackground="#f9f9f9")
        self.P5L2.configure(activeforeground="black")
        self.P5L2.configure(background="#0B0C10")
        self.P5L2.configure(foreground="#c5c6c7")

        self.P5B1 = Button(self.Page5)
        self.P5B1.place(relx=0.0, rely=0.77, height=145, width=946)
        self.P5B1.configure(text='''Yes''')
        self.P5B1.configure(command = lambda : [self.AllTabs.select(self.Page6),Export()])#save

        self.P5B2 = Button(self.Page5)
        self.P5B2.place(relx=0.51, rely=0.77, height=145, width=946)
        self.P5B2.configure(text='''No''')
        self.P5B2.configure(command = lambda : self.AllTabs.select(self.Page6))

        self.P6L1 = Label(self.Page5)
        self.P6L1.place(relx=0.01, rely=0.66, height=91, width=1874)
        self.P6L1.configure(activebackground="#f9f9f9")
        self.P6L1.configure(activeforeground="black")
        self.P6L1.configure(background="#0B0C10")
        self.P6L1.configure(foreground="#c5c6c7")
        self.P6L1.configure(text='''Do you want to save your build?''')

        self.P6L1 = Label(self.Page6)
        self.P6L1.place(relx=0.01, rely=0.02, height=211, width=1874)
        self.P6L1.configure(activebackground="#f9f9f9")
        self.P6L1.configure(activeforeground="black")
        self.P6L1.configure(background="#0B0C10")
        self.P6L1.configure(foreground="#c5c6c7")
        self.P6L1.configure(text='''Thank You''')

        self.P6BB = Button(self.Page6)
        self.P6BB.place(relx=-0.01, rely=0.93, height=75, width=966)
        self.P6BB.configure(text='''Back''')
        self.P6BB.configure(command = lambda : self.AllTabs.select(self.Page5))

        self.P6L2 = Label(self.Page6)
        self.P6L2.place(relx=0.01, rely=0.21, height=41, width=1894)
        self.P6L2.configure(background="#0B0C10")
        self.P6L2.configure(foreground="#c5c6c7")
        self.P6L2.configure(text='''How was your experience?''')
        self.P6L2.configure(width=1894)

        self.P6E1 = Entry(self.Page6)
        self.P6E1.place(relx=0.02, rely=0.28, relheight=0.39, relwidth=0.96)
        self.P6E1.configure(background="#0B0C10")
        self.P6E1.configure(font=font10)
        self.P6E1.configure(foreground="#c5c6c7")
        self.P6E1.configure(insertbackground="black")
        self.P6E1.configure(width=1834)        

        self.star = PhotoImage(file="star.gif")

        self.P6B1 = Button(self.Page6)
        self.P6B1.place(relx=0.02, rely=0.69, height=84, width=347)
        self.P6B1.configure(image=self.star, command = lambda : ChooseStar(1))

        self.P6B2 = Button(self.Page6)
        self.P6B2.place(relx=0.215, rely=0.69, height=84, width=347)
        self.P6B2.configure(image=self.star, command = lambda : ChooseStar(2))

        self.P6B3 = Button(self.Page6)
        self.P6B3.place(relx=0.41, rely=0.69, height=84, width=347)
        self.P6B3.configure(image=self.star, command = lambda : ChooseStar(3))

        self.P6B4 = Button(self.Page6)
        self.P6B4.place(relx=0.605, rely=0.69, height=84, width=347)
        self.P6B4.configure(image=self.star, command = lambda : ChooseStar(4))

        self.P6B5 = Button(self.Page6)
        self.P6B5.place(relx=0.8, rely=0.69, height=84, width=347)
        self.P6B5.configure(image=self.star, command = lambda : ChooseStar(5))

        self.P6FB = Button(self.Page6)
        self.P6FB.place(relx=0.02, rely=0.79, height=95, width=1836)
        self.P6FB.configure(text='''Submit''')
        self.P6FB.configure(command = lambda : [self.P6FB.configure(text="Submitted"), Feedback()])

        def ChooseStar(x):
            global star
            star = x                                                                #Stores the number of stars provided from button input
            stararray = [self.P6B1,self.P6B2,self.P6B3,self.P6B4,self.P6B5]
            for i in range(star):
                stararray[i].configure(background="#FBEB19")                        #Makes all buttons Yellow
            i+=1
            while True:
                if i != 5:                                                          #If 5(i) stars is not given
                    stararray[i].configure(background="#0B0C10")                    #Makes the last star black
                    i+=1                                                            
                else:
                    break                                                           #Continues till only the clicked stars and previous are yellow

        def Feedback():
            Comment = self.P6E1.get()                                               #Fetches the feedback from the entry box
            db = sqlite3.connect("Customers.db")
            cursor = db.cursor()
            try:
                cursor.execute("""CREATE TABLE {}Feedback (id INTEGER PRIMARY KEY, Stars TEXT, Comment TEXT)""".format(UserNameV))
                                                                                    #Inserts the comment and number of stars to the database
                cursor.execute("""INSERT INTO """+UserNameV+"""Feedback (Stars, Comment) Values (?,?)""",(star,Comment))
                db.commit()
                print(pandas.read_sql_query("SELECT * FROM "+UserNameV+"Feedback", db))     
                db.close()
            except (sqlite3.OperationalError, UnboundLocalError):                   #If an error occurs..
                tkMessageBox.showerror("File Name Error", "A file with this name may already exists or this may contain special characters. Please enter another name and try again.")
                self.AllTabs.select(self.Page1)                                     #Asks the user to try another name



        ButtonsToTheme = [self.P1B1,self.P1B2,self.P2BB,self.P2B1,self.P2B2,self.P2B3,self.P2B4,
                          self.P2B5,self.P2B6,self.P2B7,self.P2FB,self.P3BB,self.P3FB,self.P4BB,
                          self.P4B1,self.P4B2,self.P5BB,self.P5B1,self.P5B2,self.P5BB,self.P6BB,
                          self.P6B1,self.P6B2,self.P6B3,self.P6B4,self.P6B5,self.P6FB]

        for i in ButtonsToTheme:                    #For all of the buttons in the array
            theme(i)                                #Theme them
       
        def UserName(UserName):                     #Passing by reference
            global UserNameV
            UserNameV=UserName
            while True:
                for i in range(6):                  #If the file name is taken
                    if UserChoices[i][1] != "":     #and a build has been created
                        break
                self.AllTabs.select(self.Page5)     #Show final build page
                break
                    
                
            

        ComponentChoice = ["","","","","","",""]
        ComponentList = ["CPU","Motherboard","Memory","Storage","VideoCard","PowerSupply","Tower"]

        def ItemSelection(ComponentInput):
            global ComponentInputV
            ComponentInputV = ComponentInput
            self.P3L1.configure(text=ComponentList[ComponentInput-1])               #To meet stakeholder requirements,
                                                                                    #Shows category name as title
            Database = sqlite3.connect("Components2.db")    
            cursor = Database.cursor()
            cursor.execute('''SELECT * FROM ''' + ComponentList[ComponentInput-1])  #Fetches all components from category
            x = []                                                                  #empty array
            y=""                                                                    #empty string
            
            for column in cursor.execute("SELECT * FROM {}".format(ComponentList[ComponentInput-1])).description:
                                                                                    #Gets table headings...
                x.append(column[0])                                                 #Stores them in array x
            for row in cursor:                                                      
                x.extend(row)                                                       #Adds all components to array
            for i in x:                                                             #This is to format the text correctly
                if isinstance(i,int) == True:                                       #When the index is the id as int,
                    print("")                                                       #Prints a new row, for diagnostics
                    y=y+"\n\n"                                                      #Adds a new row to the string
                print("{:<25s}".format(str(i)),end="")                              #The sting will be 25 characters
                                                                                    #Left aligned, not printing a new line
                y=y+"{:<40s}".format(str(i))                                        #Adds to string, left aligned 40 char
            print("\n")                                                             #New line
            y=y+"\n"                                                                #New Line
            print(y)                                                                #For diagnostics/monitoring
            self.P3L2.configure(text=y)                                             #Prints on label
                
        
        def ItemSave(ItemChoice):                                                   
            Database = sqlite3.connect("components2.db")                            
            cursor = Database.cursor()
            cursor.execute('''SELECT id FROM '''+ ComponentList[int(ComponentInputV)-1] + ''' WHERE id = ''' + ItemChoice)
            Check = cursor.fetchall()                                               #Fetches chosen component from database
            print("----------------------------------------------------------------------------------------------------")
            if Check == []:
                print("***Please enter a valid id***")                              #If that id is not there (so incorrect input)
            else:
                ComponentChoice[ComponentInputV-1] = ItemChoice                     #Saves the component


      

        def UserComponents():
            global table
            global UserChoices
            Database = sqlite3.connect("components2.db")
            cursor = Database.cursor()

            loops = 0                                                       #loops variable for number of loops
            UserChoices = [["CPU",""],                                      #2d arrays store component category and component for export
                           ["Motherboard",""],
                           ["Memory",""],
                           ["Storage",""],
                           ["Video Card",""],
                           ["Power Supply",""],
                           ["Case",""]
                           ]

            for position in ComponentChoice:                #For each component category
                while loops <= 7:                           #while loops is less than or equal to 7
                    try:
                        cursor.execute('SELECT Name FROM ' + ComponentList[loops-1] + ' WHERE id = {}'.format(ComponentChoice[loops-1]))
                        for row in cursor:                  #Gets the name of each component to save in the builds database
                            ItemText = row[0]               #[0] saves the component name without brackets
                    except sqlite3.OperationalError:        #If there is an error
                        ItemText = 0                        #Set the component to 0, meaning not choosen
                    UserChoices[loops-1][1] = ItemText      #Set this component to the corresponding index in the 2d array
                    loops = loops + 1                       #Manually increment loop
            
            table = """

 ============== ================= 
   Component    \tName     
 ============== ================= 
  ---------CPU  \t{}         
  -Motherboard  \t{}         
  ------Memory  \t{}         
  -----Storage  \t{}         
  --Video Card  \t{}         
  Power Supply  \t{}         
  --------Case  \t{}         
 ============== ================= 

""".format(UserChoices[0][1],UserChoices[1][1],UserChoices[2][1],UserChoices[3][1],UserChoices[4][1],UserChoices[5][1],UserChoices[6][1])
            self.P4L1.configure(text=table,justify = LEFT)
            self.P5L2.configure(text=table,justify = LEFT)              #Displays table

        def Export():
            global UserNameV
            global UserChoices
            file = open(UserNameV+".txt","w+")                      #Will create or ammend the file
            file.write(table)                                       #Writes the contents of variable table to the file
            file.close()                                            #Closes file to prevent data corruption
                
            db = sqlite3.connect("Customers.db")                    #Connects to customers builds database
            cursor = db.cursor()
            try:
                cursor.execute("""CREATE TABLE {} (id INTEGER PRIMARY KEY, Component TEXT, Name TEXT)""".format(UserNameV))     #Creates table
                cursor.executemany("""INSERT INTO """+UserNameV+""" Values (NULL,?,?)""",UserChoices)                           #Saves build to database
                db.commit()
                cursor.execute('''SELECT * FROM ''' +UserNameV)
                print("Saved")
                print(pandas.read_sql_query("SELECT * FROM "+UserNameV, db, "id"))                      
                self.P4L1.configure(text=pandas.read_sql_query("SELECT * FROM "+UserNameV, db, "id"))                           #Displays current build 
                db.close()
            except(sqlite3.OperationalError, UnboundLocalError):                                                                #If an error occurs.
                tkMessageBox.showerror("File Name Error", "A file with this name may already exists or this may contain special characters. Please enter another name and try again.")
                self.AllTabs.select(self.Page1)                                                                                 #Asks the user to try another file name and try again

   
        def BasicMode():
            Database = sqlite3.connect("components2.db")    
            cursor = Database.cursor()
            if ComponentChoice[0] and ComponentChoice[1] != "":                                                                                 #If a CPU and Motherboard have been selected...
                print("Checking socket compatibilty.")
                CPUCheck = cursor.execute('''SELECT Socket FROM CPU WHERE id = ''' + ComponentChoice[0]).fetchall()                             #Save CPU socket
                MotherboardCheck = cursor.execute('''SELECT Socket FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()             #Save Mobo socket
                if CPUCheck == MotherboardCheck:                                                                                                #If the socket is the same, continue
                    print("Socket is Compatible.")
                else:
                    print("The socket is not compatible. Please choose another CPU or Motherboard.")
                    tkMessageBox.showerror("Compatibility Checker", "The socket is not compatible. Please choose another CPU or Motherboard.")  #Pop up box error
                    self.AllTabs.select(self.Page2)                                                                                             #Goes to page that needs to be fixed
            else:
                print("Socket Compatibility check not required.")
            if ComponentChoice[1] and ComponentChoice[5] != "":                                                                                 #Motherboard and Power Supply
                print("Checking form factor compatibilty.")
                MotherboardCheck = cursor.execute('''SELECT FormFactor FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()
                PowerSupplyCheck = cursor.execute('''SELECT FormFactor FROM PowerSupply WHERE id = ''' + ComponentChoice[5]).fetchall()
                if MotherboardCheck == PowerSupplyCheck:
                    print("Form Factor is Compatible-1")
                else:
                    print("The Form Factor is not compatible. Please choose another Power Supply or Motherboard.")
                    tkMessageBox.showerror("Compatibility Checker", "The Form Factor is not compatible. Please choose another Power Supply or Motherboard.")
                    self.AllTabs.select(self.Page2)
            else:
                print("Form Factor Compatibility check not required-1")
            if ComponentChoice[5] and ComponentChoice[6]!= "":                                                                                  #Power Supply and Case
                print("Checking form factor compatibilty.")
                PowerSupplyCheck = cursor.execute('''SELECT FormFactor FROM PowerSupply WHERE id = ''' + ComponentChoice[5]).fetchall()
                TowerCheck = cursor.execute('''SELECT FormFactor FROM Tower WHERE id = ''' + ComponentChoice[6]).fetchall()
                if PowerSupplyCheck == TowerCheck:
                    print("Form Factor is Compatible-2")
                else:
                    print("The Form Factor is not compatible. Please choose another Power Supply or Case.")
                    tkMessageBox.showerror("Compatibility Checker", "The Form Factor is not compatible. Please choose another Power Supply or Case.")
                    self.AllTabs.select(self.Page2)
            else:
                print("Form Factor Compatibility check not required-2")
            if ComponentChoice[1] and ComponentChoice[6]!= "":                                                                                  #Motherboard and Case
                print("Checking form factor compatibilty.")
                MotherboardCheck = cursor.execute('''SELECT FormFactor FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()
                TowerCheck = cursor.execute('''SELECT FormFactor FROM Tower WHERE id = ''' + ComponentChoice[6]).fetchall()
                if MotherboardCheck == TowerCheck:
                    print("Form Factor is Compatible-3")
                else:
                    print("The Form Factor is not compatible. Please choose another Case or Motherboard.")
                    tkMessageBox.showerror("Compatibility Checker", "The Form Factor is not compatible. Please choose another Case or Motherboard.")
                    self.AllTabs.select(self.Page2)
            else:
                print("Form Factor Compatibility check not required-3") 

if __name__ == '__main__':
    start_gui()
