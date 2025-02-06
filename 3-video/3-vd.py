#3-dars
# 15.01.2025
#Mavzu:String
shahar="SHahrisabz   "
viloyat='qashqadaryo'
print(shahar+viloyat)
matn="Men yangi  📱 telefon oldim."
ism='shahzod'
print("ismim "+ism)
ism='shahzod'
familya='Ravshanov'
print(ism+familya)
ism='Shahzod'
familya='Ravshanov'
print(ism +'  '+familya)
ism='Shahzod'
familya='Ravshanov'
ism_sharif=f"{ism} {familya}"
print(ism_sharif)

ism='Shahzod'
familya='Ravshanov'
print(f"Salom mening ismim {ism}.{ism} {familya}")

print("Hello World")
print("Hello \nWorld")
print('Hello \tWorld')

ism='Shahzod'
familya='Ravshanov'
ism_sharif=f"{ism}  {familya}"
print(ism_sharif.upper())

ism='shahzod'
familya='ravshanov'
ism_sharif=f"{ism}  {familya}"
print(ism_sharif.lower())

ism_sharif=f"{ism}  {familya}"
print(ism_sharif.title())
print(ism_sharif.capitalize())


Meva='     olma    '
print("Men"+Meva.rstrip()+"yaxshi kuraman,")
print('Men'+Meva.lstrip()+'yaxshi kuraman.')
print('Men' + Meva.strip()+'yaxshi kuraman')
print('Men'+Meva+'yaxshi kuraman')


ism=input("Ismingiz nima?")
print("Assalomu alaykum"+ism)
ism=input('Ismingiz nima?\n>>>>')
print('Assalomu alaykum ,   '+ism.title())


#Amaliy mashg'ulot
kocha="Beshbek"
Mahalla="xisorak"
tuman="SHahrisabz"
Viloyat='Qashqadaryo'
print(f'{kocha.title()}, {Mahalla.title()}, {tuman.title()} , {viloyat.title()}')

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos quyidagi ma\'lumotlarni kiriting")
Viloyat=input('Viloyat:')
Tuman=input('Tuman:')
Mahalla=input('Mahalla:')
Kocha=input('kocha:')
# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
print(f"{Viloyat.title()} viloyati ,{Tuman.capitalize()} tumani, {Mahalla.title()} mahallasi , {Kocha.upper()} kochasi ")
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(Viloyat + "   Viloyati\n"+ Tuman+"   tumani\n"+Mahalla+"   mahallasi\n"+Kocha+"  kochasi")

##manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
Manzil=f"{Viloyat.title()} viloyati ,{Tuman.capitalize()} tumani, {Mahalla.title()} mahallasi , {Kocha.upper()} kochasi"
print(Manzil.title())
print(Manzil.upper())
print(Manzil.lower())
print(Manzil.strip())









