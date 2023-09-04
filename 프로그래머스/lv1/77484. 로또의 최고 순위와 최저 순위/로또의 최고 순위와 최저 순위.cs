using System;
using System.Linq;

public class Solution
{
    public int[] solution(int[] lottos, int[] win_nums)
    {
        int corr = 0;
        int zero = 0;

        foreach (int num in lottos)
        {
            if (win_nums.Contains(num))
                corr += 1;

            else if (num == 0)
                zero += 1;
        }

        return new int[] { Math.Min(6, 7 - corr - zero), Math.Min(6, 7 - corr) };
    }
}