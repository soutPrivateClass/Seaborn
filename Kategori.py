import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from warnings import filterwarnings


filterwarnings('ignore')
sns.set()
os.system("clear")

"""
DATA KATEGORI ADALAH DATA YANG MEMILIKI NILAI NON NUMERIK (BUKAN NUMERIK)
"""

dataKapal = pd.read_csv('kapal_titanic.csv')
dataKategori = dataKapal.describe(include='O') # include DEKLARASI KHUSUS UNTUK DATA YANG BERORIENTASI NON NUMERIK
print(dataKategori)
print(50*"-")
print(dataKapal.head())

# barplot (histogram)
# AKAN MENGHASILKAN NILAI RATA RATA 
sns.barplot(x='sex', y='fare', data=dataKapal) # SALAH SATU DATA HARUS BERNILAI NUMERIK ANTARA SUMBU X ATAU SUMBU Y
plt.show()

# AKAN MENGHASILKAN NILAI JUMLAH 
sns.barplot(x='sex', y='fare', data=dataKapal, estimator=sum) # estimator ATRIBUT UNTUK MENGHASILKAN NILAI JUMLAH DATA
plt.show()

# np.std (STANDART DEVIASI)
sns.barplot(x='sex', y='fare', data =dataKapal, estimator=np.std)
plt.show()

# countplot AKAN MENAMPILKAN JUMLAH DATA KATEGORI
sns.countplot(x='sex', data=dataKapal)
plt.show()

# countplot DENGAN KATEGORI KOLOM 'deck' DAN AKAN DIPISAHKAN BRDASARKAN KOLOM 'sex' DENGAN ATRIBUT hue='sex'
sns.countplot(x='deck', hue='sex', data=dataKapal, order=['A','B','C','D','E','F','G'] ) # order UNTUK MENGURUTKAN URUTAN SUMBU X AGAR SUPAYA URUT
plt.show()

# boxplot (box & whiskers plot) = SEBUAH PLOT DIMANA KITA BISA MELIHAT / MENGANALISA NILAI : 
# Q1 = QUARTAL 1 = 25 %
# Q2 (QUARTAL 2) = 50 %
# Q3 (QUARTAL 3) = 75 %
# Q4 (QUARTAL 4) = 100 %
# TERMASUK JUGA OUTLIER
# OUTLIER ATAS ADALAH HASIL DARI : Q3 + 1.5 * (Q3-Q1), JIKA OUTLIER BAWAH HASIL DARI : Q1 - 1.5 * (Q3 - Q1), Q3 - Q1 ADALAH JARAK ATAU INTERQUARTILE RANGE (IR)
# MENGHAPUS ATAU MENGHILANGKAN OUTLIER DENGAN MENGUNAKAN NILAI MEDIAN (CENTRAL TENDETION)

sns.boxplot(x='sex', y='fare', data=dataKapal, hue='deck',hue_order=['A','B','C','D','E','F','G'])
plt.show()

# violinplot = SAMA DENGAN BOX PLOT HANYA BERBEDA, JIKA BOX PLOT HANYA MENUNJUKKAN NILAI Q1 - Q4, & NILAI OUTLIER NYA
# MELIHAT ATAU MENGANALISA DISTRIBUSI KEPADATAN ATAU DENSITY DATA 
sns.violinplot(x='deck', y='fare', hue='sex', data=dataKapal, order=['A','B','C','D','E','F','G'], split=True) # split BERLAKU UNTUK DATA KATEGORI ATAU NILAI DATA hue YANG HANYA MEMILIKI 2 NILAI SAJA
plt.show()

# stripplot = FOKUS PADA DATA POINTER ATAU TITIK TITIK SCATTER YANG DIHASILKAN
sns.stripplot(x='deck', y='fare',hue='sex' ,data=dataKapal, order=['A','B','C','D','E','F','G'], jitter=True) # jitter AGAR DATA TERLIHAT SEDIKIT TERSEBAR, NAMUN HASIL YANG DIHASILKAN TIDAK TERLALU SIGNIFIKAN 
plt.show()

# swarmplot = GABUNGAN DARI stripplot DAN violinplot 
sns.swarmplot(x='deck', y='fare',hue='sex' ,data=dataKapal, order=['A','B','C','D','E','F','G'])
plt.show()

# GABUNGAN swarm & violinplot 
sns.swarmplot(x='deck', y='fare', hue='sex', data=dataKapal, order=['A','B','C','D','E','F','G'])
sns.violinplot(x='deck', y='fare', data=dataKapal, order=['A','B','C','D','E','F','G'])
plt.show()