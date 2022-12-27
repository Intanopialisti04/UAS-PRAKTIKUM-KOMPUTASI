'''
Menyelesaikan integral dengan menggunakan metode trapezoid atau reiman dengan
cara dipanggil minimal 10 masalah integral dari database
'''

print('+++++=============================++++')
print('----------UJIAN AKHIR SEMESTER--------')
print('-------PRAKTIKUM FISIKA KOMPUTASI-----')
print('----------INTAN OPIALISTI-------------')
print('--------------1207030002--------------')

import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return (x**7)*np.exp(-x)
a = float(input('Batas bawah(a) = '))   
b = float(input('Batas atas (b) = '))   
n = int (input('Jumlah grid (n) = '))   

#Trapezoid
dx = (b-a)/(n-1)
x = np.linspace(a,b,n)
sigma = 0
for i in range (1, n-1):
    sigma += func(x[i])
hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))
print('Hasil = ', hasil)

xp = np.linspace(a,b)
plt.plot(xp, func(xp))

for i in range (n):
    plt.bar(x[i], func(x[i]), align='edge', width=0.000001, color = 'gray', edgecolor = 'red')

plt.fill_between(x,func(x), color = 'yellow')
plt.show()
