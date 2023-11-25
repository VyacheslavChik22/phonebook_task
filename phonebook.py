inf = '\n\tВесь список телефонов:\n'
def sho_oll(file_name, inf: str):
    count = 0
    print(inf)
    with open(file_name,'r',encoding='utf-8') as fl:
        data = fl.readlines()
        data.sort(key = lambda user: user[0])
        for i in range(len(data)):
            count += 1
            print(count,"\033[34m{}\033[0m".format("".join(data[i])))
          

def copy_number(file_name, temp_file, copy_file: str):
    count = 0
    print('\n\tВесь список телефонов:\n')
    with open(file_name,'r',encoding='utf-8') as fl:
        data = fl.readlines()
        data.sort(key = lambda user: user[0])
        for i in range(len(data)):
            count += 1
            print(count,"\033[34m{}\033[0m".format("".join(data[i]))) 
    copy_line = int(input ('Введите номер строки копирования ->'))   
    with open(temp_file,'a',encoding='utf-8') as fl_copy:
        fl_copy.write(data[copy_line-1])
        temp = set()
    with open(temp_file,'r',encoding='utf-8') as fl_copy:
         flc = fl_copy.readlines()   
    for line in  flc:
        temp.add(line)
    with open(copy_file,'w',encoding='utf-8') as fl_copy:
        fl_copy.writelines(temp) 
    print("\033[34m{}\033[0m".format('\nАбонент и его номер телефона добавлены в новый справочник "new_phonebook", спасибо.')) 
    inf = '\n\tНовый справочник:\n' 
    sho_oll(copy_file, inf)

def add_new(file_name: str):
    print("\033[32m{}\033[0m".format('\tДобавление номера в список:\n'))
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер по шаблону: +7(***)***-**-** -> ')
    input_number_phone(phone_number) 
    with open(file_name,'a',encoding='utf-8') as fl:    
        fl.write(f'{last_name}, {first_name:}, {surname:}, {phone_number}\n' )
        print("\033[32m{}\033[0m".format('\nНовый абонент и его номер телефона добавлены в справочник, спасибо.'))


def input_number_phone(phone_number): 
    sample = '0123456789()+-'        
    for i in range(len(phone_number)):
        if phone_number[i] not in sample or phone_number[6] != ')' or phone_number[10] != '-' or phone_number[13] != '-' or len(phone_number) != 16:
            print('Такая запись номера не допустима!')
            break
    return phone_number

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
            print("\033[31m{}\033[0m".format('\nДанные успешно удалены из справочника.'))
    else:
        print('Действие отменено пользователем') 


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
            print("\033[33m{}\033[0m".format('\nДанные номера успешно изменены.'))
    else:
        print('Действие отменено пользователем')  


def find_number(file_name: str):
    print("\033[35m{}\033[0m".format('\tПоиск нужного номера:\n'))
    str_query = ['1 - Поиск по фамилии', '2 - Поиск по имени', '3 - Поиск по отчеству', '4 - Поиск по номеру телефона']
    for i in str_query:
        print(i)
    search_query = int(input('\nВведите номер операции поиска -> '))
    meaning =''
    if  1<= search_query <= 4:
        if search_query == 1:
            meaning = input ('Введите искомую фамилию -> ') 
        elif search_query == 2:
            meaning = input ('Введите искомое имя -> ')
        elif search_query == 3:
            meaning = input ('Введите искомое отчество -> ')
        elif search_query == 4:
            meaning = input ('Введите искомый номер -> ')        
        index_search = int(search_query-1)
        with open(file_name,'r',encoding='utf-8') as fl:
            data = fl.readlines()
            data = list(filter(lambda x: x.replace('\n','').split(', ')[index_search] == meaning, data))
            data.sort(key = lambda user: user[0])
            print("\t\033[34m{}\033[0m".format('Найдены абоненты:'))
            print("\033[34m{}\033[0m".format("".join(data)))
    else:
        print('Такой операции для поиска у нас нет')
        
        
def main():   
    file_name = ('phoneBook.txt')
    temp_file = ('temp.txt')
    copy_file = ('new_ponebook.txt') 
    stop = False
    str = '123456x'
    while not stop:
        print()
        print('Список возможных операций в справочнике:\n')
        print('1 - Показать список всех телефонов')
        print('2 - Добавить телефон в список')
        print('3 - Удалить телефон из списка')
        print('4 - Изменить данные номера')
        print('5 - Поиск нужного номера')
        print('6 - Копия нужного номера')
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
            elif answer =='5':
                find_number(file_name)
            elif answer =='6':
                copy_number(file_name,temp_file,copy_file)         
            elif answer == 'x':
                print('\nСпасибо за обращение к справочнику.')
                stop = True
        else:
            print('Такая операция не выполнима, введите операцию из списка:')


if __name__=="__main__":
    main()