def is_influenza(patient_info):
    if patient_info[0] >= 37.5 and patient_info[1] == 1:
        return True
    return False


if __name__ == '__main__':
    number = int(input())
    patients = []
    count = 0
    for index in range(number):
        name, temperature, is_cough = map(str, input().split())
        temperature = float(temperature)
        is_cough = int(is_cough)
        if is_influenza([temperature, is_cough]):
            count += 1
            patients.append(name)
    for name in patients:
        print(name)
    print(count)
