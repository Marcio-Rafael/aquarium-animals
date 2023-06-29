import json

f = open("aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def verif_fish(animal):
    if animal["type"] == "fish":
        return True
    return False


animals_fish = list(filter(verif_fish, animals))
print(animals_fish)

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)

def assign_to_tank(animals, name_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in name_selected:
            animal["tank number"] = 42
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)