# TamaPoke v3.90.1 - Digimon Pokemon-style Motion Patch

기준: v3.90.0 DGI3 롤백 안정본  
세이브 포맷: SAVE_VERSION 2 유지  
스프라이트 포맷: DGI1/DGI2/DGI3 유지 (DGI4 사용 안 함)

## 공통 DGI3 행동 매핑

- Idle: 0 <-> 1
- Walk: 0 <-> 1
  - 원본 도트는 왼쪽을 향한다고 가정
  - 왼쪽 이동 = 원본
  - 오른쪽 이동 = 좌우 반전
- Eat: 9 <-> 8
- Sleep: 11 <-> 12
- Hurt: 13 <-> 14
- Attack: 6 <-> 7
- Pose: 1 <-> 2
- Refuse: 10 + 좌우 반전 (현재 별도 Pokemon PMD role은 아니므로 보조 규칙)

이 테이블은 DMC / Pendulum / DMUL 공통으로 사용합니다.

## Pokemon 행동 체계에서 가져온 것

- 홈 화면: Idle / Walk / Pose를 랜덤 선택
- 실제 상태가 우선: Sleep / Eat / Hurt
- 공격: Attack 프레임 + 기존 전진(lunge) 효과
- 피격: Hurt 프레임 + 기존 좌우 흔들림 효과
- 좋은 작별: Pose 후 Walk로 오른쪽 퇴장
- 도망: Hurt 후 Walk로 왼쪽 퇴장
- 진화/도감 계열 기본 표시: Idle 애니메이션

PMD 이미지 리소스를 Digimon에 복사하지 않습니다. 행동 종류와 화면 이동 효과만 공유합니다.
