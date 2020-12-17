import requests
from bs4 import BeautifulSoup
import sys
from argparse import ArgumentParser

languages = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese"\
             ,"dutch", "polish", "portuguese", "romanian", "russian", "turkish"]
orig_lang = ""
trans_lang = ""
word = ""


def parse_arguments():
    global orig_lang, trans_lang, word
    parser = ArgumentParser(description="Multilingual Online Translator (Web Scraping project)\n"+\
                                        "Usage: python translator.py [origin language] [target language] [word]")
    parser.add_argument("olang", type=str)
    parser.add_argument("tlang", type=str)
    parser.add_argument("word", type=str)
    args = parser.parse_args()
    orig_lang = args.olang.lower()
    trans_lang = args.tlang.lower()
    word = args.word
    if orig_lang not in languages:
        print(f"Sorry, the program doesn't support {orig_lang}")
        sys.exit()
    if trans_lang not in languages and trans_lang != "all":
        print(f"Sorry, the program doesn't support {trans_lang}")
        sys.exit()


def make_url():
    return f"https://context.reverso.net/translation/{orig_lang}-{trans_lang}/{word}"


def make_request_and_get_soup(url):
    headers = {'User-Agent': 'Translator-Practice-App/0.0.1'}
    try:
        r = requests.get(url, headers=headers)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
        print("Something wrong with your internet connection")
        sys.exit()
    return BeautifulSoup(r.content, 'html.parser')


def print_translations(soup, file=None):
    translations = []
    results = soup.select('#translations-content .translation', limit=5)
    if len(results) == 0:
        print(f"Sorry, unable to find {word}")
        sys.exit()
    [translations.append(x.text.strip()) for x in results]
    print(f"{trans_lang.capitalize()} Translations:")
    [print(x) for x in translations]
    with open(file, 'a', encoding='utf-8') as file_write:
        print(f"{trans_lang.capitalize()} Translations:", file=file_write)
        [print(x, file=file_write) for x in translations]


def print_phrases(soup, file=None):
    phrases = {}
    orig_phrases = soup.select_one("#examples-content .src")
    trans_phrases = soup.select_one("#examples-content .trg")
    if orig_phrases == None or trans_phrases == None:
        print(f"Sorry, unable to find {word}")
        sys.exit()
    phrases[orig_phrases.text.strip()] = trans_phrases.text.strip()
    print(f"\n{trans_lang.capitalize()} Examples:")
    [print(x, ":\n", phrases.get(x), "\n", sep="") for x in phrases.keys()]
    with open(file, 'a', encoding='utf-8') as file_write:
        print(f"\n{trans_lang.capitalize()} Examples:", file=file_write)
        [print(x, ":\n", phrases.get(x), "\n", sep="", file=file_write) for x in phrases.keys()]


def translate():
    global trans_lang
    url = make_url()
    file = (f"{word}.txt")
    with open(file, 'w', encoding='utf-8'):
        pass
    if trans_lang != "all":
        soup = make_request_and_get_soup(url)
        print_translations(soup, file)
        print_phrases(soup, file)
    else:
        for lang in languages:
            if lang.lower() == orig_lang:
                continue
            trans_lang = lang.lower()
            url = make_url()
            soup = make_request_and_get_soup(url)
            print_translations(soup, file)
            print_phrases(soup, file)


parse_arguments()
translate()
