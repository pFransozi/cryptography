using System;
using System.IO;
using System.Security.Cryptography;


public class Program
{
    public static void Main(String[] args)
    {
        ApplyingHashOverADirectory hash = new ApplyingHashOverADirectory();
        hash.Compute();

    }

    public class ApplyingHashOverADirectory
    {
        public void Compute()
        {
            Console.Write("Enter the directory path: ");
            string? directory_path = Console.ReadLine();

            if (Directory.Exists(directory_path))
            {
                var directory = new DirectoryInfo(directory_path);
                FileInfo[] files_from_dir = directory.GetFiles();

                using (SHA256 hasher_sha256 = SHA256.Create())
                {
                    foreach (FileInfo file_info in files_from_dir)
                    {
                        try
                        {
                            FileStream file_stream = file_info.Open(FileMode.Open);
                            file_stream.Position = 0;
                            byte[] hashed_file = hasher_sha256.ComputeHash(file_stream);
                            Console.Write($"{file_info.Name}: ");
                            PrintByteArray(hashed_file);
                            file_stream.Close();

                        }
                        catch(IOException exception)
                        {
                            Console.WriteLine($"I/O Exception: {exception.Message}");
                        }
                        catch(UnauthorizedAccessException exception)
                        {
                            Console.WriteLine($"There is an error with accessing the file: {exception.Message}");
                        }
                    }
                }

            }
            else
            {
                Console.WriteLine("The directory selected could not be located or found. Please, select another one.");
            }

        }
    }

    public static void PrintByteArray(byte[] array)
    {
        for(int i = 0; i < array.Length; i++)
        {
            Console.Write($"{array[i]:X2}");
            if ((i%4) == 3) Console.Write(" ");
        }
        Console.WriteLine();
    }
}
