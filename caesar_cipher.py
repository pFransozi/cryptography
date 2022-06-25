'''
The old method to cipher called Caesar Cipher.
The gold here is the use of module to circle a list from the end to the beginning, which means from Zz return to Aa

When we have a list with defined items, such as days of week (7), and it is asked from today what day of week will be after 50 days. 
So 50 + day of week today % 7.

'''
import unittest

class CeasarCipher():

    def cipher(self, message:str, key:int) -> str:

        # do not go further if message is empty.
        if len(message) == 0:
            return None

        ASCII_BASE_LOWERCASE = 97
        ASCII_BASE_UPPERCASE = 65
        ALPHABET_BASE = 26

        ascii_value = 0
        base_26_value = 0
        base_ascii = 0
        encrypted_msg = ''

        for character in message:

            # numbers, symbols remain the same
            if not character.isalpha():
                encrypted_msg += character
                continue

            # define upper- or lowercase base
            base_ascii = ASCII_BASE_LOWERCASE if character.islower() else ASCII_BASE_UPPERCASE

            ascii_value = ord(character)
            base_26_value = (ascii_value - base_ascii)
            base_26_value = ((base_26_value + key) % ALPHABET_BASE)
            ascii_value = base_26_value + base_ascii

            encrypted_msg += chr(ascii_value)

        return encrypted_msg

class TestCeasarCipher(unittest.TestCase):

    def test_caesar_cipher(self):

        message = 'This is a message to test caesar chipher'
        key = 5
        expected_encrypted_msg = 'Ymnx nx f rjxxflj yt yjxy hfjxfw hmnumjw'
        result_encrypted_msg = CeasarCipher().cipher(message, key)

        self.assertEqual(result_encrypted_msg, expected_encrypted_msg)

    def test_caesar_cipher1(self):
        message = 'Zebra'
        key = 30
        expected_encrypted_msg = 'Difve'
        result_encrypted_msg = CeasarCipher().cipher(message, key)

        self.assertEqual(result_encrypted_msg, expected_encrypted_msg)


    def test_caesar_cipher_numbers(self):
        message = '1234567890'
        key = 30
        expected_encrypted_msg = '1234567890'
        result_encrypted_msg = CeasarCipher().cipher(message, key)

        self.assertEqual(result_encrypted_msg, expected_encrypted_msg)

    def test_caesar_cipher_uppers(self):
        message = 'ZZTOP BAND'
        key = 591
        expected_encrypted_msg = 'SSMHI UTGW'
        result_encrypted_msg = CeasarCipher().cipher(message, key)

        self.assertEqual(result_encrypted_msg, expected_encrypted_msg)



if __name__ == '__main__':
    unittest.main()

