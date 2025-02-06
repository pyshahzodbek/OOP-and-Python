# 30.01.2025
# 21-dars
# Mavzu: Funksiylar. So'ngiso'z
#
# import  math
# uzunlik =lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
# product=lambda x,y:x**y
# print(product(3,2))
#
# def daraja(n):
#     return lambda x:x**n
# kvadrat= daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga , kubi {kub(3)} ga teng")
# # map() FUNKSIYASI
# from math import sqrt
# sonlar = list(range(11))
# ildizlar =list(map(sqrt,sonlar))
# print(ildizlar)

#1
# sonlar=list(range(11))
# def daraja2(x):
#     """ Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2,sonlar)))
#
# #2
# kvadratlar =list(map(lambda x:x*x,sonlar))
# print(kvadratlar)
#
# #3
# kvadratlar =[]
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)
#
# a=[4,5,6]
# b=[7,8,9]
# a_plus_b=list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)
# ismlar =['hasan','olim','anvar','husan']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# filter() FUNKSIYASI
# import  random as r
# sonlar = r.sample(range(100),10)
# print(sonlar)
#
# def juftmi(x):
#     """ x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
#     return x%2==0
# juft_sonlar= list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r
# sonlar = r .sample(range(100),10)
# juft_sonlar =list(filter(lambda x:x%2==0,sonlar))
# print(sonlar)
# print(juft_sonlar)
import  random as r
sonlar =r.sample(range(500),50)
toq_sonlar =list(filter(lambda x: x%2!=0,sonlar))
print(sonlar)
print(toq_sonlar)

mevalar=['olma','anor','anjir','shaftoli','o\'rik','tarvuz','qovun','banan','rad','aadar']
mevalar_b=list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)

mevalar_a= list(filter(lambda meva:meva.startswith('a'),mevalar))
print(mevalar_a)
mevalar_c=list(filter(lambda meva: meva.startswith('c'),mevalar))
print(mevalar_c)

mevalar2=list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar2)
# .endswith oxirgi tugaydigan harfni chiqaradi
m=list(filter(lambda meva:(meva.startswith('a')and meva.endswith('r')),mevalar))
print(m)


