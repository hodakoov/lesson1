# Комплексные типы данных: словари

d = {"city": "Москва", "temperature": "20"}
print(d['city'])
d['temperature'] = int(d['temperature']) - 5
print(d)

print(d.get('country', 'Россия'))
d['date'] = "27.05.2019"
print(len(d))