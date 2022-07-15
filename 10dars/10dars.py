#10-dars: if/else

#yanfi ruyxat tuzib ruyxatdagi qiymatlarni birinchi xarifini katta qilish
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())

#(!=) teng emas belgisi
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else:
    print(car.upper()) 

#foydalanuvchidan login surash
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")


son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")

 
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')