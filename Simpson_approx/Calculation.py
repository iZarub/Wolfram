import numpy as np
import math

N = 50
KS = np.arange(1, 120, 1) # Можно добавить выбор интервала

def check_for_pi(str: str) -> float:
    '''
    Самая тупая реализация перевода строки в число для пределов,
    можно сделать намного лучше, но это уже не надо
    '''
    str = str.replace("pi", "3.14")

    return float(str)


def Simpson(k: int, func_str: str, llim: str, rlim: str) -> float:
    '''
    Вычисляет приближенный интеграл от введенной функции func по формуле Симпсона
    с N = 50 для одного значения k.
    '''

    func_str = func_str.replace("k", f"{k}")

    llim = check_for_pi(llim)
    rlim = check_for_pi(rlim)
    x = np.linspace(llim, rlim, 2*N)
    func = lambda x: eval(func_str)

    f = []
    for val in x:
        f.append(func(val))

    return np.pi/(6*N)*(f[0] + f[-1] + 4 * sum(f[1:-1:2]) + 2 * sum(f[2:-2:2]))



def Simpson_dependence(func: str, llim: str, rlim: str) -> tuple:
    '''
    Вычисляет массив значений интеграла при наборе частот k
    '''

    return [Simpson(k, func, llim, rlim) for k in KS], KS



def real_dependence(integral_str: str) -> tuple:
    '''
    Получает на вход преобразованную строку, полученную Вольфрамом
    и возвращает реальную зависимость интеграла от k.
    '''

    print(integral_str)
    integral = lambda k: eval(integral_str)
    return [integral(k) for k in KS], KS
