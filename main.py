def main():
    def get_name():
        #Prompt to get user name.
        char_name = input("Enter character name:")
        if len(char_name) <= 4:
            raise Exception("The character name is too short.")
        else:
            print(f"Welcome {char_name}!")
    get_name()
main()
