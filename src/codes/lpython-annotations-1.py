a: i32
b: i64 # similarly i8, i16
c: u32
d: u64 # similarly for u8, u16
e: f32
f: f64
g: c32
h: c64

i: bool 
j: Const[i32] = 5 # similarly other types
k: CPtr
l: i32[5] = empty([5], dtype=int32)
m: Allocatable[i32[:]] = empty([n], dtype=int32)

n: list[f32]
o: tuple[i32, i64, str]

@dataclass
class Student:
    name: str