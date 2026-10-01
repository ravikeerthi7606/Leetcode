
def solution(nums, target):
    seen={}
    for i, num in enumerate(nums):
        complement = target - num
        print(f"Current number: {num}, Complement: {complement}, Seen: {seen}")
        if complement in seen:
            print([seen[complement], i])
            return [seen[complement], i]

        seen[num] = i
    return None

print(solution([2, 7, 11, 15], 22))  # Output: [0, 1]