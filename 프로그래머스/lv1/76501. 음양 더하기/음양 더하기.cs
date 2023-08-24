public class Solution {
    public int solution(int[] absolutes, bool[] signs) {
        int answer = 0;
        for (int i = 0; i < signs.Length; i++)
            answer += absolutes[i] * (signs[i] ? 1 : -1);
        return answer;
    }
}