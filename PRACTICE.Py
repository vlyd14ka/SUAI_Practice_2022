import time #импорт библиотеки time для засекания времени


def inp_to_array(text):
    # убираем все символы, не явл. буквами и заменяем их на пробелы
    reform_text = ""
    for i in range(len(text)):
        if not text[i].isalpha():
            reform_text += " "
        else:
            reform_text += text[i].lower()

    #анализируем получившуюся строку
    result = []
    now_symbols = ""
    for i in range(len(reform_text)):
        if reform_text[i] == " ":
            if len(now_symbols) != 0:
                result.append(now_symbols)
            now_symbols = ""
        else:
            now_symbols += reform_text[i]
    if len(now_symbols) != 0:
        result.append(now_symbols)
    # возвращаем список слов, отсортированых по первой букве (от 'а' до 'я')
    return result

# cортировка массива
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# считываем входной файл
path = input("File to read: ")
inp_file = open(path, encoding="utf8")
text = inp_file.read()
inp_file.close()

# сортировка и засекание времени
words_list = inp_to_array(text)
time_begin = time.time_ns()
insertion_sort(words_list)
time_end_sec = (time.time_ns() - time_begin) / 1000000000




# определение файла для результата
output_path = input("Output file path: ")
file_res = open(output_path, "w+", encoding="utf8")
last_symb = words_list[0][0]
for word in words_list:
    if word[0] != last_symb:
        last_symb = word[0]
        file_res.write("\n")
        file_res.write(f"{word} ")
    else:
        file_res.write(f"{word} ")

file_res.close()

# записываем аналитку
anal_path = input("Analysis path: ") #получение пути к файлу анализа
file_analysis = open(anal_path, "w+", encoding="utf8") #открытие файла для записи, перекодировка в формат utf8
file_analysis.write("Введенный текст:""\n")
file_analysis.write(text) #запись анализируемого текста в новый файл
file_analysis.write("\n\n")
file_analysis.write(f"Вариант 15: кириллица, по алфавиту, по возрастанию, игнорировать числа, быстрая сортировка\n")
file_analysis.write(f"Количество слов = {len(words_list)}\n") #вывод количества слов
file_analysis.write(f"Время сортировки: {time_end_sec}\n") # вывод времени сортировки
file_analysis.write(f"Статистика (количество слов на каждую букву алфавита):""\n") #вывод статистики количества слов на каждую букву



n = 0
for i in range(1, len(words_list)): #считаем количество букв
    n += 1
    if words_list[i][0] != words_list[i - 1][0]:
        file_analysis.write(f"{words_list[i][0]} - {n} \n") #запись результата в файл
        n = 0


file_analysis.close()
