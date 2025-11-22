# Азбука Морза
MORSE_CODE_DICT = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.',
    'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--',
    'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
    'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--',
    ':': '---...', '?': '..--..', "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '!': '-.-.--', '*': '-..-', '\n': '-.--.-.--'
}

def decrypt(morse_code):
    morse_code += ' '
    decipher = ''
    word = ''
    for letter in morse_code:
        if letter != ' ':
            i = 0
            word += letter
        else:
            if word:
                if i == 2:
                    decipher += ' '
                else:
                    if word in MORSE_CODE_DICT.values():
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(word)]
                    else:
                        decipher += '?'
                word = ''
            i += 1
    return decipher

# Функция для чтения текста из файла
def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

# Функция для записи текста в файл
def write_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

# Чтение текста из файла
input_file2 = "law_encrypt.txt"
encrypted_text = read_file(input_file2)

# Расшифрование текста
decrypted_text = decrypt(encrypted_text)
print(f"Послание расшифровано перейди в файл, чтобы прочитать его")

# Запись расшифрованного текста в файл
output_decrypt_file = "LawOfGod_decrypt.txt"
write_file(output_decrypt_file, decrypted_text)
