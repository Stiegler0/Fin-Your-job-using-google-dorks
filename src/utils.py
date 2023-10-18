import json,argparse
def argument_parser():
    parser = argparse.ArgumentParser(prog='Job sniper using google dorks')
    parser.add_argument('--url')
    parser.add_argument('--title')
    parser.add_argument('--text')
    parser.add_argument('--site')
    args = parser.parse_args()
    return args.url, args.title, args.text,args.site


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

def latest_dorks():
    with open('searches.json','r') as f:
        dorks = json.load(f)
        return dorks[-5:]

def save_search(dork):
    searches = []
    try:
        # Try to load existing searches from the file
        with open('data/searches.json', 'r') as f:
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
