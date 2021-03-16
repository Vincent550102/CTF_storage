#include<iostream>
// using namespace std;

int foo(int n){
    return n+2;
}
int main(){
    int a = 0;
    for(int i = 0; i<5; i++){
        int tmp = foo(i);
        a += tmp;
    }
    std::cout << a; 
}
