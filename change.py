import tkinter as tk
from tkinter import *
from tkinter import ttk
from regex import P
import requests
from bs4 import BeautifulSoup
import datetime

#Настройки
root = tk.Tk()
w = 600
h = 400
root.geometry(f'{w}x{h}')
root.resizable(False,False) 
root.config(bg='#ffffff')
what_conv = ['EUR','USD','RUB']

#Главное

root.title('Конвертер Валют')
genlabel = tk.Label(root,text='Конвертер Валют',font=('Arial',15,'bold'),bg='#fff')
conv = tk.Label(root,text='Что хотите конвертировать?: ',bg='#fff')
conv_what = tk.Label(root,text='Во что конвертировать?: ',bg='#fff')
What_to_translate = ttk.Entry(root,width=50)
valute = ttk.Combobox(root,values=what_conv,width=5)
valute2 = ttk.Combobox(root,values=what_conv,width=5)


def convertiroval():
    if valute.get() == 'EUR':
        #Получаем сколько стоит Евро
        url_eur = 'https://www.banki.ru/products/currency/eur/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='currency-table__large-text')

        #Получает сколько стоит Доллар(USD)
        url_usd = 'https://www.banki.ru/products/currency/usd/'
        response_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(response_usd.text, 'lxml')
        quete_usd = soup_usd.find_all('div',class_='currency-table__large-text')
        a = quete_eur[0].text
        b = quete_usd[0].text

        if valute2.get() == 'RUB':
            rub = tk.Label(root,text='Ответ: {:.2f}RUB'.format(float(a.replace(',','.'))*int(What_to_translate.get())),font=('Leto Text Sans',10,'bold'),bg='#fff')
            rub.place(relx=.02,rely=.45)
        elif valute2.get() == 'USD':
            oneusd = float(a.replace(',','.'))/float(b.replace(',','.'))
            usd = tk.Label(root,text='Ответ: {:.2f}USD'.format(int(What_to_translate.get())*oneusd),font=('Leto Text Sans',10,'bold'),bg='#fff')
            usd.place(relx=.02,rely=.45)
        else:
            ty = tk.Label(root,text='Пожалуйста Выберите во что конвертировать!!!')
            ty.place(relx=.02,rely=.45)

    elif valute.get() == 'USD':
        #Получаем сколько стоит Евро
        url_eur = 'https://www.banki.ru/products/currency/eur/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='currency-table__large-text')

        #Получает сколько стоит Доллар(USD)
        url_usd = 'https://www.banki.ru/products/currency/usd/'
        response_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(response_usd.text, 'lxml')
        quete_usd = soup_usd.find_all('div',class_='currency-table__large-text')
        
        a = quete_eur[0].text
        b = quete_usd[0].text

        if valute2.get() == 'RUB':
            rub1 = tk.Label(root,text='Ответ: {:.2f}RUB'.format(float(b.replace(',','.'))*int(What_to_translate.get())),font=('Leto Text Sans',10,'bold'),bg='#fff')
            rub1.place(relx=.02,rely=.45)
        elif valute2.get() == 'EUR':
            oneur = float(b.replace(',','.'))/float(a.replace(',','.'))
            usd1 = tk.Label(root,text='Ответ: {:.2f}USD'.format(int(What_to_translate.get())*oneur),font=('Leto Text Sans',10,'bold'),bg='#fff')
            usd1.place(relx=.02,rely=.45)
        else:
            ty = tk.Label(root,text='Пожалуйста Выберите во что конвертировать!!!')
            ty.place(relx=.02,rely=.45)
        
    elif valute.get() == 'RUB':
        #Получаем сколько стоит Евро
        url_eur = 'https://www.banki.ru/products/currency/eur/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='currency-table__large-text')

        #Получает сколько стоит Доллар(USD)
        url_usd = 'https://www.banki.ru/products/currency/usd/'
        response_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(response_usd.text, 'lxml')
        quete_usd = soup_usd.find_all('div',class_='currency-table__large-text')
        
        a = quete_eur[0].text
        b = quete_usd[0].text

        if valute2.get() == 'EUR':
            eur1 = tk.Label(root,text='Ответ: {:.2f}EUR'.format(int(What_to_translate.get())/float(a.replace(',','.'))),font=('Leto Text Sans',10,'bold'),bg='#fff')
            eur1.place(relx=.02,rely=.45)
        elif valute2.get() == 'USD':
            usd2 = tk.Label(root,text='Ответ: {:.2f}USD'.format(int(What_to_translate.get())/float(b.replace(',','.'))),font=('Leto Text Sans',10,'bold'),bg='#fff')
            usd2.place(relx=.02,rely=.45)
        else:
            ty = ttk.Label(root,text='Пожалуйста Выберите во что конвертировать!!!')
            ty.place(relx=.02,rely=.45)
ButtonConv = ttk.Button(root,text='Конвертировать',command=convertiroval)
dest = ttk.Button(root,text='Quit',command=root.destroy)

#grid
genlabel.place(relx=.47,rely=.05,anchor='c')
conv.place(relx=.01,rely=.12)
conv_what.place(relx=.01,rely=.24)
What_to_translate.place(relx=.27,rely=.2,anchor='c')
valute2.place(relx=.06,rely=.32,anchor='c')
valute.place(relx=.57,rely=.2,anchor='c')
ButtonConv.place(relx=.09,rely=.4,anchor='c')
dest.place(relx=.9,rely=.93,anchor='c')
root.mainloop()