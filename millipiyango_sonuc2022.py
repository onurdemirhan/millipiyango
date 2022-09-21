import os
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"}
the_folder = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(the_folder, "millipiyango.txt")

#50 tane çünkü çekilen tarih itibarıyla 50 çekiliş var
for cekilis_no in range(1,51):
    webpage = "https://www.millipiyangoonline.com/sisalsans/drawdetails.millypiyango." + str(cekilis_no) + ".2022.json"
    with requests.get(webpage, headers=headers) as url:
        data = url.json()
    #çekiliş bilgileri
    tarih = data["dateDetails"]
    yuksek01_name = data['firstCategoryName']
    yuksek01_value = data['firstCategoryWinning'][0]
    yuksek02_name = data['secondCategoryName']
    yuksek02_value = data['secondCategoryWinning'][0]
    #bir altta, ile joinlemek için hepsini birleştir
    hepsi = tarih, yuksek01_name, yuksek01_value, yuksek02_name, yuksek02_value
    with open(out, 'a', encoding='utf-8') as ff:
                print(", ".join(hepsi), file=ff)
