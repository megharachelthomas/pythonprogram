def range_Armstrong(start, end):
    armstrong = []
    for num in range(start, end + 1):
        digits = len(str(num))
        sum = 0
        checknum = num
        while checknum > 0:
            sum += (checknum % 10) ** digits
            checknum = int(checknum / 10)
        if (sum == num):
            armstrong.append(num)
    print(armstrong) 
    return armstrong
range_Armstrong(100, 1000)
range_Armstrong(500, 9000)