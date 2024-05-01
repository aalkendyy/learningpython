"""

Sure! Here's a medium-level question related to dealing with indices in loops:

**Question:**

You are given a list of integers. Write a Python function `find_pairs(lst, target)` that takes in a list `lst` of integers and an integer `target`. The function should return a list of tuples representing pairs of indices `(i, j)` such that `lst[i] + lst[j] = target`. Each pair should appear only once, and the order of the pairs in the output list does not matter. If no such pair exists, return an empty list.

**Example:**
```python
find_pairs([2, 4, 3, 7, 0, 5], 7)
```
Output:
```
[(0, 3), (1, 2), (4, 6)]
```
Explanation: In the given list, elements at indices 0 and 3 sum up to 7 (2 + 5), elements at indices 1 and 2 sum up to 7 (4 + 3), and elements at indices 4 and 6 sum up to 7 (0 + 7).

**Constraints:**
- The input list `lst` will contain at most 10^4 integers.
- Each integer in the list will be in the range [-10^9, 10^9].
- The target integer `target` will be in the range [-10^9, 10^9].

**Note:**
- You can assume that each input will have exactly one solution.

**Tasks:**
1. Define the `find_pairs` function.
2. Implement the logic to find pairs of indices such that the elements at those indices sum up to the target.
3. Test your function with different test cases to ensure it works as expected.


"""






def find_pairs(arr, target):
    arr1=[]
    
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==target and i != j:
                 arr1.append((arr[i], arr[j]))
    return arr1
            
                       
                





a=find_pairs([2, 4, 3, 7, 0, 5], 7)
print(a)
