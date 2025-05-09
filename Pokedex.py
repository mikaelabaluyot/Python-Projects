


class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ',' + self.name + '!')

    def display_details(self):
        print("The Pokemon" " " + self.name + " " "is a" " " + self.types + " " "type pokemon!" )

        print("It is described as" " " + self.description)

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + ' hasn\'t been caught yet.')



bulba = Pokemon(1, "Bulbasaur", "grass-posion", "broccoli that speaks", "True")
pika = Pokemon(25,"Pikachu", "electric", "lightning bolt frog", "True")
squir = Pokemon(7,"Squirtle", "water", "turtle that squirts", "True" )
psy = Pokemon(54,"Psyduck", "water", "chronic duck head-ache", "True")
dit = Pokemon(132, "Ditto", "normal", "purple blob", "False")
jiggle = Pokemon(39, "Jigglypuff", "fairy", "big eyed pink blob", "True")
slow = Pokemon(79,"Slowpoke", "water-psychic", "slow and a bit daft", "False")
rai = Pokemon(26, "Raichu","electric-psychic", "lidl pikachu", "False")

pika.speak()
pika.display_details()

