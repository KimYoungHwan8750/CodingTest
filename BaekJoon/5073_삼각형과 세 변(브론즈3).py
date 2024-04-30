while True:
    X, Y, Z = map(int, input().split())
    if X | Y | Z == 0:
        break
    XYZ = [X, Y, Z]
    max_ = max(XYZ)
    other = 1
    o = []
    for i, value in enumerate(XYZ):
        if max_ == value:
            XYZ.pop(i)
            break
    if max_ >= XYZ[0]+XYZ[1]:
        print("Invalid")
    elif X == Y and Y == Z:
        print("Equilateral")
    elif X == Y or X == Z or Y == Z:
        print("Isosceles")
    else:
        print("Scalene")

