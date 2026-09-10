class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        esquerda = 0
        direita = len(numbers) - 1
        while esquerda < direita:
            soma = numbers[esquerda] + numbers[direita]
            if soma == target:
                return [esquerda + 1, direita + 1]
            elif soma < target:
                esquerda += 1
            else:
                direita -= 1
        return []