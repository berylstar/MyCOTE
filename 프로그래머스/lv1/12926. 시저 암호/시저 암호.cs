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

            if (big.Contains(now))
            {
                answer += big[(big.IndexOf(now) + n) % 26];
            }
            else if (small.Contains(now))
            {
                answer += small[(small.IndexOf(now) + n) % 26];
            }
            else
                answer += " ";
        }

        return answer;
    }
}