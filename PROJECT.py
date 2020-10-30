from tkinter import *
import time
import random
import tkinter.messagebox

root =Tk()
root.geometry("1400x800+0+0")
root.title("Restaurant Billing System")
root.configure(background='yellow')

Tops = Frame(root, bg='red', bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text=' RISTORANTE BILLING SYSTEM', bd=5, bg='light pink',
                fg='dark blue', justify=LEFT)
lblTitle.grid(row=0,column=0)



ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='light green', bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame,bg='sky blue',bd=4)
Drinks_Function.pack(side=TOP)


Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)
# variables

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Total_of_Food = StringVar()
Total_of_Drinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

cocktail = StringVar()
iced_tea = StringVar()
hot_chocolate = StringVar()
orange_juice = StringVar()
milkshake = StringVar()
mountain_dew = StringVar()
sting = StringVar()
coffee = StringVar()

fried_chicken = StringVar()
piz_za = StringVar()
crispy_pasta = StringVar()
Rice_Bowl = StringVar()
Chinese_Noodles = StringVar()
Aloo_Parantha = StringVar()
Fried_Momos = StringVar()
Chilli_Potato = StringVar()

cocktail.set("0")
iced_tea.set("0")
hot_chocolate.set("0")
orange_juice.set("0")
milkshake.set("0")
mountain_dew.set("0")
sting.set("0")
coffee.set("0")

fried_chicken.set("0")
piz_za.set("0")
crispy_pasta.set("0")
Rice_Bowl.set("0")
Chinese_Noodles.set("0")
Aloo_Parantha.set("0")
Fried_Momos.set("0")
Chilli_Potato.set("0")

Date_of_Order.set(time.strftime("%y/%m/%d"))

# Function Declaration

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Total_of_Food.set("")
    Total_of_Drinks.set("")
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


    cocktail.set("0")
    iced_tea.set("0")
    hot_chocolate.set("0")
    orange_juice.set("0")
    milkshake.set("0")
    mountain_dew.set("0")
    sting.set("0")
    coffee.set("0")

    fried_chicken.set("0")
    piz_za.set("0")
    crispy_pasta.set("0")
    Rice_Bowl.set("0")
    Chinese_Noodles.set("0")
    Aloo_Parantha.set("0")
    Fried_Momos.set("0")
    Chilli_Potato.set("0")

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textCocktail.configure(state=DISABLED)
    textIcedTea.configure(state=DISABLED)
    textHotChocolate.configure(state=DISABLED)
    textOrangeJuice.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textMountainDew.configure(state=DISABLED)
    textSting.configure(state=DISABLED)
    textCoffee.configure(state=DISABLED)
    textFriedChicken.configure(state=DISABLED)
    textPizza.configure(state=DISABLED)
    textCrispypasta.configure(state=DISABLED)
    textRiceBowl.configure(state=DISABLED)
    textChineseNoodles.configure(state=DISABLED)
    textAlooParantha.configure(state=DISABLED)
    textFriedMomos.configure(state=DISABLED)
    textChilliPotato.configure(state=DISABLED)

def TotalofUnit():
    Unit1 = float(cocktail.get())
    Unit2 = float(iced_tea.get())
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(orange_juice.get())
    Unit5 = float(milkshake.get())
    Unit6 = float(mountain_dew.get())
    Unit7 = float(sting.get())
    Unit8 = float(coffee.get())

    Unit9 = float(fried_chicken.get())
    Unit10 = float(piz_za.get())
    Unit11 = float(crispy_pasta.get())
    Unit12 = float(Rice_Bowl.get())
    Unit13 = float(Chinese_Noodles.get())
    Unit14 = float(Aloo_Parantha.get())
    Unit15 = float(Fried_Momos.get())
    Unit16 = float(Chilli_Potato.get())

    Prices_Drinks = (Unit1 * 50) + (Unit2 * 45) + (Unit3 * 60) + (Unit4 * 35) + (Unit5 * 70) + (Unit6 * 40) + (Unit7 * 55) + (Unit8 * 75)

    Prices_Food = (Unit9 * 200) + (Unit10 * 250) + (Unit11 * 100) + (Unit12 * 60) + (Unit13 * 120) + (Unit14 * 30) + (Unit15 * 80) + (Unit16 * 100)



    DrinksPrices = "R" + str('%.2f' % Prices_Drinks)
    FoodsPrices = "R" + str('%.2f' % Prices_Food)
    Total_of_Food.set(FoodsPrices)
    Total_of_Drinks.set(DrinksPrices)
    Total_of_Drinks.set(DrinksPrices)
    SC = "R" + str('%.2f' % 2.00)
    ServiceCharge.set(SC)

    Sub_Total_of_Unit = "R" + str('%.2f'%(Prices_Drinks + Prices_Food + 2.00))
    SubTotal.set(Sub_Total_of_Unit)

    Tax = "R" + str('%.2f'%((Prices_Drinks + Prices_Food + 2.00) * 0.18))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks + Prices_Food + 2.00) * 0.18)
    TC = "R" + str('%.2f'%(Prices_Drinks + Prices_Food + 2.00 + TT))
    TotalCost.set(TC)


