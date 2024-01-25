# optimization: calculate all elements and index the elements
def countItems(s):
    total_items = 0
    temp_counter = 0
    start = False
    for char in s:
        if char == "|": # add at the end
            total_items += temp_counter
            temp_counter = 0
            start = True
        elif start:
            temp_counter += 1
    return total_items

def numberOfItems(s, startIndices, endIndices):
    items_counter = []
    item_searches = zip(startIndices, endIndices)
    
    for start, end in item_searches:
        items_counter.append(countItems(s[start-1:end]))
    return items_counter
