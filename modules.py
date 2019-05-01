import datetime
import sys

class Note:
    note_number = 0
    def __init__(self, tag,text):
        self.tag = tag
        self.text = text
        self.date = datetime.datetime.now().strftime('%d-%m-%Y')
        Note.note_number+=1
        self.ID = Note.note_number
    def match(test):
        if  test and test.strip():
            return True
        else:
            return False
    def __str__(self):
        return "Nr.{ID} ||Tags:{tag}|\n{text}\n{date}".format(ID=self.ID,tag=self.tag,text=self.text,date=self.date)

class Notebook:
    def __init__(self):
        self.note_list = list()
    def Show_notes(self,mode,obj_list):  #mode  0 <-(full) 1<-(tags[:20],text[:30]) 2<-(tags[]:20)
        self.options={
            0: self.full,
            1: self.some,
            2: self.tags
        }
        self.options[mode](obj_list)
    def full(self,obj_list):
        for note in obj_list:
            print(note)
    def some(self,obj_list):
        for note in obj_list:
            print("\nID: {ID}, Tags:{tag}\n Text: {text}".format(ID=note.ID, tag=note.tag[:20],
                                                                 text=note.text[:30]))
    def tags(self,obj_list):
        for note in obj_list:
            print("\nID: {ID}, Tags:{tag}".format(ID=note.ID, tag=note.tag[:20]))
    def New_note(self):
        self.tag  = input("Tag: ")
        self.text = input("Write text: ")
        if Note.match(self.tag) and Note.match(self.text):
            self.note_list.append(Note(self.tag,self.text))
            print('\n Note added')
        else:
            print("\n text or tags are empty")
    def Modify_text(self):
        self.Show_notes(1,self.note_list)
        self.notes_to_change = input("\nText from which notes do you want to change? give ID: ")
        if int(self.notes_to_change):
            self.number = int(self.notes_to_change)
            if self.number<= sys.getsizeof(self.note_list)/sys.getsizeof(self.note_list[0]) :
                self.new_text = input("Enter new content: ")
                self.note_list[self.number-1].text =  self.new_text
            else:
                print("Note with that ID does not exist ")
    def Modify_tag(self):
        self.Show_notes(2,self.note_list)
        self.notes_to_change = input("\nTag from which notes do you want to change? give ID ")
        if int(self.notes_to_change):
            self.number = int(self.notes_to_change)
            if self.number <= sys.getsizeof(self.note_list) / sys.getsizeof(self.note_list[0]):
                self.new_tags = input("Enter new content: ")
                self.note_list[self.number - 1].tag = self.new_tags
            else:
                print("Note with that ID does not exist")
    def Search(self):
        self.results = list()
        self.phrase = input("Write some key words:")
        if Note.match(self.phrase):
            for note in self.note_list:
                if note.text.find(self.phrase) !=-1:
                    self.results.append(note)
                elif note.tag.find(self.phrase) !=-1:
                    self.results.append(note)
        if Note.match(self.results):
            self.Show_notes(0,self.results)
        else:
            print("Don't find anything")


class Test():
    def  __init__(self):
      #  self.note = Note("jaja","jak berety")
       # print(self.note)
        self.nono = Notebook()
        self.nono.New_note()
        self.nono.Modify_text()
        self.nono.Show_notes(0,self.nono.note_list)


#gogo=Test()