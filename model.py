
import sem7.view as view

exp = ''



opSelect = {
    '*': lambda x, y: int(x)*int(y),
    '/': lambda x, y: (int(x)/int(y)) if int(y) !=0 else view.division_by_zero(),
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y)}


def expression_form(exp):
    exp = exp.replace(' ', '')
    exp = exp.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    list = exp.split()
    return list


