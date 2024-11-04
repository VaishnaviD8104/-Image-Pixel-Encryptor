from PIL import Image 

def swap_pixels(image):
    """Swap pixels from top-left to bottom-right."""
    width, height = image.size
    pixels = image.load()

    for i in range(width // 2):
        for j in range(height // 2):
            # Swap pixel (i, j) with its mirrored counterpart (width-i-1, height-j-1)
            original_pixel = pixels[i, j]
            mirrored_pixel = pixels[width - i - 1, height - j - 1]

            # Swap the pixels
            pixels[i, j], pixels[width - i - 1, height - j - 1] = mirrored_pixel, original_pixel

    return image

def apply_math_operation(image, value):
    """Apply a basic mathematical operation to each pixel."""
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Add a constant value to each RGB channel (with wrapping)
            new_r = (r + value) % 256
            new_g = (g + value) % 256
            new_b = (b + value) % 256

            pixels[i, j] = (new_r, new_g, new_b)

    return image

def main():
    # Load the image
    img_path = input("Enter the path of the image: ")
    image = Image.open(img_path)
    image.show()

    # Choose operation
    print("1. Swap Pixels")
    print("2. Apply Mathematical Operation (Add)")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        encrypted_image = swap_pixels(image)
    elif choice == 2:
        value = int(input("Enter the value to add to each pixel (0-255): "))
        encrypted_image = apply_math_operation(image, value)
    else:
        print("Invalid choice!")
        return

    # Save and display the encrypted image
    encrypted_image.show()
    encrypted_image.save("encrypted_image.png")
    print("Encrypted image saved as 'encrypted_image.png'.")

if _name_ == "_main_":
    main()