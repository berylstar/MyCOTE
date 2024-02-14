#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    
    int dp[10] = {0};
    dp[0] = 1;

    for (int i = 0; i < N; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            dp[j] += dp[j-1];
            dp[j] %= 10007;
        }
    }

    int answer = 0;
    
    for (int k = 0; k < 10; k++)
    {
        answer += dp[k];     
        answer %= 10007;
    }

    cout << answer;
    return 0;
}