import sys
import requests
import json
from requests.structures import CaseInsensitiveDict

bing_addr="https://www.bing.com"
json_link="http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

savedir = sys.argv[1]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(json_link, headers=headers)

if resp.ok:
    webjson = json.loads(resp.content.decode())
    imageurl = bing_addr + webjson['images'][0]['url']
    imagename = webjson['images'][0]['url'].split('&')[0].split('=')[1]
    imagepath = savedir + '/' + imagename
    imager = requests.get(imageurl)
    with open(imagepath, 'wb') as f:
        f.write(imager.content)
    print(imagepath)
else:
    raise ValueError('Fetching website failed.')
