# Complete the hourglassSum function below.
def hourglassSum(arr):
    # arr is a 6 by 6 2d array

    hour_glass_indicies = [[0, 0], [1, 0], [
        2, 0], [1, 1], [2, 0], [2, 1], [2, 2]]

    sums = []

    for x in range(0, 3):
        for y in range(0, 4):
            # Corners of each hour glass
                a = arr[y][x]
                b = arr[y][x+1]
                c = arr[y][x+2]
                d = arr[y+1][x+1]
                e = arr[y+2][x]
                f = arr[y+2][x+1]
                g = arr[y+2][x+2]
                t_sum = a+b+c+d+e+f+g
                sums.append(t_sum)
                print('X',x)
                print('Y', y)
    print(sums)
    return max(sums)


b = [[-9, -9, -9, 1, 1, 1],[0, -9, 0, 4, 3, 2],[-9, -9, -9, 1, 2, 3],
     [0, 0, 8, 6, 6, 0],[0, 0, 0, -2, 0, 0],[0, 0, 1, 2, 4, 0]]

a = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]

print(hourglassSum(b))
