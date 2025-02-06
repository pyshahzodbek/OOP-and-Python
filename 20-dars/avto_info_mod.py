def avto_info(kompaniya, model,rangi,korobka, yili, narxi=None):
    """Avtomobil haqidagi ma'lumotlarni
     lug'at ko'rinishida qaytaruvchi funksiya"""
    avto={
        "kompaniya":kompaniya,
        "model":model,
        "rangi":rangi,
        "korobka":korobka,
        "yili":yili,
        "narxi":narxi
    }
    return avto
def avto_kirit():
    """Avtomobil haqidagi ma'lumotlarni
    kirituvchi funksiya"""
    avtolar=[]
    while True:
     print("\n Quyidagi ma'lumotlarni kiriting:",end='')
     kompaniya=input("Kompaniya nomi: ")
     model=input("Model: ")
     rangi=input("Rangi: ")
     korobka=input("Korobka: ")
     yili=input("Yili: ")
     narxi=input("Narxi: ")
     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))
     javob= input("Yana avtomobil qo'shishni kerakmi? (y/n): ")
     if javob=='n':
         break
    return avtolar
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar
    saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()}"
          f"{avto_info['model'].upper()},{avto_info['korobka']} korobka"
          f"{avto_info['yili']} yili,{avto_info['narxi']}$")