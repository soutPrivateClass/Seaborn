import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import os

sns.set()
os.system('clear')

"""
matrixplot SAMA HALNYA DENGAN heatmap
HANYA BISA DIIMPLEMENTASIKAN PADA DATA NUMERIK UNTUK DATA YANG BERBENTUK MATRIX DAN MEMILIKI INDEX DENGAN NILAI KATEGORI (BUKAN INDEX ANGKA)
"""

dataKapal = pd.read_csv('kapal_titanic.csv')
print(dataKapal.head())
print("\n")

# 1. MENGGUNAKAN TABEL MATRIX KORELASI UNTUK MEMBUAT matrix plot :
dataKorelasi = dataKapal.corr(numeric_only=True) # corr UNTUK MENGUBAH DATA MENJADI TABEL MATRIX KORELASI
sns.heatmap(dataKorelasi, annot=True, cmap='Greens') # annot UNTUK MEMBERIKAN NILAI YANG SPESIFIK PADA MATRIX
plt.show()

# 2. MENGGUNAKAN KOLOM YANG MEMILIKI NILAI KATEGORI SEBAGAI INDEXING UNTUK MEMBUAT matrix plot : s
dataBaru = pd.read_csv('kapal_titanic.csv', index_col='embarked')
sns.heatmap(dataBaru.iloc[:,[0,1,3]].head(), annot= True, cmap='Greens')
plt.show()

# DEKLARASI DATA BARU BAWAAN DARI SEABORN :
dataPenerbangan = sns.load_dataset('flights') # IMPORT DATA SET BAWAAN DARI SEABORN
print(dataPenerbangan)

# pivot_table atau RINGKASAN DATA AGAR LEBIH MUDAH UNTUK DIJADIKAN SEBAGAI heatmap plot 
pivot = dataPenerbangan.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(pivot, annot=True, cmap='Greens', linecolor='white', linewidths=1) # linecolor UNTUK WARNA GARIS PEMBATAS, linewidths UNTUK MENENTUKAN KETEBALAN GARIS PEMBATAS
plt.show()

# clustermap plot HASIL DARI PROSES ALGORITMA CLUSTERING PADA PROSES UNSUPERVISED LEARNING  
sns.clustermap(pivot, cmap='coolwarm', standard_scale=1) # standard_scale MERUBAH NILAI ANGKA SKALA 0 - 1, SEHINGGA LEBIH MUDAH UNTUK INTREPETASINYA
plt.show()