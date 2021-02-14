def pascal_triangle(n):
    for i in range(n):
        for j in range(i+1):
            if(j==i):
                print(bin_coeff(i,j), end="\n")
            else:
                print(bin_coeff(i,j), end=" ")

def bin_coeff(n, r):
    if(r==0):
        return 1
    elif(n==0):
        return 0
    else:
        return(bin_coeff(n-1, r) + bin_coeff(n-1, r-1))

if __name__=="__main__":
    pascal_triangle(5)
