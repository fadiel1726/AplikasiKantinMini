import random
import string
import time
import mysql.connector
from cProfile import label
from tkinter import *
from tkinter import filedialog, messagebox
from turtle import clear
from PIL import Image, ImageTk

# untuk mengkonekan python ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kantinMini"
)
mycursor = mydb.cursor()

# Membuat Frame aplikasi
root = Tk()

root.geometry("1175x650+0+0")
root.resizable(0,0)
root.title("Kantin Mini")

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Kantin Mini',font=('Poppins',29,'bold'),fg='black',bg='skyblue', bd=5,width=45)
labelTitle.grid(row=0,column=8)

root.config(bg='#1c1c1c')
# batas Frame aplikasi

# VARIABLE

# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

# variabel menu makanan
e_nasiayamgeprek = StringVar()
e_nasiayambakar = StringVar()
e_nasiayamkatsu = StringVar()
e_nasigorengbiasa = StringVar()
e_nasigorengkampung = StringVar()
e_miegoreng = StringVar()
e_dimsum = StringVar()
e_ricebowl = StringVar()

# variabel menu minuman
e_estehmanis = StringVar()
e_lemontea = StringVar()
e_milktea = StringVar()
e_jusbuah = StringVar()
e_saladbuah = StringVar()
e_softdrink = StringVar()
e_chocolateice = StringVar()
e_airmineral = StringVar()

# variabel Harga dalam struk
hargadarimakananvar=StringVar()
hargadariminumanvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_nasiayamgeprek.set('0')
e_nasiayambakar.set('0')
e_nasiayamkatsu.set('0')
e_nasigorengbiasa.set('0')
e_nasigorengkampung.set('0')
e_miegoreng.set('0')
e_dimsum.set('0')
e_ricebowl.set('0')

e_estehmanis.set('0')
e_lemontea.set('0')
e_milktea.set('0')
e_jusbuah.set('0')
e_saladbuah.set('0')
e_softdrink.set('0')
e_chocolateice.set('0')
e_airmineral.set('0')

# FUNGSI

# Variabel-variabel global
billnumber = ""
date = ""
hargadarimakanan = 0
hargadariminuman = 0
subtotalItems = 0

