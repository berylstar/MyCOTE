// public class Solution {
//     public string solution(int num) => (num % 2 == 0) ? "Even" : "Odd";
// }

using System;
public class Solution {
    public string solution(int num) => new string[] { "Even", "Odd" }[Math.Abs(num) % 2];
}