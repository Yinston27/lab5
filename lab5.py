import re
import csv

# 1
with open("task1-en.txt") as task1:
    line_task1 = ''.join(task1.readlines())
    res1 = re.findall(r'\b\w*[e]\b', line_task1)
    res2 = re.findall(r'\([0-9]+\)', line_task1)
    # print(res1)
    # print(res2)


# 2
with open('task2.html', encoding='utf-8') as f:
    html = f.read()

image_sizes = re.findall(r'(?:width|height)\s*=\s*["\']?(\d+)(?:px)?["\']?', html, re.IGNORECASE)
pixel_values = re.findall(r'(\d+(?:\.\d+)?)px', html)

with open('task2_result.txt', 'w') as f:
    f.write("Размеры изображений:\n" + '\n'.join(image_sizes) + '\n\n')
    f.write("Значения в пикселях:\n" + '\n'.join(pixel_values))


# 3
with open('task3.txt') as f:
    data_items = f.read().split()
    print(data_items)

ids, surnames, emails, dates, websites = [], [], [], [], []

for item in data_items:
    if re.match(r'^\d{1,3}$', item):
        ids.append(item)
    elif re.match(r'^[A-ZА-ЯЁ][a-zа-яё-]+$', item):
        surnames.append(item)
    elif re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', item, re.IGNORECASE):
        emails.append(item)
    elif re.match(r'^\d{4}-\d{2}-\d{2}$', item):
        dates.append(item)
    elif re.match(r'^(?:https?://)?(?:www\.)?[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', item, re.IGNORECASE):
        websites.append(item)

num_records = min(map(len, [ids, surnames, emails, dates, websites]))

with open('task3_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Email', 'Дата регистрации', 'Сайт'])
    for i in range(num_records):
        writer.writerow([ids[i], surnames[i], emails[i], dates[i], websites[i]])


# 4
with open('task_add.txt') as f:
    text = f.read()

date_pattern = r'\s\d{1,2}[-./]\d{1,2}[-./]\d{2,4}|\s\d{4}[-./]\d{1,2}[-./]\d{1,2}'
dates = re.findall(date_pattern, text, re.IGNORECASE)
emails = re.findall(r'\s[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}', text)
websites = re.findall(r'\s(?:https?://)+[\w.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?', text)

with open('task_add_result.txt', 'w') as f:
    f.write("Даты:\n" + '\n'.join(d.strip() for d in dates) + '\n\n')
    f.write("Email:\n" + '\n'.join(e.strip() for e in emails) + '\n\n')
    f.write("Сайты:\n" + '\n'.join(w.strip() for w in websites))