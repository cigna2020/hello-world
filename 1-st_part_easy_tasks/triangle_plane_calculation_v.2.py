from math import sqrt, acos, degrees


def compute_len(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area

def compute_angle(a_1, a_2, a_3):
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2) /
                     (2 * a_1 * a_2))
    return degrees(angle_rad)

x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a + c <= b:
    print("error")
else:
    s = compute_area(a, b, c)
    p = a + b + c

    r = (sqrt(((p/2-a) * (p/2-b)*(p/2-c))/(p/2)))
    R = (a*b*c)/(4*s)
    Ma = 1/2 *sqrt(2*(c**2+b**2) - a**2)
    Mb = 1/2 *sqrt(2*(a**2+c**2) - b**2)
    Mc = 1/2 *sqrt(2*(a**2+b**2) - c**2)
    M = Ma + Mb + Mc

    print(round(r, 4), round(R, 4), round(M, 4))