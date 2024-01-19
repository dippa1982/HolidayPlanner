from tkinter import ttk
import tkinter as Tk
import datetime
import math

def num_weeks(tab):
    def calculate_weeks():
        try:
            day = int(day_entry.get())
            month = int(month_entry.get())
            year = int(year_entry.get())
            input_date = datetime.date(year, month, day)
            start_date = datetime.date.today()
            start_date_monday = start_date - datetime.timedelta(days=start_date.weekday())
            num_of_weeks = math.ceil((input_date - start_date_monday).days / 7.0)
            number_of_week.config(text=str(num_of_weeks))
        except ValueError:
            print("Please enter valid day, month, and year.")

    day_label = Tk.Label(tab,text="Enter Day/Month/Year in each box",font=('Times', 16))
    day_entry = Tk.Entry(tab,width=15, font=('Georgia 20'))
    month_entry = Tk.Entry(tab,width=15, font=('Georgia 20'))
    year_entry = Tk.Entry(tab,width=15, font=('Georgia 20'))
    day_label.pack()
    day_entry.pack()
    month_entry.pack()
    year_entry.pack()
    calculate_button = Tk.Button(tab, text="Calculate Weeks", command=calculate_weeks)
    calculate_button.pack()
    number_of_week = Tk.Label(tab, text="")
    number_of_week.pack()
    return number_of_week

def total():
    holiday_cost = holiday_amount.get()
    spend_cost = spending_amount.get()
    train_cost = train_entry.get()
    hotel_cost = hotel_entry.get()
    parking_cost = parking_entry.get()
    transfer_cost = transfer_entry.get()
    fuel_cost = fuel_entry.get()
    airport_cost = airport_entry.get()
    total_additional = float(train_cost) + float(hotel_cost) + float(parking_cost) + float(transfer_cost) + float(fuel_cost) + float(airport_cost)
    total_cost_2 = float(holiday_cost) + float(total_additional) + float(spend_cost)
    num_weeks_label = num_weeks_label_page1
    total_entry.delete(0, Tk.END)
    total_entry.insert(0, total_cost_2)
    num_of_weeks = float(num_weeks_label.cget("text"))
    spread_entry.delete(0, Tk.END)
    rounded_result = round(total_cost_2 / num_of_weeks,2)
    spread_entry.insert (0, rounded_result)

#####Window_1#####
window_1 = Tk.Tk()
window_1.geometry("400x600")
window_1.title("Holiday Planner")

notebook = ttk.Notebook(window_1)
page_1 = ttk.Frame(notebook)
notebook.add(page_1, text="Date Entry")
num_weeks_label_page1 = num_weeks(page_1)

####Window_2######
page_2 = ttk.Frame(notebook)
notebook.add(page_2, text="Additional costs")

######Creating##########
holiday_label = Tk.Label(page_2, text="Enter Holiday Amount",font=('Times', 16))
holiday_amount = Tk.Entry(page_2,width=15, font=('Georgia 20'))
spend_label = Tk.Label(page_2, text="Amount of Spending Money",font=('Times', 16))
spending_amount = Tk.Entry(page_2,width=15, font=('Georgia 20'))
train_label = Tk.Label(page_2, text="Train Cost",font=('Times', 16))
train_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))
hotel_label = Tk.Label(page_2, text="Hotel Cost",font=('Times', 16))
hotel_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))
parking_label = Tk.Label(page_2, text="Parking Cost",font=('Times', 16))
parking_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))
fuel_label = Tk.Label(page_2,text="Fuel/Charging Cost",font=('Times', 16))
fuel_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))
airport_label = Tk.Label(page_2,text="Airport Food/Lounge Cost",font=('Times', 16))
airport_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))
transfer_label = Tk.Label(page_2,text="Airport Transfer Cost",font=('Times', 16))
transfer_entry = Tk.Entry(page_2,width=15, font=('Georgia 20'))

########Packing####
holiday_label.pack()
holiday_amount.pack()
spend_label.pack()
spending_amount.pack()
train_label.pack()
train_entry.pack()
hotel_label.pack()
hotel_entry.pack()
parking_label.pack()
parking_entry.pack()
fuel_label.pack()
fuel_entry.pack()
airport_label.pack()
airport_entry.pack()
transfer_label.pack()
transfer_entry.pack()

####Window_3######
page_3 = ttk.Frame(notebook)
notebook.add(page_3, text="Total Costs")

total_cost = Tk.Label(page_3, text="Total Cost",font=('Times', 16))
spread_cost = Tk.Label(page_3, text="Spread Across Weeks",font=('Times', 16))

total_entry = Tk.Entry(page_3,width=15, font=('Georgia 20'))
spread_entry = Tk.Entry(page_3,width=15, font=('Georgia 20'))
calculate_button = Tk.Button(page_3, text="Calculate", command=total)

total_cost.pack()
total_entry.pack()
spread_cost.pack()
spread_entry.pack()
calculate_button.pack()
notebook.pack(expand=True, fill="both")

Tk.mainloop()
