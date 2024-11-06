def quick_sort(n):

    pivot = n[-1]

    for num in n:
        if num > pivot:
            l = num
            rPos = i
            break



        for i in range(len(n)-1, -1, -1):
            if n[i] < pivot:
                r = n[i]
                rPos = i
                break
        

