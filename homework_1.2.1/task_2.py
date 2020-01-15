countries_temperature = [
 ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
 ['Germany', [57.2, 55.4, 59, 59, 53.6, 55.4, 57.2]],
 ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
 ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4, 51.8]],
]

NAME_INDEX = 0
TEMPERATURE_LIST_INDEX = 1


def is_temperature_data_valid(country_week_temperature):
    return country_week_temperature is not None and len(country_week_temperature) > 0


def get_average_fahrenheit(country_week_temperature):
    return sum(country_week_temperature) / len(country_week_temperature)


def fahrenheit_to_celsius(fahrenheit_value):
    return (fahrenheit_value - 32) / 1.8


def show_average_temperature(country_name, average_celsius):
    print(f'{country_name} : {round(average_celsius, 2)}')


def is_initial_data_valid(countries_temperature):
    if countries_temperature is None or len(countries_temperature) == 0:
        return False

    for country_temperature in countries_temperature:
        if countries_temperature is None or len(country_temperature) < 2:
            return False

        if (country_temperature[NAME_INDEX] is None
                or country_temperature[TEMPERATURE_LIST_INDEX] is None):
            return False

    return True


def main():
    week_temperature = None
    average_fahrenheit = None
    average_celsius = None

    if is_initial_data_valid(countries_temperature):

        for country_week_temperature in countries_temperature:
            week_temperature = country_week_temperature[TEMPERATURE_LIST_INDEX]

            if is_temperature_data_valid(week_temperature):
                average_fahrenheit = get_average_fahrenheit(week_temperature)
                average_celsius = fahrenheit_to_celsius(average_fahrenheit)

                show_average_temperature(country_week_temperature[NAME_INDEX], average_celsius)


main()
