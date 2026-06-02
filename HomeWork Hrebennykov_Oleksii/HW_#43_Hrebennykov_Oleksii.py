#-----------------------------------------------Task_#1-----------------------------------------------------------------
#------------------------------------------Добавление товаров-----------------------------------------------------------

# Создайте программу, которая подключается к MongoDB и:
# выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# очищает коллекцию перед началом
# добавляет 3 товара с полями: name, price, stock
# выводит сообщение о количестве добавленных товаров

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]

products = db["products_121225_ptm_Hrebennykov"]

products.delete_many({})

items = [
    {
        "name": "Pen",
        "price": 1.50,
        "stock": 300
    },
    {
        "name": "Notebook",
        "price": 3.99,
        "stock": 120
    },
    {
        "name": "Backpack",
        "price": 25.00,
        "stock": 50
    }
]

result = products.insert_many(items)

print(f"{len(result.inserted_ids)} products inserted.")

#--------------------------------------------------Task_#2--------------------------------------------------------------
#------------------------------------------------Увеличение цен---------------------------------------------------------
# Продолжите предыдущую задачу. Теперь программа должна:
# увеличить цену всех товаров на 20%
# вывести количество обновлённых записей
# затем вывести список всех товаров с новыми ценами

result = products.update_many(
    {},
    {
        "$mul": {
            "price": 1.2
        }
    }
)

print(f"Prices updated for {result.modified_count} products.")


print("\nUpdated products:")

for item in products.find({}, {"_id": 0}):
    print(f"- {item['name']} - ${item['price']:.2f}")
