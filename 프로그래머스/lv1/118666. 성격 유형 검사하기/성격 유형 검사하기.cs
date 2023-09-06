using System;
using System.Collections.Generic;

public class Solution
{
    public string solution(string[] survey, int[] choices)
    {
        string answer = "";
        string type = "RCJATFMN";
        int[] count = new int[8] { 0, 0, 0, 0, 0, 0, 0, 0 };
        Dictionary<string, int> idx = new Dictionary<string, int>() { { "RT", 0 }, { "CF", 1 }, { "JM", 2 }, { "AN", 3 }, { "TR", 4 }, { "FC", 5 }, { "MJ", 6 }, { "NA", 7 } };

        for (int i = 0; i < survey.Length; i++)
        {
            count[idx[survey[i]]] += (4 - choices[i]);
        }

        for (int i = 0; i < 4; i++)
        {
            answer += (count[i] >= count[i + 4]) ? type[i] : type[i + 4];
        }


        return answer;
    }
}