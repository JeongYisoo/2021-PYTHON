def linear_binary(num, findL):
    """
    선형 탐색 알고리즘 공부
    인덱스 0부터 num을 찾고 해당 인덱스 반환
    num이 없을 경우 None을 리턴

    리스트에 몇 개 포함됐는지 리턴(최종)
    """
    count=0
    for i in range(len(findL)):
        if findL[i] is num:
            count+=1
        #return count
    return count


listTest=[2, 4, 6, 6, 7, 9, 0, 1]
print(linear_binary(2,listTest))
print(linear_binary(6,listTest))