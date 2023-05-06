# """
# AVTOSERVIS []

#     car = {
#         "id":1,
#         "miqdori":10,
#         "narxi":100000000,
#         "nomi":Lixus 570,
#         "firmasi":Toyoto
#         "rangi":Qora,
#         "otkuchi":3000,
#         "yili":2020
#         "information":idsi 1, quantity 10, narxi 10000$, nomi Lixus 570, firmasi Toyoto, rangi Qora, yili 2020.
#     }

#     shunday data bo'ladi

# --------------------------------------------
# #     -----   1) Mashina soni          -----
# #     -----   2) Mashina qo'shish      -----
# #     -----   3) Mashina sotib olish   -----  
# #     -----   4) Mashina qidirish      -----
# #     -----   5) Chiqish               -----
# #     --------------------------------------

#     Menyuda shular bo'lishi kerak

# --------------------------------------------
# #     -----   1) Mashina soni          -----
# #     -----   2) Mashina qo'shish      -----
# #     -----   3) Mashina sotib olish   -----  
# #     -----   4) Mashina qidirish      -----
# #     -----   5) Chiqish               -----
# #     --------------------------------------

#     1ni bosganda  mana shu menyu chiqsin

#     data kiritilganda iddagi barcha ma'limotlar chiqarilsin

# """


AVTOSERVIS = []
car__buy__id = []

cars_1 = {
    "id":1,
    "quantity":1,
    "price":10000,
    "name":"Lixus 570",
    "firm":"Toyoto",
    "colour":"Qora",
    "shooter":3000,
    "year":2020,
    "information":"id: 1, quantitiy: 1, price: 10000, name: Lixus 570, firm: Toyoto, colour: Qora, shooter: 300, year: 2020."
    }

cars_2 = {
    "id":2,
    "quantity":2,
    "price":60000,
    "name":"Ferrari",
    "firm":"BMW",
    "colour":"Qizil",
    "shooter":2500,
    "year":2021,
    "information":"id: 2, quantity: 2, price: 60000, name: Ferrari, firm: BMW, colour: Qizil, shooter: 250, year: 2021."
    }

cars_3 = {
    "id":3,
    "quantity":3,
    "price":30000,
    "name":"Mers s class",
    "firm":"JM",
    "colour":"Oq",
    "shooter":1000,
    "year":2019,
    "information":"id: 3, quantity: 3, price 30000, name: Mers s class, firm: JM, colour: Oq, shooter: 1000, year: 2019."
    }

cars_4 = {
    "id":4,
    "quantity":4,
    "price":2000,
    "name":"Bugatti chiron A 1",
    "firm":"Bugatti",
    "colour":"Kulrang",
    "shooter":3000,
    "year":2023,
    "information":"id: 4, quantity: 4, price:2000, name: Bugatti chirom A 1, firm: Bugatti, colour: Kulrang, shooter: 3000, year: 2023."
    }

cars_5 = {
    "id":5,
    "quantity":5,
    "price":2500,
    "name":"Malibu",
    "firm":"Chevrolet",
    "colour":"Qora",
    "shooter":2000,
    "year":2023,
    "information":"id: 5, quantity: 5, price: 2500, name: Malibu, firm: Chevrolet, colour: Qora, shooter: 2000, year: 2023."
    }

cars_6 = {
    "id":6,
    "quantity":6,
    "price":2800,
    "name":"Tracker best",
    "firm":"Tracker",
    "colour":"Qora",
    "shooter":1000,
    "year":2017,
    "information":"id: 6, quantity: 6, price: 2800, name: Tracker best, firm: Tracker, colour: Qora, shooter: 100, year 2017."
    }

cars_7 = {
    "id":7,
    "quantity":7,
    "price":4000,
    "name":"Lada vesta",
    "firm":"Lada",
    "colour":"Qizil",
    "shooter":1500,
    "year":2016,
    "information":"id: 7, quantity: 7, price: 150, name: Lada vesta, firm: Lada, colour: Qizil, shooter: 150, year: 2016."
    }

cars_8 = {
    "id":8,
    "quantity":8,
    "price":5000,
    "name":"Toyoto x class",
    "firm":"Toyoto",
    "colour":"Oq",
    "shooter":2000,
    "year":2023,
    "information":"id: 8, quantity: 8, price: 5000, name: Toyoto x class, firm: Toyoto, colour: Oq, shooter: 2000, year: 2023."
    }

