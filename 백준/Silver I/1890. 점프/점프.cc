#include <iostream>
using namespace std;

int N;
int graph[100][100];
long long dp[100][100];

int main()
{
    cin >> N;
    
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> graph[i][j];
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (dp[i][j] == 0 || (i == N-1 && j == N-1)) continue;
            
            if (j + graph[i][j] < N)
                dp[i][j + graph[i][j]] += dp[i][j];
            
            if (i + graph[i][j] < N)
                dp[i + graph[i][j]][j] += dp[i][j];
        }
    }
    
    cout << dp[N-1][N-1] << endl;
    return 0;
}