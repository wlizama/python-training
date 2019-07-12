from PyInquirer import prompt

questions = [
    {
        'type': 'password',
        'message': 'Enter your git password',
        'name': 'password'
    }
]

answers = prompt(questions)
print(answers)