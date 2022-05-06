from tkinter import*

root = Tk()

root.title("Sales Application")
root.geometry("1000x1000")
root.configure(background="blue")

label_month = Label(root)
label_profits = Label(root)
label_max_profits = Label(root)
label_min_profits = Label(root)


months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
profits = (20000, 45000, 78000, 97000, 12000, 400000, 65000, 54000, 10000,30000,70000,90000)

label_month["text"] = "months: " + str(months)
label_profits["text"] = "Profits are: " + str(profits)

def maxProfit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)
    
    max_profit_month = months[max_profit_index]
    label_max_profits["text"] = "The Maximum Profit of " + str(max_profit) + " was recorded in " + str(max_profit_month)

def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)

    min_profit_month = months[min_profit_index]
    label_min_profits["text"] = "The Minimun Profit of " + str(min_profit) + " was recorded in " + str(min_profit_month)
    
btn = Button(root,text="Show max Profit month ", command=maxProfit, bg="blue", fg="black")
btn2 = Button(root,text="Show min Profit month ", command=minProfit, bg="blue", fg="black")

label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profits.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label_max_profits.place(relx=0.5, rely=0.5, anchor=CENTER)
btn2.place(relx=0.5, rely=0.6, anchor=CENTER)
label_min_profits.place(relx=0.5, rely=0.7, anchor=CENTER)




root.mainloop()