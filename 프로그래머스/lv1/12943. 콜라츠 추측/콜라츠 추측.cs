public class Solution {
    public int solution(int num) {
        long ll = num;
        for (int i = 0; i < 500; i++)
        {
            if (ll == 1)
                return i;
            
            if (ll % 2 == 0)
                ll /= 2;
            else
                ll = ll * 3 + 1;
        }
        
        return -1;
    }
}