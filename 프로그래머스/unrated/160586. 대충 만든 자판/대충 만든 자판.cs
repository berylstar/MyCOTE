using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] keymap, string[] targets) {
        Dictionary<char, int> d = new Dictionary<char, int>();
        
        foreach (string key in keymap)
        {
            for (int i = 0; i < key.Length; i++)
            {
                if (d.ContainsKey(key[i]))
                    d[key[i]] = Math.Min(d[key[i]], i + 1);
                else
                    d[key[i]] = i + 1;
            }
        }
        
        List<int> answer = new List<int>();
        
        foreach (string target in targets)
        {
            int temp = 0;
            
            foreach (char c in target)
            {
                if (d.ContainsKey(c))
                    temp += d[c];
                else
                {
                    temp = -1;
                    break;
                }
            }
            
            answer.Add(temp);
        }
        
        return answer.ToArray();
    }
}