def indexOf(numbers: list[int], num: int) -> int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    i = 0
    while i < len(numbers):
        if numbers[i] == num: return i
        i += 1
    return -1

def lastIndexOf(numbers: list[int], num: int) -> int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    i = len(numbers) - 1
    while i >= 0:
        if numbers[i] == num: return i
        i -= 1
    return -1

def min_even (numbers: list[int]) -> int:
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    cur = None
    for x in numbers:
        if x % 2 == 0 and (cur is None or x < cur):
            cur = x
    return cur if cur is not None else -1

def count(numbers: list[int], num: int) -> int:
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    cnt = 0
    for x in numbers:
        if x == num: cnt += 1
    return cnt

def sumOfTwoExists(numbers: list[int], sum: int) -> bool:
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """ 
    for i in range(len(numbers)-1):
        x = numbers[i]
        for y in numbers[i+1::]:
            # 2 returns for early stop
            if x + y == sum: return True
    return False


# print calls for testing the above functions

# I know that we didn't learn assert(), 
# but I found it better to use than just print output and check manually

assert indexOf([10, 20, 30, 20, -1], 20) == 1
assert indexOf([10, 20, 30, 20, -1], 10) == 0
assert indexOf([10, 20, 30, 20, -1], -1) == 4
assert indexOf([20, 10, 20, 30, 20, -1], 20) == 0
assert indexOf([20, 10, 20, 30, 20, -1, 20], 20) == 0
assert indexOf([10, 20, 30], 99) == -1
assert indexOf([], 10) == -1

assert lastIndexOf([10, 20, 30, 20, -1], 20) == 3
assert lastIndexOf([10, 20, 30, 20, -1], 10) == 0
assert lastIndexOf([10, 20, 30, 20, -1], -1) == 4
assert lastIndexOf([20, 10, 20, 30, 20, -1], 20) == 4
assert lastIndexOf([20, 10, 20, 30, 20, -1, 20], 20) == 6
assert lastIndexOf([10, 20, 30], 99) == -1
assert lastIndexOf([], 10) == -1

assert min_even([9, 4, 7, 2]) == 2
assert min_even([-8, -3, -4, 5]) == -8
assert min_even([5, 0, 3, 2]) == 0
assert min_even([6]) == 6

assert count([10, 20, 30, 20, -1], 20) == 2
assert count([10, 20, 30, 20, -1], 30) == 1
assert count([10, 20, 30, 20, -1], 10) == 1
assert count([10, 20, 30, 20, -1], -1) == 1
assert count([1, 2, 3], 4) == 0
assert count([5, 5, 5], 5) == 3
assert count([], 5) == 0

assert sumOfTwoExists([1, -1, 40, 50, 0], 0) is True
assert sumOfTwoExists([1, -1, 40, 50, 0], 39) is True
assert sumOfTwoExists([1, -1, 40, 50, 0], 41) is True
assert sumOfTwoExists([1, -1, 40, 50, 0], 50) is True
assert sumOfTwoExists([1, -1, 40, 50, 0], 2) is False
assert sumOfTwoExists([1, 2, 3], 5) is True
assert sumOfTwoExists([3, 3], 6) is True
assert sumOfTwoExists([1], 2) is False

print("All tests passed!")