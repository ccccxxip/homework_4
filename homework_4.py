def ping_statistics():
    # Запрашиваем у пользователя имя сервера
    server_name = input("Введите имя сервера: ")

    # Инициализация переменных
    times = []
    lost_packets = 0
    total_packets = 4

    print("Введите результаты ping (введите 'end' для завершения):")

    for _ in range(total_packets):
        response = input(f"Ответ {len(times) + lost_packets + 1}: ")
        if response.lower() == "end":
            break
        elif response == "Time out":
            lost_packets += 1
        else:
            # Извлекаем время из ответа
            parts = response.split()
            time_str = parts[-1]  # "Time=number"
            time_value = int(time_str.split('=')[1])
            times.append(time_value)

    # Подсчет статистики
    received_packets = total_packets - lost_packets
    average_time = round(sum(times) / received_packets) if received_packets > 0 else 0
    max_time = max(times) if times else 0
    min_time = min(times) if times else 0

    # Формирование и вывод результата
    print(f"nPing statistics for {server_name}:")
    print(f"Packets: Sent = {total_packets}, Received = {received_packets}, Lost = {lost_packets} ({(lost_packets / total_packets) * 100:.0f}% loss)")

    if received_packets > 0:
        print(f"Approximate round trip times:")
        print(f"Minimum = {min_time}, Maximum = {max_time}, Average = {average_time}")
    else:
        print("Approximate round trip times:")
        print("Minimum = 0, Maximum = 0, Average = 0")


# Вызов функции
ping_statistics()