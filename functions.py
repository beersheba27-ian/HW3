def indexOf(numbers: list[int], num: int) -> int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    return -1 if num not in numbers else numbers.index(num)

def lastIndexOf(numbers: list[int], num: int) -> int:
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    # 2 returns for early stop
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == num: return i
    return -1

def min_even (numbers: list[int]) -> int:
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    numbers.sort()
    # 2 returns for early stop
    # I wanted to make it with filter by lambda function, but we didn't study it yet
    for x in numbers:
        if x % 2 == 0: return x
    return -1

def count(numbers: list[int], num: int) -> int:
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    # I wanted to make it with numbers.count(num), but we didn't study it yet
    return len([x for x in numbers if x == num])

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