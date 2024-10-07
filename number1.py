def split_list(user_list, split_index):
    list1 = user_list[:split_index]
    list2 = user_list[split_index:]
    return list1, list2

def input_list():
    while True:
        try:
            N = int(input("Введіть кількість елементів у списку: "))
            if N <= 0:
                print("Кількість елементів має бути додатним числом. Спробуйте ще раз.")
            else:
                break
        except ValueError:
            print("Помилка! Введено некоректне значення. Введіть ціле число.")

    user_list = []
    print(f"Введіть {N} елементів списку:")
    for i in range(N):
        while True:
            try:
                element = int(input(f"Елемент {i + 1}: "))
                user_list.append(element)
                break
            except ValueError:
                print("Помилка! Введено не ціле число. Спробуйте ще раз.")

    return user_list


if __name__ == "__main__":
    user_list = input_list()

    while True:
        try:
            split_index = int(input("Введіть індекс для розбиття списку (від 1 до N): ")) - 1
            if 0 < split_index < len(user_list):
                break
            else:
                print("Індекс має бути в межах списку. Спробуйте ще раз.")
        except ValueError:
            print("Помилка! Введіть ціле число.")

    list1, list2 = split_list(user_list, split_index)

    print("Перший список:", list1)
    print("Другий список:", list2)
