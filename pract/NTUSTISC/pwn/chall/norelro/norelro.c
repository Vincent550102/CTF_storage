#include <stdio.h>

// gcc norelro.c -o norelro -z lazy

void init()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

int main()
{
    init();

    printf("hello\n");
    printf("my friend.\n");

    return 0;
}
