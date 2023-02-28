# Колобов Д. ИБ-301
# алфавитный словарь
def eng_dict_chars():
    return {i: k for i, k in enumerate('abcdefghijklmnopqrstuvwxyz')}


# индекс совпадений
def match_index(text: str):
    index = 0
    d = eng_dict_chars()
    for i in d:
        index += (text.count(d[i])/len(text))**2
    return index


# взаимный индекс совпадений
def mutual_match_index(text1: str, text2: str):
    index = 0
    d = eng_dict_chars()
    for i in d:
        index += (text1.count(d[i])/(len(text1))) * \
            (text2.count(d[i])/(len(text2)))
    return index


# разбивание текста на i столбов, где i - длинна ключа
def columns(text: str, len_password: int):
    d = {i: '' for i in range(len_password)}
    for i, k in enumerate(text):
        d[i % len_password] += k
    return d


# сдвиг текста на i символов вправо
def shift_r(text: str, len_shift: int):
    d = eng_dict_chars()
    text = [k for c in text for k, v in d.items() if v == c]
    for i in range(len(text)):
        text[i] += len_shift
        if text[i] > 25:
            text[i] -= 26
    return ''.join(map(str, [d[i] for i in text if i in d]))


# сдвиг текста на i символов влево
def shift_l(text: str, len_shift: int):
    d = eng_dict_chars()
    text = [k for c in text for k, v in d.items() if v == c]
    for i in range(len(text)):
        text[i] -= len_shift
        if text[i] < 0:
            text[i] += 26
    return ''.join(map(str, [d[i] for i in text if i in d]))


# расшифровка
def decoding(cipher: list, key: list):
    text = []
    d = eng_dict_chars()
    for v in range(len(cipher)):
        text.append((text[v]-key[v]) % len(d))
    return ''.join(map(str, [d[i] for i in text]))


if __name__ == "__main__":

    with open('ciphertext.txt', 'r', encoding='utf-8-sig') as f:
        text = f.read()

     # поиск длинны ключа
    possible_key_length = int(
        input('Введите максимальную предполагаюмую длину ключа: '))+2
    print('Длина ключа --> индекс совпадений')
    for i in range(1, possible_key_length + 1):
        print(f'{i: <2} --> ' + str(match_index(columns(text, i)[0]))[:6])

    key_length = int(input(
        'Введите длину ключу (опирайтесь на индекс, максимально близкий к 0.065): '))
    print('\n\n\n')

    # поиск сдвигов относительной первого стобца
    shift_list = []
    for sym in range(key_length):
        print(
            f'Номер символа --> индекс совпадений. Прогресс [{sym}/{key_length-1}]')
        for i in range(len(eng_dict_chars())):
            print(f'{i: <2} --> ' + str(mutual_match_index(columns(text, key_length)[0],
                                                           shift_r(columns(text, key_length)[sym], i)))[:6])
        shift_list.append(int(input(
            'Введите номер символа (опирайтесь на индекс, максимально близкий к 0.065): ')))
    print(shift_list)

    # уравнивание сдвига всех столбцов к первому столбцу
    exp_list = list(text)
    for i, sym in enumerate(text):
        exp_list[i] = shift_r(sym, shift_list[i % key_length])
    text = ''.join(exp_list)

    # поиск последнего контрольного сдвига
    for i in range(len(eng_dict_chars())):
        text = shift_r(text, 1)

        print(f'Превью расшифрованого текста:\n{text[:100]}')
        if str(input('Сохранить? [д/н] ')) == 'д':
            break

    # сохранение открытого текста
    with open('text.txt', 'w', encoding='utf-8-sig') as w:
        w.write(text)
    print('Done!')
