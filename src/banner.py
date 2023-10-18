from termcolor import colored

def displayasci():
    print("""


 ██████  ███████ ██ ███    ██ ████████     ████████  ██████   ██████  ██          ████████  ██████       ██████  ███████ ████████     ██   ██ ██ ██████  ███████ ██████  
██    ██ ██      ██ ████   ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██       ██         ██        ██   ██ ██ ██   ██ ██      ██   ██ 
██    ██ ███████ ██ ██ ██  ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██   ███ █████      ██        ███████ ██ ██████  █████   ██   ██ 
██    ██      ██ ██ ██  ██ ██    ██           ██    ██    ██ ██    ██ ██             ██    ██    ██     ██    ██ ██         ██        ██   ██ ██ ██   ██ ██      ██   ██ 
 ██████  ███████ ██ ██   ████    ██           ██     ██████   ██████  ███████        ██     ██████       ██████  ███████    ██        ██   ██ ██ ██   ██ ███████ ██████  
                                                                                                                                                                         
                                                                                                                                                                        

          """)
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
