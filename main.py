from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4,4)
print("Regular matrix:")
print_matrix(matrix)
print("Identity Matrix:")
ident_matrix = new_matrix(4,4)
ident(ident_matrix)
print("Multiplying regular and identity matrices:")
matrix_mult(ident_matrix, matrix)

m1 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
m2 = [[5,6],[1,2],[5,6],[1,2]]
print("M1:")
print_matrix(m1)
print("M2:")
print_matrix(m2)
print("Multiplying m1 and m2. Results in m2:")
m2 = matrix_mult(m1,m2)



#########Edges and other

edge_mat = [[140, 201, 40, 20], [20, 32, 19, 8], [18, 43, 8, 23], [43, 12, 32, 12]]
print("Printing edge matrix:")
print_matrix(edge_mat)
print("Adding point (0,2) to edge matrix:")
add_point(edge_mat, 0, 2, 0)
print_matrix(edge_mat)
for i in range(0, 400): 
    add_edge(edge_mat, 10, 10, 2, i, 404, 0)
print("Would print edge matrix with new edges but there are far too many")
draw_lines(edge_mat, screen, color)
for i in range(0, 100): 
    add_edge(edge_mat, 300, 400, 2, i, 404, 0)
draw_lines(edge_mat, screen, [ 21, 255, 43 ])
display(screen)
