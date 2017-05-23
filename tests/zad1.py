import sys

def suma(a,b):
	return a+b
def main(a,b):
	res = suma(a,b)
	print(res)

if __name__ == '__main__':
    if len(sys.argv) > 2 :
        main(int(sys.argv[1]),int(sys.argv[2]))