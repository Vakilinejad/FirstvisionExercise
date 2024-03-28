from projects import dataframe, two_column_sum, image_read

array_1 = [12, 36, 20, 45]
array_2 = [96, 2, 0, 17]

image_dir = './image2.jpg'

name = 'image_read'
if name == 'dataframe':
    dataframe()

if name == 'two_column_sum':
    two_column_sum(array_1, array_2)

if name == 'image_read':
    image_read(image_dir)
