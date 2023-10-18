import webbrowser
from utils import argument_parser,latest_dorks, generate_dork, save_search, load_previous_searches
from banner import displayasci,display_banner
from termcolor import colored



#implement function: to choose which option the user will use
#site is crucial, and not optional







def interactive_menu():
    displayasci()
    display_banner()
    print('Bienvenue')
    while True:
        print(colored("##################################", 'green'))
        print(colored("#", 'green') + "              MENU              " + colored("#", 'green'))
        print(colored("##################################", 'green')) 
        print(colored("#", 'green') + " 1. " + colored("Generer un nouveau dork.", 'cyan'))
        print(colored("#", 'green') + " 2. " + colored("Sauvegarder un nouveau dork.", 'cyan'))
        print(colored("#", 'green') + " 3. " + colored("Afficher les dorks sauvegardés.", 'cyan'))
        print(colored("#", 'green') + " 4. " + colored("Ouvrir le dork.", 'cyan'))
        print(colored("#", 'green') + " 5. " + colored("Quitter.", 'red'))
        print(colored("##################################", 'green'))
        choice = input(colored("#", 'green') + " " + colored("Entrez votre choix:", 'yellow', attrs=['bold']) + " ")
        if choice == '1':
            insite,inurl,intitle,intext= argument_parser()
            dork = generate_dork(insite,inurl,intitle,intext)
            print(dork)
            save_search(dork)
            
        elif choice == '2':
            dork = input("Entrez le dork à sauvegarder: ")
            save_search(dork)
            print(colored('[+]','green') +f"'{dork}' a été sauvegardé!")
            
        elif choice == '3':
            loaded_dorks = load_previous_searches()
            print("\nDorks précédemment sauvegardés:")
            for dork in loaded_dorks:
                print(dork)
            
        elif choice=='4':
            print("Choose one of the following dork from your latest 5 generated ones: ")
            last = latest_dorks()
            for i in range(len(last)):
                print(f"{i}: {last[i]}")
            choice2 = int(input(colored("#", 'green') + " " + colored("Entrez votre choix du dork:", 'yellow', attrs=['bold']) + " "))
            for a in range(len(last)):
                if a==choice2:
                    dork= last[a]['dork']
                    print(dork)
                    c = webbrowser.get('firefox')
                    c.open(f"https://www.google.com/search?q={dork}")
            #webbrowser.open(f"https://www.google.com/search?q={dork}")
            
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    #think abt adding if conditions if user do not enter all parameters
    
    interactive_menu()
