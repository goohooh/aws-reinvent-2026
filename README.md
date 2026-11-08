# AWS re:Invent 2026 세션 가이드

AWS re:Invent 2026 세션 카탈로그를 바탕으로 전체 주제의 흐름, AI Ops·Security 실무 추천, 향후 6~12개월의 트렌드를 정리한 개인 연구 저장소입니다. 사람과 AI 에이전트가 같은 원본과 추천 근거를 읽고 후속 분석에 사용할 수 있습니다.

핵심 해석은 **에이전트가 실제 업무를 수행하도록 만들고, 그 결과·권한·비용을 운영하는 방법**이 프로그램의 중심이라는 것입니다. 분석은 세션 제목·초록에 근거하며, 실제 발표 결과나 제품 출시를 확인한 기록은 아닙니다.

## 바로 읽기

- [세션 흐름, 실무 추천, 단기 트렌드](docs/analysis.ko.md)
- [데이터 구조와 집계 방법](docs/data-guide.md)
- [다른 에이전트를 위한 작업 안내](AGENTS.md)
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

## 검색과 재현

Python 3.10 이상과 표준 라이브러리만 사용합니다. 설치·API 키·네트워크 연결이 필요 없습니다. 출력은 JSON입니다.

```bash
git clone https://github.com/goohooh/aws-reinvent-2026.git
cd aws-reinvent-2026
python3 scripts/catalog.py validate
python3 scripts/catalog.py stats
python3 scripts/catalog.py search 'MCP' --limit 10
python3 scripts/catalog.py search '보안' --unique
python3 scripts/catalog.py show COP401-R --repeats
python3 scripts/catalog.py shortlist --category security
```

다른 세션이나 에이전트에게는 다음처럼 요청할 수 있습니다.

> 이 저장소의 AGENTS.md, docs/analysis.ko.md, data/curation.json을 읽고 기존 분석을 이어가세요. 세션 설명은 data/reinvent2026_sessions.json에서 확인하고, 추천에는 정확한 코드와 근거를 포함하세요. 기존 추천을 출발점으로 삼되 내 새로운 목표에 맞게 우선순위를 조정하세요.

## 출처와 이용 범위

AWS 공식 저장소가 아닙니다. 원본은 사용자가 제공한 `reinvent2026_sessions.json`이며 바이트 단위로 보존했습니다. 제목·초록 등 제3자 콘텐츠의 권리는 각 권리자에게 있습니다. 한국어 제목·요약의 작성 방식은 확인되지 않았습니다. 분석·추천·전망은 이 저장소의 해석이며, 세션 내 성과 수치는 발표자의 주장입니다. 원본을 포함한 모든 자료에 일괄적인 오픈소스 라이선스를 부여하지 않습니다.

2026-11-05에 제품 맥락을 확인한 공식 참고 자료: [Amazon Bedrock AgentCore](https://aws.amazon.com/ko/bedrock/agentcore/), [AWS DevOps Agent](https://aws.amazon.com/ko/devops-agent/). 이 링크들은 세션 일정이나 카탈로그 전체의 진위를 검증하는 출처가 아닙니다.
