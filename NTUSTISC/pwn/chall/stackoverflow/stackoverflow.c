#define MAX_LENGTH 100
#include <stdio.h>

// gcc stackoverflow.c -o stackoverflow

void init()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

void backdoor()
{
    system("/bin/sh");
}

int main()
{
    char buf[10] = { 0 };

    init();
    printf("[DEBUGING] main: %p\n", main);
    printf("Hello, What's Your name?\n");

    read(0, buf, MAX_LENGTH);

    printf("%s", buf);
    printf("Welcome!\n");
    printf("But wait, WHO ARE YOU?\n");

    read(0, buf, MAX_LENGTH);

    printf("I don't know you, so bye ;)\n");

    return 0;
}

