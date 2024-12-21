import pandas as pd
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return None
def get_names_for_year(data, year):
    year_data = data[data['Year'] == year]
    if year_data.empty:
        print(f"Нет данных по именам за {year} год.")
        return None
    boys_names = year_data[year_data['Gender'] == 'boy']['Name'].tolist()
    girls_names = year_data[year_data['Gender'] == 'girl']['Name'].tolist()
    return boys_names, girls_names

def main():
    file_path = 'baby_names.csv' 
    data = load_data(file_path)
    if data is not None:
        year = int(input("Введите год для получения имен: "))
        boys_names, girls_names = get_names_for_year(data, year)
        if boys_names:
            print(f"Имена для мальчиков в {year} году: {', '.join(boys_names)}")
        else:
            print(f"В {year} году не было имен для мальчиков.")

        if girls_names:
            print(f"Имена для девочек в {year} году: {', '.join(girls_names)}")
        else:
            print(f"В {year} году не было имен для девочек.")

if __name__ == "__main__":
    main()
