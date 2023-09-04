using System;

public class Solution
{
    public string solution(string X, string Y)
    {
        int[] xx = new int[10];
        int[] yy = new int[10];

        foreach (char s in X)
            xx[int.Parse(s.ToString())] += 1;

        foreach (char s in Y)
            yy[int.Parse(s.ToString())] += 1;

        string answer = "";

        for (int i = 9; i >= 0; i--)
            answer += new string((char)(i + '0'), Math.Min(xx[i], yy[i]));
        
        if (answer == "")
            return "-1";
        else if (answer[0] == '0')
            return "0";
        else
            return answer;
    }
}