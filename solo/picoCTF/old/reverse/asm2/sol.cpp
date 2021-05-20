#include<bits/stdc++.h>
using namespace std;
#define dword u_int32_t

int main(){
    dword v1 = 46, v2 = 11;
    // v1 = [ebp-0x4] 0x2e, v2 = [ebp-0x8] 0xb
    while(v2 <= 25587){
        v1++;
        v2-=4294967168;
        //cout << v2 << endl;
    }
    cout << v1 << endl;
    /*
    dword tmp = 1;
    cout << tmp -2;
    */
}
