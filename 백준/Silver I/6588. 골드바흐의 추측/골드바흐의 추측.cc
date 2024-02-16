#include <iostream>
 
using namespace std;
 
const int MAX = 1000000;
 
bool primeArr[MAX] = {false, };
 
void primeChk(){
    
    for(int i = 2; i*i<=MAX; i++){
        
        if(!primeArr[i]){
        
            for(int j = i*i; j<=MAX; j+=i){
                primeArr[j] = true;
            }
        }
        
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    primeChk();
 
    
    while(1){
        
        cin >> n;
        if(n==0){
            break;
        }
                   
        bool chk = false;
        
        for(int a = 3; a<= n; a+=2){
            if(!primeArr[a] && !primeArr[n-a]) {
                cout << n << " = " << a << " + " << n-a << "\n";
                chk = true;
                break;
            }
        }
        if(!chk){
            cout << "Goldbach's conjecture is wrong.\n";
        }
    }
  
    
    return 0;
}