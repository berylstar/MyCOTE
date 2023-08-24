public class Solution {
    public string solution(string phone_number) => "".PadLeft(phone_number.Length - 4, '*') + phone_number.Substring(phone_number.Length - 4);
}