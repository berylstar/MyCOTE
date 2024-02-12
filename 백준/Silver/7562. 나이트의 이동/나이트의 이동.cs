using System;
using System.Collections.Generic;

namespace MyCompiler {
    class Program {
        static int[] dirX = {2, -2, 2, -2, 1, -1, 1, -1};
        static int[] dirY = {1, 1, -1, -1, 2, 2, -2, -2};
        static int L;
        static int targetX, targetY;
        static int [,] graph;

        static void BFS(int x, int y)
        {
            Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();
            queue.Enqueue(new Tuple<int, int>(x, y));

            while (queue.Count > 0)
            {
                Tuple<int, int> curr = queue.Dequeue();

                if (curr.Item1 == targetX && curr.Item2 == targetY)
                {
                    Console.WriteLine(graph[targetX, targetY]);
                    break;
                }

                for (int i = 0; i < 8; i++)
                {
                    int newX = curr.Item1 + dirX[i];
                    int newY = curr.Item2 + dirY[i];

                    if (newX < 0 || newX >= L || newY < 0 | newY >= L) continue;
                    if (graph[newX, newY] != 0) continue;

                    graph[newX, newY] = graph[curr.Item1, curr.Item2] + 1;
                    queue.Enqueue(new Tuple<int, int>(newX, newY));
                }
            }
        }
        
        public static void Main() {
            int N = int.Parse(Console.ReadLine());

            for (int i = 0; i < N; i++)
            {
                L = int.Parse(Console.ReadLine());
                string[] start = Console.ReadLine().Split();
                string[] target = Console.ReadLine().Split();
                graph = new int[311, 311];

                targetX = int.Parse(target[0]);
                targetY = int.Parse(target[1]);

                BFS(int.Parse(start[0]), int.Parse(start[1]));
            }
            
        }
    }
}