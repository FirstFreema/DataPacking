import pickle

class CountryState:
    def __init__(self):
        self.data = {}

    def add_country_capital(self, country, capital):
        self.data[country] = capital

    def remove_country_capital(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"Страна '{country}' не найдена.")

    def get_capital_by_country(self, country):
        if country in self.data:
            return self.data[country]
        else:
            print(f"Cтрана '{country}' не найдена.")
            return None

    def get_country_by_capital(self, capital):
        for country, cap in self.data.items():
            if cap == capital:
                return country
        print(f"Столица '{capital}' не найдена.")
        return None

    def update_capital(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"Страна '{country}' не найдена.")

    def save_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")




# Проверка
country_state = CountryState()

country_state.add_country_capital('Russia', 'Moscow')
country_state.add_country_capital('USA', 'Washington, D.C.')
country_state.add_country_capital('Japan', 'Tokyo')
country_state.add_country_capital('Kazakhstan', 'Astana')

print(country_state.get_capital_by_country('Russia'))
print(country_state.get_capital_by_country('Canada'))

print(country_state.get_country_by_capital('Tokyo'))
print(country_state.get_country_by_capital('Berlin'))

country_state.update_capital('Kazakhstan', 'Nur-Sultan')
print(country_state.get_capital_by_country('Kazakhstan'))

country_state.save_data('country_state.pickle')

country_state.load_data('country_state.pickle')
