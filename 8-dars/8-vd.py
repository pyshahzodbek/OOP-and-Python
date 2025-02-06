# # 19.01.2025-yil
# # 8-dars
# #Mavzu:Tarmoqlanish
# from platform import java_ver
#
# avtolar=['audi','bmw','volvo','kia','hyunadi']
# for avto in avtolar:  # avtolar ichidadi har bir avto uchun ...
#     if avto =='bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
#
#
# ism='Ali'
# print(ism.lower()=='ali')
# ism=input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':  # Agar ism Aliga teng bo'lmasa ...
#     print(f'Uzur , {ism.title()} biz Alini kutyapmiz.')
# else:
#     print('Salom, Ali')
#
# javob=float(input('12*6 nechiga teng? >>>'))
# if javob!=72:
#     print('Javob xato')
# else:
#     print('Tug\'ri')
#
# yosh=int(input('Yoshingiz nechchida?>>>'))
# if yosh>=18:
#     print('Xush kelibsiz')
# else:
#     print('Kirish mumkin emas')
#
# login=input('Yangi login tanlang:')
# if len(login)<=5:
#     print('Login 5 harfdan ko\'proq bo\'lishi kerak!')
# yil=int(input('Tug\'ilgan yilingizni kiriting:'))
# if 2025-yil<18:
#     print(f'Yoshingiz {2025-yil}da ekan')
#     print('Kirish mumkin emas!')
# else:
#     print('Xush kelibiz!')
#
# Yosh=int(input('Yoshingiz nechida?>>>'))
# if yosh>65:print('Siz COVID-19 risk guruhida ekansiz')
# x,y=25,50
# print('x>y')if x>y else print("x<y")
# Amaliymashg'ulot
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.upper())
# else:
#     print(car.title())
login = 'admin'
# ism = input('Ismingiz nima?>>>')
#
# if ism.lower() == login:
#     print("Xush kelibsiz, Admin.Foydalanuvchilar ro\'yxatini ko\'rasizmi?")
# else:
#     print(f'Xush kelibsiz, {ism}!')
#     print(ism.lower())
# son=int(input('Birinchi sonni kiriting:'))
# son1=int(input('Ikkkinchi sonni kiriting:'))
# if son==son1:
#     print('Sonlar teng')
# else:
#     print('sonlar tengemas')
#
# son2=int(input('Istalgan sonni kiriting:'))
# if son2<0:
#     print('Manfiy son ekan')
# else:
#     print('Musbat son ekan')
# son3=int(input('Son kiriting:'))
# if son3>0:
#     print(son3**1//2)
# else:
#     print('Musbat son kiriting')

# Yosh=int(input('Yoshingizni kiriting:'))
# if Yosh>=18:
#     print("Xush kelibsiz")
# else:
#     print('Siz hali voyaga yetmagansiz!!!')
#
# baho = float(input('Bahoni kiriting:'))
# if 90<=baho<=100:
#     print('Sizning natijangiz: A')
# elif   70<=baho<=89.9:
#     print('Sizning natijangiz:B')
# elif 60<=baho<=79.9:
#     print('Siz ning natijangiz:C')
# elif 50<=baho<=59.9:
#     print('Sizning natijangiz:D')
# else:
#     print('Sizning natijangiz:F')
#
# son=int(input('Sonni kiriting:'))
# if son>0:
#     print("Musbat")
# elif son<0:
#     print('Manfiy')
# else:
#     print('o')

a=int(input("Birinchi sonni kiriting:"))
b=int(input("Ikkinchi sonni kiriting:"))
c=int(input('Uchinchi sonni kiriting'))
#
# maxx =a
# l = []

# for i in  b , c:
#     if maxx <i:
#         maxx = i
# print(maxx)

if a> b and a> c:
    print(f"Kattasi {a}")
elif b>a and b>c:
    print(f"Kattasi {b}")
else:
    print(f"Kattasi {c}")

