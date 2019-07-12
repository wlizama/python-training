from PyInquirer import prompt

questions = [
    {
        'type': 'rawlist',
        'name': 'theme',
        'message': 'What do you want to do?',
        'choices': [
            'Order a pizza',
            'Make a reservation',
            'Ask opening hours',
            'Talk to the receptionist'
        ]
    },
    {
        'type': 'rawlist',
        'name': 'size',
        'message': 'What size do you need',
        'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
        'filter': lambda val: val.lower()
    }
]

answers = prompt(questions)
print(answers)