def drinksCocktail():
    if variable1.get() == 1:
        textCocktail.configure(state=NORMAL)
        textCocktail.focus()
        textCocktail.delete('0', END)
        cocktail.set("")
    elif variable1.get() == 0:
        textCocktail.configure(state=DISABLED)
        cocktail.set("0")

def drinksIceTea():
    if variable2.get() == 1:
        textIcedTea.configure(state=NORMAL)
        textIcedTea.focus()
        textIcedTea.delete('0', END)
        iced_tea.set("")
    elif variable2.get() == 0:
        textIcedTea.configure(state=DISABLED)
        iced_tea.set("0")

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinksOrangeJuice():
    if variable4.get() == 1:
        textOrangeJuice.configure(state=NORMAL)
        textOrangeJuice.delete('0', END)
        textOrangeJuice.focus()
    elif variable4.get() == 0:
        textOrangeJuice.configure(state=DISABLED)
        orange_juice.set("0")

def drinksMilkShake():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshake.set("0")

def drinksMountainDew():
    if variable6.get() == 1:
        textMountainDew.configure(state=NORMAL)
        textMountainDew.delete('0', END)
        textMountainDew.focus()
    elif variable6.get() == 0:
        textMountainDew.configure(state=DISABLED)
        mountain_dew.set("0")

def drinksSting():
    if variable7.get() == 1:
        textSting.configure(state=NORMAL)
        textSting.delete('0', END)
        textSting.focus()
    elif variable7.get() == 0:
        textSting.configure(state=DISABLED)
        sting.set("0")

def drinksCoffee():
    if variable8.get() == 1:
        textCoffee.configure(state=NORMAL)
        textCoffee.delete('0', END)
        textCoffee.focus()
    elif variable8.get() == 0:
        textCoffee.configure(state=DISABLED)
        coffee.set("0")

def foodsFriedChicken():
    if variable9.get() == 1:
        textFriedChicken.configure(state=NORMAL)
        textFriedChicken.delete('0', END)
        textFriedChicken.focus()
    elif variable9.get() == 0:
        textFriedChicken.configure(state=DISABLED)
        fried_chicken.set("0")

def foodsPizza():
    if variable10.get() == 1:
        textPizza.configure(state=NORMAL)
        textPizza.delete('0', END)
        textPizza.focus()
    elif variable10.get() == 0:
        textPizza.configure(state=DISABLED)
        piz_za.set("0")

def foodsCrispypasta():
    if variable11.get() == 1:
        textCrispypasta.configure(state=NORMAL)
        textCrispypasta.delete('0', END)
        textCrispypasta.focus()
    elif variable11.get() == 0:
        textCrispypasta.configure(state=DISABLED)
        crispy_pasta.set("0")

def foodsRiceBowl():
    if variable12.get() == 1:
        textRiceBowl.configure(state=NORMAL)
        textRiceBowl.delete('0', END)
        textRiceBowl.focus()
    elif variable12.get() == 0:
        textRiceBowl.configure(state=DISABLED)
        Rice_Bowl.set("0")

def foodsChineseNoodles():
    if variable13 .get() == 1:
        textChineseNoodles.configure(state=NORMAL)
        textChineseNoodles.delete('0',END)
        textChineseNoodles.focus()
    elif(variable13.get() == 0):
        textChineseNoodles.configure(state=DISABLED)
        Chinese_Noodles.set("0")

