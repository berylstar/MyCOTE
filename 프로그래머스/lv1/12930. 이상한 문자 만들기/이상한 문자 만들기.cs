public class Solution {
    public string solution(string s) {
        string answer = "";
        int j = 0;
        
        for (int i = 0; i < s.Length; i++)
        {
            string now = s[i].ToString();
            
            if (now.StartsWith(' '))
                j = -1;
            else
                if (j % 2 == 0)
                    now = now.ToUpper();
                else
                    now = now.ToLower();
            
            answer += now;
            j += 1;
        }
        
        return answer;
    }
}