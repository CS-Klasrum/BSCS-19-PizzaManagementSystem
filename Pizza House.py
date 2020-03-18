from tkinter import*
import tkinter as tk
from tkinter import messagebox
import time

root=Tk()
root.geometry("730x510+0+0")
root.title("Pizza Hauz")
root.configure(background = 'Cadet blue')
root.resizable(False,False)
#######################################################################    title #######################################################################################
Tops = Frame(root, bg='Cadet blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP, fill =X)
lblTitle = Label (Tops, font=('Times New Roman', 60, 'bold'),text = "PIZZA HOUSE", bd=21, bg= 'Cadet blue', fg='cornsilk', justify=CENTER)
lblTitle.pack (side = TOP)
##################################################################### 1st frame ######################################################################################
MenuFrame = Frame(root, bg='Cadet blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT,fill=Y)
Pizza_Frame= Frame (MenuFrame,  bg='Cadet blue',  bd=10)
Pizza_Frame.pack (side=TOP,fill=Y)
Pizza_Frame= Frame (MenuFrame,  bg='Powder blue',  bd=10, relief=RIDGE )
Pizza_Frame.pack (side=LEFT,fill=Y)
flavorlbl = Label(Pizza_Frame,text = 'Flavors', bg = 'Powder blue', fg = 'white',font = ('Times new roman',20,'bold','italic'))
flavorlbl.pack(side = TOP)
########################################################################### 2nd Frame ##############################################################################
Second_Frame = Frame (root, bg='Cadet blue', bd=10, relief=RIDGE)
Second_Frame.pack(side=TOP, fill = X)
Add_Toppings_Frame =Frame (Second_Frame, bg='Powder blue',   bd=10, relief=RIDGE )
Add_Toppings_Frame.pack(side=RIGHT, fill = Y)
askTppngs = Label(Add_Toppings_Frame,text = 'DO YOU WANT \nADDITIONAL\nTOPPINGS?', bg = 'Powder blue', fg = 'white',font = ('arial',12,'bold'))
askTppngs.pack(side = TOP)
Size_Frame= Frame (Second_Frame,  bg='Powder blue',   bd=10, relief=RIDGE )
Size_Frame.pack (side=LEFT, fill = Y)
Quantity_Frame= Frame (Second_Frame,  bg='Powder blue',   bd=10, relief=RIDGE)
Quantity_Frame.pack (side=LEFT, fill = Y)

##########################################################      bottom Frame        ####################################################################################

Bottom_Frame = Frame (root, bg='Cadet blue', bd=10, relief=RIDGE)
Bottom_Frame.pack(side=TOP, fill = X)
Total_Frame = Frame(Bottom_Frame,  bg='Powder blue',   bd=10, relief=RIDGE )
Total_Frame.pack (side=LEFT, fill=Y)
Container_Frame = Frame(Bottom_Frame,  bg='Powder blue',   bd=10, relief=RIDGE )
Container_Frame.pack (side=RIGHT)
#####################################################FUNCTION#####################################################################################################
def C1():
    checkbuttons=[C2,C3,C4,C5]
    for i in checkbuttons:
        i.deselect()
def C2():
    checkbuttons=[C1,C3,C4,C5]
    for i in checkbuttons:
        i.deselect()
def C3():
    checkbuttons=[C2,C1,C4,C5]
    for i in checkbuttons:
        i.deselect()
def C4():
    checkbuttons=[C2,C3,C1,C5]
    for i in checkbuttons:
        i.deselect()
def C5():
    checkbuttons=[C2,C3,C4,C1]
    for i in checkbuttons:
        i.deselect()
def Yes():
    Additional_Toppings2.deselect()
def No():
    Additional_Toppings1.deselect()
def Small():
    checkbuttons=[Medium, Large]
    for i in checkbuttons:
        i.deselect()
def Medium():
    checkbuttons=[Small, Large]
    for i in checkbuttons:
        i.deselect()
def Large():
    checkbuttons=[Medium, Small]
    for i in checkbuttons:
        i.deselect()
########################################################## FUNCTION FOR PAYMENT SOLVING ###########################################################################
def total():
    entryTotal.config(state = NORMAL)
    entryTotal.delete(0,END)
    H = var1.get()
    BC = var2.get()
    VG = var3.get()
    PP = var4.get()
    PC = var5.get()
    S = var6.get()
    M = var7.get()
    L = var8.get()
    quanty = varquancount.get()
    ADD = var10.get()
    ADDNO = var11.get()
    if H == 1:
        flav_price = 30
    if BC == 1:
        flav_price = 25
    if VG == 1:
        flav_price = 20
    if PP == 1:
        flav_price = 15
    if PC == 1:
        flav_price = 20
    if ADD == 1:
        addtop = 20
    if ADDNO == 1:
        addtop = 0
    if S == 1:
        size = 50
    elif M == 1:
        size = 90
    elif L == 1:
        size = 130
    else:
        messagebox.showerror("Error","Incomplete Order")
        flav_price = 0
        addtop = 0
        size = 0
        quanty = 0
    if flav_price > 0 and size >0 and quanty >0:
        entryTotal.insert(0,(flav_price+addtop+size)*quanty)
    entryTotal.config(state = DISABLED)
        
##################################################     FLAVOR OF THE PIZZA     #########################################################################################
var1=IntVar()
C1 = Checkbutton(Pizza_Frame, text= "Hawaian   Pizza\t",variable=var1, onvalue = 1, offvalue=0,  font=('Times New Roman', 20, 'bold', 'italic'), bg='Powder blue',command = C1)
var2=IntVar()
C2 = Checkbutton(Pizza_Frame, text= "Bacon and Cheese\t", variable= var2, onvalue = 1, offvalue=0,  font=('Times New Roman', 20, 'bold', 'italic'), bg='Powder blue', command = C2)
var3=IntVar()
C3 = Checkbutton(Pizza_Frame, text= "Vegetable   Garden\t", variable= var3, onvalue = 1, offvalue=0,  font=('Times New Roman', 20, 'bold', 'italic'), bg='Powder blue', command = C3)
var4=IntVar()
C4 = Checkbutton(Pizza_Frame, text= "People's   Choice\t", variable= var4, onvalue = 1, offvalue=0,  font=('Times New Roman', 20, 'bold', 'italic'), bg='Powder blue', command = C4)
var5=IntVar()
C5 = Checkbutton(Pizza_Frame, text= "Pepperoni &Cheese", variable= var5, onvalue = 1, offvalue=0,  font=('Times New Roman', 20, 'bold', 'italic'), bg='Powder blue', command =C5)
C1.pack(side=TOP)
C2.pack(side=TOP)
C3.pack(side=TOP)
C4.pack(side =TOP)
C5.pack(side = TOP)
#################################### FUNCTION EXIT #########################################################################
def exits():
    root.destroy()
#################################### CLEAR FUNCTION #########################################################
def clear():
    entryTotal.config(state = NORMAL)
    entryTotal.delete(0,END)
    checkbuttons=[C2,C1,C3,C4,C5,Small,Medium,Large,Additional_Toppings1,Additional_Toppings2]
    for i in checkbuttons:
        i.deselect()
    counts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    quanEntry['menu'].delete(0,END)
    entryTotal.config(state = DISABLED)
##############################      size of the pizza       ######################


asksize = Label(Size_Frame, text = "SIZE?", bg = 'Powder blue', fg = 'white',font = ('arial',15,'bold'))
asksize.pack(side = TOP, fill = X)
var6=IntVar()
Small = Checkbutton(Size_Frame, text= "Small\t", variable= var6, onvalue =1 , offvalue=0,  font=('arial', 15), bg='Powder blue' , command = Small)
Small.pack(side=TOP,  fill=X)
var7=IntVar()
Medium = Checkbutton(Size_Frame, text= "Medium\t", variable= var7, onvalue = 1, offvalue=0,  font=('arial', 15), bg='Powder blue', command = Medium)
Medium.pack(side=TOP, fill=X)
var8=IntVar()
Large = Checkbutton(Size_Frame, text= "Large\t", variable= var8, onvalue =1, offvalue=0,  font=('arial', 15), bg='Powder blue' , command = Large )
Large.pack(side=TOP,  fill=X)

###############################         QUANTITY    ######################################

var9=IntVar()
Quantity = Label(Quantity_Frame, text= "\nQUANTITY\n", font=('arial', 15), bg='Powder blue',fg="White" )
Quantity.pack(side=TOP,  fill=X)
counts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
varquancount = IntVar(Quantity_Frame)
varquancount.set(counts[0])
quanEntry = OptionMenu(Quantity_Frame, varquancount, *counts)
quanEntry.config( font = ('Times New Roman', 25,'bold'))
quanEntry.pack(side=TOP)

#############################       ADDITIONAL TOPPINGS         #########################
var10=IntVar()
Additional_Toppings1 = Checkbutton (Add_Toppings_Frame, text="Yes\t", variable=var10,onvalue=1, offvalue=0,  font=('arial', 15), bg='Powder blue' , command = Yes)
Additional_Toppings1.pack(side=TOP)
var11=IntVar()
Additional_Toppings2 = Checkbutton(Add_Toppings_Frame, text="No\t", variable=var11, offvalue=0,  font=('arial', 15), bg='Powder blue', command =No)
Additional_Toppings2.pack(side=TOP)

####################################        TOTAL       ###############################

Totalcost = Label(Total_Frame, text = "Total Cost:", font = ('times new roman', 15), bg="Powder blue")
Totalcost.pack(side=TOP, fill=X)
entryTotal = Entry(Total_Frame, width = 10, font = ('times new roman',43,'bold'),state = DISABLED)
entryTotal.pack(side=BOTTOM)

##################################      TOTAL BUTTON        ############################

btnTotal = Button (Container_Frame, padx=16,pady=1, bd=7, fg="black", font=('times new roman',10,"bold"), width=5, text="Total", bg='cyan2',command = total)
btnTotal.pack(side=BOTTOM)

####################################        CLEAR/RESET  BUTTON         #########################

btnReset = Button (Container_Frame, padx=16,pady=1, bd=7, fg="black", font=('times new roman',10,'bold'), width=5, text="Reset/Clear", bg='Green2',command = clear).pack(side=TOP, fill=X)

##################################      EXIT BUTTON         ############################

btnExit = Button (Container_Frame, padx=16,pady=1, bd=7, fg="black", font=('times new roman',10,"bold"), width=5, text="Exit", bg='IndianRed1',command = exits).pack(side=BOTTOM, fill=X)

root.mainloop()
