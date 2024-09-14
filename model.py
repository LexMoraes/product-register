class Produto:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code

    # Getter e Setter para name
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    # Getter e Setter para price
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.price = price

    # Getter e Setter para code
    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, code):
        self.code = code


class Component(Produto):
    def __init__(self, name, price, code, material, imported):
        super().__init__(name, price, code)
        self._material = material
        self._imported = imported

    # Getter e Setter para material
    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    # Getter e Setter para imported
    @property
    def imported(self):
        return self._imported

    @imported.setter
    def imported(self, imported):
        self._imported = imported



