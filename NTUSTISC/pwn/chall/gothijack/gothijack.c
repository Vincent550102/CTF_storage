#include <stdio.h>

// gcc gothijack.c -o gothijack -z lazy

unsigned long long array[0x100];

void init()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

void menu()
{
    printf("1: set\n");
    printf("2: get\n");
}

int main()
{
    char buf[0x100] = { 0 };
    int choice;
    int idx;
    unsigned long long value;

    init();

    while (1) {
        menu();
        scanf("%256s", buf);
        choice = atoi(buf);

        printf("idx:\n");
        scanf("%d", &idx);

        if (choice == 1) {
            printf("value:\n");
            scanf("%llu", &value);
            array[idx] = value;
        } else if (choice == 2) {
            printf("%#llx\n", array[idx]);
        }
    }

    exit(1);
}
