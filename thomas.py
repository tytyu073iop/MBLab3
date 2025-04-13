def thomas(a, b, c, d):
    """
    Решает трехдиагональную систему уравнений методом прогонки (Томаса).
    
    Параметры:
    a (list): Нижняя диагональ (a[0] не используется)
    b (list): Главная диагональ
    c (list): Верхняя диагональ (c[-1] не используется)
    d (list): Вектор правой части
    
    Возвращает:
    list: Вектор решения x
    """
    n = len(b)
    c_prime = [0] * n
    d_prime = [0] * n
    x = [0] * n
    
    # Прямой ход
    c_prime[0] = -c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    
    for i in range(1, n):
        denominator = b[i] + a[i] * c_prime[i-1]
        d_prime[i] = (d[i] - a[i] * d_prime[i-1]) / denominator
        if i != n-1:
            c_prime[i] = - c[i] / denominator
    
    # Обратный ход
    x[-1] = d_prime[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] + c_prime[i] * x[i+1]
    
    return x

# Пример использования
if __name__ == "__main__":
    # Пример системы:
    # 2x +  y     = 5
    # 3x +4y + z  = 6
    #    2y +5z   = 7
    a = [0, 3, 2]    # a[0] не используется
    b = [2, 4, 5]    # Главная диагональ
    c = [1, 1, 0]    # c[-1] не используется
    d = [5, 6, 7]    # Правая часть
    
    solution = thomas(a, b, c, d)
    print("Решение:", [round(x, 5) for x in solution])
    # Ожидаемый результат: [3.19048, -1.38095, 1.95238]