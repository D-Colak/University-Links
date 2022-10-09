"""This app will ask the user for a university.
Using the hippolabs university api, it will output the corresponding public website."""
import requests


def header():
    """header for app"""
    print('--The University Website Grabber--')


def check_status(url):
    """gets url and tries to establish a secure connection. If not, says error code and quits."""
    try:
        test = requests.get(url)
        test.raise_for_status()
        print(f'You are securely connected. Status Code: {test.status_code}')
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e)


def inputs():
    """Asks for country and keywords, then returns"""
    country = input('Input a country, press enter if no country.\n').title()
    if country in ['Usa', 'Us', 'United States of America', 'America', 'U.S.', 'U.S', 'U.S.A', 'U.S.A.']:
        country = 'United States'
    elif country in ['Great Britain', 'Uk', 'Britain', 'United Kingdom of Great Britain and Northern Ireland',
                     'British Isles']:
        country = 'United Kingdom'
    elif country == 'Brunei':
        country = 'Brunei Darussalam'
    elif country == 'Burkina':
        country = 'Burkina Faso'
    elif country in ['Cabo Verde', 'Republic of Cabo Verde', 'Republic of Cape Verde']:
        country = 'Cape Verde'
    elif country in ['Congo', 'Republic of Congo']:
        try:
            congo = int(input('Type 1 for Republic of Congo, 2 for Democratic Republic of Congo.\n'))
            if congo == 1:
                country = 'Congo'
            elif congo == 2:
                country = 'Congo, the Democratic Republic of the'
            else:
                raise ValueError
        except ValueError:
            print('Please enter either 1 or 2.')
            inputs()
    elif country in ['Ivory Coast', 'Cote D\'ivore', 'Cote Divore']:
        country = 'Côte d\'Ivoire'
    elif country in ['Vatican City', 'Vatican State', 'Vatican City State', 'Holy See']:
        country = 'Holy See (Vatican City State)'
    elif country == 'Korea':
        korea = int(input('Type 1 for North Korea, 2 for South Korea.\n'))
        try:
            if korea == 1:
                country = 'Korea, Republic of'
            elif korea == 2:
                country = 'Korea, Democratic People\'s Republic of'
            else:
                raise ValueError
        except ValueError:
            print('Please enter either 1 or 2.')
            inputs()
    elif country in ['North Korea, Republic of Korea']:
        country = 'Korea, Republic of'
    elif country in ['South Korea', 'Democratic People\'s Republic of Korea']:
        country = 'Korea, Democratic People\'s Republic of'
    elif country == 'Laos':
        country = 'Lao People\'s Democratic Republic'
    elif country in ['Moldova', 'Republic of Moldova']:
        country = 'Moldova, Republic of'
    elif country in ['Palestine', 'State of Palestine']:
        country = 'Palestine, State of'
    elif country == 'Russian Federation':
        country = 'Russia'
    elif country == 'Reunion':
        country = 'Réunion'
    elif country == 'Syria':
        country = 'Syrian Arab Republic'
    elif country in ['Tanzania', 'United Republic of Tanzania']:
        country = 'Tanzania, United Republic of'
    elif country == 'Uae':
        country = 'United Arab Emirates'
    elif country in ['Venezuela', 'Bolivarian Republic of Venezuela']:
        country = 'Venezuela, Bolivarian Republic of'
    elif country == 'Vietnam':
        country = 'Viet Nam'
    elif country in ['Virgin Islands', 'British Virgin Islands']:
        country = 'Virgin Islands, British'

    keyword = input('Input a keyword(s), press enter if no keyword(s).\n').title()
    return keyword, country


def data_retrieve(keyword, country):
    """gets data from server using newly formed inputs, then stores the data in a variable"""
    url = requests.get('http://universities.hipolabs.com/search?name={}&country={}'.format(keyword, country))
    w1 = url.json()
    w = []
    for i in range(len(w1)):
        if w1[i] not in w1[i + 1:]:
            w.append(w1[i])
    return w


def data_present(w):
    """tries to narrow down user's search to one university, then gives the website for it."""
    name_dict = {}
    if len(w) > 50:
        while True:
            try:
                x = int(
                    input('Your search has more than 50 results.\nType 1 to restart and refine your search or 2 to '
                          'continue.\n'))
            except ValueError:
                print('Please enter the number 1 or 2.')
            if x == 1:
                part2()
            elif x == 2:
                break

    for i in range(1, len(w)):
        w = sorted(w, key=lambda x: x['name'])  # sorting nested dicts
        name_dict[i] = {'name': w[i - 1]['name'], 'web': w[i - 1]['web_pages']}  # creating new lists
        print(f'{i}: {name_dict[i]["name"]}')  # printing lists
    while True:
        try:
            numpick = int(input('Pick the number corresponding to the desired university.\n'))
            if numpick in name_dict:
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter a number from the list.')
    print(name_dict[numpick]['web'][0])
    exit()


# main driver code
def part1():
    header()
    check_status('http://universities.hipolabs.com/search?name=')


def part2():
    keyword, country = inputs()
    w = data_retrieve(keyword, country)
    data_present(w)


def main():
    part1()
    part2()


main()



