import easyocr


def text_recognition(file_path, text_file_name='result.txt'):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f'{line}\n\n')
    return f'Result wrote into {text_file_name}'


def main():
    file_path = input("Enter file's path: ")
    file_name = input('Enter name for text file: ')
    if file_name == '':
        print(text_recognition(file_path=file_path))
    else:
        print(text_recognition(file_path=file_path, text_file_name=file_name))


if __name__ == '__main__':
    main()
