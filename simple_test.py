# Задача:
# Дан массив натуральных чисел, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
# [3781, 3902, 2850, 7121, 8090] (3781, 19)

def sort_method(sample):
    """
    метод сортировки элементов массива для решения задачи
    """
    if not sample:
        raise TypeError('Пусто на входе')
    biggest_number = 0
    key = 0
    for counter, value in enumerate(sample):
        if value == 0:
            raise ValueError('На входе не натуральное число : 0')
        summa = 0
        for digit in str(value):
            try:
                summa += int(digit)
            except ValueError as e:
                raise ValueError('На входе не натуральное число : ' + str(e))
        if biggest_number <= summa:
            biggest_number = summa
            key = counter
    return sample[key], biggest_number


if '__name__' != '__main__':

    positive_test_table = {
        (3781, 3902, 2850, 7121, 8090): (3781, 19),
        (3781, 3781, 3902, 2850, 7121, 8090): (3781, 19),
        (3781, 3781, 3955502, 2850, 7121, 8090): (3955502, 29),
        (3781, 3781, 3902, 2850, 7121, 8090999): (8090999, 44),
    }

    negative_test_cases = [
        [],
        [3, 0o_5, 2850, 7121, 0, 100000],
        [-3781, 3902, -2850, 7121, -8090],
        [3781, 4, 2850, 'error', 8090],
        [378.1, 390.2, 2850, 7121, 8090],
    ]

    print('ДАНО:\tМассив из НАТУРАЛЬНЫХ чисел.\n'
          'ЗАДАЧА:\n'
          '\t- Найти элемент массива с наибольшим числом по сумме его цифр\n'
          '\t- Вывести на экран этот элемент и сумму его цифр.\n'
          'ПРИМЕР:\n\t- массив: 3781 3902 2850 7121 8090\n\t- ответ: 3781 19')
    print(f'\nПозитивные тесты:\n\tВСЕГО: {len(positive_test_table)} шт.')
    tests = 0
    for item in positive_test_table:
        print('Тестмассив:', *item, ' Результат: ', *sort_method(item))
        assert sort_method(item) == positive_test_table[item], 'ошибка в данных тестового примера - ' \
                                                               'перепроверьте ожидаемое значение'
        tests += 1
        print(f'\tТест {tests} выполнен - OK')

    print(f'\nНегативные тесты:\n\tВСЕГО: {len(negative_test_cases)} шт.')
    for item in negative_test_cases:
        try:
            assert sort_method(item), "Что-то пошло совсем не так: приоритет 1"
        except TypeError as e:
            assert str(e) == "Пусто на входе", "Что-то пошло не так: приоритет 2"
            print('Тестмассив:', *item, ' Результат: ', str(e))
        except ValueError as e:
            assert "На входе не натуральное число" in str(e), "Что-то пошло не так: приоритет 3"
            print('Тестмассив:', *item, ' Результат: ', str(e))
        finally:
            tests += 1
            print(f'\tТест {tests} выполнен OK')

    print(f'ВСЕГО выполнено тестов: {tests}')
