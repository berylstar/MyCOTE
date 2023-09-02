public class Solution {
    public int solution(int number, int limit, int power) {
        number += 1;
        int[] dp = new int[number];
        
        for (int i = 1; i < number; i++)
        {
            for (int j = i; j < number; j += i)
            {
                dp[j] += 1;
            }
        }
        
        int answer = 0;
        
        foreach (int num in dp)
        {
            answer += (num > limit)? power : num;
        }
        
        return answer;
    }
}