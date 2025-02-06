# 26.01.2025
# 13-dars
# Mavzu: Nesting
# car0={
#     'model':'lacetti',
#     'rang':'oq',
#     'yil':2018,
#     'narh':13000,
#     'km':50000,
#     'karobka':'avtomat'
# }
# car1={
#     'model':'nexia3',
#     'rang':'qora',
#      'yil':2015,
#     'narh':9000,
#     'km':89000,
#     'karobka':'mexanika'
# }
# car2={
#     'model':'gentra',
#     'rang':'qizil',
#      'yil':2019,
#     'narh':15000,
#     'km':20000,
#     'karobka':'mexanika'
# }
# car=car0
# print(f"{car['model'].title()} "
#       f"{car['rang'].title()}"
#       f" {car['yil']}-yil ,{car['narh']}$")
# car=car1
# print(f"{car['model'].title()} "
#       f"{car['rang'].title()}"
#       f" {car['yil']}-yil ,{car['narh']}$")
# car=car2
# print(f"{car['model'].title()} "
#       f"{car['rang'].title()}"
#       f" {car['yil']}-yil ,{car['narh']}$")
# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()} "
#           f"{car['rang'].title()}"
#           f" {car['yil']}-yil ,{car['narh']}$")
# print(car0)
# print(car1)
# print(car2)
# print(car0['model'])
# print(f"{cars[2]['rang'].title()}  "
#       f"{cars[2]['model']}")
# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car={
#         'model':'malibu',
#         'rang':'None',
#         'yil':2020,
#         'narh':'None',
#         'km':0,
#         'karobka':'avto'
#     }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
# print(malibus)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu in malibus[6:]:
#     malibu['rang']='oq'
#     malibu['karobka']='mexanika'
# for malibu in malibus:
#     if malibu['karobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000
# print(malibus)
# dasturchilar={
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()}quyidagi dasturchilar biladi:")
#     for til in tillar:
#         print(til.upper(),end='')
# hamkasblar ={
#     'ali':{'familya':"valiyev",
#            't_yil':2000,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familya':"aliyev",
#            't_yil':2001,
#             'malumot':'o\'rta-maxsus',
#             'tillar':['html','css','js']
#             },
#     'hasan':{'familya':"khasanov",
#            't_yil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']
#              }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()}{info['familya'].title()},"
#           f" {info['t_yil']}-yilda tug'ilgan."
#           f"Ma'lumot: {info['malumot'].title()}\n "
#           f"Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#Amaliyot
# mashhur_shaxs={
#     'Abdulla':{'familya':'qodiriy',
#                't_yil':1894,
#                'manzil':'toshkent',
#                'umr':44
#                },
#     'erkin':{'familya':'Vohidov',
#              't_yil':1936,
#              'manzil':'farg\'ona',
#              'umr':80
#              },
#     'alisher':{'familya':'Navoiy',
#                't_yil':1441,
#                'manzil':'xirotda',
#                'umr':60
#                },
#     'abu abdulloh muhammad ':{
#         'familya':'ibn ismoil',
#         't_yil':810,
#         'manzil':'buxorada',
#         'umr':60
#     }
# }
# for ism, info in mashhur_shaxs.items():
#     print(f"\n{ism.title()}  {info['familya'].title()} "
#           f"{info['manzil'].title()}da {info['t_yil']}-yilda tug'ilgan."
#           f"{info['umr']} yil umr kurgan")
# mashhur={
#     'abu abdulloh':{
#         'familya':'ibn ismoil',
#         "asar":['al-jome\' as-sahih','al-adab al-mufrad','at-tarix al-kabir','at-tarix as-sag\'ir']
#     },
#     'abdulla':{
#         'familya':'qodiriy',
#         "asar":["o\'tkan kunlar",'mehrobdan chayon','obid ketmon']
#     },
#     'erkin':{
#         'familya':'Vohidov',
#         'asar':['tong nafasi',"qo'shiqlarim sizga","o'zbegim",'qiziquvchan matmusa']
#     },
#     'alisher':{
#         'familya':'Navoiy',
#         "asar":['xamsa','lison ut-tayr','mahbub al-qulub','munojot']
#
#     }
# }
# for ism, info in mashhur.items():
#     print(f"\n{ism.title()}  {info['familya'].title()}ning mashxur asarlari: ")
#     for i in info['asar']:
#      print(i.title())
# kino={
#     'ali':{
#         "kino":['terminator','rambo','titanic']
#     },
#     'vali':{
#         'kino':['star wars','avengers','matrix']
#
#     },
#     'hasan':{
#         'kino':['abdullajon','bomba','shaytanat']
#     },
#     'husan':{
#         'kino':['mahallada duv-duv gap','john wick']
#     }
# }
# for ism, info in kino.items():
#     print(f'\n{ism.title()}ning sevimli kinolari:')
#     for i in info['kino']:
#         print(i.title())
davlatlar = {
    'o\'zbekiston' :{
        'poytaxti':'toshkent',
        'hudud':448978,
        'aholi':37000000,
        'pul birligi':'so\'m'
    },
    'rossiya':{
        'poytaxti':'moskva',
        'hudud':1448978,
        'aholi':17000000,
        'pul birligi':'rubl'
    },
    'aqsh':{
        'poytaxti':'vashington',
        'hudud':9631418,
        'aholi':32700000,
        'pul birligi':'dollar'
    },
    'malayziya':{
        'poytaxti':'kuala-lumpur',
        'hudud':329750,
        'aholi':25000000,
        'pul birligi':'rinnigit'
    }
}
# for davlat, info in davlatlar.items():
    # print(f"\n{davlat.title()} davlatida {info['poytaxti'].title()} poytaxti")
    # print(f"Hudud: {info['hudud']} so'm")
    # print(f"Aholi: {info['aholi']} so'm")
    # print(f"Pul birligi: {info['pul birligi']}")
# davlat1=input('Davlatni kiriting:').lower()
# if davlat1 in davlatlar:
#     i =davlatlar[davlat1]
#     print(f"\n{davlat1.capitalize()} ning poytaxti: {i['poytaxti'].title()}"
#           f"\n Hudud: {i['hudud']} kv.km"
#           f"\n Aholi: {i['aholi']} "
#           f"\n Pul birligi: {i['pul birligi']}")
# else:
#     print('Bizda bu davlat haqida ma\'lumotlar mavjud emas')
