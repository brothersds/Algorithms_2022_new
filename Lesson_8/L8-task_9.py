"""
Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""

import heapq
from collections import Counter
from collections import namedtuple


class Node (namedtuple("Node", ["left", "right"])):
    """Класс узлов"""
    def step(self, code_n, acc):
        """
        Функция формирования структуры (узлов)
        """
        self.left.step(code_n, acc + "0")
        self.right.step(code_n, acc + "1")


class Leaflet (namedtuple("Leaflet", ["symbol"])):
    """Класс листьев дерева, в них хранятся значения"""
    def step(self, code_l, acc):
        """
        Первоначальная информация для формирования узлов содержится в листиках
        :param code_l:
        :param acc: количество шагов
        """
        code_l[self.symbol] = acc or "0"


def func_code(line):
    """
    Функция кодирования
    :param line: вводимая строка
    :return: словарь элементов с кодами + кодированную строку
    """
    head = []
    for char, freq in Counter(line).items():
        head.append((freq, len(head), Leaflet(char)))  # формирование структуры листиков
    heapq.heapify(head)  # формирование двоичного дерева (кучи)
    counter = len(head)
    while len(head) > 1:
        freq1, _counter1, left = heapq.heappop(head)
        freq2, _counter2, right = heapq.heappop(head)
        heapq.heappush(head, (freq1 + freq2, counter, Node(left, right)))
        counter += 1
    dic_code = {}
    if head:
        [(freq, _count, root)] = head
        root.step(dic_code, "")
    return dic_code, "".join(dic_code[char] for char in string)


def func_decode(encode_in, code_in):
    """
    Функция раскодирования по словарю
    :param encode_in: кодирование фраза в коде Хаффмана
    :param code_in: словарь
    :return: раскодированная строка
    """
    decode_line = []
    encode_char = ''
    for ch_in in encode_in:
        encode_char += ch_in
        for key in code_in:
            if code_in.get(key) == encode_char:
                decode_line.append(key)
                encode_char = ''
                break
    return "".join(decode_line)


if __name__ == '__main__':
    string = input('Введите строку:\n')
    code, encode = func_code(string)
    print(f'Строка в коде Хаффмана\n {encode}\n')
    print('Обратное преобразование')
    print(func_decode(encode, code))
    print('Словарь по этой фразе:')
    for ch in sorted(code):
        print(f'{ch} : {code[ch]}')

'''
Введите строку:
Привет всем животным мира
Строка в коде Хаффмана
 11100101100101011001101011010111011100100011111100010101111111010000000110001110000110111010

Обратное преобразование
Привет всем животным мира
Словарь по этой фразе:
  : 011
П : 11100
а : 1010
в : 010
е : 1100
ж : 11110
и : 001
м : 100
н : 0000
о : 11111
р : 1011
с : 11101
т : 1101
ы : 0001
'''