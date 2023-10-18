import argparse
import webbrowser
import json

#implement function: to choose which option the user will use
#site is crucial, and not optional
def argument_parser():
    parser = argparse.ArgumentParser(prog='Job sniper using google dorks')
    parser.add_argument('--url')
    parser.add_argument('--title')
    parser.add_argument('--text')
    parser.add_argument('--site')
    args = parser.parse_args()
    return args.url, args.title, args.text,args.site

def displayasci():
    print("""


 ██████  ███████ ██ ███    ██ ████████     ████████  ██████   ██████  ██          ████████  ██████       ██████  ███████ ████████     ██   ██ ██ ██████  ███████ ██████  
██    ██ ██      ██ ████   ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██       ██         ██        ██   ██ ██ ██   ██ ██      ██   ██ 
██    ██ ███████ ██ ██ ██  ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██   ███ █████      ██        ███████ ██ ██████  █████   ██   ██ 
██    ██      ██ ██ ██  ██ ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██    ██ ██         ██        ██   ██ ██ ██   ██ ██      ██   ██ 
 ██████  ███████ ██ ██   ████    ██           ██     ██████   ██████  ███████        ██     ██████       ██████  ███████    ██        ██   ██ ██ ██   ██ ███████ ██████  
                                                                                                                                                                         
                                                                                                                                                                        

          """)
from termcolor import colored

def display_banner():
    banner_lines = [
        "########################################################################################",
        "#                                                                                      #",
        "#                                     OSINT Dork Tool                                  #",
        "#                                                                                      #",
        "#    Author   : Yassine Jemlaoui                                                       #",
        "#    Contact  : mail@.com                                                              #",
        "#    Twitter  : @leeekafka    [https://twitter.com/]                                   #",
        "#    LinkedIn : [https://www.linkedin.com//]                                           #",
        "#                                                                                      #",
        "########################################################################################"
    ]
    
    # Imprimez chaque ligne de la bannière avec des couleurs.
    for line in banner_lines:
        if "OSINT Dork Tool" in line:
            print(colored(line, 'yellow', attrs=['bold']))
        elif "Author" in line or "Contact" in line or "Twitter" in line or "LinkedIn" in line:
            print(colored(line, 'cyan'))
        else:
            print(colored(line, 'green'))


def generate_dork(url,title,text,site):
    dork =f"site:{site}"
    if url:
        dork+=f" inurl:{url}"
    if title:
        dork+=f" intitle:{title}"
    if text:
        dork+=f" intext:{text}"
    return dork
    #think about implement/call api which helps to generate similar dorks
    # based on user inputs
def fetch_historical_data(dork):
    return f"https://web.archive.org/web/*/https://www.google.com/search?q={dork}"

def save_search(dork):
    searches = []
    try:
        # Try to load existing searches from the file
        with open('searches.json', 'r') as f:
            searches = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or it's empty/corrupt, just start with an empty list
        pass

    # Append the new search to the list of searches
    searches.append({'dork': dork})

    # Write the updated list back to the file
    with open('searches.json', 'w') as f:
        json.dump(searches, f)

def load_previous_searches():
    with open('searches.json', 'r') as f:
        searches = json.load(f)

    return searches

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
            break
        elif choice == '3':
            loaded_dorks = load_previous_searches()
            print("\nDorks précédemment sauvegardés:")
            for dork in loaded_dorks:
                print(dork)
            break
        elif choice=='4':
            webbrowser.open(f"https://www.google.com/search?q={dork}")
            break
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    #think abt adding if conditions if user do not enter all parameters
    
    interactive_menu()
