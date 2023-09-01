public class Solution
{
    public string solution(string[] cards1, string[] cards2, string[] goal)
    {
        int p1 = 0, p2 = 0;

        foreach (string g in goal)
        {
            if (p1 < cards1.Length && cards1[p1] == g)
                p1 += 1;
            else if (p2 < cards2.Length && cards2[p2] == g)
                p2 += 1;
            else
                return "No";
        }

        return "Yes";
    }
}