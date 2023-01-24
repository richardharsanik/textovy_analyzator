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

        volba = input("Enter a number btw. 1 and 3 to select: ")

        if volba.isdigit():
            volba = int(volba)
            vybrane_cislo = akcie[volba].replace(",","").replace(".","").replace("-","")
            slova = vybrane_cislo.split()
            
            #vybrane_cislo = akcie[volba].strip('.,:=-')
            #slova = vybrane_cislo.split()
            print(vybrane_cislo)
            print(slova)
            if volba in akcie.keys():

                #vybrane_cislo = akcie[volba].strip('.,:=-')

                #slova = vybrane_cislo.split()
                
                pocet_slov = sum(1 for i in slova )

                titlcase_words_sum = sum(1 for i in slova if i[0].isupper())

                upper_case = sum(1 for i in slova if i.isupper() and not i[0].isnumeric())

                lowercase = sum(1 for i in slova if i[0].islower())

                numeric = sum(1 for i in slova if i[0].isnumeric() and i[-1].isnumeric())

                sum = sum(int(s) for s in slova if s.isnumeric())

                dlzky_slov = {}

                for a in slova:
                    #print(a)
                    if len(a) in dlzky_slov:
                        dlzky_slov[len(a)] += 1
                    else:
                        dlzky_slov[len(a)] = 1
                        
                # print(f"There are {pocet_slov} words in the selected text.")
                # print(f"There are {titlcase_words_sum} titlecase words.")
                # print(f"There are {upper_case} uppercase words.")
                # print(f"There are {lowercase} lowercase words.")
                # print(f"There are {numeric} numeric strings.")
                # print(f"The sum of all numbers {sum}")
                # print(oddelovac)

                total = 0 

                for dlzka in sorted(dlzky_slov):
                    #print(dlzky_slov)
                    pocet = dlzky_slov[dlzka]                
                    total += pocet
                    #print(f"{dlzka}| {'*' * pocet} {pocet}")
                    #print("{:<3}|{:<16}|{:<3}".format(dlzka, '*' * pocet, pocet))
                        
            else:
                if volba not in akcie.keys():
                    print("Invalid input. Please enter a valid number.")
    else:
        print("wrong password")
else:
    print("unregistered user, terminating the program..")