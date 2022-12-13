import requests
res = requests.get('https://api.covidtracking.com')
print("api.covidtracking.com: ")
print(f'Статус кода: {res.status_code}')
KEY = '7640e08088885cc268147fbd5165ff9e' # ключ для API с сайта Openweather
print()
print("OpenWeather")
def weather():
    try:
        city_name = input("City name: ")
        res_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}')
        response = res_weather.json()
        print(f'Погода: {response["weather"][0]["main"]}')
        Gradus = round(response["main"]["temp"] - 273)
        Pressure = response["main"]["pressure"]//1.33
        print(f'Страна: {response["sys"]["country"]}')
        print(f'Температура: {Gradus}°')
        print(f'Влажность: {response["main"]["humidity"]}%')
        print(f'Давление: {Pressure} мм рт.ст')
    except KeyError:
        print("Такого города не существует, либо введите город корректно")

weather()
print()
print("Covidtracking")
def covid():
    try:
        daily = input(f'Введите дату, год, месяц, день: ')
        res_cov = requests.get(f'https://api.covidtracking.com/v1/us/{daily}.json')
        response_cov = res_cov.json()
        print(f'Количество новых больных в эту дату: {response_cov["hospitalizedIncrease"]}')
        print(f'Количество смертей в эту дату: {response_cov["deathIncrease"]}')
        print(f'Количество смертей за все время на эту дату: {response_cov["death"]}')
        print(f'Количество заболевших за все время на эту дату: {response_cov["hospitalized"]}')
        print(f'Количество тестов в ожидании на эту дату: {response_cov["pending"]}')
    except KeyError:
        print("К сожалению, выбранная вами дата неверная или на эту дату нет данных, попробуйте другую")

covid()