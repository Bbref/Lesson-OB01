class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание нескольких магазинов
store1 = Store("Продуктовый магазин", "ул. Ленина, 10")
store1.add_item("Яблоки", 89.99)
store1.add_item("Молоко", 54.0)

store2 = Store("Аптека", "пр. Победы, 15")
store2.add_item("Аспирин", 220.0)
store2.add_item("Бинт", 19.5)

store3 = Store("Книжный магазин", "ул. Пушкина, 5")
store3.add_item("Мастер и Маргарита", 1000)
store3.add_item("Преступление и наказание", 800)

# Тестирование методов
print("Тестирование методов магазина 1:")
print("Цена Яблок в магазине 1:", store1.get_price("Яблоки"))
store1.update_price("Яблоки", 96.6)
print("Новая цена Яблок в магазине 1:", store1.get_price("Яблоки"))
print("Товары в магазине 1 до удаления:", store1.items)
store1.remove_item("Молоко")
print("Товары в магазине 1 после удаления:", store1.items)
