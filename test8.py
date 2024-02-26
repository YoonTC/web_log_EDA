import pandas as pd
import numpy as np

def get_rating_matrix(filename):
    # CSV 파일을 데이터프레임으로 읽어오기
    df = pd.read_csv(filename)
    
    # 사용자와 영화 이름을 정렬하여 unique한 값으로 추출
    users = np.sort(df['source'].unique())
    movies = np.sort(df['target'].unique())
    
    # 사용자와 영화 이름을 기준으로 인덱스 설정
    user_index = {user: idx for idx, user in enumerate(users)}
    movie_index = {movie: idx for idx, movie in enumerate(movies)}
    
    # 평점 행렬 생성
    rating_matrix = np.zeros((len(users), len(movies)), dtype=np.float32)
    
    # 각 행렬 요소에 평점 할당
    for _, row in df.iterrows():
        user = row['source']
        movie = row['target']
        rating = row['rating']
        user_idx = user_index[user]
        movie_idx = movie_index[movie]
        rating_matrix[user_idx, movie_idx] = rating
    
    return rating_matrix

# 테스트
if __name__ == "__main__":
    rating_matrix = get_rating_matrix("movie_rating.csv")
    print(rating_matrix)
    
#import build_matrix as test_code
#test_code.get_rating_matrix("movie_rating.csv")