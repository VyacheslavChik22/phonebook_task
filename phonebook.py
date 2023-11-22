def sho_oll(file_name: str):
    print('\n\tВесь список телефонов:\n')
    with open(file_name,'r',encoding='utf-8') as fl:
        data = fl.readlines()
        data.sort(key = lambda user: user[0])
        #print("".join(data))
        print("\033[34m{}\033[0m".format("".join(data)))

def add_new(file_name: str):

    print("\033[32m{}\033[0m".format('\tДобавление номера в список:\n'))
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file_name,'a',encoding='utf-8') as fl:    
        fl.write(f'{last_name}, {first_name:}, {surname:}, {phone_number}\n' )
        print('\nНовый абонент и его номер телефона добавлены в справочник, спасибо.')

def del_number(file_name: str):
    print("\033[31m{}\033[0m".format('\tУдаление данных из списка:\n'))
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    confirmation_del = input("\033[31m{}\033[0m".format('\n\tВы действительно хотите удалить данные этого номера?\n\tВведите Y чтобы удалить или N чтобы отменить действие -> '))
    if confirmation_del == 'Y':
        data = ""
        with open(file_name,'r',encoding='utf-8') as fl:
            data = fl.readlines()
            str = f'{last_name}, {first_name:}, {surname:}, {phone_number}\n' 
            data.remove(str)
        with open(file_name,'w',encoding='utf-8') as fl:
            fl.writelines(data)    
            print('\nДанные успешно удалены из справочника.')
    else:
        main()        
def change_number(file_name: str):
    print("\033[33m{}\033[0m".format('\tИзменение данных номера:\n'))
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    new_last_name = input('Введите другую фамилию: ')
    new_first_name = input('Введите другое имя: ')
    new_surname = input('Введите другое отчество: ')
    new_phone_number = input('Введите другой номер телефона: ')

    confirmation_change = input("\033[33m{}\033[0m".format('\n\tВы действительно хотите изменить данные этого номера?\n\tВведите Y чтобы изменить или N чтобы отменить действие -> '))
    if confirmation_change == 'Y':
        data = ""
        with open(file_name,'r',encoding='utf-8') as fl:
            data = fl.readlines()
            old_str = data.index(f'{last_name}, {first_name:}, {surname:}, {phone_number}\n') 
            data[old_str] = f'{new_last_name}, {new_first_name:}, {new_surname:}, {new_phone_number}\n'
        with open(file_name,'w',encoding='utf-8') as fl:
            fl.writelines(data)    
            print('\nДанные номера успешно изменены.')
    else:
        main()         

def main():
    
    file_name = ('phoneBook.txt')
    stop = False
    str = '1234x'
    while not stop:
        print()
        print('Список возможных операций в справочнике:\n')
        print('1 - Показать список всех телефонов')
        print('2 - Добавить телефон в список')
        print('3 - Удалить телефон из списка')
        print('4 - Изменить данные номера')
        print('x - Отказ от обращения к справочнику')
        answer = input('\nВведите нужную операцию -> ')
        if answer in str:
            if answer == '1':
                sho_oll(file_name)
            elif answer =='2':
                add_new(file_name)
            elif answer =='3':
                 del_number(file_name)
            elif answer =='4':
                 change_number(file_name)    
            elif answer == 'x':
                print('\nСпасибо за обращение к справочнику.')
                stop = True
        else:
            print('Такая операция не выполнима, введите операцию из списка:')


if __name__=="__main__":
    main()