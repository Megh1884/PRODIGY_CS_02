import numpy as np
from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypt an image using XOR operation with a given key.

    Args:
        image_path (str): Path to the image file.
        key (int): Encryption key.

    Returns:
        encrypted_image (Image): Encrypted image.
    """
    image = Image.open(image_path)
    if image.mode == 'RGBA':  # Check if the image is in RGBA mode
        image = image.convert('RGB')  # Convert to RGB mode
    pixels = np.array(image)
    encrypted_pixels = pixels ^ key
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    return encrypted_image

def decrypt_image(encrypted_image, key):
    """
    Decrypt an encrypted image using XOR operation with the same key.

    Args:
        encrypted_image (Image): Encrypted image.
        key (int): Decryption key.

    Returns:
        decrypted_image (Image): Decrypted image.
    """
    encrypted_pixels = np.array(encrypted_image)
    decrypted_pixels = encrypted_pixels ^ key
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    return decrypted_image

def main():
    image_path = "./Banner.png"
    key = 145  # Choose a random key for encryption

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save("encrypted_image.jpg")

    # Decrypt the encrypted image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.save("decrypted_image.jpg")

if __name__ == "__main__":
    main()
