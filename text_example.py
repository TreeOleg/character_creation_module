from math import sqrt

message = (
    'Добро пожаловать в самую лучшую '
    'программу для вычисления '
    'квадратного корня из заданного числа'
)


def сalculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Поверяет заданное число и вычисляет квадратный корень."""
    if your_number <= 0:
        return
    result = сalculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из '
          f'введённого вами числа. Это будет: '
          f'{result}')


print(message)
calc(25.5)
