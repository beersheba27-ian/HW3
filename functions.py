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
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum: return True
    return False
