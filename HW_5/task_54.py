# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('rle.txt', 'r') as data:
    my_text = data.read()


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


encoded_text = rle_encode(my_text)
print(my_text)
print(encoded_text)

with open('rle_encoded.txt', 'w') as data2:
    data2.write(encoded_text)


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


decoded_text = rle_decode(encoded_text)
print(decoded_text)
with open('rle_decoded.txt', 'w') as data3:
    data3.write(decoded_text)
