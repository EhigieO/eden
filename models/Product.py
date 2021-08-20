import decimal

from models.Category import Category


class Product:
    def __init__(self, category, name, price):
        self.__category: Category = category
        self.__name: str = name
        self.__price: decimal = price
        self.__description: str
        self.__id: str

    @property
    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    @property
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    @property
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    @property
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description