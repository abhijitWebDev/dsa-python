
# Method definition
def isCollinearPoints(x1, x2, x3, y1, y2, y3):
    if((y2 - y1) * (x3-x2) == (y3 - y2) * (x2-x1)):
        print("Given points are collinear")
    else:
        print("Given points are non collinear")

# Approach two : By calculate area of triangle

def isCollinearPointsNew(x1, x2, x3, y1, y2, y3):
    area = 0.5 * (x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
    print("Area is" , area)
    if(area == 0):
        print("The points are collinear")
    else:
        print("The points are non collinear")





# Driver code
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9
isCollinearPoints(x1, x2, x3, y1, y2, y3)

p1, p2, p3, q1, q2, q3 = 1, 2, 3, 6, 0, 9
isCollinearPointsNew(p1, p2, p3, q1, q2, q3)