class TangaBank:
    def __init__(self, birinchi="person_1", ikkinchi="person_2"):
        self.birinchi = birinchi
        self.ikkinchi = ikkinchi

        self.mavjud_1 = 3
        self.mavjud_2 = 3
        print("Qurilma ishga tushdi !\n")

    def name_input(self):
        """Odamlarning ismlarini kiritish."""
        self.birinchi = input("Birinchi inson ismi : ")
        self.ikkinchi = input("Ikkinchi inson ismi : ")

    def share_or_steal(self, harakatlar):


        birinchi_1= harakatlar
        ikkinchi_2=harakatlar

        if birinchi_1 == 'share' and ikkinchi_2 == 'share':
            self.mavjud_1 += 2
            self.mavjud_2 += 2
        elif birinchi_1 == 'share' and ikkinchi_2 == 'steal':
            self.mavjud_1 -= 1  
            self.mavjud_2 += 3  
        elif birinchi_1 == 'steal' and ikkinchi_2 == 'share':
            self.mavjud_1 += 3  
            self.mavjud_2 -= 1  
        elif birinchi_1 == 'steal' and ikkinchi_2 == 'steal':
            self.mavjud_1 += 0  
            self.mavjud_2 += 0
        else:
            print("Xato kiritilgan!!!")
            return False  


    def print_natija(self):
  
        print(f"{self.birinchi} da {self.mavjud_1} ta tanga!")
        print(f"{self.ikkinchi} da {self.mavjud_2} ta tanga!")

tanga = TangaBank()

while True:

    tanga.name_input()

    harakatlar = []
    harakat1 = input(f"\n{tanga.birinchi} 'share' yoki 'steal': ").lower()
    harakat2 = input(f"\n{tanga.ikkinchi} 'share' yoki 'steal': ").lower()

    harakatlar.append(harakat1)
    harakatlar.append(harakat2)

    tanga.share_or_steal(harakatlar)
    tanga.print_natija()

    print("\n[1] - Davom etish")
    print("[0] - To'xtatish")
    a = int(input("Tanlang: "))

    if a == 1:
        continue
    elif a == 0:
        print("Dastur yakunlandi.")
        break
    else:
        print(f"Not found: {a}. Xato ma'lumot kiritilgan!")
