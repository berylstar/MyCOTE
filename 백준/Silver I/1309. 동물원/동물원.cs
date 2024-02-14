using System;

namespace MySolution
{
    class Program
    {
        static void Main()
        {
            int N = int.Parse(Console.ReadLine());
            int[] dp = new int[N+2];
            dp[1] = 3;
            dp[2] = 7;
            for (int i = 3; i < N+1; i++)
            {
                dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901;
            }
            
            Console.WriteLine(dp[N]);
        }
    }
}