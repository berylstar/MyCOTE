#include <iostream>
#include <queue>
using namespace std;

int N, M;
int dirX[4] = {0, 0, 1, -1};
int dirY[4] = {1, -1, 0, 0};
int graph[501][501] = {0,};
queue<pair<int, int>> Q;
int number = 0;
int maxx = 0;

void BFS(int i, int j)
{
    graph[i][j] = 0;
    int curr = 1;
    Q.push({i, j});

    int x, y;
    int nx, ny;

    while (!Q.empty()){
        x = Q.front().first;
        y = Q.front().second;
        Q.pop();

        for (int k = 0; k < 4; k++){
            nx = x + dirX[k];
            ny = y + dirY[k];

            if (nx<0 || nx>=N || ny<0 || ny>=M) continue;
            if (graph[nx][ny] == 0) continue;

            graph[nx][ny] = 0;
            Q.push({nx, ny});
            ++curr;
        }
    }

    if (curr > maxx)
    {
        maxx = curr;
    }
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            if (graph[i][j] == 0) continue;

            BFS(i, j);
            ++number;
        }
    }

    cout << number << endl << maxx;
}