# 마스터 사용자 프로필 스키마 (Master User Profile Schema)

사용자의 모든 프로필 정보를 표준화하여 저장하기 위한 마스터 스키마입니다. 이 스키마는 개인 기본 정보부터 학력, 전체 경력, 보유 역량, 개인 서술까지 포괄적인 데이터를 구조화하여 관리의 일관성과 확장성을 보장합니다.

---

### 주요 필드 설명

-   **`name`** (string, **필수**): 사용자 이름.
-   **`age`** (integer, **필수**): 나이.
-   **`gender`** (string, **필수**): 성별 (`Male`, `Female`, `Other`).
-   **`email`** (string, **필수**): 이메일 주소.
-   **`phone`** (string, **필수**): 연락처.
-   **`urls`** (array of strings): 이력서, 포트폴리오, 블로그 등 개인 관련 URL 링크 목록.
-   **`brief`** (string): 사용자에 대한 한 줄 자기소개 또는 요약.
-   **`education`** (array of objects): 학력 정보 목록.
    -   `schoolName` (string, **필수**), `major` (string), `degree` (string), `startDate` (string, **필수**), `endDate` (string)
-   **`workExperience`** (array of objects): 정규직, 계약직 등 공식적인 경력 정보 목록.
    -   `companyName` (string, **필수**), `jobGroup` (string, **필수**), `job` (string, **필수**), `startDate` (string, **필수**), `endDate` (string), `description` (string)
-   **`experience`** (array of objects): 경력 외 모든 경험 목록 (예: 개인 프로젝트, 대외활동, 스터디 등).
    -   `title` (string, **필수**), `description` (string), `link` (string), `techStack` (array), `startDate` (string), `endDate` (string)
-   **`competencies`** (array of strings): 보유 역량 목록 (예: Python, JavaScript, Communication, Leadership).
-   **`preferredPosition`** (array of objects): 희망하는 직무 및 직군 목록.
    -   `jobGroup` (string, **필수**), `job` (string)
-   **`certifications`** (array of objects): 자격증, 수상 내역, 수료증 등 증빙 가능한 성취 목록.
    -   `name` (string, **필수**), `agency` (string), `issueDate` (string, **필수**)
-   **`QnAs`** (array of objects): 사용자의 가치관, 성격, 경험 등을 보여주는 문답(Q&A) 형식의 개인 서술 목록.
    -   `title` (string), `content` (string), `category` (string)

---

### Python 클래스 활용
현재 models.py에 최신화되어 있지 않습니다.

```