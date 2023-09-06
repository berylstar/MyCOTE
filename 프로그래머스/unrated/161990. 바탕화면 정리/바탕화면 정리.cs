using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int[] solution(string[] wallpaper)
    {
        List<int> x = new List<int>();
        List<int> y = new List<int>();

        for (int i = 0; i < wallpaper.Length; i++)
        {
            for (int j = 0; j < wallpaper[0].Length; j++)
            {
                if (wallpaper[i][j] == '#')
                {
                    x.Add(i);
                    y.Add(j);
                }
            }
        }

        return new int[] { x.Min(), y.Min(), x.Max() + 1, y.Max() + 1};
    }
}