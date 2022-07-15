#08-dars: Ro'yxatlar bilan ishlash

#Ro'yxatni uznligini len tekshiradi
print(len(davlatlar))

#sorted() ruyxatni tartiblab beradi
print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda taxlaydi
print(sorted(davlatlar, reverse=True))

#reverse() metodi ruyxatni orqadan boshlab konsolga chiqaradi
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqarish
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200))

#Ro'yxatdagi sonlar yig'indisini hisoblash 
print(sum(sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblash
print(max(sonlar)-min(sonlar))

#Ro'yxatdagi elementlar sonini hisoblash
print(len(sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqarish
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#taomlar degan ro'yxat yaratib va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa olish
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldir, va qo'shimcha 2 ta taom qo'sh
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham konsolga chiqarish
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantirish va nonushta[0] = "qaymoq va non" deb qiymat berib ko'r
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"