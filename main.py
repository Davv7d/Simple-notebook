from modules import *
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
class Menu:
    def __init__(self):
        self.notebook=Notebook()
        self.options={
            "1":self.Show_notes,
            "2":self.Search_notes,
            "3":self.Add_note,
            "4":self.Modify_notes,
            "5":self.Quit
        }
    def Show_menu(self):
        clear()
        print("\n1 - Show notes\n"
              "2 - Search notes\n"
              "3 - Add note\n"
              "4 - Modify note\n"
              "5 - Quite")
    def Run(self):
        self.Show_menu()
        pick = input("Select your option")
        if pick in self.options.keys():
            self.options[pick]()
        else:
            print("WRONG INPUT,\n You must enter a number between 1-5!!!")
            input("")
            clear()
            self.Run()
    def Show_notes(self):
        self.notebook.Show_notes(0,self.notebook.note_list)
        input("")
        clear()
        self.Run()
    def Search_notes(self):
        self.notebook.Search()
        input("")
        clear()
        self.Run()
    def Add_note(self):
        self.notebook.New_note()
        input("")
        clear()
        self.Run()
    def Modify_notes(self):
        self.tag_or_text = input("What You wanna change ? tag or text : ")
        if self.tag_or_text =="text":
            self.notebook.Modify_text()
        elif self.tag_or_text =="tag":
            self.notebook.Modify_tag()
        else:
            print("WRONG INPUT")
        input("")
        clear()
        self.Run()
    def Quit(self):
        exit()

go=Menu()
go.Run()