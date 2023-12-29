# 코딩테스트 연습

### 하루에 3문제씩 풀어보자

### ON : `Programmers`, `BOJ`

### LANG : `PYTHON`,  `C#`

# 파이썬 리멤버스

배열이 있으면 배열 없으면 -1
> ```
> return answer if len(answer) > 0 else -1
> =>
> return answer or -1
> ```

배열 속 배열 합치기
> ```
> arr1 = [[1], [2, 3], [4, 5, 6]]
> arr2 = sum(arr1, [])
> =>
> # arr2 = [1, 2, 3, 4, 5, 6]
> ```

배열의 누적 집계 : reduce
> ```
> from functools import reduce
> gcd = reduce(GCD, numbers)
> ```

배열 깊은 복사 : deepcopy
> ```
> import copy
> newGraph = copy.deepcopy(graph)
> ```

소수점 표현하기
> ```
> print(f"{number:.2f}")
> ```

배열의 원소 한줄로
> ```
> print(*numbers, sep=" ")
> ```
> ```
> print(" ".join(numbers))
> ```

딕셔너리 value의 최댓값을 가진 key 찾기
> ```
> print(max(dic, key=dic.get))
> ```
