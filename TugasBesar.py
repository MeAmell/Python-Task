def bukaData(data): #membuat fungsi bukaData
    file = open(data, "r")  #membaca file text
    teks = file.readline() #membaca string di dalam file text

    list = [] #membuat list kosong
    while teks != "": #melakukan perulangan sampai menemukan string kosong
        a = teks.split() #split() untuk memisahkan string menjadi per string
        list.append(a) #menambahkan string yang sudah di list di variabel a
        teks = file.readline()  #membaca string di dalam file text
    
    daftar_CLO = {} #membuat dictionary kosong
    for i in list: 
        value = [int(item) for item in i[1:]] #membuat value dengan dictionary berupa index 1 sampai terakhir yang sudah di casting ke integer
        key = i[0] #membuat key untuk dictionary dengan index 0 dari list
        daftar_CLO[key] = value #pembuatan dictionary

    file.close() #menutup file
    return daftar_CLO #mereturn daftar_CLO

def remedial_report(daftar_CLO): #membuat fungsi remedial_report 
    for key, values in daftar_CLO.items(): #meloop setiap pasangan key dan value dalam dictionary
        print("Data Mahasiswa dengan NIM:", key) #print data NIM Mahasiswa dengan key nya untuk nilai
        i = 0 #untuk nomor CLO
        for value in values:  #iterasi setiap elemen di dalam list values
            if value < 50: #melakukan pengecekan nilai
                print("CLO", i+1, "Remedial dengan nilai:", value) #output untuk remedial dengan value untuk nilai
                i += 1
            else:
                print("CLO", i+1, "Tidak Remedial") #output untuk tidak remedial
                i += 1
        print()

daftar_CLO = bukaData("nilai.txt") #memanggil fungsi buka data dan nama file text
print("dictionary daftar_CLO :", bukaData("nilai.txt")) #untuk menampilkan file teks berupa dictionary daftar_CLO
remedial_report(daftar_CLO) #memanggil fungsi remedial_report(daftar_CLO)