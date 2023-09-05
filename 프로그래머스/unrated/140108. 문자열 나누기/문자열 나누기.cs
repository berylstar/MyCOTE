public class Solution {
    public int solution(string s) {
        int answer = 0;
        int count = 0;
        string now = "";
        
        foreach (char c in s)
        {
            now += c;
            
            if (c == now[0])
                count += 1;
            
            else if (count != 0 && now.Length >= 2 * count)
            {
                count = 0;
                now = "";
                answer += 1;
            }
        }
        
        return (now.Length > 0)? answer + 1 : answer;
    }
}