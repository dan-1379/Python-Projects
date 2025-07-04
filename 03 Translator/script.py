from translate import Translator

translator = Translator(to_lang = "ja")

try:
    with open("test.txt", mode = "r") as file:
        text = file.read()
        translation = translator.translate((text))
        print(translation)

        with open("test-ja.txt", mode = "w") as output:
            output.write(translation)

except FileNotFoundError as err:
    print("File not found!")
    raise err
