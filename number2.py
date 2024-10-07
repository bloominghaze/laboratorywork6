def find_longest_word(words_list):
    longest_word = max(words_list, key=len)
    return longest_word

def input_words_list():
    while True:
        try:
            N = int(input("Введіть кількість слів у списку: "))
            if N <= 0:
                print("Кількість слів має бути додатним числом. Спробуйте ще раз.")
            else:
                break
        except ValueError:
            print("Помилка! Введено некоректне значення. Введіть ціле число.")

    words_list = []
    print(f"Введіть {N} слів:")
    for i in range(N):
        word = input(f"Слово {i + 1}: ")
        words_list.append(word)

    return words_list

if __name__ == "__main__":
    words_list = input_words_list()

    longest_word = find_longest_word(words_list)

    print("Найдовше слово в списку:", longest_word)
