#You are given three integers  "x, y, z" representing the dimensions of a cuboid along with an integer "n". Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i,j,k) is not equal to "n".

def task(x,y,z,n):
    first_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    second_list = [i for i in first_list if sum(i) != n]
    print(second_list)

task(1,1,2,3)