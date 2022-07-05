using System;
using System.IO;
using System.Security.Cryptography;

namespace AESExampleOfImplementation
{
    class AESExampleOfImplementation
    {
        public static void Main()
        {
            string genuineMessage = "Welome to Apress!";

            using (AesManaged encryptor_aes = new AesManaged())
            {
                byte[] encrypted = EncryptStringToBytes_Aes(
                                original,
                                encryptor_aes.Key,
                                encryptor_aes.IV
                        );

                string roundtrip = DecryptStringFromBytes_Aes(
                                encrypted,
                                encryptor_aes.Key,
                                encryptor_aes.IV
                        );

                Console.WriteLine("Original:   {0}", genuineMessage);
                Console.WriteLine("Round Trip: {0}", roundtrip);

                Console.WriteLine("The encrypted message is (byte-to-byte): {0}",
                                    PrintByteArray(genuineMessage)
                );

                Console.WriteLine("The encrypted message is (default view): {0}",
                                    Encoding.Default.GetString(genuineMessage)
                );

                Console.WriteLine("The encrypted message is (UTF8 view): {0}",
                                    Encoding.UTF8.GetString(genuineMessage)
                );

                Console.WriteLine("Encrypted message is (UTF32 view): {0}",
                                    Encoding.UTF32.GetString(genuineMessage)
                );

                Console.ReadKey();
            }
        }

        static string PrintByteArray(byte[] encrypted_message)
        {
            var build_string = new StringBuilder("new byte[] { ");
            foreach (var each_byte in encrypted_message)
            {
                build_string.Append(each_byte + " ");
            }

            build_string.Append("}");
            return build_string.ToString();
        }

        static byte[] EncryptStringToBytes_Aes(string genuineText, byte[] crypto_key, byte[] initialization_vector)
        {
            if (string.IsNullOrEmpty(genuineText))
                throw new ArgumentNullException("genuineText");

            if (crypto_key == null || crypto_key.Length <= 0)
                throw new ArgumentNullException("crypt_key");

            if (initialization_vector == null || initialization_vector.Length <= 0)
                throw new ArgumentNullException("initialization_vector IV");

            byte[] encryption_representation;
            using (Aes aes_algorithm = Aes.Create())
            {
                aes_algorithm.Key = crypto_key;
                aes_algorithm.IV = initialization_vector;

                ICryptoTransform crypto_transformation = aes_algorithm.CreateEncryptor(aes_algorithm.Key, aes_algorithm.IV);
                using (MemoryStream memoryStreamForEncryption = new MemoryStream)
                {
                    using (CryptoStream cryptoStreamEncryption = new CryptoStream(memoryStreamForEncryption, crypto_transformation, CryptoStreamMode.Write))
                    {
                        using (StreamWriter streamWriterForEncryption = new StreamWriter(cryptoStreamEncryption))
                        {
                            streamWriterForEncryption.Write(genuineText);
                        }
                        encryption_representation = memoryStreamForEncryption.ToArray();
                    }
                }
            }
            return encryption_representation;
        }

        static string DecryptStringToBytes_Aes(byte[] encryptedText, byte[] encryption_key, byte[] initialization_vector)
        {
            if (encryptedText == null || encryptedText.Length <= 0)
                throw new ArgumentNullException("encryptedText");

            if (encryption_key == null || encryption_key.Length <= 0)
                throw new ArgumentNullException("Key");
            
            if (initialization_vector == null || initialization_vector.Length <= 0)
                throw new ArgumentNullException("IV");

            string original_text = null;

            using(Aes aes_algorithm = Aes.Create())
            {
                aes_algorithm.Key = encryption_key;
                aes_algorithm.IV = initialization_vector;

                ICryptoTransform decrypt_transform = aes_algorithm.CreateDecryptor(aes_algorithm.Key, aes_algorithm.IV);

                using (MemoryStream memoryStreamDecryption = new MemoryStream(encryptedText))
                {
                    using(CryptoStream cryptoStreamDecryption = new CryptoStream(memoryStreamDecryption, decrypt_transform, CryptoStreamMode.Read))
                    {
                        using(StreamReader streamReaderDecryption = new StreamReader(cryptoStreamDecryption))
                        {
                            original_text = streamReaderDecryption.ReadToEnd();
                        }
                    }
                }
            }

            return original_text;
        }
    }
}