numb_1 = input('Ввелите первое число')
user_apperand = input('Введите знак')
numb_2 = input('Введите второе число')

try:
            numb_1 = int(numb_1)
            numb_2 = int(numb_2)

            number_result = 0
            if user_apperand == '+':
                number_result = numb_1 + numb_2
                print(number_result)
            if user_apperand == '-':
                number_result = numb_1 - numb_2
                print(number_result)
            if user_apperand == '*':
                number_result = numb_1 * numb_2
                print(number_result)
            if user_apperand == '/':
                number_result = numb_1 / numb_2
                print(number_result)
            if user_apperand == '//':
                number_result = numb_1 // numb_2
                print(number_result)
            if user_apperand == '%':
                number_result = numb_1 % numb_2
                print(number_result)
            if user_apperand == '**':
                number_result = numb_1 ** numb_2
                print(number_result)
except ZeroDivisionError:
    print('На нуль делить нельзя')
except OverflowError:
    print('Слишком большое число')
except TypeError:
    print('Вы ввели строку!')

