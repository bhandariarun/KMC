def is_magic_square(matrix):
    # Check if the matrix is 3x3
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return False

    # Check if all elements are integers
    for row in matrix:
        for element in row:
            if not isinstance(element, int):
                return False

    # Calculate the sum of the first row
    target_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for j in range(3):
        if sum(matrix[i][j] for i in range(3)) != target_sum:
            return False

    # Check main diagonal
    if sum(matrix[i][i] for i in range(3)) != target_sum:
        return False

    # Check secondary diagonal
    if sum(matrix[i][2 - i] for i in range(3)) != target_sum:
        return False

    return True


def main():
    # Ask the user to input a 3x3 matrix
    print("Enter a 3x3 matrix (nine integer values):")
    matrix = []
    for _ in range(3):
        row = input().strip().split()
        matrix.append([int(val) for val in row])

    # Check if the given matrix forms a magic square
    if is_magic_square(matrix):
        print("The given matrix forms a magic square.")
    else:
        print("The given matrix does not form a magic square.")


if __name__ == "__main__":
    main()