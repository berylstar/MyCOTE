using System;

class Solution
{
    bool IsPrime(int num)
    {
        for (int i = 2; i < Math.Sqrt(num) + 1; i++)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }

    public int solution(int[] nums)
    {
        int answer = 0;

        for (int i = 0; i < nums.Length - 2; i++)
        {
            for (int j = i + 1; j < nums.Length - 1; j++)
            {
                for (int k = j + 1; k < nums.Length; k++)
                {
                    answer += (IsPrime(nums[i] + nums[j] + nums[k])) ? 1 : 0;
                }
            }
        }
        return answer;
    }
}