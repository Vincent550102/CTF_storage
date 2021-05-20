#define MAX_LENGTH 0x100
#include <stdio.h>

// gcc rop.c -o rop -static

void init()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

int main()
{
    char buf[10] = { 0 };

    init();
    puts("Hello, What's Your name?\n");

    read(0, buf, MAX_LENGTH);

    puts(buf);
    puts("Welcome!\n");
    puts("But wait, WHO ARE YOU?\n");

    read(0, buf, MAX_LENGTH);

    puts("I don't know you, so bye ;)\n");

    return 0;
}

