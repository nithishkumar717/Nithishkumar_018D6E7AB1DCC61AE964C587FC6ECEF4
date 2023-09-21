def linear_search_product(products, target_product):
    indices = []  
  
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i) 
    return indices  

# Example usage:
product_list = ["ninja h2r", "hayabusa", "s1000rr", "hayabusa", "z900", "r15"]
target = "hayabusa"
result = linear_search_product(product_list, target)
print(result)
