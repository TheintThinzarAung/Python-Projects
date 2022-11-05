from tkinter import *
from tkinter import ttk
import tkinter as tk
import tempfile
import os
from time import strftime
from datetime import datetime

class PosPython:

    def __init__(self, root):
        self.root = root
        self.root.title("Point-of-Sale System Software")
        self.root.geometry("1380x780+0+0")
        self.root.configure(background="#3399ff")
        self.input_value = True

        # =============================== Variable Declaration ==================================

        self.Coffee1 = PhotoImage(file="images/coffee1.gif")
        self.Coffee2 = PhotoImage(file="images/coffee2.gif")
        self.Coffee3 = PhotoImage(file="images/coffee3.gif")
        self.Coffee4 = PhotoImage(file="images/coffee4.gif")
        self.Coffee5 = PhotoImage(file="images/coffee5.gif")
        self.Coffee6 = PhotoImage(file="images/coffee6.gif")

        self.Cake1 = PhotoImage(file="images/cake1.gif")
        self.Cake2 = PhotoImage(file="images/cake2.gif")
        self.Cake3 = PhotoImage(file="images/cake3.gif")
        self.Cake4 = PhotoImage(file="images/cake4.gif")
        self.Cake5 = PhotoImage(file="images/cake5.gif")
        self.Cake6 = PhotoImage(file="images/cake6.gif")

        self.Juice1 = PhotoImage(file="images/juice1.gif")
        self.Juice2 = PhotoImage(file="images/juice2.gif")
        self.Juice3 = PhotoImage(file="images/juice3.gif")
        self.Juice4 = PhotoImage(file="images/juice4.gif")
        self.Juice5 = PhotoImage(file="images/juice5.gif")
        self.Juice6 = PhotoImage(file="images/juice6.gif")

        self.Fruit1 = PhotoImage(file="images/fruit1.gif")
        self.Fruit2 = PhotoImage(file="images/fruit2.gif")
        self.Fruit3 = PhotoImage(file="images/fruit3.gif")
        self.Fruit4 = PhotoImage(file="images/fruit4.gif")
        self.Fruit5 = PhotoImage(file="images/fruit5.gif")
        self.Fruit6 = PhotoImage(file="images/fruit6.gif")

        global operator
        operator = ""
        change_input = StringVar()
        cash_input = StringVar()
        tax_input = StringVar()
        subtotal_input = StringVar()
        total_input = StringVar()
        choice = StringVar()

        # ============================== Layout Management ======================================
        main_frame = Frame(self.root, bg="#3399ff")
        main_frame.grid(padx=8, pady=8)

        ait_frame = Frame(main_frame, bd=0, width=1360, height=100, padx=4, pady=10, bg="#3399ff",
                          relief=RIDGE)
        ait_frame.pack(side=TOP, anchor=W)

        lbl_ait = Label(ait_frame, font=("arial", 24, "bold"), text="Point of Sale System by Theint Thinzar Aung",
                        bd=0, fg="white", bg="#3399ff")
        lbl_ait.pack()

        time_frame = Frame(main_frame, bd=0, width=1360, height=100, padx=4, pady=4, bg="#3399ff",
                           relief=RIDGE)
        time_frame.pack(side=TOP, anchor='e')

        lbl_date = Label(time_frame, text=f"{datetime.now(): %a, %d %b %Y}", fg="white", bg="#3399ff",
                         font=("helvetica", 12))
        lbl_date.pack()

        # ================================= Display Current Time ==================================
        def time():
            string = strftime("%H:%M:%S %p")
            lbl_current_time.config(text=string)
            lbl_current_time.after(1000, time)

        lbl_current_time = Label(time_frame, fg="white", bg="#3399ff", font=("helvetica", 12, "bold"))
        lbl_current_time.pack()
        time()

        address_frame = Frame(main_frame, width=1350, height=160, padx=4, pady=4, bg="#3399ff")
        address_frame.pack(side=BOTTOM, anchor='e')

        lbl_address = Label(address_frame, text="theintthinzaraung1995@gmail.com, +959 969690358", fg="white",
                            bg="#3399ff", font=("helvetica", 12, "bold"))
        lbl_address.pack()

        button_frame = Frame(main_frame, bd=5, width=1350, height=160, padx=4, pady=4, bg="#3399ff",
                             relief=RIDGE)
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=5, width=1300, height=400, padx=5, pady=4, bg="#3399ff",
                           relief=RIDGE)
        data_frame.pack(side=BOTTOM)

        data_frame_left_cover = LabelFrame(data_frame, bd=5, width=800, height=300, pady=2,
                                           bg="#3399ff", relief=RIDGE, font=("Arial", 12, "bold"),
                                           text="Point of Sale")
        data_frame_left_cover.pack(side=LEFT)

        change_button_frame = Frame(data_frame_left_cover, bd=5, width=300, height=460, pady=5,
                                    relief=RIDGE)
        change_button_frame.pack(side=LEFT, padx=4)

        receipt_frame = Frame(data_frame_left_cover, bd=5, width=200, height=400, pady=5, padx=1,
                              relief=RIDGE)
        receipt_frame.pack(side=RIGHT, padx=0)

        food_item_frame = LabelFrame(data_frame, bd=5, width=450, height=300, padx=5, pady=5,
                                     relief=RIDGE, bg="#3399ff", font=("Arial", 12, "bold"),
                                     text="Items")
        food_item_frame.pack(side=RIGHT)

        cal_frame = Frame(button_frame, bd=5, width=432, height=140, relief=RIDGE, bg="#0080ff")
        cal_frame.grid(row=0, column=0, padx=5)

        change_frame = Frame(button_frame, bd=5, width=500, height=140, pady=2, relief=RIDGE, bg="#0080ff")
        change_frame.grid(row=0, column=1, padx=5)

        remove_frame = Frame(button_frame, bd=5, width=500, height=140, pady=2, relief=RIDGE, bg="#3399ff")
        remove_frame.grid(row=0, column=2, padx=5)

        # =================================== Functions =======================================
        def ait_cake1():
            item_cost = 1500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake One", "1", "1500"))
            self.txtReceipt.insert(END, ("Cake One" + "\t\t\t") + "1" + "\t\t\t\t" + "1500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1500) + ((item_cost-1500) * tax)/100)))

        def ait_cake2():
            item_cost = 5500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake Two", "1", "5500"))
            self.txtReceipt.insert(END, ("Cake Two" + "\t\t\t") + "1" + "\t\t\t\t" + "5500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-5500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-5500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-5500) + ((item_cost-5500) * tax)/100)))

        def ait_cake3():
            item_cost = 9500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake Three", "1", "9500"))
            self.txtReceipt.insert(END, ("Cake Three" + "\t\t\t") + "1" + "\t\t\t\t" + "9500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-9500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-9500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-9500) + ((item_cost-9500) * tax)/100)))

        def ait_cake4():
            item_cost = 8500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake Four", "1", "8500"))
            self.txtReceipt.insert(END, ("Cake Four" + "\t\t\t") + "1" + "\t\t\t\t" + "8500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-8500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-8500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-8500) + ((item_cost-8500) * tax)/100)))

        def ait_cake5():
            item_cost = 4500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake Five", "1", "4500"))
            self.txtReceipt.insert(END, ("Cake Five" + "\t\t\t") + "1" + "\t\t\t\t" + "4500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-4500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-4500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-4500) + ((item_cost-4500) * tax)/100)))

        def ait_cake6():
            item_cost = 7500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Cake Six", "1", "7500"))
            self.txtReceipt.insert(END, ("Cake Six" + "\t\t\t") + "1" + "\t\t\t\t" + "7500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-7500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-7500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-7500) + ((item_cost-7500) * tax)/100)))

        def ait_coffee1():
            item_cost = 1500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee One", "1", "1500"))
            self.txtReceipt.insert(END, ("Coffee One" + "\t\t\t") + "1" + "\t\t\t\t" + "1500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1500) + ((item_cost-1500) * tax)/100)))

        def ait_coffee2():
            item_cost = 1500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee Two", "1", "1500"))
            self.txtReceipt.insert(END, ("Coffee Two" + "\t\t\t") + "1" + "\t\t\t\t" + "1500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1500) + ((item_cost-1500) * tax)/100)))

        def ait_coffee3():
            item_cost = 2000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee Three", "1", "2000"))
            self.txtReceipt.insert(END, ("Coffee Three" + "\t\t\t") + "1" + "\t\t\t\t" + "2000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-2000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-2000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-2000) + ((item_cost-2000) * tax)/100)))

        def ait_coffee4():
            item_cost = 6500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee Four", "1", "6500"))
            self.txtReceipt.insert(END, ("Coffee Four" + "\t\t\t") + "1" + "\t\t\t\t" + "6500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-6500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-6500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-6500) + ((item_cost-6500) * tax)/100)))

        def ait_coffee5():
            item_cost = 6500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee Five", "1", "6500"))
            self.txtReceipt.insert(END, ("Coffee Five" + "\t\t\t") + "1" + "\t\t\t\t" + "6500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-6500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-6500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-6500) + ((item_cost-6500) * tax)/100)))

        def ait_coffee6():
            item_cost = 4500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Coffee Six", "1", "4500"))
            self.txtReceipt.insert(END, ("Coffee Six" + "\t\t\t") + "1" + "\t\t\t\t" + "4500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-4500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-4500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-4500) + ((item_cost-4500) * tax)/100)))

        def ait_fruit1():
            item_cost = 2000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit One", "1", "2000"))
            self.txtReceipt.insert(END, ("Fruit One" + "\t\t\t") + "1" + "\t\t\t\t" + "2000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-2000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-2000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-2000) + ((item_cost-2000) * tax)/100)))

        def ait_fruit2():
            item_cost = 2000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit Two", "1", "2000"))
            self.txtReceipt.insert(END, ("Fruit Two" + "\t\t\t") + "1" + "\t\t\t\t" + "2000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-2000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-2000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-2000) + ((item_cost-2000) * tax)/100)))

        def ait_fruit3():
            item_cost = 3000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit Three", "1", "3000"))
            self.txtReceipt.insert(END, ("Fruit Three" + "\t\t\t") + "1" + "\t\t\t\t" + "3000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-3000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-3000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-3000) + ((item_cost-3000) * tax)/100)))

        def ait_fruit4():
            item_cost = 3000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit Four", "1", "3000"))
            self.txtReceipt.insert(END, ("Fruit Four" + "\t\t\t") + "1" + "\t\t\t\t" + "3000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-3000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-3000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-3000) + ((item_cost-3000) * tax)/100)))

        def ait_fruit5():
            item_cost = 1000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit Five", "1", "1000"))
            self.txtReceipt.insert(END, ("Fruit Five" + "\t\t\t") + "1" + "\t\t\t\t" + "1000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1000) + ((item_cost-1000) * tax)/100)))

        def ait_fruit6():
            item_cost = 2000
            tax = 5
            self.POS_record.insert("", tk.END, values=("Fruit Six", "1", "2000"))
            self.txtReceipt.insert(END, ("Fruit Six" + "\t\t\t") + "1" + "\t\t\t\t" + "2000" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-2000)))
                tax_input.set(str("Ks %.2f" % (((item_cost-2000) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-2000) + ((item_cost-2000) * tax)/100)))

        def ait_juice1():
            item_cost = 1500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice One", "1", "1500"))
            self.txtReceipt.insert(END, ("Juice One" + "\t\t\t") + "1" + "\t\t\t\t" + "1500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1500) + ((item_cost-1500) * tax)/100)))

        def ait_juice2():
            item_cost = 1500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice Two", "1", "1500"))
            self.txtReceipt.insert(END, ("Juice Two" + "\t\t\t") + "1" + "\t\t\t\t" + "1500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-1500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-1500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-1500) + ((item_cost-1500) * tax)/100)))

        def ait_juice3():
            item_cost = 4500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice Three", "1", "4500"))
            self.txtReceipt.insert(END, ("Juice Three" + "\t\t\t") + "1" + "\t\t\t\t" + "4500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-4500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-4500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-4500) + ((item_cost-4500) * tax)/100)))

        def ait_juice4():
            item_cost = 2500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice Four", "1", "2500"))
            self.txtReceipt.insert(END, ("Juice Four" + "\t\t\t") + "1" + "\t\t\t\t" + "2500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-2500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-2500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-2500) + ((item_cost-2500) * tax)/100)))

        def ait_juice5():
            item_cost = 5500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice Five", "1", "5500"))
            self.txtReceipt.insert(END, ("Juice Five" + "\t\t\t") + "1" + "\t\t\t\t" + "5500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-5500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-5500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-5500) + ((item_cost-5500) * tax)/100)))

        def ait_juice6():
            item_cost = 5500
            tax = 5
            self.POS_record.insert("", tk.END, values=("Juice Six", "1", "5500"))
            self.txtReceipt.insert(END, ("Juice Six" + "\t\t\t") + "1" + "\t\t\t\t" + "5500" + "\n")
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
                subtotal_input.set(str("Ks %.2f" % (item_cost-5500)))
                tax_input.set(str("Ks %.2f" % (((item_cost-5500) * tax)/100)))
                total_input.set(str("Ks %.2f" % ((item_cost-5500) + ((item_cost-5500) * tax)/100)))

        def btn_click(numbers):
            global operator
            operator += str(numbers)
            cash_input.set(operator)

        def change():
            cash_input.set("0")
            change_input.set("")

        def i_print():
            q = self.txtReceipt.get("1.0", "end-1c")
            print(q)
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(q)
            os.startfile(filename)

        def method_of_pay():
            if choice.get()== "Cash":
                self.txtCost.focus()
                cash_input.set("")
            elif choice.get() == "":
                cash_input.set("0")
                change_input.set("")

        def give_change():
            item_cost = 0
            tax = 5
            cashing = float(cash_input.get())
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
            change_input.set(str("Ks %.0f" % (cashing-(item_cost + ((item_cost * tax)/100)))))
            if cash_input.get() == "0":
                change_input.set("")
                method_of_pay()

        def btn_clear_display():
            global operator
            operator = ""
            change_input.set("")
            cash_input.set("0")
            tax_input.set("")
            subtotal_input.set("")
            total_input.set("")
            for i in self.POS_record.get_children():
                self.POS_record.delete(i)

        def delete():
            item_cost = 0
            tax = 5
            selected_item = (self.POS_record.selection()[0])
            self.POS_record.delete(selected_item)
            for child in self.POS_record.get_children():
                item_cost += float(self.POS_record.item(child, "values")[2])
            subtotal_input.set(str("Ks %.2f" % item_cost))
            tax_input.set(str("Ks %.2f" % ((item_cost * tax)/100)))
            total_input.set(str("Ks %.2f" % (item_cost + ((item_cost * tax)/100))))
            give_change()

        # =================================== Calculate Frame =================================
        self.lblSubTotal = Label(cal_frame, font=("arial", 14, "bold"), text="Sub Total", bd=5,
                                 fg="white", bg="#0080ff")
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(cal_frame, font=("arial", 14, "bold"), bd=2, width=24, justify="left",
                                 textvariable=subtotal_input)
        self.txtSubTotal.grid(row=0, column=1)

        self.lblTax = Label(cal_frame, font=("arial", 14, "bold"), text="Tax", bd=5,
                            fg="white", bg="#0080ff")
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(cal_frame, font=("arial", 14, "bold"), bd=2, width=24, justify="left",
                            textvariable=tax_input)
        self.txtTax.grid(row=1, column=1)

        self.lblTotal = Label(cal_frame, font=("arial", 14, "bold"), text="Total", bd=5,
                              fg="white", bg="#0080ff")
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(cal_frame, font=("arial", 14, "bold"), bd=2, width=24, justify="left",
                              textvariable=total_input)
        self.txtTotal.grid(row=2, column=1)

        # ===============================  Change Frame Widget ===============================
        self.lblMop = Label(change_frame, font=("arial", 14, "bold"), text="Method of Payment", bd=2,
                            fg="white", bg="#0080ff")
        self.lblMop.grid(row=0, column=0, sticky=W, padx=2)

        self.cboMop = ttk.Combobox(change_frame, width=36, font=("arial", 14, "bold"), state="readonly",
                                   textvariable=choice, justify=RIGHT)
        self.cboMop['values'] = ('', 'Cash', 'KBZ Pay', 'Wavemoney', 'CB Pay', 'AYA Pay')
        self.cboMop.current(0)
        self.cboMop.grid(row=0, column=1)

        self.lblCost = Label(change_frame, font=("arial", 14, "bold"), text="Cost", bd=5,
                             fg="white", bg="#0080ff")
        self.lblCost.grid(row=1, column=0, sticky=W, padx=2)
        self.txtCost = Entry(change_frame, font=("arial", 14, "bold"), bd=2, width=38,
                             textvariable=cash_input, justify=RIGHT)
        self.txtCost.grid(row=1, column=1)
        self.txtCost.insert(0, '0')

        self.lblChange = Label(change_frame, font=("arial", 14, "bold"), text="Change", bd=5,
                               fg="white", bg="#0080ff")
        self.lblChange.grid(row=2, column=0, sticky=W, padx=2)
        self.txtChange = Entry(change_frame, font=("arial", 14, "bold"), bd=2, width=38,
                               textvariable=change_input, justify=RIGHT)
        self.txtChange.grid(row=2, column=1, sticky=W)

        # ======================== Buttons for Pay, Print, Remove, Reset ====================
        self.btnPay = Button(remove_frame, padx=2, font=("ariial", 15, "bold"), text="Pay", width=10,
                             height=1, bd=2, fg="white", bg="#0066CC", command=give_change)
        self.btnPay.grid(row=0, column=0, padx=4, pady=2)

        self.btnPrint = Button(remove_frame, padx=2, font=("ariial", 15, "bold"), text="Print", width=10,
                               height=1, bd=2, fg="white", bg="#0066CC", command=i_print)
        self.btnPrint.grid(row=1, column=1, padx=4, pady=2)

        self.btnReset = Button(remove_frame, padx=2, font=("ariial", 15, "bold"), text="Reset", width=10,
                               height=1, bd=2, fg="white", bg="#0066CC", command=btn_clear_display)
        self.btnReset.grid(row=1, column=0, padx=4, pady=2)

        self.btnRemoveItem = Button(remove_frame, padx=2, font=("ariial", 15, "bold"), text="Remove Item", width=10,
                                    height=1, bd=2, fg="white", bg="#0066CC", command=delete)
        self.btnRemoveItem.grid(row=0, column=1, padx=4, pady=2)

        # ================================= Number Button Calculate 7, 8, 9 =============================
        self.btn7 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="7",
                           bd=8, bg="#3399ff", command=lambda: btn_click(7)).grid(row=0, column=0)
        self.btn8 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="8",
                           bd=8, bg="#3399ff", command=lambda: btn_click(8)).grid(row=0, column=1)
        self.btn9 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="9",
                           bd=8, bg="#3399ff", command=lambda: btn_click(9)).grid(row=0, column=2)

        self.btn4 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="4",
                           bd=8, bg="#3399ff", command=lambda: btn_click(4)).grid(row=1, column=0)
        self.btn5 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="5",
                           bd=8, bg="#3399ff", command=lambda: btn_click(5)).grid(row=1, column=1)
        self.btn6 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="6",
                           bd=8, bg="#3399ff", command=lambda: btn_click(6)).grid(row=1, column=2)

        self.btn1 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="1",
                           bd=8, bg="#3399ff", command=lambda: btn_click(1)).grid(row=2, column=0)
        self.btn2 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="2",
                           bd=8, bg="#3399ff", command=lambda: btn_click(2)).grid(row=2, column=1)
        self.btn3 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="3",
                           bd=8, bg="#3399ff", command=lambda: btn_click(3)).grid(row=2, column=2)

        self.btn0 = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="0",
                           bd=8, bg="#3399ff", command=lambda: btn_click(0)).grid(row=3, column=0)
        self.btnDot = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text=".",
                           bd=8, bg="#3399ff", command=lambda: btn_click(".")).grid(row=3, column=1)
        self.btnC = Button(change_button_frame, padx=13, pady=22, font=("arial", 20, "bold"), text="C",
                           bd=8, bg="#3399ff", command=change).grid(row=3, column=2)

        # ================================= Button for Coffee ================================
        self.btnCoffee1 = Button(food_item_frame, padx=2, image=self.Coffee1, width=104, height=104, bd=2,
                                 command=ait_coffee1)
        self.btnCoffee1.grid(row=0, column=0, padx=4, pady=2)
        self.btnCoffee2 = Button(food_item_frame, padx=2, image=self.Coffee2, width=104, height=104, bd=2,
                                 command=ait_coffee2)
        self.btnCoffee2.grid(row=0, column=1, padx=4, pady=2)
        self.btnCoffee3 = Button(food_item_frame, padx=2, image=self.Coffee3, width=104, height=104, bd=2,
                                 command=ait_coffee3)
        self.btnCoffee3.grid(row=0, column=2, padx=4, pady=2)
        self.btnCoffee4 = Button(food_item_frame, padx=2, image=self.Coffee4, width=104, height=104, bd=2,
                                 command=ait_coffee4)
        self.btnCoffee4.grid(row=0, column=3, padx=4, pady=2)
        self.btnCoffee5 = Button(food_item_frame, padx=2, image=self.Coffee5, width=104, height=104, bd=2,
                                 command=ait_coffee5)
        self.btnCoffee5.grid(row=0, column=4, padx=4, pady=2)
        self.btnCoffee6 = Button(food_item_frame, padx=2, image=self.Coffee6, width=104, height=104, bd=2,
                                 command=ait_coffee6)
        self.btnCoffee6.grid(row=0, column=5, padx=4, pady=2)

        # ================================= Button for Cake ================================
        self.btnCake1 = Button(food_item_frame, padx=2, image=self.Cake1, width=104, height=104, bd=2,
                               command=ait_cake1)
        self.btnCake1.grid(row=1, column=0, padx=4, pady=2)
        self.btnCake2 = Button(food_item_frame, padx=2, image=self.Cake2, width=104, height=104, bd=2,
                               command=ait_cake2)
        self.btnCake2.grid(row=1, column=1, padx=4, pady=2)
        self.btnCake3 = Button(food_item_frame, padx=2, image=self.Cake3, width=104, height=104, bd=2,
                               command=ait_cake3)
        self.btnCake3.grid(row=1, column=2, padx=4, pady=2)
        self.btnCake4 = Button(food_item_frame, padx=2, image=self.Cake4, width=104, height=104, bd=2,
                               command=ait_cake4)
        self.btnCake4.grid(row=1, column=3, padx=4, pady=2)
        self.btnCake5 = Button(food_item_frame, padx=2, image=self.Cake5, width=104, height=104, bd=2,
                               command=ait_cake5)
        self.btnCake5.grid(row=1, column=4, padx=4, pady=2)
        self.btnCake6 = Button(food_item_frame, padx=2, image=self.Cake6, width=104, height=104, bd=2,
                               command=ait_cake6)
        self.btnCake6.grid(row=1, column=5, padx=4, pady=2)

        # ================================= Button for Juice ================================
        self.btnJuice1 = Button(food_item_frame, padx=2, image=self.Juice1, width=104, height=104, bd=2,
                                command=ait_juice1)
        self.btnJuice1.grid(row=2, column=0, padx=4, pady=2)
        self.btnJuice2 = Button(food_item_frame, padx=2, image=self.Juice2, width=104, height=104, bd=2,
                                command=ait_juice2)
        self.btnJuice2.grid(row=2, column=1, padx=4, pady=2)
        self.btnJuice3 = Button(food_item_frame, padx=2, image=self.Juice3, width=104, height=104, bd=2,
                                command=ait_juice3)
        self.btnJuice3.grid(row=2, column=2, padx=4, pady=2)
        self.btnJuice4 = Button(food_item_frame, padx=2, image=self.Juice4, width=104, height=104, bd=2,
                                command=ait_juice4)
        self.btnJuice4.grid(row=2, column=3, padx=4, pady=2)
        self.btnJuice5 = Button(food_item_frame, padx=2, image=self.Juice5, width=104, height=104, bd=2,
                                command=ait_juice5)
        self.btnJuice5.grid(row=2, column=4, padx=4, pady=2)
        self.btnJuice6 = Button(food_item_frame, padx=2, image=self.Juice6, width=104, height=104, bd=2,
                                command=ait_juice6)
        self.btnJuice6.grid(row=2, column=5, padx=4, pady=2)

        # ================================= Button for Fruit ================================
        self.btnFruit1 = Button(food_item_frame, padx=2, image=self.Fruit1, width=104, height=104, bd=2,
                                command=ait_fruit1)
        self.btnFruit1.grid(row=3, column=0, padx=4, pady=2)
        self.btnFruit2 = Button(food_item_frame, padx=2, image=self.Fruit2, width=104, height=104, bd=2,
                                command=ait_fruit2)
        self.btnFruit2.grid(row=3, column=1, padx=4, pady=2)
        self.btnFruit3 = Button(food_item_frame, padx=2, image=self.Fruit3, width=104, height=104, bd=2,
                                command=ait_fruit3)
        self.btnFruit3.grid(row=3, column=2, padx=4, pady=2)
        self.btnFruit4 = Button(food_item_frame, padx=2, image=self.Fruit4, width=104, height=104, bd=2,
                                command=ait_fruit4)
        self.btnFruit4.grid(row=3, column=3, padx=4, pady=2)
        self.btnFruit5 = Button(food_item_frame, padx=2, image=self.Fruit5, width=104, height=104, bd=2,
                                command=ait_fruit5)
        self.btnFruit5.grid(row=3, column=4, padx=4, pady=2)
        self.btnFruit6 = Button(food_item_frame, padx=2, image=self.Fruit6, width=104, height=104, bd=2,
                                command=ait_fruit6)
        self.btnFruit6.grid(row=3, column=5, padx=4, pady=2)

        # =============================== Tree View Text Widget ==================================
        scroll_y = Scrollbar(receipt_frame, orient=VERTICAL)
        self.POS_record = ttk.Treeview(receipt_frame, height=20, columns=("Item", "Qty", "Amount"),
                                       yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_record.heading("Item", text="Item")
        self.POS_record.heading("Qty", text="Qty")
        self.POS_record.heading("Amount", text="Amount")

        self.POS_record['show'] = 'headings'

        self.POS_record.column("Item", width=120)
        self.POS_record.column("Qty", width=100)
        self.POS_record.column("Amount", width=100)

        self.POS_record.pack(fill=BOTH, expand=1)
        self.POS_record.bind("<ButtonRelease-1>")

        self.txtReceipt = Text(receipt_frame, width=79, height=1, font=("arial", 5, "bold"))
        self.txtReceipt.pack()

        self.txtReceipt.insert(END, "Item\t\t\t\t Qty\t\t\t Amount\t\n")

if __name__ == "__main__":
    root = Tk()
    application = PosPython(root)
    root.mainloop()
