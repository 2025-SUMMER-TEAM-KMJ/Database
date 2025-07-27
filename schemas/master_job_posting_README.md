# 크롤러 로그 항목 스키마 (crawler_log_item.schema.json)

크롤러가 처리할 개별 로그 항목의 데이터 구조를 정의하는 스키마입니다. 이 스키마는 **단일 로그 항목**을 나타내며, 이런 항목들이 모여 전체 로그 데이터(예: MongoDB 컬렉션)를 구성하게 됩니다.

> ⚠️ **이전 버전과의 차이점**
> 이전 스키마는 파일 자체가 로그 목록(`{"urls": [...]}`)을 담는 구조였지만, 현재 스키마는 각 로그 항목이 독립적인 객체(문서)가 되는 것을 전제로 합니다. 이는 데이터베이스의 확장성과 쿼리 성능에 더 최적화된 방식입니다.

---

### 주요 필드 설명

- **`url`** (string, **필수**):
  - **설명**: 수집 대상이 되는 고유한 URL입니다.
  - **예시**: `"https://www.wanted.co.kr/wd/12345"`

- **`purposes`** (array of strings):
  - **설명**: 해당 URL에서 수집해야 할 데이터의 목적들을 정의하는 목록입니다. 하나의 URL에서 채용 공고와 기업 정보를 모두 수집하는 등 여러 목적을 가질 수 있습니다.
  - **예시**: `["job_posting", "company_profile"]`

- **`crawledAt`** (string or null, **필수**):
  - **설명**: 이 로그 항목을 마지막으로 처리(크롤링)한 시각을 나타내는 타임스탬프입니다. 아직 한 번도 처리되지 않은 새로운 항목의 경우 `null` 값을 가집니다.
  - **예시**: `"2025-07-26T14:30:00Z"` 또는 `null`

---

### Python 클래스 활용

`models.py`에 정의된 `MasterCrawlerLog` 클래스를 사용하여 이 스키마를 따르는 데이터를 생성하고 검증할 수 있습니다.

```python
from models import MasterCrawlerLog
from typing import List

# 개별 로그 항목 데이터 생성
log_data_1 = {
    "url": "https://www.wanted.co.kr/wd/12345",
    "purposes": ["job_posting", "company_profile"],
    "crawledAt": "2025-07-26T14:30:00Z"
}

log_data_2 = {
    "url": "https://www.saramin.co.kr/zf_user/jobs/view?rec_idx=98765",
    "purposes": ["job_posting"],
    "crawledAt": None  # 아직 처리되지 않은 항목
}

try:
    # 딕셔너리로부터 클래스 인스턴스 생성
    item1 = CrawlerLogItem.from_dict(log_data_1)
    item2 = CrawlerLogItem.from_dict(log_data_2)

    # 실제 데이터는 이런 인스턴스들의 리스트로 관리됩니다.
    all_logs: List[CrawlerLogItem] = [item1, item2]

    print("생성된 로그 항목 1:", item1)
    print("생성된 로그 항목 2:", item2.to_dict())

except ValueError as e:
    print(f"데이터 생성 실패: {e}")
```

### 데이터베이스(MongoDB)에서의 활용

이 스키마는 각 로그 항목이 MongoDB 컬렉션의 **개별 문서(Document)**가 되도록 설계되었습니다. 이 구조는 인덱싱을 통한 빠른 조회와 뛰어난 확장성을 제공합니다.

-   **`url` 필드**: 고유 인덱스(Unique Index)를 생성하여 중복 수집을 방지할 수 있습니다.
-   **`purposes` 필드**: 다중 키 인덱스(Multikey Index)를 생성하여 `"job_posting"`과 같은 특정 목적을 가진 모든 URL을 효율적으로 조회할 수 있습니다.

**쿼리 예시:**
```javascript
// 모든 'job_posting' 목적의 로그 찾기
db.crawler_logs.find({ 
    purposes: "job_posting"
})
```