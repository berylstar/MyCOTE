using System.Collections.Generic;

public class Solution
{
    public int[] solution(string s)
    {
        List<int> answer = new List<int>();
        Dictionary<char, int> dict = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++)
        {
            int now = dict.ContainsKey(s[i]) ? i - dict[s[i]] : -1;
            answer.Add(now);

            dict[s[i]] = i;
        }

        return answer.ToArray();
    }
}