# Awal fungsi perhitungan harga total
tax=(11/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadarimakanan,hargadariminuman,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0:

        item1=int(e_nasiayamgeprek.get())
        item2=int(e_nasiayambakar.get())
        item3=int(e_nasiayamkatsu.get())
        item4=int(e_nasigorengbiasa.get())
        item5=int(e_nasigorengkampung.get())
        item6=int(e_miegoreng.get())
        item7=int(e_dimsum.get())
        item8=int(e_ricebowl.get())

        item10=int(e_estehmanis.get())
        item11=int(e_lemontea.get())
        item12=int(e_milktea.get())
        item13=int(e_jusbuah.get())
        item14=int(e_saladbuah.get())
        item15=int(e_softdrink.get())
        item16=int(e_chocolateice.get())
        item17=int(e_airmineral.get())

        hargadarimakanan=(item1*15000) + (item2*15000) + (item3*16000) + (item4*12000) + (item5*15000) + (item6*10000)  \
        + (item7*10000) + (item8*14000)
        hargadariminuman=(item10*3000) + (item11*5000) + (item12*7000) + (item13*8000) + (item14*10000) + (item15*6000) \
        + (item16*8000) + (item17*3000)

        hargadarimakananvar.set(str(hargadarimakanan))
        hargadariminumanvar.set(str(hargadariminuman))

        subtotalItems=hargadarimakanan+hargadariminuman
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax

        servicetaxvar.set(totaltax)
        
        tottalcost=subtotalItems+totaltax
        totalcostvar.set(str(tottalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# awal fungsi cetak struk
def struk():
    global billnumber, date, hargadarimakanan, hargadariminuman, subtotalItems
    if hargadarimakananvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%y/%m/%d')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'******************\n')
        textStruk.insert(END,'Items:\t\t            Harga Total (Rp)\n')
        textStruk.insert(END,'******************\n')

        if e_nasiayamgeprek.get()!='0':
            textStruk.insert(END,f'Nasi Ayam Geprek\t\t\tRp. {int(e_nasiayamgeprek.get())*15000}\n\n')

        if e_nasiayambakar.get()!='0':
            textStruk.insert(END,f'Nasi Ayam Bakar\t\t\tRp. {int(e_nasiayambakar.get())*15000}\n\n')

        if e_nasiayamkatsu.get()!='0':
            textStruk.insert(END,f'Nasi Ayam Katsu\t\t\tRp. {int(e_nasiayamkatsu.get())*16000}\n\n')

        if e_nasigorengbiasa.get() != '0':
            textStruk.insert(END, f'Nasi Goreng Biasa:\t\t\tRp. {int(e_nasigorengbiasa.get()) * 12000}\n\n')

        if e_nasigorengkampung.get() != '0':
            textStruk.insert(END, f'Nasi Goreng Kampung:\t\t\tRp. {int(e_nasigorengkampung.get()) * 15000}\n\n')

        if e_miegoreng.get() != '0':
            textStruk.insert(END, f'Mie Goreng:\t\t\tRp. {int(e_miegoreng.get()) * 10000}\n\n')

        if e_dimsum.get() != '0':
            textStruk.insert(END, f'Dimsum:\t\t\tRp. {int(e_dimsum.get()) * 10000}\n\n')

        if e_ricebowl.get() != '0':
            textStruk.insert(END, f'Ricebowl:\t\t\tRp. {int(e_ricebowl.get()) * 14000}\n\n')

        if e_estehmanis.get() != '0':
            textStruk.insert(END, f'Es Teh Manis:\t\t\tRp. {int(e_estehmanis.get()) * 3000}\n\n')

        if e_lemontea.get() != '0':
            textStruk.insert(END, f'Lemon tea:\t\t\tRp. {int(e_lemontea.get()) * 5000}\n\n')

        if e_milktea.get() != '0':
            textStruk.insert(END, f'Milktea:\t\t\tRp. {int(e_milktea.get()) * 7000}\n\n')

        if e_jusbuah.get() != '0':
            textStruk.insert(END, f'Jus Buah:\t\t\tRp. {int(e_jusbuah.get()) * 8000}\n\n')

        if e_saladbuah.get() != '0':
            textStruk.insert(END, f'Salad Buah :\t\t\tRp. {int(e_saladbuah.get()) * 10000}\n\n')

        if e_softdrink.get() != '0':
            textStruk.insert(END, f'Softdrink:\t\t\tRp. {int(e_softdrink.get()) * 6000}\n\n')

        if e_chocolateice.get() != '0':
            textStruk.insert(END, f'Ice Chocolate:\t\t\tRp. {int(e_chocolateice.get()) * 8000}\n\n')

        if e_airmineral.get() != '0':
            textStruk.insert(END, f'Air Mineral:\t\t\tRp. {int(e_airmineral.get()) * 3000}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadarimakananvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari makanan\t\t\tRp. {hargadarimakanan}\n\n')
        if hargadariminumanvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari minuman\t\t\tRp. {hargadariminuman}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam database
def save():
    global billnumber, date, hargadarimakanan, hargadariminuman, subtotalItems
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="KantinMini"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO transaksi_struk (bill_number, date, hargadarimakanan, hargadariminuman, subtotal) VALUES (%s, %s, %s, %s, %s)"
        val = (billnumber, date, hargadarimakanan, hargadariminuman, subtotalItems)
        mycursor.execute(sql, val)

        # Commit perubahan ke database
        mydb.commit()

        # Tutup koneksi
        mycursor.close()
        mydb.close()

        messagebox.showinfo('Struk dan data berhasil disimpan ke dalam database')
    except Exception as e:
        messagebox.showerror('Error', f'Gagal menyimpan ke database: {e}')

# Batas fungsi simpan dalam perangkat

# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_nasiayamgeprek.set('0')
    e_nasiayambakar.set('0')
    e_nasiayamkatsu.set('0')
    e_nasigorengbiasa.set('0')
    e_nasigorengkampung.set('0')
    e_miegoreng.set('0')
    e_dimsum.set('0')
    e_ricebowl.set('0')

    e_estehmanis.set('0')
    e_lemontea.set('0')
    e_milktea.set('0')
    e_jusbuah.set('0')
    e_saladbuah.set('0')
    e_softdrink.set('0')
    e_chocolateice.set('0')
    e_airmineral.set('0')
    # batas untuk variables

    textnasiayamgeprek.config(state=DISABLED)
    textnasiayambakar.config(state=DISABLED)
    textnasiayamkatsu.config(state=DISABLED)
    textnasigorengbiasa.config(state=DISABLED)
    textnasigorengkampung.config(state=DISABLED)
    textmiegoreng.config(state=DISABLED)
    textnasigorengbiasa.config(state=DISABLED)
    textnasigorengkampung.config(state=DISABLED)

    textestehmanis.config(state=DISABLED)
    textlemontea.config(state=DISABLED)
    textmilktea.config(state=DISABLED)
    textjusbuah.config(state=DISABLED)
    textsaladbuah.config(state=DISABLED)
    textsoftdrink.config(state=DISABLED)
    textchocolateice.config(state=DISABLED)
    textsoftdrink.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    hargadariminumanvar.set('')
    hargadarimakananvar.set('')
    subtotalvar.set('')
# batas fungsi reset

# mengaktifkan fungsi entry menu makanan
def nasiayamgeprek():
    if var1.get()==1:
        textnasiayamgeprek.config(state=NORMAL)
        textnasiayamgeprek.delete(0,END)
        textnasiayamgeprek.focus()
    else:
        textnasiayamgeprek.config(state=DISABLED)
        e_nasiayamgeprek.set('0')

def nasiayambakar():
    if var2.get()==1:
        textnasiayambakar.config(state=NORMAL)
        textnasiayambakar.delete(0,END)
        textnasiayambakar.focus()
    else:
        textnasiayambakar.config(state=DISABLED)
        e_nasiayambakar.set('0')

def nasiayamkatsu():
    if var3.get()==1:
        textnasiayamkatsu.config(state=NORMAL)
        textnasiayamkatsu.delete(0,END)
        textnasiayamkatsu.focus()
    else:
        textnasiayamkatsu.config(state=DISABLED)
        e_nasiayamkatsu.set('0')

def nasigorengbiasa():
    if var4.get()==1:
        textnasigorengbiasa.config(state=NORMAL)
        textnasigorengbiasa.delete(0,END)
        textnasigorengbiasa.focus()
    else:
        textnasigorengbiasa.config(state=DISABLED)
        e_nasigorengbiasa.set('0')

def nasigorengkampung ():
    if var5.get()==1:
        textnasigorengkampung.config(state=NORMAL)
        textnasigorengkampung.delete(0,END)
        textnasigorengkampung.focus()
    else:
        textnasigorengkampung.config(state=DISABLED)
        e_nasigorengkampung.set('0')

def miegoreng():
    if var6.get()==1:
        textmiegoreng.config(state=NORMAL)
        textmiegoreng.delete(0,END)
        textmiegoreng.focus()
    else:
        textmiegoreng.config(state=DISABLED)
        e_miegoreng.set('0')

def dimsum():
    if var7.get()==1:
        textdimsum.config(state=NORMAL)
        textdimsum.delete(0,END)
        textdimsum.focus()
    else:
        textdimsum.config(state=DISABLED)
        e_dimsum.set('0')

def ricebowl():
    if var8.get()==1:
        textricebowl.config(state=NORMAL)
        textricebowl.delete(0,END)
        textricebowl.focus()
    else:
        textricebowl.config(state=DISABLED)
        e_ricebowl.set('0')
# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu minuman
def estehmanis():
    if var9.get()==1:
        textestehmanis.config(state=NORMAL)
        textestehmanis.delete(0,END)
        textestehmanis.focus()
    else:
        textestehmanis.config(state=DISABLED)
        e_estehmanis.set('0')

def lemontea():
    if var10.get()==1:
        textlemontea.config(state=NORMAL)
        textlemontea.focus()
        textlemontea.delete(0, END)
    else:
        textlemontea.config(state=DISABLED)
        e_lemontea.set('0')

def milktea():
    if var11.get()==1:
        textmilktea.config(state=NORMAL)
        textmilktea.delete(0,END)
        textmilktea.focus()
    else:
        textmilktea.config(state=DISABLED)
        e_milktea.set('0')

def jusbuah():
    if var12.get()==1:
        textjusbuah.config(state=NORMAL)
        textjusbuah.delete(0,END)
        textjusbuah.focus()
    else:
        textjusbuah.config(state=DISABLED)
        e_jusbuah.set('0')

def saladbuah():
    if var13.get()==1:
        textsaladbuah.config(state=NORMAL)
        textsaladbuah.delete(0,END)
        textsaladbuah.focus()
    else:
        textsaladbuah.config(state=DISABLED)
        e_saladbuah.set('0')

def softdrink():
    if var14.get()==1:
        textsoftdrink.config(state=NORMAL)
        textsoftdrink.delete(0,END)
        textsoftdrink.focus()
    else:
        textsoftdrink.config(state=DISABLED)
        e_softdrink.set('0')

def chocolateice():
    if var15.get()==1:
        textchocolateice.config(state=NORMAL)
        textchocolateice.delete(0,END)
        textchocolateice.focus()
    else:
        textchocolateice.config(state=DISABLED)
        e_chocolateice.set('0')

def airmineral():
    if var16.get()==1:
        textairmineral.config(state=NORMAL)
        textairmineral.delete(0,END)
        textairmineral.focus()
    else:
        textairmineral.config(state=DISABLED)
        e_airmineral.set('0')
# batas mengaktifkan entry minuman

# FRAME KIRI

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=5)
hargaFrame.pack(side=BOTTOM)

makananFrame=LabelFrame(menuFrame,text=' Makanan ',font=('Poppins',12,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
makananFrame.pack(side=LEFT)

minumanFrame=LabelFrame(menuFrame,text=' Minuman ',font=('Poppins',12,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=RIGHT)
# batas frame kiri (menu cafe)

# membuat tampilan daftar menu makanan
nasiayamgeprek=Checkbutton(makananFrame,text=' Nasi Ayam Geprek ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=nasiayamgeprek, bg='#f6f6f6')
nasiayamgeprek.grid(row=0,column=0,sticky=W)

nasiayambakar=Checkbutton(makananFrame,text=' Nasi Ayam Bakar ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=nasiayambakar, bg='#f6f6f6')
nasiayambakar.grid(row=1,column=0,sticky=W)

nasiayamkatsu=Checkbutton(makananFrame,text=' Nasi Ayam Katsu ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=nasiayamkatsu, bg='#f6f6f6')
nasiayamkatsu.grid(row=2,column=0,sticky=W)

nasigorengbiasa=Checkbutton(makananFrame,text=' Nasi Goreng Biasa ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=nasigorengbiasa, bg='#f6f6f6')
nasigorengbiasa.grid(row=3,column=0,sticky=W)

nasigorengkampung=Checkbutton(makananFrame,text=' Nasi Goreng Kampung ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=nasigorengkampung, bg='#f6f6f6')
nasigorengkampung.grid(row=4,column=0,sticky=W)

miegoreng=Checkbutton(makananFrame,text= ' Mie Goreng ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=miegoreng, bg='#f6f6f6')
miegoreng.grid(row=5,column=0,sticky=W)

dimsum=Checkbutton(makananFrame,text=' Dimsum ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=dimsum, bg='#f6f6f6')
dimsum.grid(row=6,column=0,sticky=W)

ricebowl=Checkbutton(makananFrame,text=' Ricebowl ',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=ricebowl, bg='#f6f6f6')
ricebowl.grid(row=7,column=0,sticky=W)

# menambahkan fields entri untuk item makanan
textnasiayamgeprek=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasiayamgeprek)
textnasiayamgeprek.grid(row=0,column=1)

textnasiayambakar=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasiayambakar)
textnasiayambakar.grid(row=1,column=1)

textnasiayamkatsu=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasiayamkatsu)
textnasiayamkatsu.grid(row=2,column=1)

textnasigorengbiasa=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasigorengbiasa)
textnasigorengbiasa.grid(row=3,column=1)

textnasigorengkampung=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasigorengkampung)
textnasigorengkampung.grid(row=4,column=1)

textmiegoreng=Entry(makananFrame,font=('Poppins','12','bold'),bd=7, width=8,state=DISABLED,textvar=e_miegoreng)
textmiegoreng.grid(row=5,column=1)

textdimsum=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_dimsum)
textdimsum.grid(row=6,column=1)

textricebowl=Entry(makananFrame,font=('Poppins','12','bold'),bd=7,width=8,state=DISABLED,textvar=e_ricebowl)
textricebowl.grid(row=7,column=1)


# membuat tampilan daftar menu minuman
estehmanis=Checkbutton(minumanFrame,text='Es Teh Manis',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=estehmanis, bg='#f6f6f6')
estehmanis.grid(row=0,column=0,sticky=W)

lemontea=Checkbutton(minumanFrame,text='Lemon Tea',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=lemontea, bg='#f6f6f6')
lemontea.grid(row=1,column=0,sticky=W)

milktea=Checkbutton(minumanFrame,text='Milk Tea',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=milktea, bg='#f6f6f6')
milktea.grid(row=2,column=0,sticky=W)

jusbuah=Checkbutton(minumanFrame,text='Jus Buah',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=jusbuah, bg='#f6f6f6')
jusbuah.grid(row=3,column=0,sticky=W)

saladbuah=Checkbutton(minumanFrame,text='Salad Buah',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=saladbuah, bg='#f6f6f6')
saladbuah.grid(row=4,column=0,sticky=W)

softdrink=Checkbutton(minumanFrame,text='Softdrink',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var14,
                        command=softdrink, bg='#f6f6f6')
softdrink.grid(row=5,column=0,sticky=W)

chocolateice=Checkbutton(minumanFrame,text='Ice Chocolate',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var15,
                        command=chocolateice, bg='#f6f6f6')
chocolateice.grid(row=6,column=0,sticky=W)

airmineral=Checkbutton(minumanFrame,text='Air Mineral',font=('Poppins',12,'bold'),onvalue=1,offvalue=0,variable=var16,
                        command=airmineral, bg='#f6f6f6')
airmineral.grid(row=7,column=0,sticky=W)

# menambahkan fields entri untuk item minuman
textestehmanis=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_estehmanis)
textestehmanis.grid(row=0,column=1)

textlemontea=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_lemontea)
textlemontea.grid(row=1,column=1)

textmilktea=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_milktea)
textmilktea.grid(row=2,column=1)

textjusbuah=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_jusbuah)
textjusbuah.grid(row=3,column=1)

textsaladbuah=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_saladbuah)
textsaladbuah.grid(row=4,column=1)

textsoftdrink=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_softdrink)
textsoftdrink.grid(row=5,column=1)

textchocolateice=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_chocolateice)
textchocolateice.grid(row=6,column=1)

textairmineral=Entry(minumanFrame,font=('Poppins','12','bold'),bd=7,width=7,state=DISABLED,textvar=e_airmineral)
textairmineral.grid(row=7,column=1)


# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=4,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariMakanan=Label(hargaFrame,text='    HARGA DARI MAKANAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMakanan.grid(row=0,column=0)

textHargadariMakanan=Entry(hargaFrame,font=('Poppins',12,'bold'),bd=6,width=12,state='readonly',textvariable=hargadarimakananvar)
textHargadariMakanan.grid(row=0,column=1,padx=41)

LabelHargadariMinuman=Label(hargaFrame,text='    HARGA DARI MINUMAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman=Entry(hargaFrame,font=('Poppins',12,'bold'),bd=6,width=12,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=1,column=2)

textSubTotal=Entry(hargaFrame,font=('Poppins',12,'bold'),bd=6,width=12,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=1,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan = Button(buttonFrame, text='Simpan', font=('arial', 12, 'bold'), fg='#fefefe', bg='#b38b59', bd=3, padx=12, command=save)
buttonSimpan.grid(row=0, column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=3)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()
