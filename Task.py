def main():
    array = input('Введите данные для массива(через пробел): ')
    array = array.split()
    sort_array = get_sort_array(array, 3)
    print(sort_array)

def get_sort_array(array, n):
    array2 = []
    for i in range(len(array)):
        if len(array[i]) <= n:
            array2.append(array[i])
    return array2        

if __name__ == '__main__':
    main()