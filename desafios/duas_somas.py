'''def duas_somam(nums, alvo):
    lista = set()
    for n in nums:
        if alvo - n in lista:
            return True
        lista.add(n)
    return False'''


'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}  # dicionário: número -> índice
        for i, n in enumerate(nums):          enumerate() — é só um jeito de percorrer uma lista já pegando índice + valor juntos, evita você ter que fazer for i in range(len(nums)) e depois nums[i] toda hora.
            complemento = target - n  dict vs set — set guarda só "o que existe"; dict guarda "o que existe e a que valor está associado" (aqui, o índice). Regra prática: se a pergunta é só "existe?", use set. Se é "existe, e o que tem junto?", use dict.
            if complemento in vistos:
                return [vistos[complemento], i]
            vistos[n] = i'''

'''def duas_somam(nums,alvo):
    for i in range(len(nums)):
        for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == alvo:
                    return True
    return False'''

'''print(duas_somam([2, 7, 11, 15], 9))   # esperado: True (1+4 ou 2+3)
print(duas_somam([1, 2, 3], 100))    # esperado: False
print(duas_somam([3, 3], 6))'''

# Two Pointers

'''def duas_somam_ordenado(nums, alvo):
    esquerda = 0
    direita = len(nums) - 1
    while esquerda < direita:
        soma = nums[esquerda] + nums[direita]
        if soma == alvo:
            return True
        elif soma < alvo:
            esquerda += 1   # soma pequena demais, precisa de número maior
        else:
            direita -= 1    # soma grande demais, precisa de número menor
    return False'''
