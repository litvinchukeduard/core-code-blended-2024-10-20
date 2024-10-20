from typing import Any
'''
В нас є файл, в якому є числа

1 32 15 30 5 4 6 3 25 100 200 300

Написати код, який буде читати ці числа та оцінювати їх

Якщо число ділиться на 3 без остачі, замінити число на Fizz
Якщо число ділиться на 5 без остачі, замінити число на Buzz
Якщо число ділиться на 3 та 5 без остачі, замінити його на FizzBuzz

В ншому випадку не змінювати число

Записати числа та слова у новий файл

1 32 FizzBuzz FizzBuzz Buzz 4 Fizz Fizz Buzz Buzz Buzz FizzBuzz
'''

# 5 / 2 => 2 і 1 в залишку

number_list = [1, 32, 15, 30, 5, 4, 6, 3, 25, 100, 200, 300, 0]

def read_numbers_from_file(path: str) -> list[str]:
    with open(path, 'r') as file:
        for line in file:
            return line.split(' ')
        
def convert_strings_to_numbers(number_string_list: list[str]) -> list[int]:
    result = []
    for number_string in number_string_list:
        result.append(int(number_string))
    return result

def write_numbers_to_file(path: str, string_list: list[Any]):
    with open(path, 'w') as file:
        for string_value in string_list:
            file.write(f'{str(string_value)} ')

def convert_to_fizz_buzz(number_list: list[int]) -> list[int]:
    result = []
    for number in number_list:
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(number)
    return result


number_strings = read_numbers_from_file('example.txt')
number_numbers = convert_strings_to_numbers(number_strings)

print(number_numbers)

fizz_buzz_numbers = convert_to_fizz_buzz(number_numbers)

print(fizz_buzz_numbers)

write_numbers_to_file('out.txt', fizz_buzz_numbers)
