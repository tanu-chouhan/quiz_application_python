# Tanu Chouhan 2024
# Quiz Application

from random import shuffle

questions:list[dict[str,str]] = [
    {
        'question':'Who created programming language Python?',
        'choices': {
            'a':'James Goseling',
            'b':'Bjare Strostrup',
            'c':'Guido Von Rossum',
            'd':'Branden Eich'
        },
        'correct choice':'c'
    },
    {
        'question':'When python was created?',
        'choices': {
            'a':'1991',
            'b':'1995',
            'c':'2000',
            'd':'2007'
        },
        'correct choice':'a'
    },
    {
        'question':'Which type of programming does python support?',
        'choices': {
            'a':'object-oriented programming',
            'b':'structural programming',
            'c':'functional programming',
            'd':'all of above'
        },
        'correct choice':'d'
    },
    {
        'question':'Correct extension of python file is?',
        'choices': {
            'a':'.python',
            'b':'.py',
            'c':'.p',
            'd':'.pf'
        },
        'correct choice':'b'
    },
    {
        'question':'What type of language python is?',
        'choices': {
            'a':'compiled',
            'b':'assembly',
            'c':'interpreted',
            'd':'none'
        },
        'correct choice':'c'
    },
]
shuffle(questions)
    

if __name__ == '__main__':
    score:int = 0
    print('==============================================================')
    for index, question in enumerate(questions, start=1):
        print(f'{index}. {question['question']}')
        for choice in question.get('choices'):
            print(f'{choice}) {question['choices'][choice]}')
        print()
        input_choice = input('select an option (a/b/c/d): ')[0]
        if input_choice == question.get('correct choice'):
            print('Correct :-)')
            score+=1
        else:
            print('Incorrect :-(')
            print(f'correct option is: {question.get('correct choice')}')
        print('==============================================================')
    print(f'Your score: {score}')
    print(f'Total: {len(questions)}')
