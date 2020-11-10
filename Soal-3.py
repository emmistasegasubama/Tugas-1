#!/usr/bin/env python
# coding: utf-8

# In[3]:


Nama = input("Nama Siswa = ")
Teori = int(input("Nilai ujian teori = "))
Praktik = int(input("Nilai ujian praktik = "))
if Teori>=70 :
    if Praktik>=70:
        print("Selamat, anda lulus!")
    else :
        print("Anda harus mengulang ujian praktik.")
else :
    if Praktik>=70:
        print("Anda harus mengulang ujian teori")
    else :
        print("Anda harus mengulang ujian teori dan praktik.")


# In[ ]:




