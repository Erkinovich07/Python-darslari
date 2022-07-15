#18-dars: WHILE VA RO'YXATLAR

mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != "ha":
        break
print("Mahsulotlar qo'shildi")