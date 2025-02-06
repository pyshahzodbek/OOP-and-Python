# 31.01.2025
# Son topish o'yini
import random as r

def son_topish_oyini(x=10):
    tasodifiy_son=r.randint(1,x)
    taxminlar=0
    print("1 dan 10 gacha son o'yladim topishga harakat qiling.")
    while True:
        taxmin=int(input(">>>"))
        taxminlar+=1
        if taxmin==tasodifiy_son:
            print(f"Tabriklayman topdiz!!! {taxminlar} ta o'rinishda.")
            break
        elif taxmin>tasodifiy_son:
            print(f" Men o'ylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            print(f"Men o'ylagan son bundan kattaroq. Yana harakat qiling.")

    return taxminlar


def son_topish_kk(x=10):
    tasodifiy_son=r.randint(1,x)
    taxminlark=0
    quyi=1
    yuqori=x
    print(" siz 1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    while True:
       taxminlark+=1
       tasodif=(quyi+yuqori)//2
       javob=input(f" Siz {tasodif} ni o'yladingiz.(T/+/-)").lower()
       if javob=="t":
            print(f" {taxminlark} ta o'rinishda topdim.")
            break
       elif javob=="-":
          yuqori=tasodif-1
       elif javob=="+":
               quyi=tasodif+1


    return taxminlark

def play():
    
    yana=True

    while yana:
        tasodifiy_user = son_topish_oyini()
        tasodifiy_kk = son_topish_kk()
        if tasodifiy_user==tasodifiy_kk:
            print("Durang!!!")
        elif tasodifiy_user>tasodifiy_kk:
            print("Men yutdim!!!")
        else:
            print("Siz yutdingiz!!!")
        yana=int(input(f"Yana uynaymizmi.ha(1)/yo'q(0)\n>>>"))



play()


