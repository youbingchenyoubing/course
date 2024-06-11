def is_full_number(number):
    data = 1
    for i in range(2, int(number / 2)):
        if number % i == 0:
            discount = int(number / i)
            if discount < i:
                break
            elif i == discount:
                data += i
            else:
                data += i + int(number / i)
    return True if data == number else False


def is_full_number_2(number):
    data = 1
    index = 2
    while True:
        if number % index == 0:
            discount = int(number / index)
            if discount < index:
                break
            elif index == discount:
                data += index
            else:
                data += index + discount
        index += 1
        if index * index >= number:
            break
    return True if data == number else False


if __name__ == '__main__':
    number = int(input())
    for i in range(2, number + 1):
        if is_full_number_2(i):
            print(i)
