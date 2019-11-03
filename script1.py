from tkinter import *
import random
import time

def ref():
    x = random.randint(1000,600000)
    randomref = str(x)
    rand.set(randomref)
    #cof = float(fries.get())
    cob = float(burger.get())
    c_of_cheese = float(cheese.get())
    coc = float(chicken.get())

    cod = float(drink.get())
    #cost_of_fries = cof * 50.90
    cost_of_burger = cob * 70.5
    cost_of_chicken = coc * 120.6
    cost_of_cheese = c_of_cheese * 90.55
    cost_of_drink = cod * 70.55
    cost = "RS",str('%.2f'%(cost_of_burger + cost_of_chicken + cost_of_cheese + cost_of_drink))

    pay_tax = ((cost_of_burger + cost_of_chicken + cost_of_cheese + cost_of_drink)* 5.20)
    totalcost = (cost_of_burger + cost_of_chicken + cost_of_cheese + cost_of_drink)
    ser_charge = ((cost_of_burger + cost_of_chicken + cost_of_cheese + cost_of_drink)/9)
    service = "Rs",str("%.2f"%(ser_charge))
    overallcost = "Rs",str("%.2f"%(pay_tax+totalcost+ser_charge))
    paidtax = "Rs",str("%.2f"%(pay_tax))
    service_charge.set(service)
    cost_of_meal.set(cost)
    tax.set(paidtax)
    total.set(overallcost)


def exit():
    t.destroy()

def reset():
    fries.set(0)
    burger.set(0)
    chicken.set(0)
    cheese.set(0)
    drink.set(0)
    cost_of_meal.set(0)
    service_charge.set(0)
    tax.set(0)
    total.set(0)

t = Tk()
t.geometry("1600x800+0+0")
t.title("Restaurant Manager System")

text_input = StringVar()
rand = StringVar()
#tops = Frame(t,width = 1600,bg='lime',height = 50,relief = SUNKEN)
#tops.pack(side = TOP)

#f1 = Frame(t,width = 800,height = 700,relief = SUNKEN)
#f1.pack(side = LEFT)

#f2 = Frame(t,width = 800,height = 700,relief = SUNKEN)
#f2.pack(side = RIGHT)

localtime = time.asctime(time.localtime(time.time()))
lb1info = Label(t,font = ('arial',50,'bold'),text = 'Restaurant Management System',fg='steel blue',bd=10,anchor = 'w')
lb1info.place(x=150,y=20)

l2 = Label(t,font = ('arial',15,'bold'),text = localtime,fg='steel blue',bd=10,anchor = 'w')
l2.place(x=550,y=120)

#calculator
#txtdisplay = Entry(f2,font = ('arial',20,'bold'),textvariable = text_input,bd=30,insertwidth = 4)
#txtdisplay.grid(columnspan=4)

#-------------------------Main--------------------
fries = IntVar()
burger = IntVar()
chicken = IntVar()
cheese = IntVar()
drink = IntVar()
cost_of_meal = IntVar()
service_charge = IntVar()
tax = IntVar()
total = IntVar()

lblreference = Label(t,font = ('arial',16,'bold'),text = 'Reference No',bd = 16,anchor = 'w')
lblreference.place(x=100,y=180)
txtreference = Entry(t,font = ('arial',16,'bold'),textvariable = rand,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtreference.place(x=350,y=180)

lbfries = Label(t,font = ('arial',16,'bold'),text = 'Fires',bd = 16,anchor = 'w')
lbfries.place(x=100,y=250)
txtfries = Entry(t,font = ('arial',16,'bold'),textvariable = fries,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtfries.place(x=350,y=250)


lbburger = Label(t,font = ('arial',16,'bold'),text = 'Burger',bd = 16,anchor = 'w')
lbburger.place(x=100,y=320)
txtburger = Entry(t,font = ('arial',16,'bold'),textvariable = burger,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtburger.place(x=350,y=320)

lbchicken = Label(t,font = ('arial',16,'bold'),text = 'Chicken',bd = 16,anchor = 'w')
lbchicken.place(x=100,y=390)
txtchicken = Entry(t,font = ('arial',16,'bold'),textvariable = chicken,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtchicken.place(x=350,y=390)

lbcheese = Label(t,font = ('arial',16,'bold'),text = 'Cheese',bd = 16,anchor = 'w')
lbcheese.place(x=100,y=460)
txtcheese = Entry(t,font = ('arial',16,'bold'),textvariable = cheese,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtcheese.place(x=350,y=460)


lbdrink = Label(t,font = ('arial',16,'bold'),text ='Drink',bd = 16,anchor = 'w')
lbdrink.place(x=750,y=180)
txtdrink = Entry(t,font = ('arial',16,'bold'),textvariable = drink,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtdrink.place(x=990,y=180)


lbcost_of_meal = Label(t,font = ('arial',16,'bold'),text = 'Cost Of Meal',bd = 16,anchor = 'w')
lbcost_of_meal.place(x=750,y=250)
txtcost_of_meal = Entry(t,font = ('arial',16,'bold'),textvariable = cost_of_meal,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtcost_of_meal.place(x=990,y=250)

lbservice_charge = Label(t,font = ('arial',16,'bold'),text = 'Service Charge',bd = 16,anchor = 'w')
lbservice_charge.place(x=750,y=320)
txtservice_charge = Entry(t,font = ('arial',16,'bold'),textvariable = service_charge,bd = 10,insertwidth=4,bg='green',justify = 'right')
txtservice_charge.place(x=990,y=320)

lbtax = Label(t,font = ('arial',16,'bold'),text = 'Tax',bd = 16,anchor = 'w')
lbtax.place(x=750,y=390)
txttax = Entry(t,font = ('arial',16,'bold'),textvariable = tax,bd = 10,insertwidth=4,bg='green',justify = 'right')
txttax.place(x=990,y=390)


lbtotal = Label(t,font = ('arial',16,'bold'),text = 'Total',bd = 16,anchor = 'w')
lbtotal.place(x=750,y=460)
txttotal = Entry(t,font = ('arial',16,'bold'),textvariable =total,bd = 10,insertwidth=4,bg='green',justify = 'right')
txttotal.place(x=990,y=460)



btntotal = Button(t,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Total',bg='orange',command=ref).place(x=350,y=550)
btnreset = Button(t,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Reset',bg='white',command=reset).place(x=600,y=550)
btnexit = Button(t,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Exit',bg='green',command=exit).place(x=850,y=550)



t.mainloop()


#btntotal = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Total',bg='orange',command=ref).grid(row=7,column=2)
#btnreset = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Reset',bg='white',command=reset).grid(row=7,column=3)
#btnexit = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text = 'Exit',bg='green',command=exit).grid(row=7,column=4)
#t.mainloop()