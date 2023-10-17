import argparse
import webbrowser

#implement function: to choose which option the user will use
#site is crucial, and not optional
def argument_parser():
    parser = argparse.ArgumentParser(prog='Job sniper using google dorks')
    parser.add_argument('--inurl')
    parser.add_argument('--intitle')
    parser.add_argument('--intext')
    args = parser.parse_args()
    return args.inurl, args.intitle, args.intext

def generate_dork(url,title,text):
    site = "insite:linkedin.com"
    dork1 = f"{site} inurl:{url} intitle:{title} intext:{text}"
    #dork1 = site + "inurl:" + url + "intitle: " + title + "text: " + text
    return dork1
    #think about implement/call api which helps to generate similar dorks
    # based on user inputs



if __name__ == "__main__":
    inurl,intitle,intext= argument_parser()
    dork = generate_dork(inurl,intitle,intext)
    #think abt adding if conditions if user do not enter all parameters
    print(f"Generated Google Dork: {dork}")
    open_browser = input("Do you want to open this in your browser? (y/n): ")
    if open_browser.lower() == 'y':
        print("Opening now!")
        webbrowser.open(f"https://www.google.com/search?q={dork}")

