#include<bits/stdc++.h>
using namespace std;

constexpr int mxN = 1e6;

bool is_prime(int n){
    for(int i = 2; i<=sqrt(n); i++){
        if(n%i==0)return 0;
    }
    return 1;
}

int digit_sum(int n){
    int sum = 0;
    while(n){
        sum+=n%10;
        n/=10;
    }
    return(sum);
}

int main(){
   int cnt = 0;
   string ans = "";
   for(int i = mxN; i; i++){
       if(cnt == 2) break;
       if(is_prime(i) and is_prime(digit_sum(i))){
           cnt++;
           ans+= to_string(i);
       }
   }
   cout << ans << endl;
}
