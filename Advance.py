import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from warnings import filterwarnings

sns.set()
os.system('clear')
filterwarnings('ignore')

"""
PEMBELAJARAN LANJUTAN MENGENAI SEABORN YANG LEBIH ADVANCE LEVEL ATAU SEDIKIT RUMIT 
"""

# READ DATA SET BAWAAN DARI SEABORN :
sns.get_dataset_names()

# AKSES SALAH SATU DATA SET BAWAAN DARI SEABORN : 
dataTips = sns.load_dataset('tips') # DATA TIPS

dataDiamond = sns.load_dataset('diamonds') # DATA DIAMONDS 

# CEK KATEGORI PADA KOLOM
cek = dataDiamond.cut.unique() # CEK NILAI APA SAJA YANG ADA PADA KATEGORI KOLOM CUT, HANYA BISA UNTUK KOLOM BERORIENTASI KATEGORI
print(cek, "\n")

# PairGrid plot (MENAMPILKAN FIGURE DENGAN PLOT - PLOT KOSONG YANG MEMILIKI BENTUK PLOT SEPERTI pairplot)
pairGrid = sns.PairGrid(dataDiamond)
pairGrid.map(plt.scatter) # .map(plt.scatter) UNTUK MENGISI PLOT DENGAN scatter plot
plt.show()

# PairGrid DENGAN MODEL CUSTOM plot (MENGGUNAKAN MODEL plot SESUAI KETENTUAN)
pairGrid = sns.PairGrid(dataDiamond)
pairGrid.map_diag(sns.distplot) # plot DIAGONAL BERBENTUK distribusi plot
pairGrid.map_upper(plt.scatter) # plot BAGIAN ATAS DIAGONAL BERBENTUK scatter plot
pairGrid.map_lower(sns.kdeplot) # # plot BAGIAN BAWAH DIAGONAL BERBENTUK kde plot
plt.show()

# FacetGrid plot (BISA MENENTUKAN BARIS & KOLOM, MENENTUKAN APA SAJA YANG AKAN DI PLOT)
# IMPLEMENTASI FaceeGird 3 KOLOM DATA SEAGAI INFORMASI DENGAN distribution plot :
faceGrid = sns.FacetGrid(row='smoker', col='day', data=dataTips)
faceGrid.map(sns.distplot,'total_bill') # KOLOM total_bill yang akan di plot 
plt.show()

# IMPLEMENTASI FaceeGird 5 KOLOM DATA SEAGAI INFORMASI DENGAN scatter plot :
faceGird = sns.FacetGrid(row='smoker', col='day', hue='time', data=dataTips)
faceGird.map(plt.scatter,'total_bill','sex')
plt.show()