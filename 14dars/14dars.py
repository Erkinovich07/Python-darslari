#14 dars lugat

#sodda lugat
car_0 = {'model':'ferrari','rang':'qizil'}


talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")

 #yangi juftlik quwiw
 talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika' 

#bush lugat
talaba_1 = {}


talaba_1['ism'] = 'samandar erkinovich'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#kalit suz qiymatini uchirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

#lugatni qatorga bulib yozish

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

#get metodi
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")