using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string s, string skip, int index) {
        
        List<char> alphabet = new List<char>();
        
        foreach (char c in "abcdefghijklmnopqrstuvwxyz")
        {
            if (!skip.Contains(c))
                alphabet.Add(c);
        }
        
        string answer = "";
        
        foreach (char c in s)
        {
            answer += alphabet[(alphabet.IndexOf(c) + index) % alphabet.Count];
        }
        
        return answer;
    }
}