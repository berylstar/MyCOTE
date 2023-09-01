public class Solution
{
    public string solution(int a, int b)
    {
        int[] month = new int[] { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int answer = 4;
        for (int i = 0; i < a - 1; i++)
        {
            answer += month[i];
        }
        answer = (answer + b) % 7;
        return new string[] { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" }[answer];
    }
}