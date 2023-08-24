public class Solution {
    public int[] solution(int[] arr)
    {
        if (arr.Length == 1)
            return new int[] { -1 };
        
        int[] answer = new int[arr.Length - 1];

        int minIndex = 0;
        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[minIndex] > arr[i])
                minIndex = i;
        }

        int j = 0;
        int k = 0;
        while (j < arr.Length)
        {
            if (j != minIndex)
            {
                answer[k] = arr[j];
                k += 1;
            }

            j += 1;
        }

        return answer;
    }
}