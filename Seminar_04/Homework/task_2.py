print('Задача2')

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(kwargs_to_dict(name='Алексей', sername='Нестеров', weight=35.5,
                     months=['January', 'February', 'March'],
                     courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))
