import math


def print_matrix( matrix ):
    for c in matrix:
        for wow in c:
            print str(wow) + "\t",
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
    mtemp = new_matrix(len(m2[0]), len(m2))
    for row in range(0, len(m1)):
        for col in range(0, len(m2[0])):
            for row2 in range(0, len(m2)):
                mtemp[row][col] += m1[row][row2] *m2[row2][col]
    m2 = mtemp
    print_matrix(m2)
    pass




def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

###TEST CALLS

#ident(new_matrix(4,4))

#m1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#m2 = [[1,2],[2,4],[7,8],[9,10]]

#print_matrix(m2)

#matrix_mult(m1,m2)
