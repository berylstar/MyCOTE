using System.Collections.Generic;
using System;
using System.Linq;
public class Solution
{
    public int[] solution(int[] answers)
    {
        int[][] student = new int[3][] { new int[] { 1, 2, 3, 4, 5 }, new int[] { 2, 1, 2, 3, 2, 4, 2, 5 }, new int[] { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 } };
        int[] score = new int[3] { 0, 0, 0 };

        for (int i = 0; i < answers.Length; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                score[j] += (answers[i] == student[j][i % student[j].Length]) ? 1 : 0;
            }
        }

        List<int> answer = new List<int>();
        for (int i = 0; i < 3; i++)
        {
            if (score[i] == score.Max())
            {
                answer.Add(i + 1);
            }
        }
        return answer.ToArray();
    }
}