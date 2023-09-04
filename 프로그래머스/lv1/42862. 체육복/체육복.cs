using System.Collections.Generic;
using System;
using System.Linq;
public class Solution
{
    public int solution(int n, int[] lost, int[] reserve)
    {
        Array.Sort(lost);
        List<int> l = lost.ToList();
        Array.Sort(reserve);
        List<int> r = reserve.ToList();

        List<int> g = new List<int>();

        foreach (int num in l)
        {
            if (r.Contains(num))
            {
                g.Add(num);
            }
        }

        foreach (int num in g)
        {
            l.Remove(num);
            r.Remove(num);
        }

        int answer = n;

        foreach (int num in l)
        {
            if (r.Contains(num - 1))
                r.Remove(num - 1);
            else if (r.Contains(num + 1))
                r.Remove(num + 1);
            else
                answer -= 1;
        }

        return answer;
    }
}