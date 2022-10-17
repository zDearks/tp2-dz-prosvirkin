def _max(array):
    mx = array[0]
    if len(array) > 1:
        for i in range(1, len(array)):
            if array[i] > mx:
                mx = array[i]
    return mx

def _min(array):
    mx = array[0]
    if len(array) > 1:
        for i in range(1, len(array)):
            if array[i] < mx:
                mx = array[i]
    return mx

def _mult(array):
    mx = array[0]
    if len(array) > 1:
        for i in range(1, len(array)):
            mx= mx * array[i]
    return mx

def _sum(array):
    s = array[0]
    if len(array) > 1:
        for i in range(1, len(array)):
            s += array[i]
    return s
