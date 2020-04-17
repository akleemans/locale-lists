import csv

import requests

response = requests.get('https://translate.wordpress.org/')

english = []
native = []
for lang in response.text.split('<div class="locale percent-')[1:]:
    tag = lang.split('<li class="code"><a')[1].split('>')[1].split('<')[0]
    native_name = lang.split('<li class="native"><a')[1].split('>')[1].split('<')[0]
    english_name = lang.split('<li class="english"><a')[1].split('>')[1].split('<')[0]
    english.append((tag, english_name))
    native.append((tag, native_name))

with open('wordpress_en.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(english)

with open('wordpress_native.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(native)
