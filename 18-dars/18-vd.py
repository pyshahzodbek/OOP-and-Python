# 29.01.2025
#18-dars
# Mavzu: Funksiya va ro'yxat tuzish
# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning baholini kiriting: ")
#         baholar[ism]=baho
#     return baholar
# talabalar=["ali","vali","hasan","husan"]
# baholar=bahola(talabalar)
# print(baholar)
# talabalar=["ali","vali","hasan","husan"]
# baholar=bahola(talabalar[:])
# print(talabalar)
# print(baholar)
#Amaliyot
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
# ismlar=["ali","vali","hasan","husan"]
# katta_harf(ismlar)
# print(ismlar)
#
# def asl_ruyxat(matn):
#     """ asl ro'yxatni o'zgartirmaydigan
#     va yangi ro'yxat qaytaradigan qilib o'zgartiradigan funksiya """
#     matn=matn[:]
#     for i in range(len(matn)):
#         matn[i]=matn[i].title()
#         return matn
# ismlar =['ali','vali','hasan','husan']
# yangi_ismlar=asl_ruyxat(ismlar)
# print(yangi_ismlar)
# print(ismlar)
talabalar=["ali",'vali','hasan','husan']
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
baholar=bahola(talabalar)
print(baholar)
print(talabalar)

