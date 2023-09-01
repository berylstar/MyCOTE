public class Solution
{
    public string solution(int[] food)
    {
        string left = "";
        string right = "";

        for (int i = 0; i < food.Length; i++)
        {
            string sFood = new string((char)(i + '0'), food[i] / 2);
            left = left + sFood;
            right = sFood + right;
        }
        
        return left + '0' + right;
    }
}