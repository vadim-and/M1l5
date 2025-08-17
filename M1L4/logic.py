from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.name = self.get_name()
        self.hp = randint(50, 150) 
        self.power = randint(10, 30)  
        Pokemon.pokemons[pokemon_trainer] = self

    def get_name(self):
        try:
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            response.raise_for_status()
            return response.json()['name']
        except Exception:
            return "Pikachu"

    def info(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Сила: {self.power}"

    def attack(self, target):
        damage = self.power
        target.hp -= damage
        print(f"{self.name} атакует {target.name} и наносит {damage} урона!")

class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.mana = randint(30, 70)

    def attack(self, target):
        if self.mana >= 15:
            damage = self.power + self.mana // 5
            target.hp -= damage
            self.mana -= 15
            print(f"{self.name} (Волшебник) атакует магией и наносит {damage} урона!")
        else:
            print(f"{self.name} (Волшебник) использует обычную атаку.")
            super().attack(target)

class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.stamina = randint(40, 80)

    def attack(self, target):
        if self.stamina >= 20:
            damage = self.power * 1.2
            target.hp -= damage
            self.stamina -= 20
            print(f"{self.name} (Боец) использует мощный удар и наносит {damage} урона!")
        else:
            print(f"{self.name} (Боец) использует обычную атаку.")
            super().attack(target)