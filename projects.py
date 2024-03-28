import pandas as pd
import cv2
# import matplotlib.pyplot as plt


def dataframe():
    data = {
        'column 1': [1, 2, 3, 4],
        'column 2': ['mohammad', 'reza', 'Tileh', 'babri'],
    }

    df = pd.DataFrame(data)
    print(df)


def two_column_sum(array_1, array_2):
    array_sum = []
    array_index = []
    for i, num in enumerate(array_2):
        array_sum.append(array_1[i] + array_2[i])
        string = f'Cell {i}'
        # array_index.append('Cell'+str(i))
        array_index.append(string)
    data = {'Column 1': array_1,
            'Column 2': array_2,
            'Sum': array_sum}
    df = pd.DataFrame(data, index=array_index)
    print(df)


def remove_large_shapes(binary_image, max_pixels):
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is greater than the specified maximum number of pixels, remove the contour
        if area < max_pixels:
            cv2.drawContours(binary_image, [contour], 0, (0, 0, 0), -1)  # Fill contour with black color

    return binary_image


def image_read(image):
    img = cv2.imread(image)
    # print(img)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary = cv2.threshold(gray_image, 110, 255, cv2.THRESH_BINARY)[-1]
    binary_crop = binary[390:550, 380:650]
    # print(binary_crop)
    clean_pic = remove_large_shapes(binary_crop, 1000)
    cv2.imshow('aks', clean_pic)
    cv2.waitKey(0)
    cv2.destroyAllWidows()




