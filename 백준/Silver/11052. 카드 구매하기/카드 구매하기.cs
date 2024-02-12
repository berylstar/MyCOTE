using System;
namespace my
{
    class Program
    {
        static void Main()
        {
            int N = int.Parse(Console.ReadLine());
            string[] cards = Console.ReadLine().Split();
            int[] dp = new int[N+1];
            
            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    dp[i] = Math.Max(dp[i], int.Parse(cards[j-1]) + dp[i-j]);
                }
            }
            Console.WriteLine(dp[N]);
        }
    }
}