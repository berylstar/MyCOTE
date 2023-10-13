# 코딩테스트 연습

### 하루에 3문제씩 풀어보자

### ON : `Programmers`, `BOJ`

### LANG : `PYTHON`,  `C#`

# 파이썬 리멤버스

> 배열이 있으면 배열 없으면 -1
> ```
> return answer if len(answer) > 0 else -1
> =>
> return answer or -1
> ```

> 배열 속 배열 합치기
> ```
> arr1 = [[1], [2, 3], [4, 5, 6]]
> arr2 = sum(arr1, [])
> =>
> # arr2 = [1, 2, 3, 4, 5, 6]
> ```

> 배열의 누적 집계 : reduce
> ```
> from functools import reduce
> gcd = reduce(GCD, numbers)
> ```
