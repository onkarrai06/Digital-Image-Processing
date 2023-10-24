import numpy as np
import cv2


def label_components(image):
    rows, cols = image.shape
    labels = np.zeros((rows, cols), dtype=np.uint8)
    label = 1
    eq_table = {}

    def find_root(x):
        if x not in eq_table:
            eq_table[x] = x
            return x
        if eq_table[x] != x:
            eq_table[x] = find_root(eq_table[x])
        return eq_table[x]

    for row in range(rows):
        for col in range(cols):
            if image[row, col] == 255:
                neighbors = [
                    labels[row, col - 1],
                    labels[row - 1, col - 1],
                    labels[row - 1, col],
                ]

                if col + 1 < cols:
                    neighbors.append(labels[row - 1, col + 1])

                valid_neighbors = [n for n in neighbors if n != 0]

                if not valid_neighbors:
                    labels[row, col] = label
                    label += 1
                else:
                    labels[row, col] = min(valid_neighbors)
                    root = find_root(labels[row, col])
                    for neighbor in valid_neighbors:
                        if find_root(neighbor) != root:
                            eq_table[find_root(neighbor)] = root

    for row in range(rows):
        for col in range(cols):
            labels[row, col] = eq_table[find_root(labels[row, col])]

    return eq_table, labels


binary_image = cv2.imread("Image_01.bmp", 0)
threshold, image = cv2.threshold(binary_image, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", image)
table, labelled_image = label_components(image)
rows, cols = labelled_image.shape

unique_labels = np.unique(labelled_image)
print(unique_labels)
num_objects = len(unique_labels) - 1
print(num_objects)


color = [
    [0, 0, 0],
    [0, 0, 255],
    [0, 255, 0],
    [255, 0, 0],
    [0, 255, 255],
    [255, 0, 255],
    [255, 255, 0],
    [255, 255, 255],
    [50, 80, 100],
]

fin_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)


for i in range(1, num_objects + 1):
    for row in range(rows):
        for col in range(cols):
            if labelled_image[row, col] == unique_labels[i]:
                fin_image[row][col][0] = color[i][0]
                fin_image[row][col][1] = color[i][1]
                fin_image[row][col][2] = color[i][2]

cv2.imshow("Labelled", fin_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
