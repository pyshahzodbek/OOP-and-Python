#5-dars
#17.01.2025
#Mavzu: List(Ro'yxat)


mevalar=['Olma','Anjir','Banan','Shaftoli'] #mevalar ro'yxati(matnlar)
narhlar=[1200,1500,2500,3600] # narhlar ro'xati(Sonlar)
Ismlar=[]
print('Birinchi meva',mevalar[0].title())
print('Ikkinchi meva',mevalar[1].upper())
print(narhlar[0]+narhlar[1])
cars_model=['Nexia','Malibu','Treker','cobalt']
print(cars_model[-1])# Listning eng oxirgi elementiga -1 bilan murojat qilamiz

narhlar=[1200,1500,2500,3600]
narhlar[0]=18000
narhlar[1]=27000
narhlar[2]=56000
print(narhlar)


mevalar=['Olma','Anjir','Banan','Shaftoli']
mevalar.append('tarvuz') # mevalar ga tarvuz qo'shamiz
print(mevalar)
cars=[]
cars.append('Malibu')
cars.append('Captiva')
cars.append('Cobalt')
print(cars)
cars=['Nexia','Malibu','Treker','cobalt']
cars.insert(0,'Nexia 3')
print(cars)
cars.insert(2,'ferarri')
print(cars)

mevalar=['olma','Anjir','Banan','Shaftoli']
del mevalar[1]
print(mevalar)
del mevalar[0]
print(mevalar)
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('olma') #Ruyxatdan olmani uchirdik
print(mevalar)
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar)
bozorlik=['Non','Go\'sht','Piyoz','Sabzi']
Mahsulot=bozorlik.pop(3)
print('Men',Mahsulot,'sotib oldim')
print('olinmagan mahsulot:',bozorlik)

#Amaliymashg'ulot
ismlar=['Otabek', 'Dilshod','Ozodbek']
print(f'Salom',ismlar[0],',','bugun choyxona bormi?')
print(ismlar[1]+', choyxonaga boramizmi?')
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar=[12,-4,3,12.5]
sonlar[0]=sonlar[0]+2
sonlar[1]=sonlar[1]-12
sonlar.append('45')
del sonlar[3]
sonlar.remove(3)
print(sonlar)
sonlar[2]=sonlar[0]+sonlar[1]
print(sonlar)

t_Shaxslar=['Alsher Navoiy','Amir Temur','Alxorazimiy']
z_shaxslar=['Bill Geyst','Ilon Mask','Jahongir Ortiqxo\'jayev']
print("Men tarixiy shaxslardan  "+t_Shaxslar[1]+'  bilan, zamonaviy shaxslardan'+z_shaxslar[1]+' bilan suhbat qilmoqchiman' )
print(f'men tarixiy shaxslardan {t_Shaxslar[0]} bilan , zamonaviy shaxslardan {z_shaxslar[0]} bilan suhbatlash  moqchiman')

friends=[]
friends.append('Dilshod')
friends.append('Otabek')
friends.append('Lazizbek')
friends.append('Ozodbek')
print(friends)
friends.remove("Otabek")
print(friends)
friends.insert(0,"Islombek")
friends.insert(1,'Diyorbek')
friends.append("Elbek")
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print('Kelgan mehmonlar:',mehmonlar)
