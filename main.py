from database import db

db.create_table_brands()
db.create_table_models()


def add_brand():
    brand = input("Brand nomini kiriting: ")
    db.insert_brand(brand)
    yes_no = input("Yana brand qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_brand()


def del_brand():
    view_brands()
    brand = input("O'chirmoqchi bo'lgan brand nomini kiriting: ")
    db.delete_brand(brand)
    yes_no = input("Yana brand o'chirasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        del_brand()


def view_brands():
    brands = db.select_brands()
    for brand in brands:
        print(brand[0], brand[1])


def add_model():
    model = input("Model nomini kiriting: ")
    color = input("Model rangini kiriting: ")
    price = int(input("Model narxini kiriting: "))
    view_brands()
    brand_id = int(input("Brand id sini kiriting: "))
    db.insert_model(model, color, price, brand_id)
    yes_no = input("Yana model qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_model()

def view_models():
    models = db.select_models()
    for model in models:
        model_id, model, color, price, brand = model
        print(model_id, model, color, price, brand)

def add_employee():
    employee_id = int(input('Ishchini id sini kiriting: '))
    first_name = input('Ischini ismini kiriting: ')
    last_name = input('Ishchini familiyasini kiriting: ')
    birth_date = int(input("Ishchini tug'ilgan yilini kiriting: "))
    phone_number = int(input('Ischini telefon raqamini kiritng: '))
    email = input("Ischini email addresini kiriting")
    country = input('Ischi qaysi davlattan kelgan? ')
    city = input('Ishchi qaysi shaharda tugilgan? ')
    db.insert_employee(employee_id, first_name, last_name, birth_date, phone_number, email, country, city)
    yes_no = input("Yana model ishchi qoshasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_employee()

def add_order():
    car_count = int(input('Nechta sotib oluvchi nechta avtomobil sotib olgan? '))
    order_date = input('Avtomobil qachon sotib olingan? ')
    db.insert_orders(car_count, order_date)
    yes_no = input("Yana model ishchi qoshasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_order()

def add_customer():
    first_name = input('Sotib oluvchi odamni ismini kiriting: ')
    last_name = input('Sotib oluvchi odamni familiyasini kiriting: ')
    birth_date = int(input("Sotib oluvchi odamni tug'ilgan yilini kiriting: "))
    phone_number = int(input('Sotib oluvchi odamni telefon raqamini kiritng: '))
    email = input("Sotib oluvchi odamni email addresini kiriting: ")
    country = input('Sotib oluvchi odam qaysi davlattan kelgan? ')
    city = input('Sotib oluvchi odam qaysi shaharda tugilgan? ')
    db.insert_customer(first_name, last_name, birth_date, phone_number, email, country, city)
    yes_no = input("Yana model ishchi qoshasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_employee()
def run():
    while True:
        command = input("Nima qilmoqchisiz? : ").lower()
        if command == 'add brand':
            add_brand()

        if command == 'del brand':
            del_brand()

        if command == 'view brands':
            view_brands()

        if command == 'add model':
            add_model()

        if command == 'view models':
            view_models()

        if command == 'add employee':
            add_employee()

        if command == 'add customer':
            add_customer()

        if command == 'add order':
            add_order()

        if command == 'stop':
            break



if __name__ == '__main__':
    run()
