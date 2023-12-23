import numpy as np
from PIL import Image
import cv2


# CONSTANTS
POST_PROCESS_SIZE = 28
THRESHOLD_VALUE = 0


def main():
    og_img_array = cv2.imread(r"C:/Users/Taj/Documents/GitHub/digit-detection-python/bin/image.png", cv2.IMREAD_GRAYSCALE)

    resized_img = Image.fromarray(og_img_array).resize((POST_PROCESS_SIZE, POST_PROCESS_SIZE), Image.NEAREST)
    ret, threshold_array = cv2.threshold(np.asarray(resized_img), THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    post_image = Image.fromarray(threshold_array)
    post_image.show()
    post_image.save(r"C:/Users/Taj/Documents/GitHub/digit-detection-python/bin/resized.png")

    post_img_array = np.array(post_image).flatten()
    post_img_array = post_img_array.reshape(-1, 1).T

    columns = []
    for i in range(POST_PROCESS_SIZE*POST_PROCESS_SIZE):
        columns.append(f"pixel{i}")
    columns = np.array(columns)
    columns = columns.reshape(-1, 1).T

    with open(r"C:/Users/Taj/Documents/GitHub/digit-detection-python/bin/post_image.csv", "wb") as out:
        np.savetxt(out, columns, delimiter=",", fmt="%s")
        np.savetxt(out, post_img_array, delimiter=",", fmt="%1.0f")


if __name__ == "__main__":
    main()
