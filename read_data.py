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

def get_surah_name(file_name:str):
    """
    Read Quran Academy data
    """
    # read json data type
    f = open(file_name, 'r').read().split('\n')
    surah_name_list = [0]
    for surah_name in f:
        surah_name_list.append(surah_name.split(',')[1])
    return surah_name_list

def sort_surah(data_arabic_and_uzbek:list,surah_name_list:list)->list:
    
    # print(surah_name_list)
    surah_list = dict()
    ayah_list = []
    for ayah in data_arabic_and_uzbek:
        ayah_list.append(ayah)
        if ayah['verse'] == 1 and ayah['chapter'] != 1:
            surah_list[surah_name_list[ayah['chapter']-1]] = ayah_list
            ayah_list = []
            ayah_list.append(ayah)

    surah_list[surah_name_list[ayah['chapter']]] = ayah_list
    return surah_list
    

data_arabic = read_quranacademy('data/ara-quranacademy.json')
data_uzbek = read_quranacademy('data/uzb-muhammadsodikmu.json')

conv = arabic2uzbek(data_arabic, data_uzbek)
surah_name = get_surah_name('surah.txt')

surah_list = sort_surah(conv,surah_name)
print(len(surah_list))