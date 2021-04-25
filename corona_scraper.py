import requests
from bs4 import BeautifulSoup
import shutil
from datetime import date

shutil.copy('indexBACKUP.html', 'index.html')

# get total world population
# URL = 'https://worldpopulationhistory.org/map/2020/mercator/1/0/25/'
# page = requests.get(URL)
# data = page.content
# soup = BeautifulSoup(data, 'html.parser')
# world_population = soup.find_all('strong', attrs={'id', 'total-pop'})
# world_population = world_population[0].contents[6]
world_population = 7_778_810_523

# get total number of cases
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')
main_counter = soup.find('div', attrs={'class', 'maincounter-number'})
total_cases = str(main_counter.findChild('span').contents[0])
total_cases = int(total_cases.replace(',', ''))

# do the math
percent_infected = round(((total_cases / world_population) * 100), 9)

with open('index.html', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('POPHERE', str(world_population))
filedata = filedata.replace('INFECTHERE', str(total_cases))
filedata = filedata.replace('PERCENTHERE', str(percent_infected))

with open('index.html', 'w') as file:
    file.write(filedata)


# update the guthub README if its a new day

d2 = '12/02/2020'  # the day I created this section
today = date.today()
d1 = today.strftime("%d/%m/%Y")

with open('README.md', 'r') as ghrm:
    ghrmd = ghrm.read()
    if d1 in ghrmd:
        print("same day, do nothing")
    else:
        ghrmd = ghrmd.replace('GHRM', d1 + f" : {percent_infected} % \n\nGHRM")
        print("changed to " + d1)
        with open('README.md', 'w') as ghrm:
            ghrm.write(ghrmd)



