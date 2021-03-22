#include<bits/stdc++.h>
using namespace std;
//using ll = long long;
#define ll long long
const ll MOD = 4294967295;

ll a = 597130609;
ll b = 0;
/*
void L2();

void L4(){
    if((a&1) != 0){
        b=(b+3)%MOD;
    }
    a=((a%MOD)<<1)%MOD;
    L2();
    return;
}

void L2(){ 
    cerr << a << endl;
    if(a!=0){
        L4();
    }
    return;
}*/

signed main(){
    while(a!=0){
        cerr << a << " " <<b<< endl;
        if(a&1){
            b+=3;
        }
        a = (a>>1);
    }
    //string t = "5"; 
    cout << b;
}
