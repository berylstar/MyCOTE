using System;
public class Solution {
    public int GCD(int a, int b)
    {
        if (a % b == 0)
            return b;
        else
            return GCD(b, a % b);
    }
    
    public int[] solution(int n, int m) {
        int a = Math.Max(n, m);
        int b = Math.Min(n, m);
        return new int[] { GCD(a, b), a * b / GCD(a, b) };
    }
}