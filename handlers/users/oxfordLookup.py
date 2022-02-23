"""
Created on Wed Feb  9 20:08:06 2022

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import requests
from googletrans import Translator
translator = Translator()

app_id = "53f20bb2"
app_key = "2eda4bc5ab3228d6de786407ebca5b0f"
language = "en-gb"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        answer = sense['definitions'][0]
        # uzbek = f"🇺🇿👉{translator.translate(answer, 'uz').text}"
        definitions.append(f"🇺🇸👉 {answer}\n.\n")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == '__main__':
    print(getDefinitions('Great Britain'))
    print(getDefinitions('sdsdsdsds'))