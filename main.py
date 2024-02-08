"""
Створіть клас "Місто".
Необхідно зберігати в полях класу:
назву міста,
назву регіону,
назву країни,
кількість жителів міста,
поштовий індекс міста, телефонний код міста.
Реалізуйте доступ до окремих полів (Інкапсуляція).
"""


class City:
    __name = "None"
    __region = "None"
    __country = "None"
    __population = 0
    __post_code = 0

    def __init__(self, name, region, country, population, post_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.post_code = post_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_city):
        if 1 <= len(name_city) <= 20:
            self.__name = name_city
        else:
            print('Invalid city name.')

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region_city):
        if 1 <= len(region_city) <= 20:
            self.__region = region_city
        else:
            print('Invalid region name.')

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country_city):
        if 1 <= len(country_city) <= 10:
            self.__country = country_city
        else:
            print('Invalid country name')

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population_city):
        if 1 <= population_city <= 3000000:
            self.__population = population_city
        else:
            print('Invalid population of city.')

    @property
    def post_code(self):
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code_city):
        if 5 <= len(str(post_code_city)) <= 8:
            self.__post_code = post_code_city
        else:
            print('Invalid post code of city.')

    def show_info(self):
        print(
            f'City: {self.__name}, Region: {self.__region}, Country: {self.__country}, Population: {self.__population}, post code: {self.__post_code}')


Odessa = City('Odessa', 'Odessa', 'Ukraine', 1000000, 65000)
Odessa.show_info()

Nothing = City('', '', '', -20, -3)
Nothing.show_info()

"""
Створіть клас "Країна". 
Необхідно зберігати в полях класу: 
назву країни, 
назву континенту, 
кількість жителів країни, 
телефонний код країни, 
назву столиці, 
назву міст країни. 
Реалізуйте доступ до окремих полів (Інкапсуляція).
"""


class Country:
    __name = "None"
    __continent = "None"
    __population = 0
    __code = 0
    __capital = "None"
    __cities = []

    def __init__(self, name, continent, population, code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.code = code
        self.capital = capital
        self.cities = cities

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, country_name):
        if 1 <= len(country_name) <= 10:
            self.__name = country_name
        else:
            print('Invalid country name')

    @property
    def continent(self):
        return self.__continent

    @continent.setter
    def continent(self, country_continent):
        if 1 <= len(country_continent) <= 15:
            self.__continent = country_continent
        else:
            print('Invalid country continent')

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, country_population):
        if 1 <= country_population <= 100000000:
            self.__population = country_population
        else:
            print('Invalid country population')

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, country_code):
        if 1 <= len(str(country_code)) <= 3:
            self.__code = country_code
        else:
            print('Invalid country code.')

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, country_capital):
        if 1 <= len(country_capital) <= 15:
            self.__capital = country_capital
        else:
            print('Invalid country capital')

    @property
    def cities(self):
        return self.__cities

    @cities.setter
    def cities(self, country_cities):
        if 2 <= len(country_cities) <= 1000:
            self.__cities = country_cities
        else:
            print('Invalid country cities')

    def show_info(self):
        print(
            f'Country: {self.__name}, Continent: {self.__continent}, Population: {self.__population}, Code: +{self.__code}, Capital: {self.__capital}, Cities: {self.__cities}')


Ukraine = Country('Ukraine', 'Europe', 40000000, 380, 'Kyiv', ['Odessa', 'Izmail'])
Ukraine.show_info()
