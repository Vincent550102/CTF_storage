#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include<iostream>
using namespace std;
int main(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    unsigned long long rax, rdi, rsi, rdx;
    scanf("%llu %llu %llu %llu", &rax, &rdi, &rsi, &rdx);
#define _ <<" "<<
    cout << rax _ rdi _ rsi _ rdx << endl;
    syscall(rax, rdi, rsi, rdx);
}
