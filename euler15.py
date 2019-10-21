import math


def main():
  # no need for much code here, it just corresponds to the bag of balls, 20 white, 20 black, and you keep picking
  # until the bag is empty -->
  # 40! / 20! ** 2
  print(math.factorial(40) / math.factorial(20)**2)


main()
