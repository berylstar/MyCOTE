using System.Collections.Generic;
public class Solution
{
    public int Date(string date)
    {
        string[] dateArr = date.Split('.');
        return int.Parse(dateArr[0]) * 336 + int.Parse(dateArr[1]) * 28 + int.Parse(dateArr[2]);
    }

    public int[] solution(string today, string[] terms, string[] privacies)
    {
        Dictionary<char, int> term = new Dictionary<char, int>();

        foreach (string t in terms)
        {
            string[] temp = t.Split(' ');
            term.Add(char.Parse(temp[0]), int.Parse(temp[1]) * 28);
        }

        int td = Date(today);

        List<int> answer = new List<int>();

        for (int i = 0; i < privacies.Length; i++)
        {
            string[] temp = privacies[i].Split(' ');
            
            if (td >= Date(temp[0]) + term[char.Parse(temp[1])])
                answer.Add(i + 1);
                
        }

        return answer.ToArray();
    }
}