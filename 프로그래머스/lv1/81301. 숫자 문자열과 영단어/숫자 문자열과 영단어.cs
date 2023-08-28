public class Solution
{
    public int solution(string s)
    {
        string[] numbers = new string[] { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

        for (int i = 0; i < numbers.Length; i++)
            s = s.Replace(numbers[i], i.ToString());

        return int.Parse(s);
    }
}