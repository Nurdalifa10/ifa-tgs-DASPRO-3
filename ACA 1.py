#================================Program 1=====================================#
print('''\n\n
               -APLIKASI LOGIN MAHASISWA-
  \n\n''')
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
        return f"Selamat Datang , {username}!"
    else:
        return "Data Yang Dimasukkan Salah."
#=================================Mengisi Login=================================#  
print (">>>>Silahkan Masukkan Data Berikut<<<<\n")  
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

result = login (username, password)
print ("\n",result)
print ("\n (~_~)_______Terima Kasih Telah Mengisi_________(~_~)\n")
