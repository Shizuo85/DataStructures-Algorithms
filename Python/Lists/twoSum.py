def find_sum(lst, k):
    # Write your code here
    rem = set()

    for num in lst:
        if k - num in rem:
            return [k-num, num]
        rem.add(num)