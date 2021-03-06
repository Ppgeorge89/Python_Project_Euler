import time
import sys

def main():
    try:
        start_time = time.time()
        for i in range(1, 1000):
            for j in range(i, 1000):
                for k in range(j, 1000):
                    if i + j + k == 1000:
                        if i**2 + j**2 == k**2:
                            print(i, j, k, "is the pythagorean triplet")
                            print(i*j*k)
                            break

    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()

    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()












    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
     main()
