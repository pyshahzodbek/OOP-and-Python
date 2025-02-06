# 22.01.2025
# 11-dars
# Mavzu: Lug'at bilan tanishuv
# car_0={'model':'ferari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# talaba_0={'ism':'murodov olimov','yosh':20,"t_yil":2000}
# print(F'{talaba_0["ism"].title()},\
#       {talaba_0["t_yil"]}-yilda tug\'ilgan,\
#       {talaba_0['yosh']} yoshda')
# talaba_0['kurs']=4
# talaba_0['fakultet']='Amaliy matematika'
# print(talaba_0)
# talaba_1={}
# talaba_1['ism']='Ravshanov Shahzod'
# talaba_1['kurs']=1
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# talaba_0 = {'ism': 'murodov olimov', 'yosh': 20, "t_yil": 2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)
# telefonlar={
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'orif':'nokia 3310'}
# print(telefonlar)
# phone=telefonlar['ali']
# print(f"Alining telefoni {phone}")
# phone=telefonlar.get('hasan','Bunday ism mavjud emas')
# print(f" Hasanning telefoni {phone}")
#
# phone=telefonlar.get('hasan')
# print(phone)
#Amaliymashg'ulot
# otam={'ismi':"Murodullo",'t_yili':"1979",'manzil':"Qashqadaryo"}
# print(f" Otamning ismi {otam['ismi'].title()},{otam['t_yili']} -yilda,{otam['manzil'].title()} tug'ilgan. ")
# taomlar={
#     'Ali':'Manti',
#     'Vali':'xonim',
#     'hasan':'Sho\'rbo'
# }
# print(f" Alining  sevimli taomi {taomlar['Ali']} .")
py={
    'int':'Butun son',
    'float':'O\'nli son',
    'if':'Agar',
    'else':'Yoki'
}
kalit=input('Kalit so\'zni kiriting:'.lower())
# print(py.get(kalit,"bunday so'z mavjud emas"))
# kalit=input('Kalit so\'zni kiriting:'.lower())

tarjima=py.get(kalit)
if tarjima==None:
    print(f"{kalit} Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima}deb tarjima qilinadi.")
