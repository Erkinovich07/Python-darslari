#07-dars: Lists

ismlar = ['Doniyor', 'Atham', 'Mumin', 'Asadbek', "Akbarjon"]
#Ro'yxatdagi har bir do'stlar uchun qisqa xabar yozish
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

#.pop metodi ruyxatni ichidan bita qiymatni sugurib oladi
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

#.append metodi ruyxatga qiymatquwadi
friends = []
friends.append('Asat')
friends.append('Akbar')
friends.append('Done')
friends.append('Sobirjon')
friends.append('Vali')
print(friends)

#remove metodi ruyxatni ichidan qiymatni uchiradi
friends.remove('Asat')
friends.remove('Akbar')
print(friends)

#Ro'yxatga qiymat quwiw
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)


mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)