import time
import requests
from bs4 import BeautifulSoup


def mp3getter(lst):  # Gets all the mp3 of the given languages
    url = "http://accent.gmu.edu/soundtracks/"
    for j in range(len(lst)):
        for i in range(1, lst[j][1]+1):
            while True:
                try:
                    fname = f"{lst[j][0]}{i}"
                    mp3 = requests.get(url+fname+".mp3")
                    print(f"\nDownloading {fname}.mp3")
                    with open(f"Audio/{fname}.mp3", "wb") as audio:
                        audio.write(mp3.content)
                except:
                    # Once file finishes downloading, a buffer time to make sure next download doesn't start too early
                    time.sleep(2)
                else:
                    break  # To break the while loop


def get_num(language):  # Returns the num of samples for a given language, useful in below function
    url = 'http://accent.gmu.edu/browse_language.php?function=find&language=' + language
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    div = soup.find_all('div', 'content')
    try:
        num = int(div[0].h5.string.split()[2])
    except AttributeError:
        num = 0
    return num


# Returns a list of tuples, (lang, num), mainly used for the mp3getter function
def get_formatted_languages(languages):
    formatted_languages = []
    for language in languages:
        num = get_num(language)
        if num != 0:
            formatted_languages.append((language, num))
    return formatted_languages


if __name__ == "__main__":
    # Add the function call here
    langs = ['arabic', 'english', 'french', 'german', 'hindi',
             'kannada', 'mandarin', 'russian', 'spanish']
    lang_tuple = get_formatted_languages(langs)
    print(lang_tuple)
    # [('arabic', 194), ('english', 646), ('french', 80), ('german', 42), ('hindi', 34), ('kannada', 9), ('mandarin', 150), ('russian', 81), ('spanish', 228)]
    print('Downloading now...')
    mp3getter(lang_tuple)
    print("DONE!!")
