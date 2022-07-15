#09-dars: for loops

ismlar = ['Asat','Vali','Akbar','Done','Olim']
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuz 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqar
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rash
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    

n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)