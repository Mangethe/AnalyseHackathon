def bubble_sort(items):
    """Return array of items, sorted in ascending order'''
        Args:
            items (array): list or array-like object containing numerical values.

        Returns:
            array of items, sorted in ascending order.

        Example(s):
            >>> bubble_sort(np.array([2, 5, 62, 5, 42, 52, 48, 5]))
            array([ 2,  5,  5,  5, 42, 48, 52, 62])
        """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: #compare item 1 and 2 (check which is greater)
                items[j], items[j+1] = items[j+1], items[j] #if above cond. is met we Swap!

    return items #return sorted items


def merge_sort(items):
    """Return array of items, sorted in ascending order'''
        Args:
            items (list): list containing numerical values or strings.

        Returns:
            array of items, sorted in ascending order.

        Example(s):
            >>> merge_sort([2, 5, 62, 5, 42, 52, 48, 5])
            [ 2,  5,  5,  5, 42, 48, 52, 62]
        """
    def merge(A, B): #this function within one, subdivides the list into 2sublits
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)
        if len(A) == 0:
            new_list = new_list + B
        if len(B) == 0:
            new_list = new_list + A
        return new_list

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    return merge(i1, i2) #returns a sorted lists


def quick_sort(items):

    """Return array of items, sorted in ascending order'''

    Args:
        items (list): list of unordered numbers.

    Returns:
        list of elements in items in ascending order.

    Example(s):
        >>> quick_sort([2, 5, 62, 5, 42, 52, 48, 5])
        [ 2,  5,  5,  5, 42, 48, 52, 62]

        >>> quick_sort([2, 5, 62, 5, 42, 52, 70, 5])
        [2, 5, 5, 5, 42, 52, 62, 70]
    """
    pivot = items[-1] #pivot = last item of the list

    smaller_items= []
    same_items = []
    bigger_items = []


    for i in items:#use for loop to split the list
        if i < pivot:
            smaller_items.append(i) #if items are smaller than our pivot we add to smaller_items list
        elif i > pivot:
            bigger_items.append(i) #if items are bigger than our pivot we add to bigger_items list
        else:
            same_items.append(i) #if items are equal to our pivot we add to same_items list

    for j in range(len(smaller_items)): #sorting the smaller items list
        for k in range(len(smaller_items)-1-j):
            if smaller_itemst[k] > smaller_items[k+1]:
                smaller_items[k], smaller_items[k+1] = smaller_items[k+1], smaller_itemst[k]

    for l in range(len(bigger_items)): #sorting the bigger items list
        for m in range(len(bigger_items)-1-l):
            if bigger_items[m] > bigger_items[m+1]:
                bigger_items[m], bigger_items[m+1] = bigger_items[m+1], bigger_items[m]

    sorted_items = smaller_items + same_items + bigger_items

    return sorted_items #returns the sorted list
