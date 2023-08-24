using System;
public class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int c = Math.Min(a, b);
        int d = Math.Max(a, b);
        
        for (int i = c; i <= d; i++)
        {
            answer += i;
        }
        
        return answer;
    }
}