cars_9 = {
    "id":9,
    "quantity":9,
    "price":3400,
    "name":"Onix a class",
    "firm":"Onix",
    "colour":"Kulrang",
    "shooter":1700,
    "year":2019,
    "information":"id: 9, quantity: 9, price: 3400, name: Onix xclass, firm: Onix, colour: Kulrang, shooter: 1700, year 2019."
    }

cars_10 = {
    "id":10,
    "quantity":10,
    "price":6430,
    "name":"Hundai B class",
    "firm":"Hundai",
    "colour":"Oq",
    "shooter":1340,
    "year":2020,
    "information":"id: 10, quantity: 10, price: 6430, name: Hundai x class, firm: Hundai, colour: Oq, shooter: 1340, year 2020."
    }

AVTOSERVIS.append(cars_1)
AVTOSERVIS.append(cars_2)
AVTOSERVIS.append(cars_3)
AVTOSERVIS.append(cars_4)
AVTOSERVIS.append(cars_5)
AVTOSERVIS.append(cars_6)
AVTOSERVIS.append(cars_7)
AVTOSERVIS.append(cars_8)
AVTOSERVIS.append(cars_9)
AVTOSERVIS.append(cars_10)

def CONSOLE__PRINT(cars__data):
    print(f"=======================================")
    print(f"===> ID: {cars__data['id'] }")
    print(f"===> quantity: {cars__data['quantity']}")
    print(f"===> price: {cars__data['price']}")
    print(f"===> name: {cars__data['name']}")
    print(f"===> firm: {cars__data['firm']}")
    print(f"===> colour: {cars__data['colour']}")
    print(f"===> shooter: {cars__data['shooter']}")
    print(f"===> year{cars__data['year']}")
    print(f"===> information{cars__data['information']}")
    print(f"=======================================\n")

def NUMBER__CARS():
    print("===>>> NUMBER__CARS bo'limiga xush kelibsiz <<<===")

    for x in AVTOSERVIS:
        CONSOLE__PRINT(x)

    MENU()

def CREATE__CARS():
    print("---->>> CREATE__CARS bo'limiga xush  kelibsiz <<<----")

    while True:
        check__boolean = {
            "quantity": False,
            "price": False,             
            "name": False,
            "firm": False,
            "colour": False,
            "shooter": False,
            "year": False,
            "information": False,
            "check": False,
            }
        
        last__cars = AVTOSERVIS.pop()
        id = last__cars['id'] + 1
        quantity = input("Siz quantityingizni kiriting: ")
        price = input("Siz priceingizni kiriting: ")
        name = input("Siz namengizni kiriting: ")
        firm = input("Siz firmingizni kiriting: ")
        colour = input("Siz colouringizni kiriting: ")
        shooter = input("Siz shooteringizni kiriting: ")
        year = input("Siz yearingizni kiriting: ")
        information = input("Siz informationingizni kiriting: ")

        if len(quantity) >= 1 and len(quantity) <=2: 
            check__boolean['quantity'] = True
        else: 
            print("Siz quantityni ma'lumotlarini to'g'ri kiritmadingiz.")

        if len(price) >= 4:
            check__boolean["price"] = True

        else:
            print("Siz priceni ma'lumotlarini to'g'ri kiritmadingiz. ")

        if len(name) >= 5 and len(name) <=16:
            check__boolean["name"] = True

        else:
            print("Siz nameni ma'lumotlarini to'g'ri kiritmagansiz.")

        if len(firm) >= 3 and len(firm) <= 9:
            check__boolean['firm'] = True

        else:
            print("Siz firmni ma'lumotini to'g'ri kiritmadingiz.")

        if len(colour) <= 2 and len(colour) <= 7:
            check__boolean["colour"] = True

        else:
            print("Siz colourni ma'lumotini to'g'ri kiritmadingiz.")

        if len(shooter) <= 4:
            check__boolean["shooter"] = True

        else:
            print("Siz shooterni ma'lumotini to'g'ri kiritmadingiz.")


        if len(year) >= 4:
            check__boolean["year"] = True

        else:
            print("Siz yearni ma'lumotini to'g'ri kiritmadingiz.")

        if len(information) >= 20 and len(information) <= 45:
            check__boolean["information"] = True

        else:
            print("Siz informationni ma'lumotini to'g'ri kiritmadingiz.")
        
        tasdiqlash = input("Siz tasdiqlang. To'g'ri bo'lsa (t) noto'g'ri bo'lsa (n): ")

        if tasdiqlash == 't':
            check__boolean["check"] = True

        else:
            print("Tasdiqlanmadi")
            MENU()
            break

        if check__boolean['check']:
            if check__boolean['quantity'] and check__boolean['price'] and check__boolean['name'] and check__boolean['firm'] and check__boolean['colour'] and check__boolean['shooter'] and check__boolean['year'] and check__boolean['information']:
                AVTOSERVIS.append({
                    "id": id,
                    "quantity": quantity,
                    "price": price,             
                    "name": name,
                    "firm": firm,
                    "colour": colour,
                    "shooter": shooter,
                    "year": year,
                    "information": information
                })

                print("Sizni ma' lumotlaringiz tasdiqlandi.")
                MENU()
                break

