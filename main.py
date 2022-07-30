import requests
import time

f = open("lenker.txt", "r")
links = []
start_link = "https://quiz.natureid.no/bird/eBook.php?specieID="
for a in f:
    links.append(start_link + a)
cookies = {'languageID_1': '1'}
html_data = requests.get(start_link, cookies=cookies).text


''' Get the name of the bird
'''

for b in links:
    html_data = requests.get(b[0:-1], cookies=cookies).text
    title_index_start = 0
    if "<title>" in html_data:
        title_index_start = html_data.index("<title>")

    title_index_stop = 0
    if "-         BirdIDs fuglebok - Nord University - Birdid" in html_data:
        title_index_stop = html_data.index("-         BirdIDs fuglebok - Nord University - Birdid")

    name_of_bird = html_data[title_index_start:title_index_stop].replace("<title>", "").replace("\n", "")
    print(name_of_bird[9:-1:])

    ''' Get the appearance description
    '''
    utseende_index_start = 0
    if '<span class="title">Utseende</span>' in html_data:
        length_of_input_utseende = len('<span class="title">Utseende</span>')
        utseende_index_start = html_data.index('<span class="title">Utseende</span>') + length_of_input_utseende

    utseende_index_stop = 0
    if '<span class="title">Lyd</span>' in html_data:
        utseende_index_stop = html_data.index('<span class="title">Lyd</span>')

    utseende_info = html_data[utseende_index_start:utseende_index_stop]

    create_substring = ""
    if "<p>" in utseende_info:
        create_substring = utseende_info[0:utseende_info.index("<p>")]

    with open('test.txt', "a") as f:
        f.write(name_of_bird[9:-1])
        f.write("\n")
        f.write("\n")
        f.write(f"LENKE: {b[0:-1]}")
        f.write("\n")
        f.write("\n")
        f.write("UTSEENDE")
        f.write("\n")
        f.write("\n")
        f.write(utseende_info[21:-22:])
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")

    print(utseende_info[21:-22:])
    time.sleep(3)
