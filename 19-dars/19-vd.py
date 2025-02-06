#30.01.2025
# 19-dars
# Mavzu: Moslashuvchan funksiya(* args , **kwargs)

# def summa(*sonlar):
#     """ Kiritilgan sonlarni summani qaytaruvchi funksiya"""
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
#
# print(summa(1,2,3))
#
# def summa(*sonlar):
#     """ Kiritilgan sonni yig'indisisni qaytaruvhci  funksiya"""
#     return  sum(sonlar)
# print(summa(4,5,6,7,8))
#
# def summa(x,y,*sonlar):
#     """ Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return  x+y+sum(sonlar)
# print(summa(2,2,1,23,4,5))
# #**kwargs USULI
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar["kompaniya"]=kompaniya
#     malumotlar["model"]=model
#     return malumotlar
# avto1=avto_info('GM','malibu',rang="qora",yil=2024)
# avto2=avto_info('Toyota','corolla',rang='qizil' ,yil=2024)
# print(avto1)
# print(avto2)
#Amaliyot
# def summa(*sonlar):
#     kupaytma=1
#     for i in sonlar:
#         kupaytma*=i
#     return kupaytma
# print(summa(1,2,3,4,5))
# def malumot(ism,familya ,**malumotlar):
#     malummotlar1={}
#     malummotlar1["ism"]=ism
#     malummotlar1["familya"]=familya
#     malummotlar1.update(malumotlar)
#     return malummotlar1
# malumotlar=malumot('shahzod','ravshanov',t_yil=2006,yashash='Qashqadaryo')
# print(malumotlar)
