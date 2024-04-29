void main0()
{
    int32_t x;
    int32_t y;
    x = 5;
    y = 3;
    printf("%d%s%d\n", x, " ", y);
    printf("%d\n", add(x, y));
}

void __main__global_stmts()
{
    main0();
}

int main(int argc, char* argv[])
{
    _lpython_set_argv(argc, argv);
    __main__global_stmts();
    return 0;
}