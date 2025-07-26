# 마스터 채용 공고 스키마 (master_job_posting.schema.json)

다양한 출처에서 수집된 채용 공고 데이터를 표준화하여 AI, 프론트엔드 등 여러 서비스에서 일관되게 사용하기 위한 마스터 스키마입니다.

---

### 주요 필드 설명

- **`metadata`** (object, **필수**): 데이터 수집 메타 정보.
- **`sourceData`** (object or string, **필수**): 원본 데이터.
- **`externalUrl`** (string): 외부 채용 공고로 직접 연결되는 URL.
- **`status`** (string, **필수**): 공고 상태 (`active` 또는 `closed`).
- **`due_time`** (string or null): 공고 마감 시각.
- **`detail`** (object, **필수**): 공고의 상세 내용 (직무, 주요 업무, 자격 요건 등).
  - `position` (object, **필수**): 채용 포지션 정보.
  - `main_tasks` (string, **필수**): 주요 업무.
  - `requirements` (string, **필수**): 자격 요건.
- **`company`** (object, **필수**): 시스템이 분석/가공한 기업 프로필 정보.
  - `address` (object, **필수**): 주소 정보.
- **`skill_tags`** (array of strings): 요구 기술 스택 목록.
- **`title_images`** (array of strings): 공고 대표 이미지 URL 목록.

---

### Python 클래스 활용

`main.py`의 `MasterJobPosting` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from main import MasterJobPosting

# 딕셔너리로부터 객체 생성
job_posting_data = {
    "metadata": {"source": "Wanted", "sourceUrl": "...", "crawledAt": "..."},
    "sourceData": "...",
    "status": "active",
    "detail": {
        "position": {"jobGroup": "개발"},
        "main_tasks": "API 개발",
        "requirements": "Python 경험 3년 이상"
    },
    "company": {"address": {"full_location": "서울시 강남구"}}
}

instance = MasterJobPosting.from_dict(job_posting_data)
print(instance)
```