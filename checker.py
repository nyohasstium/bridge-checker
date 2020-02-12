import requests
from PIL import Image

def getWestImage():
  gmap_url="https://www.google.com/maps/@51.5749806,-2.6952274,15z/data=!5m1!1e1"
  return getBridgeImage(gmap_url)

def getEastImage():
  gmap_url="https://www.google.com/maps/@51.6113365,-2.6431683,15z/data=!5m1!1e1"
  return getBridgeImage(gmap_url)

def getBridgeImage(gmap_url):
  api="https://api.apiflash.com/v1/urltoimage?access_key=1bca5e701f204615b6c758c6f28bc59e&url="
  response = requests.get(url = api+gmap_url, stream=True)
  response.raw.decode_content = True
  return Image.open(response.raw)

def isBridgeOpen(image, x, y1, y2):
  px = image.load()
  is_green_present = False
  number_of_greens = 0
  for y_axis in range(y1, y2):
    red=px[x, y_axis][0]
    green=px[x, y_axis][1]
    blue=px[x, y_axis][2]
    is_green = green-red >100 and green-blue>100
    if(is_green_present == False and is_green == True):
      is_green_present = True
      number_of_greens = number_of_greens + 1
    if(is_green_present == True and is_green == False):
      is_green_present = False
  return number_of_greens >= 2

def notify(is_west_open, is_east_open):
  is_west_open = "open" if is_west_open else "close"
  is_east_open = "open" if is_east_open else "close"
  print('The east bridge is '+is_east_open)
  print('The west bridge is '+is_west_open)

westImage = getWestImage()
is_west_open = isBridgeOpen(westImage, 415, 375, 430)
eastImage = getWestImage()
is_east_open = isBridgeOpen(eastImage, 400, 370, 400)

notify(is_west_open, is_east_open)