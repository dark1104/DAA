#fractionalknapsack



class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
def fractionalknapsack(W,arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
    finalvalue = 0.0
    for Item in arr:
        if Item.weight <= W:
            W -=Item.weight
            finalvalue += Item.value
        else:
            finalvalue += Item.value * W / Item.weight
            break
    return finalvalue
    
if __name__ == "__main__":
    W = 50
    arr = [Item(60,10), Item(100,20), Item(120,30)]
    max_val = fractionalknapsack(W, arr)
    print(max_val)