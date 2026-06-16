import os

def get_images():
    image_folder = "assets/images"

    images = []

    for file in sorted(os.listdir(image_folder)):
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):
            images.append(
                os.path.join(image_folder, file)
            )

    return images