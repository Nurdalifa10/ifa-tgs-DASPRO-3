def merge_dicts(dict1, dict2):
    merged_dict = dict1
    merged_dict.update(dict2) 
    return merged_dict 

jadwalDasproIf2 = {
    "Senin": "Pemrograman Dasar",
    "Selasa": "Algoritma dan Struktur Data",
    "Rabu": "Pemrograman Dasar",
}

jadwalDasproIf3 = {
    "Kamis": "Algoritma dan Struktur Data",
    "Jumat": "Pemrograman Dasar",
    "Sabtu": "Pemrograman Web",
}

result_dict = merge_dicts(jadwalDasproIf2, jadwalDasproIf3)

#Menampilkan hasil
print("\nHasil Penggabungan:", result_dict, "\n")