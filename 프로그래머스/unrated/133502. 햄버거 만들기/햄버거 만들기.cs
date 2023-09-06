using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        List<int> temp = new List<int>();
        
        foreach (int v in ingredient)
        {
            temp.Add(v);
            
            if (temp.Count < 4)
                continue;
            
            if (temp[temp.Count - 4] == 1 && temp[temp.Count - 3] == 2 && temp[temp.Count - 2] == 3 && temp[temp.Count - 1] == 1)
            {
                temp.RemoveRange(temp.Count - 4, 4);
                answer += 1;
            }
        }
        return answer;
    }
}