def EQUAL__CARS(id_, quanity, price, name, firm, colour, shooter, year, information):
    print("---->>> EQUAL__CARS bo'limiga xush kelibsiz <<<----")
    for i in AVTOSERVIS:
        if i['id'] == id_:
           i['quanity'] = quanity
           i['price'] = price
           i['name'] = name
           i['firm'] = firm
           i['colour'] = colour
           i['shooter'] = shooter
           i['year'] = year
           i['information'] = information

           print("Sizni ma' lumotlaringiz tasdiqlandi.")
                
           MAIN()

def CARS__ID__RETURN(id):
    print("CARS__ID__RETURN bo'limiga xush kelibsiz")
    for x in AVTOSERVIS:
        if x['id'] == id:
            CONSOLE__PRINT(x)

def BUYING__CARS():
    print("---->>> BUYING__CARS bo'limiga xush kelibsiz <<<----")

    for x in AVTOSERVIS:
        CONSOLE__PRINT(x)

    while True:
        print("Oqraga qaytish uchun (b) tanlab olsangiz (ok)")
        input__cars = input("Siz qaysi mashinani sotib olmoqchisiz id kiriting: ")

        if input__cars == "b":
            MENU()

        elif input__cars == "ok":
            MENU()

        if input__cars.isdigit():
            car__buy__id.append(int(input__cars))

def SEARCH__CARS():
    print("---->>> SEARCH__CARS bo'limiga xush kelibsiz <<<----")
    input__search = input("Qidirmoqchi bo'lgan mashinangizni kiriting: ")

    for x in AVTOSERVIS:
        if (x['name']).upper() == input__search.upper():
            CONSOLE__PRINT(x)

            MENU()
            break

def CHECKOUT():
    print("---->>> CHECKOUT bo'limiga xush kelibsiz <<<----")
    for x in car__buy__id:
        CARS__ID__RETURN(x)

    while True:
        check__out = input("Karta raqamingizni kiriting: ")

        if check__out.isdigit():
            print("Xaridingiz muvaffaqiyatli yakunlandi.")
            MENU()

        else:
            print("Siz xato password kiritdingiz.")
            print("Qayta kiriting.")

def EXIT():
    print("---->>> EXIT bo'limiga xush kelibsiz <<<----")
    print("Thank you for your purchase")        
    print("See you")

def MENU():
    print("---->>> MENU bo'limiga xush kelibsiz <<<----")
    print("""
    --------------------------------------
    -----   1) Number cars           -----
    -----   2) Create cars           -----
    -----   3) Buying cars           -----  
    -----   4) Search cars           -----
    -----   5) Checkout cars         -----
    -----   6) Exit                  -----
    --------------------------------------
    """)

    input__menu__number = int(input("Menyudan birini kiriting: "))
    if input__menu__number == 1: NUMBER__CARS()
    elif input__menu__number == 2: CREATE__CARS()
    elif input__menu__number == 3: BUYING__CARS()
    elif input__menu__number == 4: SEARCH__CARS()
    elif input__menu__number == 5: CHECKOUT()
    elif input__menu__number == 6: EXIT()
    else: print("Menyudagi sonlardan birini tanlang: ")

def MAIN():
    MENU()
MAIN()
