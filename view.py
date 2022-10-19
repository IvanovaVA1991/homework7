import sem7.model as model
import sem7.controller as controller

def division_by_zero():
    print('деление на ноль!')
    exit()

def printResult():
    print(f'{model.exp} = {controller.result}')