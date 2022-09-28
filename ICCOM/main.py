import requests
import json
import datetime

def positiveCases(response,month,year):
    totalPositive = 0
    for i in response:
        caseDate = datetime.strptime(str(i['date']), '%Y%m')
        
        if caseDate.month == month and caseDate.year == year:
            totalPositive = totalPositive+i['positive']
            return totalPositive
year = int(input('Ingrese que año: '))
while len(str(year)) != 4:
        year = int(input('Ingrese año valido: '))   #pido los datos y valido los strings

month = int(input('Ingrese mes: '))
while len(str(month)) != 1 and month <= 0 and month >= 12:    
    month = int(input('Ingrese mes valido M (3): '))
response = requests()   
totalPositivos = positiveCases(response,month,year)
print("En el mes ",month,"de" ,year," hubieron un total de ",totalPositivos , " casos positivos")

def requests():

    url = 'https://api.covidtracking.com/v1/us/daily.json'
    response=requests.__get__(url)
    if response.status_code == 200:
        data = json.loads(response.text) #convierto a diccionario y guardo todo el contenido en la variable
        

        
    return 0





