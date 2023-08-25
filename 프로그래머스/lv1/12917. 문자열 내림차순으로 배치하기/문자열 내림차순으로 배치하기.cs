using System;
public class Solution {
    public string solution(string s)
    {
        char[] ss = s.ToCharArray();

        Array.Sort(ss);
        Array.Reverse(ss);

        return new string(ss);
    }
}