def foodsAlooParantha():
    if variable14 .get() == 1:
        textAlooParantha.configure(state=NORMAL)
        textAlooParantha.delete('0', END)
        textAlooParantha.focus()
    elif variable14.get() == 0:
        textAlooParantha.configure(state=DISABLED)
        Aloo_Parantha.set("0")

def foodsFriedMomos():
    if variable15.get() == 1:
        textFriedMomos.configure(state=NORMAL)
        textFriedMomos.delete('0', END)
        textFriedMomos.focus()
    elif variable15.get() == 0:
        textFriedMomos.configure(state=DISABLED)
        Fried_Momos.set("0")

def foodsChilliPotato():
    if variable16 .get() == 1:
        textChilliPotato.configure(state=NORMAL)
        textChilliPotato.delete('0',END)
        textChilliPotato.focus()
    elif(variable16.get() == 0):
        textChilliPotato.configure(state=DISABLED)
        Chilli_Potato.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)


    textReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Cocktail:\t\t\t\t\t' + cocktail.get() + '\n')
    textReceipt.insert(END, 'Iced Tea:\t\t\t\t\t' + iced_tea.get()+'\n')
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Orange Juice:\t\t\t\t\t' + orange_juice.get()+'\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
    textReceipt.insert(END, 'Mountain Dew:\t\t\t\t\t' + mountain_dew.get()+'\n')
    textReceipt.insert(END, 'Sting:\t\t\t\t\t' + sting.get()+'\n')
    textReceipt.insert(END, 'Coffee:\t\t\t\t\t' + coffee.get()+'\n')
    textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
    textReceipt.insert(END, 'Pizza:\t\t\t\t\t' + piz_za.get()+'\n')
    textReceipt.insert(END, 'Crispy pasta:\t\t\t\t\t' + crispy_pasta.get()+'\n')
    textReceipt.insert(END, 'Rice Bowl:\t\t\t\t\t' + Rice_Bowl.get()+'\n')
    textReceipt.insert(END, 'Chinese Noodles:\t\t\t\t\t' + Chinese_Noodles.get()+'\n')
    textReceipt.insert(END, 'Aloo Parantha:\t\t\t\t\t' + Aloo_Parantha.get()+'\n')
    textReceipt.insert(END, 'Fried Momos:\t\t\t\t\t' + Fried_Momos.get()+'\n')
    textReceipt.insert(END, 'Chilli Potato:\t\t\t\t\t' + Chilli_Potato.get()+'\n')
    textReceipt.insert(END, 'Total of Drinks:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    textReceipt.insert(END, 'Total of Foods:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


# Drinks
Cocktail = Checkbutton(Drinks_Function, text='Cocktail', variable=variable1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksCocktail).grid(row=0, sticky=W)
IcedTea = Checkbutton(Drinks_Function, text='Iced Tea', variable=variable2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksIceTea).grid(row=1, sticky=W)
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksHotChocolate).grid(row=2, sticky=W)
OrangeJuice = Checkbutton(Drinks_Function, text='Orange Juice', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksOrangeJuice).grid(row=3, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMilkShake).grid(row=4, sticky=W)
MountainDew = Checkbutton(Drinks_Function, text='Mountain Dew', variable=variable6, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMountainDew).grid(row=5, sticky=W)
Sting = Checkbutton(Drinks_Function, text='Sting', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksSting).grid(row=6, sticky=W)
Coffee = Checkbutton(Drinks_Function, text='Coffee', variable=variable8, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
bg='sky blue', command=drinksCoffee).grid(row=7, sticky=W)
# Drink Entry

textCocktail = Entry(Drinks_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=cocktail)
textCocktail.grid(row=0,column=1)

textIcedTea = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=iced_tea)
textIcedTea.grid(row=1,column=1)

textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=2,column=1)

textOrangeJuice= Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=orange_juice)
textOrangeJuice.grid(row=3,column=1)

textMilkShake = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=milkshake)
textMilkShake.grid(row=4,column=1)

textMountainDew = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=mountain_dew)
textMountainDew.grid(row=5,column=1)

