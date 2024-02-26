import csv

my_dict = dict()
with open('data/vacancy.csv', encoding='utf8') as csv_file:
    """Считываем данные"""
    reader = list(csv.DictReader(csv_file, delimiter=';', quotechar='"'))
    """Отбираем в компании самые высокооплачиваемые вакансии и записываем в my_dict"""
    for row in reader:
        vacancy, salary = my_dict.get(row['Company'], ('', 0))
        if int(row['\ufeffSalary']) >= int(salary):
            my_dict[row['Company']] = (row['Role'], row['\ufeffSalary'])

"""
Заполням два списка
answer для удобной записи в csv файл,
answer_2 для поиска самых опливаемых вакансий
    
"""
answer = list()
answer_2 = list()
for company, vacancy_salary in my_dict.items():
    vacancy, salary = vacancy_salary
    answer.append({'company': company, 'role': vacancy, 'Salary': salary})
    answer_2.append((company, vacancy, salary))

"""Создаём файл"""
with open('data/vacancy_new.csv', 'w', newline='', encoding='utf8') as csv_file:
    w = csv.DictWriter(csv_file, fieldnames=['company', 'role', 'Salary'])
    w.writeheader()
    w.writerows(answer)

"""Вывод три самых высокооплачиваемых вакансии"""
cnt = 0
for company, vacancy, salary in sorted(answer_2, key=lambda x: (-int(x[2]))):
    print(f'{company} - {vacancy} - {salary}')
    cnt += 1
    if cnt == 3:
        break
