#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int cards[N];
    int dp[N+1];
    
    for (int i = 0; i < N; i++)
    {
        cin >> cards[i];
        dp[i] = 0;
    }
    dp[N] = 0;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            if (dp[i] <= cards[j-1] + dp[i-j])
            {
                dp[i] = cards[j-1] + dp[i-j];
            }
        }
    }

    cout << dp[N];

    return 0;
}