using System;
namespace MySolution
{
    class Solution
    {
        public static void Main()
        {
            int N = int.Parse(Console.ReadLine());
            int[] dp = new int[10];
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
            for (int i = 0; i < 10; i++)
            {
                answer += dp[i];
                answer %= 10007;
            }

            Console.WriteLine(answer);
        }
    }
}