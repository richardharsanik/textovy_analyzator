# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Richard Harsanik
# email: richard.harsanik@gmail.com
# discord: nakazeny#6042
# """
from task_template  import TEXTS

oddelovac = '-' * 40

username = input("username: ")

password = input("password: ")

registrovany_uzivatelia = {"bob": "123",
                          "ann": "pass123",
                          "mike": "password123",
                          "liz": "pass123"}

akcie = {    
    1: TEXTS[0],
    2: TEXTS[1],
    3: TEXTS[2]
}

hesla = registrovany_uzivatelia.values()

uzivatelia = registrovany_uzivatelia.keys()

if username in uzivatelia: 
    if password == registrovany_uzivatelia[username]:
        print(f"{oddelovac}\nWelcome to the app, {username}\nWe have 3 texts to be analyzed\n{oddelovac}")

        volba = int(input("Enter a number btw. 1 and 3 to select: "))

        vybrane_cislo = akcie[volba]

        slova = vybrane_cislo.split()

        pocet_slov = sum(1 for i in slova )

        titlcase_words_sum = sum(1 for i in slova if i[0].isupper())

        upper_case = sum(1 for i in slova if i.isupper() and not i[0].isnumeric())

        lowercase = sum(1 for i in slova if i[0].islower())

        numeric = sum(1 for i in slova if i[0].isnumeric() and i[-1].isnumeric())

        sum = sum(int(s) for s in slova if s.isnumeric())

        dlzky_slov = {}

        for a in slova:
            if len(a) in dlzky_slov:
                dlzky_slov[len(a)] += 1
            else:
                dlzky_slov[len(a)] = 1


        if volba in akcie.keys():
            print(f"There are {pocet_slov} words in the selected text.")
            print(f"There are {titlcase_words_sum} words in the selected text.")
            print(f"There are {upper_case} words in the selected text.")
            print(f"There are {lowercase} words in the selected text.")
            print(f"There are {numeric} words in the selected text.")
            print(f"There are {sum} words in the selected text.")
            print(oddelovac)

            for dlzka in sorted(dlzky_slov):
                pocet = dlzky_slov[dlzka]
                print(f"{dlzka}| {'*' * pocet} {pocet}")
        else:
            print("Numer unavailable")
            quit()
    else:
        print("wrong password")
        quit()    
        
else:
    print("unregistered user, terminating the program..")
    quit()


