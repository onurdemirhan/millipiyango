import os
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"}
the_folder = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(the_folder, "sayisal.txt")

#50 tane çünkü çekilen tarih itibarıyla 114 çekiliş var
for cekilis_no in range(1,114):
    webpage = "https://www.millipiyangoonline.com/sisalsans/drawdetails.sayisaloto." + str(cekilis_no) + ".2022.json"
    with requests.get(webpage, headers=headers) as url:
        data = url.json()
    #çekiliş bilgileri
    numbers = data["winningNumber"]
    numbers =  [str(x) for x in numbers]
    numbers.append(data["dateDetails"])
        #bir altta, ile joinlemek için hepsini birleştir
    with open(out, 'a', encoding='utf-8') as ff:
                print(", ".join(numbers), file=ff)
