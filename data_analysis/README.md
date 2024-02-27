### 1. 프로젝트 제목
- "Spaceship Titanic: A Machine Learning Approach to Predict Interdimensional Transport"

### 2. 프로젝트 설명
- 우주선 타이타닉이 시공 이상체와 충돌하는 동안 승객이 다른 차원으로 이송되었는지를 예측하는 것이 목표
- 예측을 돕기 위해, 우주선의 손상된 컴퓨터 시스템에서 복구된 개인 기록 세트가 제공됨

### 3. 데이터셋
- train.csv - 승객의 약 3분의 2(~8700명)에 대한 개인 기록으로, 교육 데이터로 사용됨
- test.csv - 테스트 데이터로 사용할 승객의 나머지 1/3(~4300)에 대한 개인 기록. 목표는 이 집합의 승객에 대한 수송량(Transported)의 값을 예측
- sample_submission.csv - 올바른 형식의 제출 파일
- Data -> https://www.kaggle.com/competitions/spaceship-titanic/data

### 4. 분석 방법론
- 각 데이터의 결측값을 데이터 형태에 맞게 결측값을 채움(ex: 평균, 최빈 등)
- 전처리 후의 데이터가 다양한 형태를 지니기 때문에 랜덤포레스트분류기 모델을 사용

### 5. 결과 및 해석
- 모델의 성능 평가 중
- 주요 발견 및 인사이트 
- https://www.kaggle.com/code/akshita0560/spaceship-titanic/notebook
- https://www.kaggle.com/code/gusthema/spaceship-titanic-with-tfdf

### 6. 시각화 및 대시보드
- 데이터 탐색 및 결과를 시각화
- ![output](https://github.com/YoonTC/YoonTC/assets/87857415/253c3cff-67ea-4be4-b00e-77a7ff779586)

### 7. 사용 기술 및 라이브러리
- Python, Pandas, Scikit-learn, Matplotlib

### 8. 설치 및 실행 방법
- 코드를 복제하고 실행하는 방법에 대한 단계별 안내

### 9. 기여 방법
- 다른 사람들이 프로젝트에 기여할 수 있는 방법 안내

### 10. 라이선스
- 프로젝트 라이선스 정보

### 11. 연락처 정보
- 질문이나 협업을 위한 연락처 정보


| Column | Description | Data Type | Example |
| ------ | ----------- | --------- | ------- |
| PassengerId | A unique Id for each passenger. | object | 0001_01 |
| CryoSleep | Indicates if the passenger was in suspended animation during the voyage. | int64 | 0 |
| VIP | Whether the passenger has paid for special VIP service. | int64 | 0 |
| Transported | Whether the passenger was transported to another dimension (target variable). | bool | False |
| HomePlanet_Earth | The planet the passenger departed from - Earth. | float64 | 0.0 |
| HomePlanet_Europa | The planet the passenger departed from - Europa. | float64 | 1.0 |
| HomePlanet_Mars | The planet the passenger departed from - Mars. | float64 | 0.0 |
| Destination_55 Cancri e | The destination planet of the passenger - 55 Cancri e. | float64 | 0.0 |
| Destination_PSO J318.5-22 | The destination planet of the passenger - PSO J318.5-22. | float64 | 0.0 |
| Destination_TRAPPIST-1e | The destination planet of the passenger - TRAPPIST-1e. | float64 | 1.0 |
| Age | The age of the passenger. | float64 | 0.493671 |
| RoomService | Amount billed for room service. | float64 | 0.0 |
| FoodCourt | Amount billed at the food court. | float64 | 0.0 |
| ShoppingMall | Amount billed at the shopping mall. | float64 | 0.0 |
| Spa | Amount billed at the spa. | float64 | 0.0 |
| VRDeck | Amount billed at the VR deck. | float64 | 0.0 |
| Deck | Cabin deck information. | object | B |
| Num | Cabin number. | object | 0 |
| Side | Cabin side (P for Port or S for Starboard). | object | P |
| Group | Group information from PassengerId. | object | 0001 |