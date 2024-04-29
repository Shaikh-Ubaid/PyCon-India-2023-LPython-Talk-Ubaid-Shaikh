from lpython import i32

def add(a: i32, b: i32) -> i32:
    return a + b

def main0():
    x: i32 = 5
    y: i32 = 3
    print(x, y)

    print(add(x, y))

main0()
