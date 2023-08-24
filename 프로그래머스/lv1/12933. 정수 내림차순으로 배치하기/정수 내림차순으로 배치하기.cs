public class Solution {
    public long solution(long n) {        
        // 배열 만들기
        string numToStr = n.ToString();
        int len = numToStr.Length;
        int[] numArr = new int[numToStr.Length];
        
        for (int i = 0; i < len; i++)
        {
            numArr[i] = int.Parse(numToStr[i].ToString());
        }
        
        // 배열 정렬
        for (int i = 0; i < len; i++)
        {
            int maxIndex = i;
            
            for(int j = i + 1; j < len; j++)
            {
                if (numArr[maxIndex] < numArr[j])
                    maxIndex = j;
            }
            
            int temp = numArr[i];
            numArr[i] = numArr[maxIndex];
            numArr[maxIndex] = temp;
        }
        
        string answer = "";
        for (int i = 0; i < len; i++)
        {
            answer += numArr[i].ToString();
        }
        
        return long.Parse(answer);
    }
}