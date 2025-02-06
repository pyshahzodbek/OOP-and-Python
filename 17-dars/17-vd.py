# 28.01.2025
# 17-dars
# Mavzu:QIYMAT QAYTARUVCHI FUNKSIYA
# def toliq_ism_yasa(ism,familya):
#     """Foydalanuvchi ismi va familiyasi yuborilgan to'liq beruvchi funksiya"""
#     toliq_ism=f"{ism} {familya}"
#     return toliq_ism
# talaba1= toliq_ism_yasa("Murat","Ravshanov")
# talaba2= toliq_ism_yasa("Dilshod","Ochilov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# Ixtiyoriy argument
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# #
# def avto_info( kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto={
#         "kompaniya":kompaniya,
#         "model":model,
#         "rangi":rangi,
#         "korobka":korobka,
#         "yili":yili,
#         "narhi":narhi
#     }
#     return avto
# avto1=avto_info("GM","Malibu","Qora","Avtomat",2024)
# avto2=avto_info("GM","Gentra","Oq","Mexanika",2023,15000)
# avtolari=[avto1,avto2]
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolari:
#     if avto["narhi"]:
#         narhi=avto["narhi"]
#     else:
#         narhi="Noma'lum"
#     print(f"{avto["rangi"]} {avto['model']} {avto['kompaniya']} {narhi} so\'m")
# def oraliq(min,max,qadam=1):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# print(oraliq(1,10,2))
# print(oraliq(10,21))
# print(oraliq(0,21,2))
#
# print("Saytimizdagi avtolar ro'ycxatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli:")
#     rangi=input("Rangi:")
#     korobka=input("Korobka:")
#     yili=int(input(" Ishlab chiqarilgan yili:"))
#     narhi=input("Narhi:")
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
#     javob=input("Yana avto qo'shasizmi? (ha/yuq):")
#     if javob=="ha":
#         continue
#     else:
#         break
# Amaliymashg'ulot
# def toliq_malumot(ism,familya,t_yil,t_joy,e_manzil=None,tel_raqam=None):
#     malumot={
#         "ism":ism,
#         "familya":familya,
#         "tug'ilgan yil":t_yil,
#         "tug'ilgan joy":t_joy,
#         "e-manzili":e_manzil,
#         "tel raqam":tel_raqam
#     }
#     return malumot
# foydalanuvchi1=toliq_malumot("Shahzod","Ravshanov",2000,"Shahrisabz")
# foydalanuvchi2=toliq_malumot("Murodov","Olimov",2001,2026,"Toshkent, Uchb-ulug'i",987654321)
# print(foydalanuvchi1)
# print(foydalanuvchi2)
# def toliq_malumot(ism,familya,t_yil,t_joy,e_manzil=None,tel_raqam=None):
#     malumot={
#         "ism":ism,
#         "familya":familya,
#         "tug'ilgan yil":t_yil,
#         "tug'ilgan joy":t_joy,
#         "e-manzili":e_manzil,
#         "tel raqam":tel_raqam
#     }
#     return malumot
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end='')
#     ism=input("Ismingizni kiriting: ")
#     familya=input("Familiyangizni kiriting: ")
#     t_yil=int(input("Tug'ilgan yili kiriting: "))
#     t_joy=(input("Tug'ilgan joy kiriting: "))
#     e_manzil=input("E-manzilini kiriting: ")
#     tel_raqam=int(input("Tel raqamini kiriting: "))
#     malumot=toliq_malumot(ism,familya,t_yil,t_joy,e_manzil,tel_raqam)
#     print(malumot)
#     javob=input("Yana ma'lumot kiritishni xohlaysizmi?(ha/yuq)")
#     print(javob)
#     if javob=="ha":
#         continue
#     else:
#         break
#
# print(malumot)
# def uchtason_kirit(a,b,c):
#     """ Uchta son kiritilganda rng kattasini topuvchi funksiya"""
#     if a>b and a>c:
#         print(f"Katttasi {a} ga teng")
#
#     elif b>a and b>c:
#         print(f"Katttasi {b} ga teng")
#
#     else:
#         print(f"Katttasi {c} ga teng")
#     return uchtason_kirit
#
#
# a=uchtason_kirit(1,2,3)
# def eng_katta1(x,y,z):
#     eng_katta=max(x,y,z)
#     return eng_katta
# x=float(input("x="))
# y=float(input('y='))
# z=float(input('z='))
# print(f"Katta soni {eng_katta1(x,y,z)} ga teng")
# def aylana_yuzi(r,d,s,p):
#     """ Aylana yuzini topuvchi funksiya"""
#     aylana={
#         'r':r,
#         "d":d,
#         "s":s,
#         "p":p
#     }
#     return aylana
# r=int(input("Aylana radiusini kiriting:"))
# d=r*2
# s=r*r*3.14
# p=2*3.14*r
#
# aylana=aylana_yuzi(r,d,s,p)
# print(aylana)
#
# def tub_sonlar(x,y=1):
#     """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya """
#     tub_son=[]
#     tub=True
#     for i in range(y,x+1):
#      if i==1:
#       tub=False
#      elif i==2:
#          tub=True
#      else:
#          for n in range(2,i):
#              if i%n==0:
#                  tub=False
#                  break
#      if tub:
#         tub_son.append(i)
#
#         return tub_son

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#
#     return tub_sonlar
# tub_sonlar_top(1, 10)
# min=int(input("Min son kiriting:"))
# max=int(input("Max son kiriting:"))
# print(tub_sonlar_top(min,max))
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar
#
#
# print(fibonacci(10))


# a = int(input("A = "))
# d = (a // 2) + 1
# b = 0
# for i in range(2, d):
#     if a % i == 0:
#         b += 1
#     else:
#         continue
# if b > 2:
#     print("Murakkab")
# else:
#     print("Tub")


def tub_son(a):
    d = (a // 2) + 1
    b = 0
    for i in range(2, d):
        if a % i == 0:
            b += 1
        else:
            continue
    if b > 2:
        return "Murakkab"
    else:
        return "Tub"


t = tub_son(11)
print(t)
