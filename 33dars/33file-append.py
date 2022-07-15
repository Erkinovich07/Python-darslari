#33-DARS. FILES

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book:
        break
    with open("amaliyot/books.txt", "a") as file:
        file.write(book + "\n")
