def digital_root(n):
    """Функция для вычисления цифрового корня числа."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


def is_lucky_ticket(ticket_number):
    """Функция для проверки, является ли билет счастливым."""
    length = len(ticket_number)

    # Проверяем все возможные разрезы
    for i in range(1, length):
        left_part = ticket_number[:i]
        right_part = ticket_number[i:]

        # Вычисляем цифровые корни
        left_root = digital_root(sum(int(digit) for digit in left_part))
        right_root = digital_root(sum(int(digit) for digit in right_part))

        if left_root == right_root:
            return "YES"

    return "NO"


# Ввод номера билета
ticket_number = input("Введите номер билета: ")
result = is_lucky_ticket(ticket_number)
print(result)
