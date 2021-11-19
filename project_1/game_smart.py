""" Компьютер сам загадывает и сам угадывает число"""

import numpy as np

def smart_predict(number:int=1) -> int:
    """Угадываем число за минимальное количество попыток

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: количество поппыток
    """
    count = 0 # количество попыток
    start_dia = 0 # нижняя граница диапазона в котором находится загаданное число
    end_dia = 100 # верхняя граница диапазона
    predict_number = end_dia
    while True:
        count+=1
        if predict_number > number:
            end_dia = predict_number
            width_dia = end_dia-start_dia # вычисляем ширину диапапзона
            predict_number -= round(width_dia/2, 0)
        elif predict_number < number:
            start_dia = predict_number
            width_dia = end_dia-start_dia
            predict_number += round(width_dia/2, 0)
        elif number == predict_number:
            break # выход из цикла если угадали
    return count


def score_game(smart_predict) -> int:
    """За какое количество ппопыток в среднем из 1000 подходов  наш алгоритм угадывает число

    Args:
        smart_predict ([type]): функция умного угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(smart_predict(number))
        
    score = int(np.mean(count_ls)) # среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

if __name__ == '__main':
    # RUN
    score_game(smart_predict)