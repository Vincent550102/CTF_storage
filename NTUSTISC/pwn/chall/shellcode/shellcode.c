#include <stdio.h>

// gcc -fno-stack-protector -z execstack -o shellcode_nx shellcode.c 
// gcc -fno-stack-protector -o shellcode shellcode.c 

void init()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

int main()
{
    char buf[100] = { 0 };

    init();
    printf("[DEBUGING] buf: %p\n", buf);
    printf("Hi! What's Your name?\n");
    read(0, buf, 0x100);
    printf("I don't know you, so bye ;)\n");

    return 0;
}