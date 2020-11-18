class Duck:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')

    def says(self):
        print(f'{self.name} goes "Quack-quack"')

class Goat:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def milk(self):
        print(f'{self.name} was milked')

    def says(self):
        print(f'{self.name} goes "Ma-a-a"')

class Chicken:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')

    def says(self):
        print(f'{self.name} goes "Co-co-co"')

class Sheep:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def shear(self):
        print(f'{self.name} was sheared')

    def says(self):
        print(f'{self.name} goes "Ba-a-a"')

class Cow:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def milk(self):
        print(f'{self.name} was milked')

    def says(self):
        print(f'{self.name} goes "Mo-o-o"')

class Goose:

    def __init__(self, name, weight=0.0):
        self.name = name
        self.weight = weight

    def feed(self, food):
        self.weight += food

    def eggs(self):
        print(f'Eggs were collected from the {self.name}')

    def says(self):
        print(f'{self.name} goes "Ga-ga-ga"')

animals = []


def init_animals():

    goose_seryj = Goose('Seryj', 2.3)
    goose_belyj = Goose('Belyj', 1.5)

    animals.append(goose_seryj)
    animals.append(goose_belyj)

    cow_manka = Cow('Manka', 200)

    animals.append(cow_manka)

    sheep_barashek = Sheep('Barashek', 20)
    sheep_kudrjavyj = Sheep('Kudrjavyj', 25)

    animals.append(sheep_barashek)
    animals.append(sheep_kudrjavyj)

    chicken_koko = Chicken('Ko-Ko', 0.52)
    chicken_kukareku = Chicken('Kukareku', 0.63)

    animals.append(chicken_koko)
    animals.append(chicken_kukareku)

    goat_roga = Goat('Roga', 65)
    goat_kopyta = Goat('Kopyta', 64)

    animals.append(goat_roga)
    animals.append(goat_kopyta)

    duck_krjakva = Duck('Krjakva', 1.2)

    animals.append(duck_krjakva)


def animal_care():

    for animal in animals:

        print()

        animal.says()
        animal.feed(1.3)

        if isinstance(animal, Cow) or isinstance(animal, Goat):
            animal.milk()

        if isinstance(animal, Sheep):
            animal.shear()

        if isinstance(animal, Chicken) or isinstance(animal, Duck) or isinstance(animal, Goose):
            animal.eggs()

def animal_weight():

    print()

    weight = 0
    max_weight = 0

    for animal in animals:

        weight += animal.weight

        if animal.weight > max_weight:
            max_weight = animal.weight
            heaviest_animal = animal.name

    print('Total weight of animals: {}'.format(round(weight, 2)))
    print(f'The heaviest animal: {heaviest_animal} with weight {max_weight}')


def main():

    init_animals()
    animal_care()
    animal_weight()


if __name__ == '__main__':
    main()