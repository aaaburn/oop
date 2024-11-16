class Hero:
    """This is a class for Hero."""

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int) -> str:
        """Reduces the hero's health by damage amount."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} is defeated."
        return f"{self.name} has {self.health} health left."

    def heal(self, amount: int) -> str:
        """Increases the hero's health by heal amount."""
        self.health += amount
        # Optional: Define a maximum health (e.g., 100)
        # self.health = min(self.health, 100)
        return f"{self.name} is healed to {self.health} health."

# Execute exercise
hero = Hero("Peter", 100)
print(hero.defend(50))  # Should print Peter has 50 health left.
print(hero.heal(50))    # Should print Peter is healed to 100 health.
print(hero.defend(99))  # Should print Peter has 1 health left.
print(hero.defend(1))   # Should print Peter is defeated.
