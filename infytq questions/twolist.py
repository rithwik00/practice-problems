list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# flag = True

sum_l1 = sum(list1)
sum_l2 = sum(list2)
print(sum_l1, sum_l2)
if sum_l1 == sum_l2:
    print(-1)
    # flag = False

else:
    odd = []
    even = []
    # pairs = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            num1 = sum_l1 - list1[i] + list2[j]
            num2 = sum_l2 + list1[i] - list2[j]

            if num1 == num2:
                if (list1[i] * list2[j]) % 2 == 0:
                    even.append((list1[i] * list2[j], (list1[i], list2[j])))
                else:
                    odd.append((list1[i] * list2[j], (list1[i], list2[j])))
                # pairs.append((list1[i], list2[j]))
    even.sort()
    print(even, odd)

    # if len(pairs) > 0:
    #     product = []
    #     for i in pairs:
    #         product.append(i[0] * i[1])
    # else:
    #     print(-1)

    '''
    larger = []
    smaller = []
    if( sum1 > sum2 ):
        larger = list1
        smaller = list2
    else:
        larger = list2
        smaller = list1
    
    
    for i in sorted(larger):
        j = (sum1+sum2)//2 + i - max(sum1, sum2)
        if(j >=0 and j in smaller):
            if( sum1 > sum2 and i > j ):
                out.append((i*j, (i, j)))
    '''