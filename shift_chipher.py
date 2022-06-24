'''
The Caesar cipher, or shift cipher, is a quite obsolete. It is not exactly a cryptography method, 
even though the idea of transform a readable message into a unreadable one is already here. The basic problem is that the permutation 
is over a small set of data. May in the Caesar time it was hard to broke the code, now it is instantaneously.

'''

import string

def shift_module_operation(dividend, divisor):
    return (dividend % divisor)

def create_shift_substitutions_alphabet_uppercase(shifting_number):

    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)

    for index in range(alphabet_size):

        letter = string.ascii_uppercase[index]
        shifted_index = shift_module_operation(index+shifting_number, alphabet_size)
        subst_letter = string.ascii_uppercase[shifted_index]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter

    return encoding, decoding

def encode(original_message, substitution_table):
    cipher_message = ''

    for letter in original_message:
        if letter in substitution_table:
            cipher_message += substitution_table[letter]
        else:
            cipher_message += letter

    return cipher_message

def decode(original_message, substitution_table):
    return encode(original_message, substitution_table)

def  printable_substitution(subst):
    mapping = sorted(subst.items())

    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)

if __name__ == '__main__':

    n = 1
    encoding, decoding = create_shift_substitutions_alphabet_uppercase(n)

    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print('Encoding table:')
            print(printable_substitution(encoding))
            print('Decoding table:')
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(
                                            encode(message.upper(), encoding)
                                            )
                )
        
        elif choice == '3':
            message = input('\nMessage to decode: ')
            print('Decoded Message: {}'.format(
                                                decode(message.upper(), decoding)
                                                )
                )

        elif choice == '4':
            new_shift = input('\nNew shift (currently {}): '.format(n))

            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions_alphabet_uppercase(n)

        elif choice == '5':
            print('Terminating. This program will self destruct in 5 seconds.\n')
            break

        else:
            print('Unknown option {}.'.format(choice))