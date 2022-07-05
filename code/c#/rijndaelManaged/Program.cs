using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace RijndaelManagedImplementationExample
{
    class RijndaelManagedImplementationExample
    {
        public static void Main()
        {
            try
            {
                string genuine_message = "Folks, Welcome to Appress!";

                using (RijndaelManaged rijndeal_crypto = new RijndaelManaged())
                {
                    rijndeal_crypto.GenerateKey();
                    rijndeal_crypto.GenerateIV();

                    byte[] encrypted = EncryptStringToBytes(
                                        genuine_message,
                                        rijndeal_crypto.Key,
                                        rijndeal_crypto.IV
                    );

                    string tripRound = DecryptStringFromBytes(
                                        encrypted,
                                        rijndeal_crypto.Key,
                                        rijndeal_crypto.IV
                    );

                    Console.WriteLine("Original Message: {0}", genuine_message);
                    Console.WriteLine("Round trip: {0}", tripRound);

                    Console.WriteLine("\nThe encrypted message is (byte to byte view): {0}",
                                        PrintByteArray(encrypted));
                    Console.WriteLine("\nThe encrypted message is (default view): {0}",
                                        Encoding.Default.GetString(encrypted));
                    Console.WriteLine("\nThe encrypted message is (UTF8 view): {0}",
                                        Encoding.UTF8.GetString(encrypted));
                    Console.WriteLine("\nThe encrypted message is (UTF32 view): {0}", Encoding.UTF32.GetString(encrypted));
                    Console.ReadKey();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("There is an error: {0}", e.Message);
            }
        }

        static string PrintByteArray(byte[] encrypted_message)
        {
            var build_string = new StringBuilder("new byte[] {");
            foreach (var each_byte in encrypted_message)
            {
                build_string.Append(each_byte + " ");
            }
            build_string.Append("}");
            return build_string.ToString();
        }

        static byte[] EncryptStringToBytes(string genuineText,
                                        byte[] encryption_key,
                                        byte[] initialization_vector)
        {
            if (genuineText == null || genuineText.Length <= 0)
                throw new ArgumentNullException("genuineText");
            if (encryption_key == null || encryption_key.Length <= 0)
                throw new ArgumentNullException("encryption_key");
            if (initialization_vector == null || initialization_vector.Length <= 0)
                throw new ArgumentNullException("initialization_vector");

            byte[] encryption_content;

            using (RijndaelManaged rijndael_algo = new RijndaelManaged())
            {
                rijndael_algo.Key = encryption_key;
                rijndael_algo.IV = initialization_vector;

                ICryptoTransform encryptorTransformation = rijndael_algo.CreateEncryptor(
                                            rijndael_algo.Key, rijndael_algo.IV
                );

                using (MemoryStream memoryStreamEncrypt = new MemoryStream())
                {
                    using (CryptoStream cryptoStreamEncrypt = new CryptoStream(
                                    memoryStreamEncrypt,
                                    encryptorTransformation,
                                    CryptoStreamMode.Write)
                    )
                    {
                        using (StreamWriter streamWriterEncrypt = new StreamWriter(cryptoStreamEncrypt))
                        {
                            streamWriterEncrypt.Write(genuineText);
                        }
                        encryption_content = memoryStreamEncrypt.ToArray();
                    }
                }
            }
            return encryption_content;
        }

        void IsValidArgument(var argument)
        {
            if (argument == null || argument.Length <= 0)
                throw new ArgumentNullException();
        }

        static void DecryptStringFromBytes(byte[] encrypted_text,
                                        byte[] encryption_key,
                                        byte[] initialization_vector)
        {
            IsValidArgument(encrypted_text);
            IsValidArgument(encryption_key);
            IsValidArgument(initialization_vector);

            string original_text = null;

            using (RijendaelManaged rijndael_algo = new RijendaelManaged())
            {
                rijndael_algo.Key = encryption_key;
                rijndael_algo.IV = initialization_vector;

                ICryptoTransform decryptionTransformation =
                        rijndael_algo.CreateDecryptor(
                                    rijndael_algo.Key,
                                    rijndael_algo.IV
                                );

                using (MemoryStream memoryStreamDecryptor = new MemoryStream(encrypted_text))
                {
                    using(CryptoStream cryptoStreamDecrypt = new CryptoStream(
                                memoryStreamDecryptor, 
                                decryptionTransformation,
                                CryptoStreamMode.Read)
                    )
                    {
                        using(StreamReader streamReaderDecryption = new StreamReader(cryptoStreamDecrypt))
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