import json
from transliterate import transliterate

def read_quranacademy(file_name):
    """
    Read Quran Academy data
    """
    # read json data type
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data['quran']

def read_quran_muhammadsodikmu(file_name):
    """
    Read Quran Academy data
    """
    # read json data type
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data['quran']

def arabic2uzbek(data_arabic:list, data_uzbek:list):
    """
    Convert Arabic to Uzbek
    """
    # convert Arabic to Uzbek
    for i,item in enumerate(data_arabic):
        arabic_word = data_arabic[i]['text']
        uzbek_work = data_uzbek[i]['text']
        uzbek_work = transliterate(uzbek_work,'latin')

        data_arabic[i]['text'] = f"{arabic_word}\n\n{uzbek_work}"
    return data_arabic

def sort_surah(data_arabic_and_uzbek:list)->list:
    surah_list = []
    ayah_list = []
    for ayah in data_arabic_and_uzbek:
        if ayah['verse'] == 1:
            surah_list.append(ayah_list)
            ayah_list = []
            ayah_list.append(ayah)
            
        else:
            ayah_list.append(ayah)
    
    return surah_list[1:]
    

data_arabic = read_quranacademy('data/ara-quranacademy.json')
data_uzbek = read_quranacademy('data/uzb-muhammadsodikmu.json')

conv = arabic2uzbek(data_arabic, data_uzbek)
surah_list = sort_surah(conv)
print(surah_list[2][4])