def linearsearchproduct(productlist, targetproduct):
    indices = []
    for index, product in enumerate(productlist):
        if product == targetproduct:
            indices.append(index)
    return indices

products = ["shoes", "boot", "loafer", "shoes", "sandel", "shoes"]
target = "shoes"
target2 = "apple"
print("SEARCH ELEMENT FOUND AT THE POSITION")

result = linearsearchproduct(products, target)
print("SEARCH 1:", target, result)
result = linearsearchproduct(products, target2)
print("SEARCH 2:", target2, result)
