import numpy as np

# Step 1: Create a 2D NumPy array (5x5) filled with random integers between 1 and 100
array = np.random.randint(1, 101, size=(5, 5))
print("Original Array:")
print(array)

# Step 2: Extract and print the middle element using NumPy indexing
middle_element = array[2, 2]  # Middle of 5x5 is at index (2, 2)
print("\nMiddle Element:")
print(middle_element)

# Step 3: Calculate and print the mean of each row
row_means = np.mean(array, axis=1)
print("\nMean of Each Row:")
print(row_means)

# Step 4: Create a new array with elements greater than the overall mean
overall_mean = np.mean(array)
new_array = array[array > overall_mean]
print("\nNew Array (Elements Greater Than Overall Mean):")
print(new_array)

# Step 5: Write the numpy_spiral_order function
def numpy_spiral_order(matrix):
    spiral_order = []
    while matrix.size:
        spiral_order.extend(matrix[0])  # Top row
        matrix = np.delete(matrix, 0, axis=0)  # Remove top row
        if matrix.size == 0:
            break
        matrix = np.rot90(matrix)  # Rotate counter-clockwise
    return spiral_order

# Compute and print spiral order
spiral_order = numpy_spiral_order(array.copy())
print("\nSpiral Order of the Array:")
print(spiral_order)
