# to run from command line:
# $ python ./Lessons/firstprog.py
print('\n\nhello world')


print('\n\nReserved words in python:')
reserved_words = [
    ['False', 'class', 'return', 'is', 'finally'],
    ['None', 'if', 'for', 'lambda', 'continue'],
    ['True', 'def', 'from', 'while', 'nonlocal'],
    ['and', 'del', 'global', 'not', 'with'],
    ['as', 'elif', 'try', 'or', 'yield'],
    ['assert', 'else', 'import', 'pass',''],
    ['break', 'except', 'in', 'raise',''],
]

for row in reserved_words:
    print("{: >20} {: >20}{: >20}{: >20} {: >20}".format(*row))