from tkinter import *

class Calculator:
    """
    This class is used to build a calculator
    """
    def __init__(self):
        self.state = 1
        self.output = ""
        self.window = Tk()
        self.width,self.height = 320,500
        self.window.title("Calculator")
        self.window.config(width=self.width,height=self.height)
        self.window.resizable(False,False)


    def input_widget(self):
        """Constructing input widget
        :param:self
        :return:None
         """
        self.create_frame()
        self.scroll = Scrollbar(self.frame,orient="horizontal")
        


        self.input_number = Entry(self.frame,width=13,fg = "red",font=("italic",40),bd=8,xscrollcommand=self.scroll.set)
        self.input_number.config(state="readonly")
        self.input_number.pack()
        self.scroll.pack(expand=1,fill=X)
        self.scroll.config(command=self.input_number.xview)
    def create_frame(self):
        self.frame = Frame(self.window)
        self.frame.pack()
        self.frame2 = Frame(self.window)
        self.frame2.pack()




    def update_input_window(self,display):
        """Update the input window "
        :param:self,display
        :return:None 
        """
        self.input_number.config(state=NORMAL)
        self.input_number.insert(END,display)
        self.input_number.config(state = "readonly")
        

    def update_output(self,update):
        """
        Retreiving inputs from the input box and calculate the final answer
        :param:self,update
        :return:None
        """
        self.current =update
        if self.state:
            if update == "1" or update == "2" or update == "3" or update == "4"or update == "5" or update == "6" or update == "7" or update == "8" or update == "9" or update == "0" or update == "." or update == "+" or update == "-" or update == "*" or update == "/" or update == "(" or update == ")" or update == ".":
                self.output+=update
                self.update_input_window(self.current)
            if update == "del":
                try:
                    if self.input_number.get() != "Syntax error":
                        self.input_number.config(state=NORMAL)
                        self.input_number.delete(len(self.input_number.get())-1,"end")
                        self.output = self.output.replace(self.output[len(self.output)-1],"")
                        self.input_number.config(state="readonly")
                    else:
                        pass
                except Exception:
                    pass
            if update == "equal":
                try:
                    self.input_number.config(state = NORMAL)
                    self.input_number.delete(0,END)
                    self.input_number.insert(END,eval(self.output))
                    self.input_number.config(state = "readonly")
                    self.output = ""
                    
                except Exception :
                    self.input_number.config(state = NORMAL)
                    self.input_number.delete(0,END)
                    self.input_number.insert(END,"Syntax error")
                    self.input_number.config(state = "readonly")
                    self.state=0

        if update == "C":
            self.input_number.config(state=NORMAL)
            self.input_number.delete(0,END)
            self.output = ""
            self.state = 1
            self.input_number.config(state="readonly")
            
        if len(self.input_number.get()) > len(self.output):
            self.output+=self.input_number.get()
    def number_widget(self):
        """
        Building Number widgets and arithmetic operator widgets
        :param:self
        :return:None
        """

        self.clear = Button(self.frame2,text="{}".format("C"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("C"))
        self.left_curly = Button(self.frame2,text="{}".format("("),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("("))
        self.right_curly = Button(self.frame2,text="{}".format(")"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output(")"))
        self.delete = Button(self.frame2,text="{}".format("del"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("del"))
        self.num_1 = Button(self.frame2,text="{}".format("1"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("1"))
        self.num_2 = Button(self.frame2,text="{}".format("2"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("2"))
        self.num_3 = Button(self.frame2,text="{}".format("3"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("3"))
        self.div = Button(self.frame2,text="{}".format("/"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("/"))
        self.num_4 = Button(self.frame2,text="{}".format("4"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("4"))
        self.num_5 = Button(self.frame2,text="{}".format("5"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("5"))
        self.num_6 = Button(self.frame2,text="{}".format("6"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("6"))
        self.mul = Button(self.frame2,text="{}".format("*"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("*"))
        self.num_7 = Button(self.frame2,text="{}".format("7"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("7"))
        self.num_8 = Button(self.frame2,text="{}".format("8"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("8"))
        self.num_9 = Button(self.frame2,text="{}".format("9"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("9"))
        self.add = Button(self.frame2,text="{}".format("+"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("+"))
        self.decimal = Button(self.frame2,text="{}".format("."),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("."))
        self.zero = Button(self.frame2,text="{}".format("0"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("0"))
        self.equal = Button(self.frame2,text="{}".format("="),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("equal"))
        self.substract = Button(self.frame2,text="{}".format("-"),fg = "black",bg = "white",activebackground="yellow",width=10,font=("arial",13),height=3,command=lambda:self.update_output("-"))
        self.clear.grid(row=1,column = 0)
        self.left_curly.grid(row=1,column = 1)
        self.right_curly.grid(row=1,column = 2)
        self.delete.grid(row=1,column = 3)
        self.num_1.grid(row=2,column = 0)
        self.num_2.grid(row=2,column = 1)
        self.num_3.grid(row=2,column = 2)
        self.add.grid(row=2,column = 3)
        self.num_4.grid(row=3,column = 0)
        self.num_5.grid(row=3,column = 1)
        self.num_6.grid(row=3,column = 2)
        self.substract.grid(row=3,column = 3)
        self.num_7.grid(row=4,column = 0)
        self.num_8.grid(row=4,column = 1)
        self.num_9.grid(row=4,column = 2)
        self.mul.grid(row=4,column = 3)
        self.decimal.grid(row=5,column = 0)
        self.zero.grid(row=5,column = 1)
        self.equal.grid(row=5,column = 2)
        self.div.grid(row=5,column = 3)
        self.window.mainloop()
        

obj = Calculator()
obj.input_widget()
obj.number_widget()


