from PyInquirer import prompt

questions = [
    {
        'type': 'list',
        'name': 'opciones',
        'message': 'Que deseas ?',
        'choices': [
            'Opcion 1',
            'Opcion 2',
            'Opcion 3',
            'Opcion 4',
            'Opcion 5',
            'Opcion 6'
        ]
    }
]

answers = prompt(questions)
print(answers)