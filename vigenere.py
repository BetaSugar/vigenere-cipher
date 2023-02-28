# алфавитный словарь
def eng_dict_chars():
    return {i: k for i, k in enumerate('abcdefghijklmnopqrstuvwxyz')}


# конвертирует все буквы в номера по алфавиту
def encode_str(text: str):
    d = eng_dict_chars()
    return [k for c in text for k, v in d.items() if v == c]


# циклирует ключ до длинны текста
def key_cycle(text: str, key: str):
    while (len(text) > len(key)):
        key += key
    while (len(text) < len(key)):
        key = key[:-1]
    return key


# форматирование текста под шифрование
def formating_text(text: str):
    f_text = ''
    d = eng_dict_chars()
    text = text.lower()
    for i in text:
        if i in d.values():
            f_text += i
    return f_text


# шифрование
def encryption(text: list, key: list):
    cipher = []
    d = eng_dict_chars()
    for v in range(len(text)):
        cipher.append((text[v]+key[v]) % len(d))
    return ''.join(map(str, [d[i] for i in cipher]))


if __name__ == "__main__":

    with open('text.txt', 'r', encoding='utf-8-sig') as f:
        text = f.read()

    key = str(input('Введите ключ для шифрования: '))

    text = encryption(encode_str(formating_text(text)),
                      encode_str(key_cycle(text, key)))

    with open('ciphertext.txt', 'w', encoding='utf-8-sig') as w:
        w.write(text)

    print('Done!')
