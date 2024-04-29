#include <inttypes.h>

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <lfortran_intrinsics.h>

int32_t add(int32_t a, int32_t b);
void main0();
void __main__global_stmts();



// Implementations
int32_t add(int32_t a, int32_t b)
{
    int32_t _lpython_return_variable;
    _lpython_return_variable = a + b;
    return _lpython_return_variable;
}