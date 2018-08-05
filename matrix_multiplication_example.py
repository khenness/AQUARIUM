import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))


print("kevins stuff:")
#video time 13.45
m1 = np.array([[1,0,4],
               [0,1,-3],
               [0,0,1]])

m2 = np.array([[2],
               [6],
               [1]])

print(np.dot(m1,m2))



def translate(x,y, a,b):
    #x and y are the point to be translated, a and b are the translations in the x direction and y direction
    # video time 13.45
    m1 = np.array([[1, 0, a],
                   [0, 1, b],
                   [0, 0, 1]])
    m2 = np.array([[x],
                   [y],
                   [1]])

    return(np.dot(m1, m2))


print("translate(2,6,4,-3) =\n"+str(translate(2,6,4,-3)))


def scale_point(x,y, s,t):
    m1 = np.array([[s, 0, 0],
                   [0, t, 0],
                   [0, 0, 1]])
    m2 = np.array([[x],
                   [y],
                   [1]])

    return(np.dot(m1, m2))

print("scale_point(2,6,2,0.5) =\n"+str(scale_point(2,6,2,0.5)))
print("scale_point(6,8,2,0.5) =\n"+str(scale_point(6,8,2,0.5)))


#def scale_line():