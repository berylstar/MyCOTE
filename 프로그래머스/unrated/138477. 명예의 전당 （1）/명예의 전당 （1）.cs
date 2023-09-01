using System.Collections.Generic;
public class Solution
{
    public class Heapq
    {
        public int Count => heapq.Count;
        private List<int> heapq;

        public Heapq () { heapq = new List<int>(); }

        public int Min
        {
            get
            {
                int min = int.MaxValue;
                for (int i = 0; i < heapq.Count; i++)
                {
                    if (heapq[i] < min)
                    {
                        min = heapq[i];
                    }
                }
                return min;
            }
        }

        public void Pop() => heapq.Remove(Min);

        public void Push(int num) => heapq.Add(num);
    }

    public int[] solution(int k, int[] score)
    {
        Heapq heapq = new Heapq();
        List<int> answer = new List<int>();

        foreach (int s in score)
        {
            heapq.Push(s);
            if (heapq.Count > k)
                heapq.Pop();
            answer.Add(heapq.Min);
        }

        return answer.ToArray();
    }
}