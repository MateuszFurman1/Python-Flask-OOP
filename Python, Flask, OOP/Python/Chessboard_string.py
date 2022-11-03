def chessboard(n):
    for row in range(n):
        for column in range(n):
            if row % 2 == 0:
                if column % 2 == 0:
                    print('#', end='')
                else:
                    print(' ', end='')
            else:
                if column % 2 == 1:
                    print('#', end='')
                else:
                    print(' ', end='')
        print()

chessboard(4)