using System.Collections.Generic;

public class Solution {
    public string[] solution(string[] players, string[] callings) {
        string[] answer = new string[players.Length];
        Dictionary<string, int> pd = new Dictionary<string, int>();
        Dictionary<int, string> id = new Dictionary<int, string>();
        
        for (int i = 0; i < players.Length; i++)
        {
            pd.Add(players[i], i);
            id.Add(i, players[i]);
        }
        
        foreach (string nowPlayer in callings)
        {
            int nowRank = pd[nowPlayer];
            string frontPlayer = id[nowRank - 1];
            
            pd[nowPlayer] -= 1;
            pd[frontPlayer] += 1;
            
            id[nowRank - 1] = nowPlayer;
            id[nowRank] = frontPlayer;
        }
        
        for (int i = 0; i < players.Length; i++)
        {
            answer[i] = id[i];
        }
        
        return answer;
    }
}