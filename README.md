# AWS re:Invent 2026 세션 가이드

AWS re:Invent 2026 세션 카탈로그를 바탕으로 전체 주제의 흐름, AI Ops·Security 실무 추천, 향후 6~12개월의 트렌드를 정리한 개인 연구 저장소입니다. 사람과 AI 에이전트가 같은 원본과 추천 근거를 읽고 후속 분석에 사용할 수 있습니다.

핵심 해석은 **에이전트가 실제 업무를 수행하도록 만들고, 그 결과·권한·비용을 운영하는 방법**이 프로그램의 중심이라는 것입니다. 분석은 세션 제목·초록에 근거하며, 실제 발표 결과나 제품 출시를 확인한 기록은 아닙니다.

## 바로 읽기

- [세션 흐름, 실무 추천, 단기 트렌드](docs/analysis.ko.md)
- [데이터 구조와 집계 방법](docs/data-guide.md)
- [다른 에이전트를 위한 작업 안내](AGENTS.md)
- [외부 행사 종류별 정리](docs/parties.ko.md) · [외부 행사 JSON](data/reinvent2026_parties.json)
- [프로젝트 스킬 reinvent-research](.agents/skills/reinvent-research/SKILL.md)
- [추천 및 전망 JSON](data/curation.json)
- [전체 세션 원본 JSON](data/reinvent2026_sessions.json)
- [재현 가능한 통계](data/stats.json) · [출처와 스냅샷 정보](data/provenance.json)

## 분석 범위

| 항목 | 수치 |
|---|---:|
| 원본 일정 레코드 | 2,468 |
| 동일 제목을 묶은 항목 | 1,849 |
| 체험·전시·행사 서비스 제외 후 주제 | 1,790 |
| Artificial Intelligence 태그 | 869 / 48.5% |
| Agentic AI 태그 | 787 / 44.0% |
| Security & Identity 태그 | 282 / 15.8% |
| Cloud Operations 태그 | 202 / 11.3% |

태그는 중복됩니다. 동일 제목은 하나의 주제로 묶되, 실제 일정은 원본에 모두 보존합니다. 최초 분석일은 2026-11-05, 저장소 정리일은 2026-11-08입니다. 카탈로그의 정확한 수집 시각과 수집 도구는 제공되지 않았습니다.

## 여섯 세션만 고른다면

1. **COP401-R** — 평가 기반 관측과 운영 실패의 회귀 평가
2. **OPN304-R** — OpenTelemetry·Langfuse로 에이전트 관측 실습
3. **COP317-R** — 장애 조사, skills·MCP 연결, 승인된 복구
4. **SEC321-R** — AI 코딩 에이전트의 개발 단계별 보안 통제
5. **SEC343** — MCP 도구 공급망 공격과 방어
6. **SEC407-R** — IAM·Cedar를 통한 실행 권한 경계

추천 순서이며 시간표가 아닙니다. 반복 회차와 일정 충돌은 별도로 확인해야 합니다.

## 프로젝트 스킬로 검색과 갱신

`.agents/skills/reinvent-research`에 프로젝트 스킬을 제공합니다. 기존 독립 CLI 스크립트는 스킬로 대체했습니다. 지원하는 에이전트는 `$reinvent-research`로 호출하고, 자동 탐색을 지원하지 않는 에이전트는 SKILL.md를 직접 읽으면 됩니다. 저장된 JSON을 읽는 데 API 키나 네트워크 연결은 필요 없습니다. 웹 갱신에는 `ego-browser`가 필요합니다.

```bash
git clone https://github.com/goohooh/aws-reinvent-2026.git
cd aws-reinvent-2026
```

사용 예시:

- `$reinvent-research MCP 보안 세션을 찾아서 추천 이유와 반복 회차를 알려줘.`
- `$reinvent-research 외부 행사에서 AI Ops와 Security 관련 점심·저녁을 찾아줘.`
- `$reinvent-research Conference Parties를 갱신하고 JSON과 종류별 Markdown을 업데이트해줘.`
- `$reinvent-research 원본 해시, 통계, 세션 참조와 외부 행사 분류를 검증해줘.`

다른 세션이나 에이전트에게는 다음처럼 요청할 수 있습니다.

> 이 저장소의 AGENTS.md와 .agents/skills/reinvent-research/SKILL.md를 읽고 작업하세요. 세션은 data/reinvent2026_sessions.json, 외부 행사는 data/reinvent2026_parties.json에서 확인하세요. JSON 증거와 Markdown 해석을 구분하고 기존 분석을 내 목표에 맞게 이어가세요.

외부 행사는 [Conference Parties](https://conferenceparties.com/reinvent2026/)의 2026-11-08 스냅샷 178개 목록 항목을 8가지 형식으로 분류했습니다. 중복 목록도 보존한 수치이며 세션 통계에 합산하지 않습니다. [데이터 구조와 한계](docs/parties-data-guide.md)를 참고하세요.

## 출처와 이용 범위

AWS 공식 저장소가 아닙니다. 원본은 사용자가 제공한 `reinvent2026_sessions.json`이며 바이트 단위로 보존했습니다. 제목·초록 등 제3자 콘텐츠의 권리는 각 권리자에게 있습니다. 한국어 제목·요약의 작성 방식은 확인되지 않았습니다. 분석·추천·전망은 이 저장소의 해석이며, 세션 내 성과 수치는 발표자의 주장입니다. 원본을 포함한 모든 자료에 일괄적인 오픈소스 라이선스를 부여하지 않습니다.

2026-11-05에 제품 맥락을 확인한 공식 참고 자료: [Amazon Bedrock AgentCore](https://aws.amazon.com/ko/bedrock/agentcore/), [AWS DevOps Agent](https://aws.amazon.com/ko/devops-agent/). 이 링크들은 세션 일정이나 카탈로그 전체의 진위를 검증하는 출처가 아닙니다.
