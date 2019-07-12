from PyInquirer import prompt

questions = [
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    },
    {
        'type': 'confirm',
        'message': 'Do you want to exit?',
        'name': 'exit',
        'default': False,
    },
]

answers = prompt(questions)
print(answers)