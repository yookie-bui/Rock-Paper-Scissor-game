from tkinter import*
import random
class rpsGui:
    def __init__(self, parent):
        self.name_label = Label(parent, text='Rock Paper Scissor')
        self.name_label.grid(row=0,column=0,columnspan=2, pady=10)
        self.user_entry = Entry(parent, width=12)
        self.user_entry.grid(row=1,column=0,padx=5)
        self.button = Button(parent,text='Enter',command=self.rps)
        self.button.grid(row=1,column=1,padx=3)
        self.result = Label(parent,text='')
        self.result.grid(row=2,column=0,columnspan=3,pady=10)
    def rps(self):
        result = ''
        choice = ['R','P','S']
        computer = random.choice(choice)
        user = self.user_entry.get()
        if user == 'R':
            if computer == 'R':
                result = 'DRAW'
            elif computer =='P':
                result = 'LOST'
            else:
                result = 'WIN'
        elif user == 'P':
            if computer == 'P':
                result = 'DRAW'
            elif computer =='S':
                result = 'LOST'
            else:
                result = 'WIN'
        else:
            if computer == 'S':
                result = 'DRAW'
            elif computer =='P':
                result = 'LOST'
            else:
                result = 'WIN' 
        self.result.config(text=result)
    
def main():
    window = Tk()
    gui = rpsGui(window)
    window.mainloop()

if __name__ = "__main__":
    main()
        
        
