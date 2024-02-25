import random as r
import os
import datetime
s = str(datetime.datetime.now())
s=s[:-7]
print(s)
os.system("slc")
pul = r.randint(100,1000)*1000
while 1:
    a = int(input('1 - HUMO\n2 - UZcart: '))
    k = input('plastik nomer: ')
    if 1 == a:
        if k[:5] == '9800':
            a = '  HUMO'
            break
        else:
            print("xato")
    elif a == 2:
        if k[:5] == '8600':
            a = 'UZcart'
            break
        else:
            print("xato") 
v = input('kod: ')
karta = {}
karta[k] = v
b = int(input('1 - Mablagni tekshirish\n2 - keyingis: '))
if b == 1:
    print(f"{pul} som")

b = int(input('1 - Pul Yechi\n2 - Toldish: '))
if b == 1:
    b = int(input('summa: '))
    if b < pul:
        print('Pul yechildi\n')
        print(f"_____________________________\n|Versiya                 5.11|\n|Data     {s}|\n|Tip                   {a}|\n|Yechilgan summa        {b}|\n|Qolgan summa          {pul-b}|\n_____________________________")
elif b == 2:
    b = int(input('summa: '))
    print('Hisobinggiz toldirildi\n')
    print(f"_____________________________\n|Versiya                 5.11|\n|Data     {s}|\n|Tip                   {a}|\n|Toldirlgan summa       {b}|\n|Jami summa            {pul+b}|\n_____________________________")


