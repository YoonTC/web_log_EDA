def vector_addition(*vector_variables):
    return [for k in vec]

#vector간 덧셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 
#일정하지 않음

# 실행결과
print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError