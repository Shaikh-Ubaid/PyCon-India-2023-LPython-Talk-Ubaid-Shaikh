from lpython import i32
from  numpy import empty, int32

def main0():
    x: i32 # i32 represents int32
    x = (2+3)*5
    print(x)

    a: i32[5] = empty([5], dtype=int32)
    print(a)

if __name__ == "__main__":
   main0()
