#include<iostream>
using namespace std;
int n=10,eight;
int rax,rdi;

void foo();

void L1(int rb){
    int rbx = rb;
    rbx--;
    rdi=rbx;
    foo();
    rax*=rb;
}          

void foo(){
    int rb;
    rb=rdi;
    if(rb!=1){
        L1(rb);
    }
    rax=1;
}


int main(){
    rax = n;
    rdi = rax;
    foo();
    cout << rax << endl;
}
