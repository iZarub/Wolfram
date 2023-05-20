import numpy as np

N = 50
KS = np.arange(1, 120, 1) # Можно добавить выбор интервала

def Simpson(k: int, func: str, llim: float, rlim: float) -> float:
    '''
    Вычисляет приближенный интеграл от введенной функции func по формуле Симпсона
    с N = 50 для одного значения k.
    '''
    x = np.linspace(llim, rlim, 2*N)
    func = lambda x: eval(func)
    f = func(x)
    return np.pi/(6*N)*(f[0] + f[-1] + 4 * sum(f[1:-1:2]) + 2 * sum(f[2:-2:2]))



def Simpson_dependence(func: str, llim: float, rlim: float) -> tuple:
    '''
    Вычисляет массив значений интеграла при наборе частот k
    '''
    return [Simpson(k, func, llim, rlim) for k in KS], KS



def real_dependence(integral: str) -> tuple:
    '''
    Получает на вход преобразованную строку, полученную Вольфрамом
    и возвращает реальную зависимость интеграла от k.
    '''
    integral = lambda k: eval(integral)
    return [integral(k) for k in KS], KS

