from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
root=Tk()

root.title("radhey fast food")
root.geometry("900x500")

burger=ImageTk.PhotoImage(Image.open("burger1.png"))
burgerimg=Label(root)
burgerimg["image"]=burger
burgerimg.place(relx=0.7,rely=0.5,anchor=CENTER)

lbl_heading=Label(root,text="Radhey fast food corner",font=("times",30,"bold"),fg="orange")
lbl_heading.place(relx=0.3,rely=0.1,anchor=CENTER)

lbl_selectDish=Label(root,text="Select Dish",font=("times",15,"bold"),fg="black")
lbl_selectDish.place(relx=0.2,rely=0.2,anchor=CENTER)

dish=["Burger","Coffee"]
dish_dd=ttk.Combobox(root,state="readonly",values=dish)
dish_dd.place(relx=0.2,rely=0.3,anchor=CENTER)

lbl_selectAddOns=Label(root,text="Select Addons",font=("times",15,"bold"),fg="black")
lbl_selectAddOns.place(relx=0.2,rely=0.5,anchor=CENTER)

toppings=[]
toppings_dd=ttk.Combobox(root,state="readonly",values=toppings)
toppings_dd.place(relx=0.2,rely=0.6,anchor=CENTER)

dish_amount=Label(root,font=("times",20,"bold"))
dish_amount.place(relx=0.3,rely=0.8,anchor=CENTER)

class parent ():
    def __init__(self):
        print("this is parent class")
    def menu(dish):
        if (dish=="Burger"):
            print("you can add the following toppings")
            print("More Cheese | More Veggies")
        elif (dish=="Coffee"):
            print("you can add the following toppings")
            print("More Ice-cream | More Chocolate")
        else :
            print("Enter an valid dish")
            
    def finalAmount(dish,addOns):
        if(dish=="Burger" and addOns=="More Cheese"):
            print("you need to pay Rs.80")
        elif(dish=="Burger" and addOns=="More Veggies"):
            print("you need to pay Rs.60")
        elif(dish=="Coffee" and addOns=="More Ice-cream"):
            print("you need to pay Rs.200")
        elif(dish=="Coffee"and addOns=="More Chocolate"):
            print("you need to pay Rs.150")
            
class child1 (parent):
    def __init__(self,dish):
        self.dish=dish
        
    def getMenu(self):
        parent.menu(self.dish)
        
class child2 (parent):
    def __init__(self,dish,addOns):
        self.dish=dish
        self.addOns=addOns
        
    def getFinalAmount(self):
        parent.finalAmount(self.dish, self.addOns)
        
child1Obj=child1("Burger")
child1Obj.getMenu()

child2Obj=child2("Coffee","More Ice-cream")
child2Obj.getFinalAmount()

root.mainloop()