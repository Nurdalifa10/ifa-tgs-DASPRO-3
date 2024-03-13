#================================Program 1=====================================#
print('''\n\n  =============|||||||||||||||||||||||==============
        ~_~    APLIKASI LOGIN MAHASISWA    ~_~
  =============|||||||||||||||||||||||==============\n\n''')
#===========================Menampilkan Data MAhasiswa==========================#
data_dictionary = {
                'acha':'07352311178',
                'ifa':'07352311179',
                'manda':'07352311180',
                'rika':'07352311181',
                'ozan':'07352311182',
                'iky':'07352311183',
                'hamdan':'07352311184',
                'lis':'07352311185',
                'maulidia':'07352311186',
                'mega':'07352311187'
}
#====================================Login=====================================#
def login(username, password):
    if username in data_dictionary and data_dictionary [username] == password:
        return f"\tSelamat Datang , {username}!"
    else:
        return "\tData Yang Dimasukkan Salah."
#=================================Mengisi Login=================================#  
print ("\t>>>>Silahkan Masukkan Data Berikut<<<<\n")  
username = input("\tMasukkan Username: ")
password = input("\tMasukkan Password: ")

result = login (username, password)
print ("\n",result)
print ("\n (~_~)_______Terima Kasih Telah Mengisi_________(~_~)\n")
