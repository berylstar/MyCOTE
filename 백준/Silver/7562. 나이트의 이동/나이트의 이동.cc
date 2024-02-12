#include <iostream>
#include <queue>
using namespace std;

int T;
int L;
int startX, startY;
int targetX, targetY;
int dirX[] = {2, -2, 2, -2, 1, -1, 1, -1};
int dirY[] = {1, 1, -1, -1, 2, 2, -2, -2};

int graph[301][301];
queue<pair<int, int>> q;

void Reset()
{
    while (!q.empty())
        q.pop();

    for (int i = 0; i < 301; i++)
    {
        for (int j = 0; j < 301; j++)
        {
            graph[i][j] = 0;            
        }
    }
}

void BFS(int x, int y)
{
    q.push({x,y});
    while (!q.empty())
    {
        int a = q.front().first;
        int b = q.front().second;
        q.pop();

        if (a == targetX && b == targetY)
        {
            cout << graph[a][b] << endl;
            Reset();
            break;
        }

        for (int i = 0; i < 8; i++)
        {
            int na = a + dirX[i];
            int nb = b + dirY[i];

            if (na < 0 || na >= L || nb < 0 || nb >= L) continue;
            if (graph[na][nb] != 0) continue;
            
            q.push({na, nb});
            graph[na][nb] = graph[a][b] + 1;
        }
    }
}

int main()
{
    cin >> T;
    
    for (int i = 0; i < T; i++)
    {
        cin >> L;
        cin >> startX >> startY;
        cin >> targetX >> targetY;

        BFS(startX, startY);
    }
    
    return 0;
}