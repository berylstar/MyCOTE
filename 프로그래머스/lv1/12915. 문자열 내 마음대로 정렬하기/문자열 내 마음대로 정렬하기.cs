using System.Linq;
public class Solution {
    public string[] solution(string[] strings, int n)
    {
        return strings.OrderBy(c => (c[n], c)).ToArray();
    }
}