using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr) {
        if (arr.Length == 1)
            return new int[] { -1 };
        
        int min = arr.Min();
        return arr.Where(num => num > min).ToArray();
    }
}