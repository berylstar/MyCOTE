#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int F, S, G, U, D;
    cin >> F >> S >> G >> U >> D;

    bool visited[F+1] = {false};
    visited[S] = true;
    
    queue<pair<int,int>> Q;
    Q.push({S, 0});

    int x, y;
    bool complete = false;
    
    while (!Q.empty()){
        x = Q.front().first;
        y = Q.front().second;
        Q.pop();

        if (x == G)
        {
            cout << y;
            complete = true;
            break;
        }

        if ((x - D > 0) && !visited[x - D])
        {
            Q.push({x - D, y + 1});
            visited[x - D] = true;
        }

        if ((x + U <= F) && !visited[x + U])
        {
            Q.push({x + U, y + 1});
            visited[x + U] = true;
        }
    }

    if (!complete)
    {
        cout << "use the stairs";
    }

    return 0;
}