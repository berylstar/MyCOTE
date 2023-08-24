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
        
        // 배열 정렬 - 삽입 정렬
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
        
        // 문자로 변환시켜서 이어 붙이기
        string answer = "";
        foreach (int num in numArr)
        {
            answer += num.ToString();
        }
        
        return long.Parse(answer);
    }
}