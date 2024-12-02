def main():
    
    new_character = Character(input("What is your name?\n"), input("What is your class?\n"), input("How much power do you have?\n"))
    #print(new_character.name, new_character.spec, new_character.power)
    welcome_message(new_character.name, new_character.spec, new_character.power)
    # Testing character class.
class Character:
    def __init__(self, name, spec, power):
        self.name = name
        self.spec = spec
        self.power = power
    
def welcome_message(name, spec, power):
    max_attempts = 5
    while max_attempts > 0:
        if len(name) >= 4:
            print("Sorry, the character name is too short. (Needs to be minimum 4 characters.)")
            break
        else:
            print("ERROR")
            max_attempts -= 1
            if max_attempts == 0:
                print("ERROR2")
                continue
main()