def sol(stu,keys):
    result = ''
    for i in range(0, len(stu), 4):
        nums = list()
        for j in range(3,-1,-1):
            num = ord(stu[i+j]) - 32
            num = (num+keys[3-j])%96
            nums.append(num+32)
        result += chr(nums[0])
        result += chr(nums[1])
        result += chr(nums[2])
        result += chr(nums[3])
    return result
stu = input()
keys = [27,54,9,86]
res = sol(stu,keys)
print(res)
