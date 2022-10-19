import model
import controller

def division_by_zero():
    print('деление на ноль!')
    exit()

def printResult():
    print(f'{model.exp} = {controller.result}')