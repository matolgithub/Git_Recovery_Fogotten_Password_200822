# не удалось установить модуль pywin32  на Ubuntu.
import itertools
from string import digits, punctuation, ascii_letters

# symbols = digits + punctuation + ascii_letters
# print(symbols)


def brute_excel_doc():
    print('--------Hello, friend!---------')

    try:
        password_length = input('Введите длину пароля (мин.-макс.), например, 2-5: ')
        password_length = [int(item) for item in password_length.split("-")]
    except:
        print('Проверьте введённые данные!', password_length)

    print('Введите 1\nЕсли в пароле только цифры\nВведите 2\nЕсли в пароле только буквы\nВведите 3\nЕсли в пароле '
          ' цифры и буквы\nВведите 4\nЕсли в пароле цифры, буквы и спецсимволы.')

    try:
        choice = int(input(': '))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = 'Что-то не то ввёл....'
        print(possible_symbols)
    except:
        print(possible_symbols)

    for pass_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)
            print(password)

def main():
    brute_excel_doc()


if __name__ == '__main__':
    main()
