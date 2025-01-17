import tkinter as tk
from tkinter import messagebox, simpledialog

class NamazManager:
    def __init__(self, master):
        self.master = master
        self.master.title("مدیریت نمازهای روزانه")
        
        self.namaz_list = []  
        
        self.label = tk.Label(master, text="لطفا گزینه مورد نظر را انتخاب کنید:")
        self.label.pack(pady=10)

        self.show_button = tk.Button(master, text="نمایش نمازها", command=self.show_namaz)
        self.show_button.pack(pady=5)

        self.add_button = tk.Button(master, text="اضافه کردن نماز", command=self.add_namaz)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(master, text="حذف نماز", command=self.remove_namaz)
        self.remove_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="خروج", command=master.quit)
        self.exit_button.pack(pady=5)

    def show_namaz(self):
        if not self.namaz_list:
            messagebox.showinfo("نمازها", "هیچ نمازی ثبت نشده است.")
        else:
            namaz_details = "\n".join([f"{i+1}. نام: {namaz['name']}, تعداد رکعت: {namaz['rakats']}, زمان اذان: {namaz['azan_time']}" 
                                       for i, namaz in enumerate(self.namaz_list)])
            messagebox.showinfo("نمازهای ثبت شده", namaz_details)

    def add_namaz(self):
        namaz_name = simpledialog.askstring("اضافه کردن نماز", "لطفا نام نماز را وارد کنید:")
        if namaz_name:
            rakats = simpledialog.askinteger("اضافه کردن نماز", "لطفا تعداد رکعت نماز را وارد کنید:")
            azan_time = simpledialog.askstring("اضافه کردن نماز", "لطفا زمان اذان نماز (به فرمت HH:MM) را وارد کنید:")
            
            if rakats is not None and azan_time:
                namaz_info = {
                    'name': namaz_name,
                    'rakats': rakats,
                    'azan_time': azan_time
                }
                self.namaz_list.append(namaz_info)
                messagebox.showinfo("موفقیت", f"نماز '{namaz_name}' با {rakats} رکعت و زمان اذان '{azan_time}' اضافه شد.")

    def remove_namaz(self):
        if not self.namaz_list:
            messagebox.showinfo("حذف نماز", "هیچ نمازی برای حذف وجود ندارد.")
        else:
            index = simpledialog.askinteger("حذف نماز", "لطفا ایندکس نمازی که می‌خواهید حذف کنید را وارد کنید:")
            if index is not None and 1 <= index <= len(self.namaz_list):
                removed_namaz = self.namaz_list.pop(index - 1)
                messagebox.showinfo("موفقیت", f"نماز '{removed_namaz['name']}' حذف شد.")
            else:
                messagebox.showerror("خطا", "ایندکس نامعتبر است.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NamazManager(root)
    root.mainloop()
