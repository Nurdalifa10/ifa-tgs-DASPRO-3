def lists_to_dict(keys, values):

    if len(keys) == len(values):

        data_dict = dict(zip(keys, values))
        return data_dict
    else:
        print("Error: Panjang list tidak sama.")
        return None
    
keys_list = ["nama", "usia", "kota"]
values_list = ["Rafika", 18, "Ternate"]

result_dict = lists_to_dict(keys_list, values_list)

if result_dict:
    print("Data Dictionary:")
    print(result_dict)
print ("\n___-Terima Kasih-___")