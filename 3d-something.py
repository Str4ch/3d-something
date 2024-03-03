'''Realisation of 3d graphics, using ASCII symbols and math formulas (better run this programm in terminal)'''

import math as m


def sphere(xs, ys, zs, r, x0, y0, z0, vx, vy, vz) -> float:
    # function that checks intersection of ray and sphere
    # and return the length of the ray

    a = vx ** 2 + vy ** 2 + vz ** 2
    b = 2 * ((x0 - xs) * vx + (y0 - ys) * vy + (z0 - zs) * vz)
    c = (x0 - xs) ** 2 + (y0 - ys) ** 2 + (z0 - zs) ** 2 - r ** 2
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 10 ** 10
    else:
        if D == 0:
            t = b / 2 * a
        else:
            t1 = (-b - D ** (1 / 2)) / 2 * a
            t2 = (-b + D ** (1 / 2)) / 2 * a
            if t1 > t2 >= 0:
                t = t2
            else:
                t = t1
        return ((t * vx) ** 2 + (t * vy) ** 2 + (t * vz) ** 2) ** (1 / 2)


def intersects(x0, y0, z0, vx, vy, vz) -> float:
    # function that checks intersection of ray and plane
    # and return the length of the ray
    t = (plane[0] * vx + plane[1] * vy + plane[2] * vz)
    if t == 0:
        return 1700
    return (-(plane[0] * x0 + plane[1] * y0 + plane[2] * z0 + plane[3])) / t


gradient = " .:!/r(l1Z4H9W8$@"

plane = [0, 0, 1, -2]
r = 1
p = 0


# for correct work better use parameters 80 24 11 25
screenWidth = int(input("Enter screen width: "))
screenHeight = int(input("Enter screen height: "))
letterWidth = int(input("Enter letter width: "))
letterHeight = int(input("Enter letter height: "))

while True:
    a = [[' '] * screenWidth + ['\n'] for k in range(screenHeight)]

    # animation of moving

    xx = m.sin(p) * 5
    zz = m.cos(p) * 5

    for i in range(screenWidth):
        for j in range(screenHeight):

            # ray direction

            x = i / screenWidth * 2 - 1
            z = j / 62 * 2 - 1
            x *= (screenWidth / screenHeight) * (letterWidth / letterHeight)

            ray = sphere(xx, 5, zz, 2, 0, 0, 0, x, 1, z)

            if ray < 16:
                if int(ray) < 0:
                    a[j][i] = gradient[0]
                else:
                    a[j][i] = gradient[16 - int(ray)]
            else:

                ray = sphere(-xx, 5, -zz, 2, 0, 0, 0, x, 1, z)
                if ray < 16:
                    if ray < 0:
                        a[j][i] = gradient[0]
                    else:
                        a[j][i] = gradient[16 - int(ray)]
                else:
                    ray = sphere(-xx, 5, zz, 2, 0, 0, 0, x, 1, z)
                    if ray < 16:
                        if ray < 0:
                            a[j][i] = gradient[0]
                        else:
                            a[j][i] = gradient[16 - int(ray)]
                    else:
                        ray = sphere(xx, 5, -zz, 2, 0, 0, 0, x, 1, z)
                        if ray < 16:
                            if ray < 0:
                                a[j][i] = gradient[0]
                            else:
                                a[j][i] = gradient[16 - int(ray)]
                        else:
                            ray = sphere(-xx, 5, 0, 3, 0, 0, 0, x, 1, z)
                            if ray < 16:
                                if ray < 0:
                                    a[j][i] = gradient[0]
                                else:
                                    a[j][i] = gradient[16 - int(ray)]
                            else:
                                ray = sphere(0, 5, -zz, 3, 0, 0, 0, x, 1, z)
                                if ray < 16:
                                    if ray < 0:
                                        a[j][i] = gradient[0]
                                    else:
                                        a[j][i] = gradient[16 - int(ray)]
                                else:
                                    ray = intersects(0, 0, 0, x, 1, z)
                                    if ray < 16:
                                        if ray < 0:
                                            a[j][i] = gradient[0]
                                        else:
                                            a[j][i] = gradient[16 - int(ray)]
    print("\033[H\033[J")
    for i in range(-screenHeight, -1):
        print(''.join(a[i]), end="")

    p += 0.1

# to implement full 3d this code needs formula of intersection ray and finite plane
