import csv

with open('data/vacancy.csv', encoding='utf8') as csv_file:
    """Считываем данные"""
    reader = list(csv.DictReader(csv_file, delimiter=';', quotechar='"'))
    """Получаем запрос"""
    st = input()
    while st != 'None':
        """
        Проводим линейный поиск.
        Т.е. проходимся по всем данным в поиске компании.
        Если ничего не находим - сообщаем об этом
        
        """
        for row in reader:
            if row['Company'] == st:
                vacancy, salary = row['Role'], row["\ufeffSalary"]
                print(f'В {st} найдена вакансия: {vacancy}. З/п составит: {salary}')
                break
        else:
            print('К сожалению, ничего не удалось найти')
        st = input()  # Получаем новый запрос
