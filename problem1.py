def get_pair(nums, target):
    numlen = len(nums)
    # errors = ""
    # if all(i >= 30 for i in my_list1)
    # if numlen < 2 or numlen > 103:
    dic = {}
    for i in range(numlen):
        if target - nums[i] in dic.keys():
            return [dic[target - nums[i]], i]
        else:
            dic[nums[i]] = i

if __name__ == '__main__':
    print(get_pair([2,7,11,15], 9))
    print(get_pair([3,2,4], 6))
    print(get_pair([3,3], 6))