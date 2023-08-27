public class Solution
{
    public string solution(string s, int n)
    {
        string big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string small = "abcdefghijklmnopqrstuvwxyz";

        string answer = "";

        foreach (char l in s)
        {
            string now = l.ToString();
            string g;

            if (big.Contains(now))
                g = big;
            else if (small.Contains(now))
                g = small;
            else
            {
                answer += " ";
                continue;
            }
            
            answer += g[(g.IndexOf(now) + n) % 26];
        }

        return answer;
    }
}