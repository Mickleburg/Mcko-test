import csv

my_dict = dict()  # в my_dict по ключу(компании) будут храниться вакансии
with open('data/vacancy.csv', encoding='utf8') as csv_file:
    """Считываем данные"""
    reader = list(csv.DictReader(csv_file, delimiter=';', quotechar='"'))
    """Заполняем my_dict"""
    for row in reader:
        sp = my_dict.get(row['Company'], list())
        sp.append((row['Role'], row['\ufeffSalary'], row['Work_Type']))
        my_dict[row['Company']] = sp

"""Ищем компанию с максимальным кол-вом вакансий"""
max_company = ''
max_k = 0
for company, sp in my_dict.items():
    if len(sp) > max_k:
        max_k = len(sp)
        max_company = company
print(max_company)
