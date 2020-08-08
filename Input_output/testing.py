# my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.readlines())

# my_file.close()

from translate import Translator
try:
    with open('./input_output/test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang="zh")
        translation = translator.translate("fuck you")

        print(translation)
except FileNotFoundError as e:
    print('Check file path')