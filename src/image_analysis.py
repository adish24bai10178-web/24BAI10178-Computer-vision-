def analyze_image(image):

    height, width, channels = image.shape

    total_pixels = width * height

    image_size_kb = image.nbytes / 1024

    return {
        "width": width,
        "height": height,
        "channels": channels,
        "total_pixels": total_pixels,
        "image_size_kb": image_size_kb
    }
