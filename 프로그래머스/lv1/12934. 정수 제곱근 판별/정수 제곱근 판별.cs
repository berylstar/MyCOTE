using System;
public class Solution {
    public long solution(long n)
    {
        if (Math.Pow(n, 0.5f) % 1 > 0)
            return -1;
        else
            return (long)Math.Pow((Math.Pow(n, 0.5f) + 1), 2);
    }
}