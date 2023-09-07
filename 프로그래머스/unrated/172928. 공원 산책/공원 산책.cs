using System.Collections.Generic;

public class Solution
{
    public int[] solution(string[] park, string[] routes)
    {
        int N = park.Length;
        int M = park[0].Length;

        int x = 0;
        int y = 0;

        for (int i = 0; i < N; i++)
        {
            if (park[i].Contains('S'))
            {
                x = i;
                y = park[i].IndexOf('S');
            }
        }

        Dictionary<char, int> ewsn = new Dictionary<char, int>() { { 'E', 0 }, { 'W', 1 }, { 'S', 2 }, { 'N', 3 } };
        int[,] dir = new int[4, 2] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        foreach (string route in routes)
        {
            int dx = dir[ewsn[route[0]], 0];
            int dy = dir[ewsn[route[0]], 1];
            
            int nx = x;
            int ny = y;
            
            bool able = true;
            
            for (int i = 0; i < int.Parse(route.Split()[1]); i++)
            {
                nx += dx;
                ny += dy;
                
                if (nx < 0 || nx >= N || ny < 0 || ny >= M || park[nx][ny] == 'X')
                {
                    able = false;
                    break;
                }
            }
            
            if (able)
            {
                x = nx;
                y = ny;
            }
        }

        return new int[] { x, y };
    }
}