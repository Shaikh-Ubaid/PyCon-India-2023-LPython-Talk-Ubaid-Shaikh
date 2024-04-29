def sayHi():
    print("Hi")

def add(a: i32, b: i32) -> i32:
    ...

T = TypeVar('T')
@restriction
def sub(x: T, y: T) -> T:
    ...

def f(a: In[Student], b: InOut[f32[:]]):
    ...

@lpython(backend="c", backend_optimisation_flags=["-ffast-math"])
def g(n: i32):
    ...

@pythoncall(module="email_extractor_util")
def get_email(text: str) -> str:
    ...
