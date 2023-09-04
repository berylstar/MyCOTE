using System;
using System.Collections.Generic;

public class Solution
{
    public int solution(string[] babbling)
    {
        Dictionary<string, string> dict = new Dictionary<string, string>() { {"ayaaya", "x"}, { "yeye", "x" }, { "woowoo", "x" }, { "mama", "x" }, { "aya", "1" }, { "ye", "1" }, { "woo", "1" }, { "ma", "1" } };

        int answer = 0;

        for (int i = 0; i < babbling.Length; i++)
        {
            string now = babbling[i];

            foreach (string key in dict.Keys)
            {
                now = now.Replace(key, dict[key]);
            }

            answer += int.TryParse(now, out int result) ? 1 : 0;
        }

        return answer;
    }
}