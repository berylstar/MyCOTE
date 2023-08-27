public class Solution {
    public int solution(string t, string p) {
        int answer = 0;
        long num = long.Parse(p);
        
        for (int i = 0; i < t.Length - p.Length + 1; i++)
        {
            if (long.Parse(t.Substring(i, p.Length)) <= num)
                answer += 1;
        }
        
        return answer;
    }
}