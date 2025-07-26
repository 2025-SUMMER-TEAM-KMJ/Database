# 프로젝트 데이터 스키마 명세

이 저장소는 프로젝트 전반에서 사용되는 모든 데이터 구조를 JSON Schema 형식으로 정의하고 관리합니다. 각 스키마는 데이터의 일관성을 보장하고, 개발자 간의 원활한 협업을 돕는 역할을 합니다.

`models.py` 파일에는 각 스키마에 대응하는 파이썬 클래스가 정의되어 있어, 타입에 안전하게 데이터를 생성하고 검증할 수 있습니다.

---

## 스키마 전체 요약

| 스키마 이름 및 파일                                            | 목적 및 설명                                                               | 상세 정보                                                 |
| -------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| **잡코리아 자소서 스키마**<br/>`jobkorea_cover_letter.schema.json`         | 잡코리아 등에서 수집된 자기소개서 원본 데이터 구조를 정의합니다.           | [자세히 보기](./schemas/jobkorea_cover_letter_README.md)    |
| **원티드 채용 공고**<br/>`wanted_job_posting.schema.json`       | 원티드에서 수집한 채용 공고 원본 데이터 구조를 정의합니다.                 | [자세히 보기](./schemas/wanted_job_posting_README.md)       |
| **원티드 기업 프로필**<br/>`wanted_company_profile.schema.json` | 원티드에서 수집한 기업 프로필 원본 데이터 구조를 정의합니다.               | [자세히 보기](./schemas/wanted_company_profile_README.md)   |
| **마스터 채용 공고**<br/>`master_job_posting.schema.json`       | 모든 채용 공고를 표준화하여 AI와 서비스에서 공통으로 사용하는 스키마입니다.  | [자세히 보기](./schemas/master_job_posting_README.md)       |
| **마스터 사용자 프로필**<br/>`master_user_profile.schema.json`   | 모든 사용자 정보를 표준화하여 공통으로 사용하는 마스터 스키마입니다.       | [자세히 보기](./schemas/master_user_profile_README.md)      |
| **크롤러 로그**<br/>`master_crawler_log.schema.json`           | 크롤러의 작업 대상 URL과 처리 상태를 관리하는 로그용 스키마입니다.         | [자세히 보기](./schemas/master_crawler_log_README.md)       |

---

## 스키마 관계 및 데이터 흐름

이 프로젝트의 데이터는 크게 **'원본(Source)'** 스키마와 **'마스터(Master)'** 스키마로 나뉩니다.

1.  **데이터 수집 (Crawling)**
    - 크롤러는 특정 플랫폼(예: 원티드, 잡코리아)의 데이터 구조를 따르는 **원본 스키마**를 사용하여 데이터를 수집합니다.
    - 예: `wanted_job_posting`, `jobkorea_cover_letter`

2.  **데이터 표준화 (Standardization)**
    - 수집된 원본 데이터는 처리 과정을 거쳐 모든 서비스에서 일관된 형태로 사용할 수 있는 **마스터 스키마**로 변환됩니다.
    - 예: `wanted_job_posting` 데이터는 `master_job_posting` 데이터로 변환됩니다.

3.  **데이터 활용 (Application)**
    - AI 모델, API 서버, 프론트엔드 등 모든 애플리케이션은 **마스터 스키마**를 기준으로 데이터를 주고받는 것을 원칙으로 합니다. 이는 데이터의 일관성을 유지하고 확장성을 높입니다.

4.  **보조 스키마**
    - `master_crawler_log`와 같은 스키마는 데이터 자체보다는 데이터 처리 프로세스를 관리하기 위해 사용됩니다.

## Python 클래스 활용

모든 스키마는 `models.py`에 파이썬 클래스로 구현되어 있습니다. 각 클래스는 데이터 생성, 딕셔너리 변환, 유효성 검증 기능을 제공하여 개발 생산성을 높입니다.

```python
# 예시: MasterJobPosting 클래스 사용
from models import MasterJobPosting

# 딕셔너리로부터 안전하게 객체 생성
# (내부적으로 스키마 유효성 검사가 수행됨)
job_data = get_job_data_from_db()
try:
    master_job = MasterJobPosting.from_dict(job_data)
    print(f"로드 성공: {master_job.detail.get('position')}")
except ValueError as e:
    print(f"데이터 형식 오류: {e}")

```