textSting = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=sting)
textSting.grid(row=6,column=1)

textCoffee = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=coffee)
textCoffee.grid(row=7,column=1)
# Foods

FriedChicken = Checkbutton(Food_Function,text="Fried Chicken\t\t\t ",variable=variable9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsFriedChicken).grid(row=0,sticky=W)
Pizza = Checkbutton(Food_Function,text="Pizza",variable=variable10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsPizza).grid(row=1,sticky=W)

Crispypasta = Checkbutton(Food_Function,text="Crispy pasta ",variable=variable11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsCrispypasta).grid(row=2,sticky=W)
RiceBowl = Checkbutton(Food_Function,text="Rice Bowl ",variable=variable12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsRiceBowl).grid(row=3,sticky=W)
ChineseNoodles = Checkbutton(Food_Function,text="Chinese Noodles ",variable=variable13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsChineseNoodles).grid(row=4,sticky=W)
AlooParantha = Checkbutton(Food_Function,text="Aloo Parantha ",variable=variable14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsAlooParantha).grid(row=5,sticky=W)
FriedMomos = Checkbutton(Food_Function,text="Fried Momos ",variable=variable15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsFriedMomos).grid(row=6,sticky=W)
ChilliPotato = Checkbutton(Food_Function,text="Chilli Potato ",variable=variable16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsChilliPotato).grid(row=7,sticky=W)

textFriedChicken=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=fried_chicken)
textFriedChicken.grid(row=0,column=1)

textPizza=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=piz_za)
textPizza.grid(row=1,column=1)

textCrispypasta=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=crispy_pasta)
textCrispypasta.grid(row=2,column=1)

textRiceBowl=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Rice_Bowl)
textRiceBowl.grid(row=3,column=1)

textChineseNoodles=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Chinese_Noodles)
textChineseNoodles.grid(row=4,column=1)

textAlooParantha=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Aloo_Parantha)
textAlooParantha.grid(row=5,column=1)

textFriedMomos=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Fried_Momos)
textFriedMomos.grid(row=6,column=1)

textChilliPotato=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Chilli_Potato)
textChilliPotato.grid(row=7,column=1)

# ToTal Cost
lblTotalofDrinks=Label(Total_Function,font=('arial',14,'bold'),text='Total of Drinks\t',bg='sky blue',fg='black',justify=CENTER)
lblTotalofDrinks.grid(row=0,column=0,sticky=W)
textTotalofDrinks=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Drinks)
textTotalofDrinks.grid(row=0,column=1)

lblTotalofFood=Label(Total_Function,font=('arial',14,'bold'),text='Total of Foods  ',bg='sky blue',fg='black',justify=CENTER)
lblTotalofFood.grid(row=1,column=0,sticky=W)
textTotalofFood=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Food)
textTotalofFood.grid(row=1,column=1)

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='sky blue',fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
# Payment information

lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Total_Function,font=('arial',14,'bold'),text='\tSub Total',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
textSubTotal=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'), insertwidth=2,justify=RIGHT,textvariable=SubTotal)
textSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
textReceipt.grid(row=0,column=0)


# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='black',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='black',command=Reset).grid(row=0,column=2)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='black',command=iExit).grid(row=0,column=3)


# Calculator Display




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




# Calculator
txtDisplay = Entry(Calculator_Function, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# CALCULATOR BUTTONS
button7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg='gold', font=('arial', 12, 'bold'), width=4, text='7',bg='black',command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='8',bg='black',command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='9',bg='black',command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='+',bg='black',command=lambda:btnClick('+')).grid(row=2,column=3)

button4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='4',bg='black',command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='5',bg='black',command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='6',bg='black',command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='-',bg='black',command=lambda:btnClick('-')).grid(row=3,column=3)

button1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='1',bg='black',command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='2',bg='black',command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='3',bg='black',command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='*',bg='black',command=lambda:btnClick('*')).grid(row=4,column=3)

button0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='0',bg='black',command=lambda:btnClick(0)).grid(row=5,column=0)
buttonClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='C',bg='black',command=btnClear).grid(row=5,column=1)
buttonEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='=',bg='black',command=btnEquals).grid(row=5,column=2)
buttonDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='/',bg='black',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()

