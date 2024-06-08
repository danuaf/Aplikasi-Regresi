# Aplikasi Regresi untuk Pemecahan Problem
Program ini adalah sebuah program yang digunakan untuk menghitung hasil regresi dengan 3 metode, yaitu :
* Linear
* Eksponensial
* Polinomial

## Panduan File dan Direktori

Pada repositori ini terdapat beberapa file serta direktori, ada beberapa hal yang perlu diketahui, yaitu:
* Pada direktori ***assets*** file csv yang diperoleh dari kaggle ***https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression***
* File ***main.py*** adalah file program utama dalam bahasa python yang digunakan untuk impelementasi
* File ***Aplikasi Regresi.ipynb*** adalah file jupyter notebook yang isi programnya sama seperti ***main.py*** akan tetapi dalam format jupyter notebook **(Direkomendasikan menggunakan file ini)**
* Sebelum menjalankan program, pastikan terdapat Library ***Numpy***, ***Matplotlib***, ***Pandas***, dan ***Scikit-Learn*** dikarenakan program ini menggunakan library tersebut.


## Testing
### Problem
Diinginkan untuk mencari hubungan faktor yang mempengaruhi nilai ujian siswa (NT) :
* Jumlah Latihan Soal (NL) terhadap nilai ujian

Data NL dan NT diperoleh dari ***https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression***, yaitu kolom ***Sample Question Papers Practiced*** dan ***Performance Index***.

Implementasikan regresi untuk mencari hubungan tersebut menggunakan metode:
* Model linear (Metode 1)
* Model eksponensial (Metode 3)
* Model lainnnya (Metode Polinomial)
Hitung juga galat RMS dari tiap metode yang digunakan