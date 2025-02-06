# 26.01.2025
# 14-dars
#Mavzu:While tskil
# ism = input('isminizni kiriting: ')
# print(f'Salom,{ism.title()}')
# ism =input('isminizni kiriting: ')
# savol = f'Salom,{ism.title()}.Yoshingiz nechida?'
# yosh = input(savol)
# while
# son= 1 # son ga 1 qiymatini beramiz
# while son<=5:
#     print(son, end="")
#     son= son+1 # songa 1 qo'shamiz.
# while va input
# print('Kiritilgan sonnining kvadratini qaytaruvcgi dastur.')
# savol= 'Istalgan sonni kiriting'
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         qiymat=float(qiymat)
#         print(f'{qiymat} ning kvadrati: {qiymat**2}')
#Ishora(flag)
# print('Kiritilgan sonning kvadratini qaytaruvchu dastur.')
# savol= 'Istalgan sonni kiriting'
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# Break operatori
# print("Kiritilgan sonning kvadratini qaytaruvchu dastur.")
# savol="Istalgan sonni kiriting(dasturni to'xtatish uchun 'exit' deb yozing):"
# savol+='(dasturni to\'xtatish uchun "exit" deb yozing):'
# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:
#         qiymat=float(qiymat)
#         print(f'{qiymat} ning kvadrati: {qiymat**2}')
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son} ning kvadrati {son**2}")
# #continue operatori
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son ==5:  # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2}")
#Abadiy tsikl tuzog'i
# infinite loop
# son=0
#
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#        print(son)
# Amaliy mashg'ulot
# print(' Foydalanuvchi yaxshi ko\'rgan kitoblarni chiqaruvchi dastur.')
# savol='Yoqtirgan kitobni kiriting:'
# savol+='Dastur to\'xtashi uchun stop deb kiting.'
# qiymat=''
# while qiymat!="stop":
#     qiymat=input(savol)
#     if qiymat=='stop':
#         break
#     else:
#         print(qiymat)
# print("Muzeyga chipta narxlarini aniqlovchi dastur.")
# savol="Yoshingizni kiriting:"
# savol+="(Dasturni to'xtatish uchun 'exit'  yoki 'quit' deb yozing):"
# while True:
#     qiymat=int(input(savol))
#     if qiymat=='exit'or qiymat=='quit':
#       break
#     elif qiymat<=7 :
#         print("narx=2000")
#     elif qiymat>7 and qiymat<=18:
#         print("narx=3000")
#     elif qiymat>18  and  qiymat<=65:
#         narx=10000
#     else:
#         print('Sizga tekin!!')

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = float(input(savol))
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")