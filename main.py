
import numpy as np
from time import sleep


def check_neighbours(size, b, y, x):

    # Periodic
    n = b[size-1][x] if y == 0 else b[y-1][x]
    e = b[y][0] if x == size-1 else b[y][x+1]
    s = b[0][x] if y == size-1 else b[y+1][x]
    w = b[y][size-1] if x == 0 else b[y][x-1]

    if (n + e + s + w) % 2 == 0:
        return 0

    return 1


def display(size, b):
    for i in range(size):
        for j in range(size):
            print("███" if b[i][j] else "   ", end="")
            # print("⬛" if b[i[j] else "⬜", end=" ")
        print()


def parity(size, b, n):

    for _ in range(n+1):

        p = np.where(b == 1)
        sleep(0.2)

        print("\033[0;0H")
        
        print(f"Number of iterations: {_}")
        print(f"\033[KParticle Count: {len(p[0])}")
        
        display(size, b)

        b_ = b.copy()

        for i in range(len(p[0])):

            p_y, p_x = p[0][i], p[1][i]

            # Periodic
            n = [size-1, p_x] if p_y == 0 else [p_y-1, p_x]
            e = [p_y, 0] if p_x == size-1 else [p_y, p_x+1]
            s = [0, p_x] if p_y == size-1 else [p_y+1, p_x]
            w = [p_y, size-1] if p_x == 0 else[p_y, p_x-1]

            b[p_y][p_x] = check_neighbours(size, b_, p_y, p_x)

            if n:
                b[n[0]][n[1]] = check_neighbours(size, b_, n[0], n[1])
            if e:
                b[e[0]][e[1]] = check_neighbours(size, b_, e[0], e[1])
            if s:
                b[s[0]][s[1]] = check_neighbours(size, b_, s[0], s[1])
            if w:
                b[w[0]][w[1]] = check_neighbours(size, b_, w[0], w[1])


if __name__ == '__main__':

    while(True):
        try:
            print(
                "\033[0;0H\033[KInput table size and number of iterations seperated by a space.", end="\n\033[K→ ")
            size, n = input().split()

            size, n = int(size), int(n)

            b = np.ones((size, size), dtype=int) * 0

            if n > -1:

                # 1x1
                # b[int(size/2)][int(size/2)] = 1

                # 2x2
                # for i in range(2):
                #     for j in range(2):
                #         b[int(size/2)-1+i][int(size/2)-1+j] = 1

                # 8x10
                for i in range(8):
                    for j in range(10):
                        b[int(size/2)-4+i][int(size/2)-4+j] = 1

                parity(size, b, n)
                break

            print("Invalid Input.")
        except:
            print("Invalid input.")
