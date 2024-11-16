class Flower():
    is_happy = False
    current_quantity = 0

    def __init__(self, name, water_requirements, is_happy):
        self.name = name
        self.water_requirements = water_requirements

    def status(self):
        return f"{self.name} is happy" if self.is_happy else f"{self.name} is not happy"

    def water(self, quantity):
        self.is_happy = (quantity >= self.water_requirements)

    # With Adding quantite
    # def water(self, quantity):
    #     self.current_quantity += quantity
    #     self.is_happy = (self.current_quantity >= self.water_requirements)


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
