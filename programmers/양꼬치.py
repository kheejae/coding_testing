def solution(n, k):
    service = n // 10
    lamb = n * 12000
    drink = (k - service) * 2000
    answer = lamb + drink
    return answer