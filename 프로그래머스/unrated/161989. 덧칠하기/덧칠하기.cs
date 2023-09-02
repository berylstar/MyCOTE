using System;
public class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int now = 0;
        
        foreach (int sect in section)
        {
            if (now < sect)
            {
                now = sect + m - 1;
                answer += 1;
            }
        }
        
        return answer;
    }
}