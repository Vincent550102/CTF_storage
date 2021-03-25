#include<bits/stdc++.h>
using namespace std;
using ll = long long;
ll w0;
vector<ll> mem[9];

void func1();

void func8(){
    //int it = mem[8].size();
    mem[8].push_back(w0);
    w0+=2;
    return;
}

void func7(){
    //int it = mem[7].size();
    mem[7].push_back(w0);
    if(w0 <=100){
        w0 = 7;
    }
    return;
}

void func5(){
    int it = mem[5].size();
    mem[5].push_back(w0);
    func8();
    mem[5][it+0]=w0;
    return;
}

void func4(){
    int it = mem[4].size();
    mem[4].push_back(w0);
    w0 = 17;
    mem[4].push_back(w0);
    func1();
    mem[4][it+1] = w0;
    return;
}

void func3(){
    //int it = mem[3].size();
    mem[3].push_back(w0);
    func7();
    return;
}

void func2(){
    int it = mem[2].size();
    mem[2].push_back(w0);
    if(w0 > 499){
      w0=mem[2][it+0];
      w0+=13;
      func5();
      return;
    }
    w0 = mem[2][it+0];
    w0 -= 86;
    func4();
    return;
}

void func1(){
    int it = mem[1].size();
    cout << it << endl; 
    mem[1].push_back(w0);
    if(w0 <= 100){
        w0 = mem[1][it+0];
        func3();
        return;
    }
    w0=mem[1][it+0];
    w0 += 100;
    func2();
    return;
}

int main(){
    w0 = 1151828495;
    func1();
    cout << w0;
}
