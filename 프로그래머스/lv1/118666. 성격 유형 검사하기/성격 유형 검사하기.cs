using System;
using System.Collections.Generic;

public class Solution
{
    public string solution(string[] survey, int[] choices)
    {
        string answer = "";
        string type = "RCJATFMN";
        int[] count = new int[8] { 0, 0, 0, 0, 0, 0, 0, 0 };
        Dictionary<string, int> val = new Dictionary<string, int>() { { "RT", 1 }, { "CF", 1 }, { "JM", 1 }, { "AN", 1 }, { "TR", -1 }, { "FC", -1 }, { "MJ", -1 }, { "NA", -1 } };
        Dictionary<string, int> idx = new Dictionary<string, int>() { { "RT", 0 }, { "CF", 1 }, { "JM", 2 }, { "AN", 3 }, { "TR", 4 }, { "FC", 5 }, { "MJ", 6 }, { "NA", 7 } };

        for (int i = 0; i < survey.Length; i++)
        {
            Console.WriteLine($"{survey[i]} {idx[survey[i]]} {(4 - choices[i])}");
            count[idx[survey[i]]] += (4 - choices[i]);
        }
        
        Console.WriteLine();
        
        for (int i = 0; i < 8; i++)
        {
            Console.WriteLine($"{i} {count[i]} {type[i]}");
        }

        for (int i = 0; i < 4; i++)
        {
            if (count[i] >= count[i + 4])
                answer += type[i];
            else
                answer += type[i + 4];
        }

        
        return answer;
    }
}