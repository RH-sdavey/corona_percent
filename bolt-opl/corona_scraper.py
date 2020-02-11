import requests
from bs4 import BeautifulSoup
import shutil

shutil.copy('indexBACKUP.html', 'index.html')


URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
data = page.content
soup = BeautifulSoup(data, 'html.parser')

# approx total world population
world_pop = 8000000000

# get total number of cases
maincounter = soup.find('div', attrs={'class', 'maincounter-number'})
total_cases = str(maincounter.findChild('span').contents[0])
total_cases =  int(total_cases.replace(',', ''))

# do the math
percent_infected = (total_cases / world_pop) * 100



with open('index.html', 'r') as file:
    filedata = file.read()



filedata = filedata.replace('POPHERE', str(world_pop))
filedata = filedata.replace('INFECTHERE', str(total_cases))
filedata = filedata.replace('PERCENTHERE', str(percent_infected))

with open('index.html', 'w') as file:
    file.write(filedata)
