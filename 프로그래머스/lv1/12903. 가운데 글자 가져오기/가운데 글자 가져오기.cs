public class Solution {
    public string solution(string s) {
        int len = s.Length;
        if (len % 2 == 1)
            return s[len / 2].ToString();
        else
            return s.Substring(len / 2 - 1, 2);
    }
}