import model 
import view

result = 0

def operation(list, i, oper):
    if list[i] == oper:          #если элемент является оператором
        list[i-1] = model.opSelect.get(oper)(int(list[i-1]), int(list[i+1]))  # обращаемся к словарю из операций в model, проводим операцию
        list.pop(i)   #удаляем i элемент 2 раза
        list.pop(i)
        return True     # возвращаем true, чтобы в calculate сработал break и заново идти в нем по строке
    return False


def calculate(list: list):
    global result
    while len(list)>1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operation(list, i, '*'): break   #когда нашел *, передает список, позицию до * и саму *, идет в operation
                if operation(list, i, '/'): break
        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operation(list, i, '+'): break
                if operation(list, i, '-'): break
    result = list[0]
    view.printResult()
    return list

