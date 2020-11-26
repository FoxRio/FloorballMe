import requests
import re

headers = {
    'authority': 'www.floorball.lv',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.floorball.lv',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.floorball.lv/lv/2020/chempionats/vv/kalendars',  # tur aktivu kada no definetajiem user_agent parlukiem
    'accept-language': 'en-US,en;q=0.9',
}

data = {
  'sEcho': '1',
  'iColumns': '7',
  'sColumns': '',
  'iDisplayStart': '0',
  'iDisplayLength': '50',
  'mDataProp_0': '0',
  'mDataProp_1': '1',
  'mDataProp_2': '2',
  'mDataProp_3': '3',
  'mDataProp_4': '4',
  'mDataProp_5': '5',
  'mDataProp_6': '6',
  'iSortingCols': '0',
  'bSortable_0': 'true',
  'bSortable_1': 'false',
  'bSortable_2': 'false',
  'bSortable_3': 'false',
  'bSortable_4': 'false',
  'bSortable_5': 'false',
  'bSortable_6': 'false',
  'url': 'https://www.floorball.lv/lv',
  'menu': 'chempionats',
  'filtrs_grupa': 'vv',
  'filtrs_sezona': '29',
  'filtrs_spelu_veids': '0',
  'filtrs_menesis': '11',
  'filtrs_komanda': '0',
  'filtrs_majas_viesi': '0'
}


response = requests.post('https://www.floorball.lv/ajax/ajax_chempionats_kalendars.php', headers=headers, data=data)


dub = ""  # izmanto lai izfiltretu liekos nosaukumus
teksts = response.json()
komanda = ""
output = open("output.txt", "a", encoding="utf-8")
output.

for x in teksts["aaData"]:
    output.write("\n")
    for i in x:
        if "href=" not in i:
            output.write(f"{i},")
        else:
            pattern = r'title=.+?"'
            m = re.search(pattern, i)
            try:
                komanda = m.group()[7:-1]  # noņem lieko no regex atrastaa
            except:
                pass
            if dub != komanda:
                output.write(f"{komanda},")
