using System.Linq;
public class Solution {
    public string[] solution(string[] strings, int n)
    {
        var sortedWords = from word in strings
                          orderby (word[n], word)
                          select word;

        return sortedWords.ToArray();
    }
}