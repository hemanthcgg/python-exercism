def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    if(len(lists)==0):
        return []
    list1 = lists[0]
    for i in lists[1:]:
        append(list1,i)
    return list1


def filter(function, list):
    return [l for l in list if(function(l))]


def length(list):
    return sum([1 for l in list])


def map(function, list):
    return [function(l) for l in list]


def foldl(function, list, initial):
    for l in list:
        initial = function(initial, l)
    return initial


def foldr(function, list, initial):
    for l in list[::-1]:
        initial = function(initial, l)
    return initial


def reverse(list):
    # return list[::-1]
    return [list[i-1] for i in range(len(list),0,-1)]
