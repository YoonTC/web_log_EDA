'웹 로그 기반 조회수 예측 해커톤'  
데이터  
| 데이터 명              | 설명                           |
|-----------------------|--------------------------------|
| sessionID             | 세션 ID                        |
| userID                | 사용자 ID                      |
| TARGET                | 세션에서 발생한 총 조회수       |
| browser               | 사용된 브라우저                 |
| OS                    | 사용된 기기의 운영체제          |
| device                | 사용된 기기                    |
| new                   | 첫 방문 여부                   |
| quality               | 세션의 질                      |
| duration              | 총 세션 시간                   |
| bounced               | 이탈 여부                      |
| transaction           | 세션 내에서 발생한 거래의 수   |
| transaction_revenue   | 총 거래 수익                   |
| continent             | 세션이 발생한 대륙             |
| subcontinent          | 세션이 발생한 하위 대륙        |
| country               | 세션이 발생한 국가             |
| traffic_source        | 트래픽이 발생한 소스           |
| traffic_medium        | 트래픽 소스의 매체             |
| keyword               | 트래픽 소스의 키워드           |
| referral_path         | referral인 경우 설정되는 경로  |

이와같은 데이터를 통해서 TARGET(조회수)을 예측하는 것이 목표