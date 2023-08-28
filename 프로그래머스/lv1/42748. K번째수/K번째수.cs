using System.Collections.Generic;
using System.Linq;
public class Solution
{
    public int[] solution(int[] array, int[,] commands)
    {
        List<int> answer = new List<int>();

        for (int i = 0; i < commands.GetLength(0); i++)
        {
            int start = commands[i, 0];
            int end = commands[i, 1];
            int idx = commands[i, 2];

            List<int> newList = new List<int>();
            for (int j = start - 1 ; j < end; j++)
            {
                newList.Add(array[j]);
            }

            answer.Add(newList.OrderBy(c => c).ToArray()[idx - 1]);
        }

        return answer.ToArray();
    }
}