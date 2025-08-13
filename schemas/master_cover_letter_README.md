# 프로필 자소서 스키마 (master_cover_letter.schema.json)

사용자의 프로필 자기소개서 데이터를 구조화하고 검증하기 위한 스키마입니다.

---

### 주요 필드 설명

- **`title`** (string): 자기소개서의 전체 제목.
- **`updatedAt`** (string, format: date-time): 최종 수정 일자. ISO 형식의 날짜와 시간으로 기록됩니다.
- **`analysis`** (object): 사용자의 역량 분석 섹션.
  - `strengths` (array of strings): 프로필에서 강조된 핵심 역량 목록.
  - `weaknesses` (array of strings): 프로필에 충분히 드러나지 않은 역량 목록.
- **`QnAs`** (array of objects): 질문과 답변 형식의 자기소개 항목 목록.
  - `question` (string, **필수**): 질문 내용 (예: "성장 과정을 들려주세요.").
  - `answer` (string, **필수**): 질문에 대한 답변 내용.

---

### Python 클래스 활용
현재 models.py에 구현되어 있지 않습니다.