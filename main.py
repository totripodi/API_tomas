import requests
import json
import datetime

def positiveCases(response,month,year):
    totalPositive = 0
    for i in response:                                      #recorro las fechas
        caseDate = datetime.strptime(str(i['date']), '%Y%m')#llamo funcion dentro de datetime
        
        if caseDate.month == month and caseDate.year == year:
            totalPositive = totalPositive+i['positive']
            return totalPositive
    return 0

def casosposistivos():    
    year = int(input('Ingrese que año: '))
    while len(str(year)) != 4:
        year = int(input('Ingrese año valido: '))#pido los datos y valido los strings

    month = int(input('Ingrese mes: '))
    while len(str(month)) != 1 and month <= 0 and month >= 12:    
        month = int(input('Ingrese mes valido M (3): '))
    response = request()   
    totalPositivos = positiveCases(response,month,year)
    print("En el mes ",month,"de" ,year," hubieron un total de ",totalPositivos , " casos positivos")

def request():

    url = 'https://api.covidtracking.com/v1/us/daily.json'
    response=requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text) #convierto a diccionario y guardo todo el contenido en la variable
        return data

        
   





