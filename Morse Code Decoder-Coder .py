
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/' 
}


def encode_morse(text):
    text = text.upper()
    coded = ''
    for char in text:
        coded += MORSE_CODE.get(char, '') + ' '
    return coded.strip()

def decode_morse(morse):
    reversed_dict = {v: k for k, v in MORSE_CODE.items()}
    words = morse.split(' ')
    decoded = ''
    for w in words:
        decoded += reversed_dict.get(w, '')
    return decoded

def count_dots_dashes(morse):
    return morse.count('.'), morse.count('-')

msg = input("Enter your message: ")
morse_msg = encode_morse(msg)
print("Encoded Morse:", morse_msg)
print("Decoded Text:", decode_morse(morse_msg))
dots, dashes = count_dots_dashes(morse_msg)
print(f"Total dots: {dots}, Total dashes: {dashes}")