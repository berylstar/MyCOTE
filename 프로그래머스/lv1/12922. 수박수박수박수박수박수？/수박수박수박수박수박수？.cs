public class Solution {
    public string solution(int n) {
        string answer = "";
        for (int i = 0; i < n; i++)
        {
            answer += "수박";
        }
        return answer.Substring(0, n);
    }
}