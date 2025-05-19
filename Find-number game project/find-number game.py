"""
19/05/2025

"SON TOPISH" o'yini

Muallif: Abdurahmon Dadajonov
"""

import random

I = taxmin - 1


# Bu qismda PC bilan o'ynayotgan odam sonni topishi kerak
def game_finding_numbers(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"O'yinni boshlaymiz!, men 1 dan {x} gacha son o'yladim, topishga harakat qiling", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>>>"))
        if taxmin<tasodifiy_son:
            print("Xato!, men o'ylagan son bundan katta. Yana bir bor harakat qilib ko'ring", end="")
        elif taxmin>tasodifiy_son:
            print("Xato!, men o'ylagan son bundan kichik. Yana bir bor harakat qilib ko'ring", end="")
        else:
            break
        
    print(f"Tabriklaymiz!, {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

# Bu qismda PC sonni topishi kerak
def game_finding_numbers_pc(x=10):
    input(f"Endi meni galim!, 1 dan {x} gacha son o'ylang va istalgan tugmangizni bosing, men topishga harakat qilaman>>>>>")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri bo'lsa (t) harifini,"
                      f"Men o'lagan son bundan katta (+), yoki kichik (-)>>>>>".lower())
        if javob == "-":
            yuqori = I
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

# Bu qismda kim g'alaba qozongani e'lon qilinadi
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = game_finding_numbers(x)
        taxminlar_pc = game_finding_numbers_pc(x)

        if taxminlar_user>taxminlar_pc:
            print("Men yuttim!")

        elif taxminlar_user<taxminlar_pc:
            print("Siz yuttingiz!")

        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))

print(play())