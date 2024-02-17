#include <iostream>
using namespace std;

void HanoiTower(int N, int start, int end)
{
    if (N == 1)
    {
        cout << start << " " << end << "\n";
    }
    else
    {
        HanoiTower(N-1, start, 6-start-end);
        cout << start << " " << end << "\n";
        HanoiTower(N-1, 6-start-end, end);
    }
}

int main()
{
    int N;
    cin >> N;
    
    cout << (1 << N) - 1 << "\n";
    HanoiTower(N, 1, 3);
}