#include<iostream>

int main(){
    int *here = new int();
    auto tmp = *(here);
    std::cout <<tmp;
    delete(here);
}
