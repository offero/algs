'''
Given an array of cooktimes and an array of fresh times (durations that a cooked
dish remains fresh),
determine an order of cooking that ensures all dishes are fresh at the end.
'''
ex1_cooktimes =  [3, 4, 5]
ex1_freshtimes = [1, 20, 4]

def c(cooktimes, freshtimes, selected, ft, n=1):
    # print(selected, ft)
    if ft <= 0:
        # print('stale')
        return False
    for i in range(len(selected)):
        if selected[i] > 0:
            continue
        selected[i] = n
        res = c(cooktimes, freshtimes, selected, 
                min(ft - cooktimes[i], freshtimes[i]), n+1)
        if res:
            return res
        else:
            selected[i] = 0
    if len([x for x in selected if x==0]) == 0:
        return True
    return False


# def transform_times(cooktimes, freshtimes):
#     return [{'ct': cooktimes[i], 'ft': freshtimes[i]} for i in range(len(cooktimes))]

def cookorder(cooktimes, freshtimes):
    ft = max(freshtimes)
    selected = [0] * len(cooktimes)
    if c(cooktimes, freshtimes, selected, ft):
        return selected
    return "no order found"



if __name__ == "__main__":
    ex_cooktimes = ex1_cooktimes
    ex_freshtimes = ex1_freshtimes
    order = cookorder(ex_cooktimes, ex_freshtimes)
    print(order)
