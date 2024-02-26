def vector_size_check(*vector_variables):
    return all([len(vector_variables[0]) == len(k) for k in vector_variables[1:]])
    
#Chat GPT 답변    
#return all(len(vector_variables[0]) == len(vector) for vector in vector_variables[1:])

#vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 
#가능 여부를 True 또는 False로 반환함

# 실행결과
print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False