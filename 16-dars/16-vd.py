# 28.01.2025
# 16-dars
# Mavzu: Funksiya
# def salom_ber():
#     """ Salom beruvchi funksiya """
#     print("Assalom alaykum")
# salom_ber()
# def salom_ber_2(ism):
#     """ Foydalanuvchi ismi yuborilgan salom beruvchi funksiya """
#     print(f"Assalom alaykum,hurmatli  {ism}")
# salom_ber_2("Murat")
# print(salom_ber_2.__doc__)
# def toliq_ism(ism,familya):
#     """Foydalanuvchi ismi va familiyasi yuborilgan toliq beruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()} \n"
#           f"Foydalanuvchi familiyasi: {familya.title()}")
# toliq_ism("Shahzod","Ravshanov")
# def yosh_hisobla(ism,tugilgan_yil):
#     """ Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")
# yosh_hisobla("Murat",2020)
# yosh_hisobla(tugilgan_yil=1997,ism="Murat")
# def yosh_hisobla_2(tugilgan_yil,joriy_yil=2024):
#     """ Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydigan funksiya"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshda siz")
# yosh_hisobla_2(1995,2025)
#Amaliy mashg'ulot
# def yosh(ism,t_yil):
#     """ Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2025-t_yil} yoshda ")
# yosh("Murat",1995)
# def son(a):
#     """Foydalanuvchidan son olib, uning kvadratini va kubini qaytaruvchi funksiya"""
#     print(f" {a} soning kvadrati: {a**2} \n"
#           f" {a} soning kubini: {a**3}")
# son(4)
# def son_1(a):
#     """ Foydalanuvchidan son olib, uning juft yoki toqligini qaytaruvchi funksiya"""
#     if a%2==0:
#         print(f"{a} soni juft son")
#     else:
#         print(f"{a} soni toq")
# # son_1(5)
# def taqqoslash(a,b):
#     """Foydalanuvchidan ikkita son olib,
#  ulardan kattasini konsolga chiqaruvchi funksiya """
#     if a>b:
#         print(f"{a} > {b}")
#     elif a<b:
#         print(f"{a} < {b}")
#     else:
#         print(f"{a} = {b}")
# taqqoslash(10,10)
# def daraja(x,y=2):
#     """Foydalanuvchidan x va y sonlarini olib,
#      x^y sonini qaytaruvchi funksiya"""
#     print(f"{x}^ {y} = {x**y}")
# daraja(6,3)
# def qoldiqsiz(x):
#     """ Foydalanuvchidan son qabul qilib,
#     sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
#     bo'linishini tekshiruvchi funksiya"""
#     for i in range(2,11):
#         if x%i==0:
#             print(f"{x} - {i} gac qoldiqsiz bo'linadi ")
#         else:
#             print(f"{x}soni  {i} qoldiqli bo'linadi")
# qoldiqsiz(16)