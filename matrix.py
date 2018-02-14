import math


def print_matrix( matrix ):
    for c in matrix:
        for wow in c:
            print str(wow) + " ",
        print "\n"
    pass

def ident( matrix ):
    n = 0
    for cool in matrix:
        for oh in range(0, len(cool)):
            if oh == n:
                cool[oh] = 1
            else:
                cool[oh] = 0
            oh += 1
        n += 1
    print_matrix(matrix)            
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

ident(new_matrix())
