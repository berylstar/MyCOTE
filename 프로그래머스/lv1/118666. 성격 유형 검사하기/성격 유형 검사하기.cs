public class Solution
{
    public string solution(string[] survey, int[] choices)
    {
        string answer = "";
        string type = "RTCFJMAN";
        int[] count = new int[8] { 0, 0, 0, 0, 0, 0, 0, 0 };

        for (int i = 0; i < survey.Length; i++)
        {
            count[type.IndexOf(survey[i][0])] += (4 - choices[i]);
        }

        for (int i = 0; i < 8; i += 2)
        {
            answer += (count[i] >= count[i + 1]) ? type[i] : type[i + 1];
        }

        return answer;
    }
}