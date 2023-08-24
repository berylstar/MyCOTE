// public class Solution {
//     public string solution(int num) => (num % 2 == 0) ? "Even" : "Odd";
// }

// public class Solution {
//     public string solution(int num) {
//         string[] evenOrOdd = { "Even", "Odd" };
//         return evenOrOdd[num % 2];
//     }
// }
using System;
public class Solution {
    public string solution(int num) => new string[] { "Even", "Odd" }[Math.Abs(num) % 2];
}