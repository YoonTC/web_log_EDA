import pandas as pd
import numpy as np

def get_frequent_matrix(filename):
    # CSV 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(filename)
    
    # 사용자와 제품 이름을 정렬하여 unique한 값으로 추출
    users = np.sort(df['source'].unique())
    products = np.sort(df['target'].unique())
    
    # 사용자와 제품 이름을 기준으로 인덱스 설정
    user_index = {user: idx for idx, user in enumerate(users)}
    product_index = {product: idx for idx, product in enumerate(products)}
    
    # Frequent Matrix 생성
    frequent_matrix = np.zeros((len(users), len(products)), dtype=np.float32)
    
    # 각 행렬 요소에 빈도 수 할당
    for _, row in df.iterrows():
        user = row['source']
        product = row['target']
        user_idx = user_index[user]
        product_idx = product_index[product]
        frequent_matrix[user_idx, product_idx] += 1
    
    return frequent_matrix

# 테스트
if __name__ == "__main__":
    frequent_matrix = get_frequent_matrix("1000i.csv")
    print(frequent_matrix)
