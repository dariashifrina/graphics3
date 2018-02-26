from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    row = matrix[0]
    row2 = matrix[1]
    for i in range(len(row) - 1): 
        draw_line(row[i], row2[i], row[i+1], row2[i+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    pass

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)
    pass

#m1

def draw_line( x, y, x1, y1, screen, color ):
    x0 = x
    y0 = y
    #chck if vertical line
    if(x1 - x0 == 0):
        if(y0 < y1):
            while( y0 < y1):
                plot(screen, color, x0, y0)
                y0 += 1
            else:
                while y0 >= y1:
                    plot(screen, color, x0, y0)
                    y0 -= 1
    else:
        slope = (float(y1)-y0)/(x1-x0)
        a = y1 - y0
        b = -1 * (x1 - x0)
        if b>=0:
            px0 = x0
            py0 = y0
            px1 = x1
            py1 = y1
            x1 = px0
            y1 = py0
            x0 = px1
            y0 = py1           
        if((slope >= 0) and (slope <= 1)): #oct1&5
            d = 2*a + b
            while x0 <= x1:
                plot(screen, color, x0,y0)
                if d > 0:
                    y0 += 1
                    d += 2 *b
                x0 += 1
                d += 2 * a
        elif(slope > 1): #oct2&4
            d = a + 2 * b
            while y0 <= y1:
                plot(screen, color, x0, y0)
                if d > 0:
                    x0 += 1
                    d += 2 *a
                y0 += 1
                d += 2 * b
        elif(slope < -1):
            d = a - 2 * b
            while( y0 >= y1):
                plot(screen, color, x0, y0)
                if( d > 0):
                    x0 += 1
                    d += 2 * a
                y0 -= 1
                d -= 2 * b

        elif( slope >= -1 and slope < 0):
            d = 2 * a - b
            while(x0 < x1):
                plot(screen, color, x0, y0)
                if(d < 0):
                    y0 -= 1
                    d -= 2 * b
                x0 += 1
                d += 2 * a
#end draw_line
