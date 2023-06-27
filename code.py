import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
import pandas as pd

def get_bitcoin_price():
    selected_date = de.get_date()
    df = pd.read_csv("bitcc.csv")
    filtered_df = df[df['Date'] == str(selected_date)]
    if filtered_df.empty:
        error_message = f"Date {selected_date} doesn't belong to the valid range (2014-09-17 to 2022-02-19)"
        tk.messagebox.showerror(title="Invalid Date", message=error_message)
    else:
        price = filtered_df['Close'].iloc[0].round(2)
        tb.delete(0, 'end')
        tb.insert(0, str(price))

root = tk.Tk()
root.title('Bitcoin')
#root.iconbitmap(tk.PhotoImage(file=r'C:\Users\Fayhaa\PycharmProjects\b\b.ico'))
root.geometry("520x320")

dt = date(2022, 2, 19) # Maximum date for selection
de = DateEntry(root, date_pattern='yy-mm-dd', firstweekday="sunday", start_date=dt)
de.grid(row=1, column=1, padx=5, pady=5)

b = tk.Button(root, text='Submit', command=get_bitcoin_price)
b.grid(row=1, column=2, padx=5)

l = tk.Label(root, text='Bitcoin Price', font=20)
l.grid(row=4, column=1, padx=5)

tb = tk.Entry(root, background='grey', font=14)
tb.grid(row=4, column=2)

root.mainloop()

