# 21.01.2025
# 10-dars
# Mavzu: Xatolar bilan ishlash
# Amaliy mashg'ulot
# son =float(input('Juft son kiriting:'))
# if not son%2==0:
#     print('Bu juft emas.')
# else:
#     print('Rahmat!!!')
# yosh = int(input('Yoshingiz nechida?'))
# if yosh<=4 or yosh>=60:
#     print('Sizga bepul!')
# elif yosh<18:
#     narh=10000
# else:
#     narh= 20000
#     print(f"Chipta {narh} so'm")
# x=float(input('Birinchi sonni kiriting:'))
# y=float(input('Ikkinchi sonni kiriting:'))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')
# else:
#     print(f'{x}>{y}')
#mahsulotlar=['un','yog\'','sovun','tuxum','piyoz','kartoshka','olma','banan','uzum','qovun']
#savat=[]
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing:'))
# if savat:
#     for i in savat:
#         if i in mahsulotlar:
#             print(f"Do'konimizda {i} bor")
#         else:
#             print(f"Do'konimizda {i} yo'q")
# else:
#     print("Savatingiz bo'sh")
# mahsulotlar=['un','yog\'','sovun','tuxum','piyoz','kartoshka','olma','banan','uzum','qovun']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing:"))
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for i in savat:
#     if i in mahsulotlar:
#         bor_mahsulotlar.append(i)
#     else:
#         mavjud_emas.append(i)
# for j in mavjud_emas:
#     print(j)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#
# else:
#     print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
ism=['alisher1983','aziza','yasina','umar']
login=input('Yangi login tanlang:')
if login in ism:
    print('login band, yangi login tanlang!')
else:
    print('Xush kelibsiz!')
