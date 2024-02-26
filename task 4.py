import csv

sum_salary, cnt_work_type = dict(), dict()
answer = list()
with open('data/vacancy.csv', encoding='utf8') as csv_file:
    """Считываем данные"""
    reader = list(csv.DictReader(csv_file, delimiter=';', quotechar='"'))
    """Считаем сумму и количество зарплат по типу работы"""
    for row in reader:
        sum_salary[row['Work_Type']] = sum_salary.get(row['Work_Type'], 0) + int(row['\ufeffSalary'])
        cnt_work_type[row['Work_Type']] = cnt_work_type.get(row['Work_Type'], 0) + 1

    for row in reader:
        work_type = row['Work_Type']
        """Считаем процент"""
        perc = ((int(row['\ufeffSalary']) * cnt_work_type[work_type]) / sum_salary[work_type]) * 100
        """Из-за неправильного чтения csv файла перезаписываем все данные"""
        new_row = dict()
        new_row['Salary'] = row['\ufeffSalary']
        new_row['Work_Type'] = row['Work_Type']
        new_row['Company_Size'] = row['Company_Size']
        new_row['Role'] = row['Role']
        new_row['Company'] = row['Company']
        new_row['percent'] = str(perc)
        answer.append(new_row)

"""СОздаём новый файл с процентами"""
with open('data/vacancy_procent.csv', 'w', newline='', encoding='utf8') as csv_file:
    w = csv.DictWriter(csv_file, fieldnames=['Salary', 'Work_Type', 'Company_Size', 'Role', 'Company', 'percent'])
    w.writeheader()
    w.writerows(answer)
