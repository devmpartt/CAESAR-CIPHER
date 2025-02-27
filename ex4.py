import re
from collections import Counter

def frequency_analysis(text, excluded_letters):
    # Poista määritellyt kirjaimet analyysistä
    filtered_text = ''.join([c for c in text if c.upper() not in excluded_letters])
    
    # Poista ei-aakkoselliset merkit ja muuta teksti isoiksi kirjaimiksi
    filtered_text = re.sub(r'[^A-Z]', '', filtered_text.upper())
    
    # Laske kirjainten taajuudet
    letter_counts = Counter(filtered_text)
    total_letters = sum(letter_counts.values())
    
    # Lasketaan prosentuaalinen taajuus
    frequency = {letter: count / total_letters * 100 for letter, count in letter_counts.items()}
    
    return frequency

def print_frequency(frequency):
    print("Letter Frequency Analysis:")
    for letter, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter}: {freq:.2f}%")

def decrypt_text(ciphertext, substitution):
    translation = str.maketrans(substitution)
    return ciphertext.translate(translation)

def main():
    # Syötä salattu teksti
    ciphertext = input("Syötä salattu teksti: ")

    # Määrittele tunnetut kirjaimet ja niiden korvaukset suoraan koodissa
    known_letters = {
       
        
        'A': 'K',
        'B': 'X',
        'C': 'V',
        'D': 'M',
        'E': 'C',
        'F': 'N',
        'G': 'O',
        'H': 'P',
        'I': 'H',
        'J': 'Q',
        'K': 'R',
        'L': 'S',
        # 'M': '',
        'N': 'Y',
        'O': 'I',
        # 'P': '',
        'Q': 'A',
        'R': 'D',
        'S': 'L',
        'T': 'E',
        'U': 'G',
        'V': 'W',
        'W': 'B',
        'X': 'U',
        'Y': 'F',
        'Z': 'T'



    }

    # Poista tunnetut kirjaimet taajuusanalyysistä
    excluded_letters = set(known_letters.keys())
    frequency = frequency_analysis(ciphertext, excluded_letters)
    print_frequency(frequency)

    # Dekryptaa teksti tunnetuilla korvauksilla
    decrypted_text = decrypt_text(ciphertext, known_letters)
    print("\nDekryptattu teksti:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
