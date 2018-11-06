def bubbleSort(nlis):
    sorted = False

    while sorted == False:
        for i in range(len(nlis)):
            if i+1 < len(nlis):
                if nlis[i] > nlis[i+1]:
                    nlis[i], nlis[i+1] = nlis[i+1], nlis[i]
        for i in range(len(nlis)):
            if i+1 < len(nlis):
                if nlis[i] < nlis[i+1]:
                    sorted = True
                elif nlis[i] > nlis[i+1] and i+1 < len(nlis):
                    sorted = False
                    break

    return nlis
