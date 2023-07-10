from evds import evdsAPI
import tkinter as tk
import tkcalendar
from pandas import ExcelWriter





    
    
    
root = tk.Tk()
root.title('Kur Sorgula')
root.geometry("250x175")
root.eval('tk::PlaceWindow . center')


label1 = tk.Label(root, text="API Anahtarı")
label1.grid(row = 0,column = 0, pady=10, padx=15)
entry1 = tk.Entry(root)
entry1.grid(row = 0,column = 1)

label2 = tk.Label(root, text="Başlangıç Tarihi")
label2.grid(row=1,column=0, padx=15)
date1 = tkcalendar.DateEntry(root, date_pattern="dd-MM-yyyy", locale="tr_TR")
date1.grid(row = 1,column = 1)


label3 = tk.Label(root, text="Bitiş Tarihi")
label3.grid(row = 2,column = 0, pady=10, padx=15)
date2 = tkcalendar.DateEntry(root, date_pattern="dd-MM-yyyy", locale="tr_TR")
date2.grid(row = 2,column = 1)
        
def run():
        
    tarih1 = date1.get_date()
    tarih1_str = tarih1.strftime("%d-%m-%Y")
    print(tarih1_str)
        
    tarih2 = date2.get_date()
    tarih2_str = tarih2.strftime("%d-%m-%Y")
    print(tarih2_str)
    print(entry1.get())
        
    api_key = entry1.get()
        
    f = open("saved_APIs.txt", "a")
    f.write(api_key)
    f.close()
        
    evds = evdsAPI(api_key, lang="TR")

    df = evds.get_data(['TP.DK.USD.A.YTL','TP.DK.EUR.A.YTL'], startdate = tarih1_str, enddate = tarih2_str)
        
    writer = ExcelWriter('Döviz Çıktısı.xlsx', engine='xlsxwriter')
    df.to_excel(writer,"Döviz Tablosu")
    writer.close()


def run2():
    
    with open("saved_APIs.txt", "r") as file:
        api_key = file.read()

            
    tarih1 = date1.get_date()
    tarih1_str = tarih1.strftime("%d-%m-%Y")
    print(tarih1_str)
        
    tarih2 = date2.get_date()
    tarih2_str = tarih2.strftime("%d-%m-%Y")
    print(tarih2_str)
    print(entry1.get())
        
    evds = evdsAPI(api_key, lang="TR")

    df = evds.get_data(['TP.DK.USD.A.YTL','TP.DK.EUR.A.YTL'], startdate = tarih1_str, enddate = tarih2_str)
        
    writer = ExcelWriter('Döviz Çıktısı.xlsx', engine='xlsxwriter')
    df.to_excel(writer,"Döviz Tablosu")
    writer.close()
    

button = tk.Button(root,text="Çıktı Al", command=run)
button.grid(row = 3,sticky=tk.EW, columnspan=2, padx=15)

button2 = tk.Button(root, text="Eski API Kullan", command=run2)
button2.grid(row = 4,sticky=tk.EW, columnspan=2,pady= 10,padx=15)


root.mainloop()
    

