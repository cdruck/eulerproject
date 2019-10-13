

def main():
    r =  range(1,101)
    sosq = sum([i**2 for i in r])
    sqos = sum(r)**2
    print(-sosq + sqos)

main()
