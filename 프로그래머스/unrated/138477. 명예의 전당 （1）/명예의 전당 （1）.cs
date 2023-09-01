using System.Collections.Generic;

public class Solution
{
    public class Heapq
    {
        public int Count => heapq.Count;
        private List<int> heapq;

        public Heapq () { heapq = new List<int>(); }

        public int[] Min()
        {
            int min = 2001;
            int idx = -1;
            for (int i = 0; i < heapq.Count; i++)
            {
                if (heapq[i] < min)
                {
                    idx = i;
                    min = heapq[i];
                }
            }
            return new int[] { idx, min };
        }

        public void Pop() => heapq.RemoveAt(Min()[0]);

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
            answer.Add(heapq.Min()[1]);
        }

        return answer.ToArray();
    }
}