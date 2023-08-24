using System.Collections.Generic;
public class Solution {
    public int[] solution(int[] arr, int divisor)
    {
        List<int> list = new List<int>();
        foreach (int num in arr)
            if (num % divisor == 0)
                list.Add(num);

        if (list.Count > 0)
            list.Sort();
        else
            return new int[] { -1 };

        return list.ToArray();
    }
}