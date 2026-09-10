# O(n²) - loop dentro de loop
"""def tem_duplicado_lento(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False"""

'''def tem_duplicado(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False

print(tem_duplicado([1, 2, 3, 4]))'''

'''def tem_duplicado(nums):
    vistos = set()
    for n in nums:
        if n in vistos:
            return True
        vistos.add(n)
    return False    # O(1) com hash para ser mais rápido

print(tem_duplicado([1, 2, 3, 2]))'''
