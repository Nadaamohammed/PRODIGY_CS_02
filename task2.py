def encrypt_image(image_path, key):
    try:
        with open(image_path, 'rb') as fin:
            image = bytearray(fin.read())
            for index, value in enumerate(image):
                image[index] = value ^ key
        with open(image_path, 'wb') as fout:
            fout.write(image)
        print("Encryption done.")
    except Exception as e:
        print('Error caught:', e)

def decrypt_image(image_path, key):
    try:
        with open(image_path, 'rb') as fin:
            image = bytearray(fin.read())
            for index, value in enumerate(image):
                image[index] = value ^ key
        with open(image_path, 'wb') as fout:
            fout.write(image)
        print("Decryption done.")
    except Exception as e:
        print('Error caught:', e)

image_path = "flower.jpg"
print("Do you want to encrypt or decrypt?")
user_input = input('Enter "e" for encryption or "d" for decryption: ').lower()
print()

if user_input == 'e':
    print("Encrypt mode")
    key = int(input('Enter the key: '))
    encrypt_image(image_path, key)

elif user_input == 'd':
    print("Decrypt mode")
    key = int(input('Enter the key: '))
    decrypt_image(image_path, key)

else:
    print("Invalid input.")
