def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    for i in range(len(apples)):
        if ((apples[i] + a) >= s) and ((apples[i] + a) <= t):
            apple_count += 1
    for i in range(len(oranges)):
        if ((oranges[i] + b) >= s) and ((oranges[i] + b) <= t):
            orange_count += 1
    print(apple_count)
    print(orange_count)


countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])