from datetime import datetime

data = 'Notes.json'
columns = ['ID', 'Название', 'Содержание', 'Дата создания']


# Чтение файла Notes.json
def ReadFile(data: str):
    newData = []
    try:
        with open(data, 'r', encoding='utf-8') as f:
            for line in f:
                record = dict(zip(columns, line.strip().split(';')))
                newData.append(record)
    except FileNotFoundError:
        print(f"Файл '{data}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return newData


# Сохранение данных в файле Notes.json
def SaveData(data, newData):
    with open(data, 'w', encoding='utf-8')as f:
        for i in range(len(newData)):
            s = ''
            for v in newData[i].values():
                s += v + '; '
            f.write(f'{s[:-1]}\n')


# Вывод данных файла Notes.json
def PrintData():
    newData = ReadFile(data)
    number = 0
    print('Заметки')
    for i in newData:
        number += 1
        print(f'{number}.', end=' ')
        print('; '.join(i.values()))


# Создание новой заметки
def NewNote():
    Directory = ReadFile(data)
    newRecord = dict()
    for i in range(len(columns) - 1):
        newRecord[columns[i]] = input(
            f'Введите данные в поле "{columns[i]}": ')
    newRecord['Дата создания'] = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    Directory.append(newRecord)
    SaveData(data, Directory)


# Редактирование выбранной заметки
def Edit():
    Directory = ReadFile(data)  # Сначала прочитаем данные из файла
    PrintData()
    try:
        Index = int(input('Номер редактируемой заметки: ')) - 1
        if Index < 0 or Index >= len(Directory):
            print('Некорректный номер заметки.')
            return
        print('Вы выбрали для редактирования следующую запись:')
        print(*Directory[Index].values())
        fields = ['ID', 'Название', 'Содержание']
        print(*enumerate(fields))
        fieldsIndex = int(input('Номер поля для редактирования: '))
        if fieldsIndex < 0 or fieldsIndex >= len(fields):
            print('Некорректный номер поля.')
            return
        Directory[Index][fields[fieldsIndex]] = input('Новые данные: ')
        SaveData(data, Directory)
        print('Запись успешно отредактирована.')
    except ValueError:
        print('Ошибка ввода. Введите корректные числа для номера заметки и номера поля.')
    except Exception as e:
        print(f'Ошибка при редактировании: {e}')


# Удаление выбранной заметки
def Delete():
    Directory = ReadFile(data)
    if not Directory:
        print('Файл пустой. Удаление невозможно.')
        return

    PrintData()
    try:
        Index = int(input('Номер удаляемой записи: ')) - 1
        if 0 <= Index < len(Directory):
            print('Вы выбрали для удаления следующую запись:')
            print(*Directory[Index].values())

            confirm = input(
                'Вы уверены, что хотите удалить эту запись? (YES (0) / NO (1)): ')
            if confirm.lower() == '0':
                Directory.pop(Index)
                SaveData(data, Directory)
                print('Заметка удалена.')
            else:
                if confirm.lower() == '1':
                    print('Заметка НЕ удалена.')
                else:
                    print('Неверный номер записи. Удаление невозможно.')

    except ValueError:
        print('Ошибка ввода. Введите корректное число для номера заметки')
    except Exception as e:
        print(f'Ошибка при удалении: {e}')


# Меню
def main():
    while True:
        print('-----Меню-----')
        print('1 - Все заметки')
        print('2 - Новая заметка')
        print('3 - Редактировать заметку')
        print('4 - Удалить заметку')
        print('0 - Выйти из программы')

        try:
            choice = int(input('Введите номер пункта меню: '))
        except ValueError:
            print('Ошибка ввода. Введите число от 0 до 4.')
            continue

        if choice == 0:
            return
        elif choice == 1:
            PrintData()
        elif choice == 2:
            NewNote()
        elif choice == 3:
            Edit()
        elif choice == 4:
            Delete()
        else:
            print('Неверный номер пункта меню. Повторите ввод')


if __name__ == '__main__':
    main()
