#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int graph[100][100];
int N, M, K;
int dirX[4] = {0, 0, 1, -1};
int dirY[4] = {1, -1, 0, 0};
queue<pair<int, int>> Q;

int BFS()
{
    int ret = 1;
    int x, y, nx, ny;
    while (!Q.empty()){
        x = Q.front().first;
        y = Q.front().second;
        Q.pop();

        for (int i = 0; i < 4; i++){
            nx = x + dirX[i];
            ny = y + dirY[i];

            if (nx<0 || nx>=M || ny<0 || ny>=N) continue;

            if (graph[nx][ny] > 0) continue;

            ++ret;
            graph[nx][ny] = 1;
            Q.push({nx, ny});
        }
    }
    return ret;
}

int main()
{
    cin >> M >> N >> K;
    int a, b, c, d;
    for (int k = 0; k < K; k++){
        cin >> a >> b >> c >> d;
        for (int i = b; i < d; i++){
            for (int j = a; j < c; j++){
                graph[i][j] = 1;
            }
        }
    }

    int index = 0;
    int area[100] = {0};

    for (int i = 0; i < M; i++){
        for (int j = 0; j < N; j++){
            if (graph[i][j] > 0) continue;

            Q.push({i,j});
            graph[i][j] = 1;
            area[index] = BFS();
            ++index;
        }
    }

    sort(area, area + index);
    cout << index << endl;
    for (int i = 0; i < index; i++){
        cout << area[i] << ' ';
    }

    return 0;
}