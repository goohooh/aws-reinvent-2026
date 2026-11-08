# AWS re:Invent 2026 세션 분석

분석일: 2026-11-05. 저장소 정리일: 2026-11-08.

전체를 보면 중심 메시지는 **에이전트가 실제 업무를 수행하도록 만들고, 그 결과·권한·비용을 운영하자**입니다. AI Ops와 Security는 이 흐름의 핵심에 있습니다.

원본의 2,468개 일정에서 동일 제목의 반복 회차를 묶고 체험·전시·행사 서비스를 제외하면 1,790개 주제입니다. 아래 내용은 발표 결과가 아닌 세션 제목·초록에 근거한 분석이고, 단기 트렌드는 분석일로부터 향후 6~12개월에 대한 판단입니다. [원본](../data/reinvent2026_sessions.json) · [집계 방법](data-guide.md) · [구조화된 추천](../data/curation.json)

## 세션들의 전체 흐름

| 주요 분야 | 주제 수 | 전체 대비 |
|---|---:|---:|
| Artificial Intelligence | 869 | 48.5% |
| Agentic AI | 787 | 44.0% |
| Security & Identity | 282 | 15.8% |
| Cloud Operations | 202 | 11.3% |

태그는 중복됩니다. 보안 세션의 43.6%, 클라우드 운영 세션의 40.6%, 개발 도구 세션의 68.6%에 Agentic AI 태그가 붙어 있습니다. 에이전트가 여러 분야의 공통 설계 조건으로 등장합니다.

| 흐름 | 핵심 질문 | 대표 세션 |
|---|---|---|
| 프로덕션에 올리기 | 데모에서 잘 되던 에이전트가 실제 업무에서도 작동하는가? | KEY003 — Data & AI Keynote; AIM212 — Best practices for production agents on AgentCore, with Nasdaq |
| 개발부터 운영까지 연결하기 | 코드를 생성한 에이전트가 테스트·배포·장애 대응에 필요한 정보도 남기는가? | DVT307 — Beyond code generation: accelerating the entire SDLC on AWS; COP407 — Build-time context for faster agentic incident response |
| 결과의 품질을 운영하기 | 오류 없이 실행됐어도 잘못된 결정을 했다면 어떻게 발견하는가? | COP337 — Wrong, Not Broken, & Why your Observability should know the difference; COP401-R — Building eval-driven observability for AI agents |
| 행동과 권한을 통제하기 | 어떤 도구를 누구의 권한으로 실행하고, 언제 사람에게 넘기는가? | SEC344 — Zero trust for non-human identities: IAM for autonomous agents; SEC349 — How to Govern an agent fleet: auto-approve the routine, escalate the ambiguous |
| 규모와 경제성 확보하기 | 장기 실행·재시도·컨텍스트·도구 호출 비용을 감당할 수 있는가? | AIM3321 — Control and optimize the cost of agents on Amazon Bedrock AgentCore; ARC317-R — Fault-tolerant AI agents: Choosing the right recovery pattern |

이 흐름 아래에는 데이터·메모리·인프라가 있습니다. **STG201 — Persistent memory, shared context, instant discovery. Solving storage for AI agents**는 에이전트 간 파일 공유와 지속 메모리, **AIM450-R — Context engineering for production agents on AgentCore**는 컨텍스트 구성, **KEY005 — Technical Innovations Keynote**는 이를 뒷받침하는 컴퓨팅·네트워크·스토리지 설계를 다룹니다.

큰 그림을 잡는 키노트는 **KEY003 → KEY001 — Developer Keynote → KEY005** 순으로 추천합니다. 프로덕션 도입의 조건, 개발 방식의 변화, 기반 기술을 연결하는 학습 순서이며 현장 시간표 순서가 아닙니다.

균형을 위해 **SNR320 — A leader's guide to what separates AI leaders from the rest**도 추천합니다. 초록은 해당 연구의 인터뷰에서 완전자율 운영 사례를 찾지 못했고 실제 가치가 데모와 다르게 나타났다고 설명합니다. 이 연구의 관찰을 전체 산업의 사실로 일반화할 수는 없지만, 자율화의 홍보 수준과 실제 위임 가능한 업무 범위를 구분하는 데 유용한 세션입니다.

## 지금 도움이 될 세션

추천 대상은 AI Ops·Security에 관심이 있고 CLI 에이전트·스킬·MCP·QA 자동화를 다루는 실무자입니다. 특정 기업의 운영 환경을 전제로 하지 않습니다. AI Ops를 다음 두 가지로 나눴습니다.

- **AI for Ops:** AI로 장애 분석·복구·보안 대응을 자동화하기.
- **Ops for AI:** 에이전트 자체의 품질·실패·권한·비용을 운영하기.

### AI Ops 우선순위

| 순위 | 세션 | 핵심 내용과 가져올 것 |
|---|---|---|
| 1 | **COP401-R — Building eval-driven observability for AI agents** · Code talk / 400 | 운영 trace를 평가 데이터셋으로 만들고 실패를 로컬에서 재현한 뒤 수정하는 전체 루프. QA 실패 사례를 재사용 가능한 회귀 평가로 연결하는 방법. |
| 2 | **OPN304-R — Observability for AI agents: Strands, OpenTelemetry, and Langfuse** · Workshop / 300 | LLM·도구 호출 추적, 토큰 비용, 프롬프트 버전, 출력 품질 평가를 직접 연결. 에이전트 실행을 관찰할 기반을 만드는 실습. |
| 3 | **COP317-R — Hands-on with AWS DevOps agent** · Workshop / 300 | EKS에 장애를 주입하고 원인을 찾은 뒤 팀 지식을 skills로 만들고 MCP·알람·승인된 복구를 연결. 운영 런북을 실행 가능한 에이전트 워크플로로 만드는 경험. |
| 4 | **COP407 — Build-time context for faster agentic incident response** · Code talk / 400 | 기능 구현 PR에 계측·알람·대시보드·운영 skills까지 포함하고 장애 대응에 재사용. 완료 기준에 운영 가능한 상태를 포함하는 패턴. |
| 5 | **AIM446-R — Beyond Prompt Engineering: Optimize the Agent Harness** · Code talk / 400 | 도구·지침·메모리·컨텍스트·오케스트레이션을 평가 실험으로 개선. 스킬과 에이전트 구성이 실제로 도움이 되는지 검증하는 방법. |

보완 세션은 **COP323-R — Trust but verify: Building the audit loop for AI agents in production**입니다. 시스템 오류는 없지만 필수 승인 없이 환불한 에이전트 사례로 감사 루프를 만듭니다. 테스트 통과와 의도·정책 준수를 별도로 확인하는 설계에 도움이 됩니다.

AWS DevOps Agent의 공식 설명도 관측 데이터·코드·배포 이력을 연결해 조사하는 구조를 강조합니다. 관련 세션에서는 우리 환경에서 필요한 맥락을 어떻게 제공할지에 집중해서 보면 좋습니다. [AWS 공식 설명](https://aws.amazon.com/ko/devops-agent/) — 2026-11-05 확인.

### Security 우선순위

| 순위 | 세션 | 핵심 내용과 가져올 것 |
|---|---|---|
| 1 | **SEC321-R — Securing AI coding agents: defense in depth across the development lifecycle** · Chalk talk / 300 | 생성 전·작성·PR·파이프라인·배포마다 규칙 기반 통제, AI 검사, 사람 판단을 배치. AGENTS.md·skills·hooks와 실제 CI 보안 통제를 연결하는 설계. |
| 2 | **SEC343 — From MCP poisoning to defense: securing the agent tool supply chain** · Builders' session / 300 | MCP 도구 오염 공격, 실행 정책, 도구 정의 변경 검사, 런타임 감시. MCP 서버와 플러그인이 늘어나는 환경에 직접 적용할 주제. |
| 3 | **SEC407-R — Constrain AI agents with permissions boundaries and Cedar in AgentCore** · Workshop / 400 | IAM 권한 경계, 정책 검증, Cedar 실행 통제. 지침에 적힌 금지 사항을 실제 실행 권한 경계로 만드는 방법. |
| 4 | **SEC416 — Orchestrating AI agents for continuous code security hardening** · Workshop / 400 | 코드·의존성·시크릿·IaC 스캐너 결과를 에이전트가 검토·분류하고 증거 기반 정책으로 통과 여부를 결정. 멀티에이전트 리뷰·QA를 보안 점검으로 확장하는 패턴. |
| 5 | **SEC344 — Zero trust for non-human identities: IAM for autonomous agents** · Builders' session / 300 | 에이전트 신원, 사용자 권한 위임, 최소 권한, 다른 에이전트로 이어지는 접근을 실습. 여러 사용자·도구·에이전트가 연결되는 권한 모델. |

보안 사고 대응 자동화가 주목적이면 **SEC347 — Agentic AI for Security: How AWS CIRT reduced triage time to minutes**를 추가합니다. 사례 수집·환경 분석·초기 판단을 자동화하면서 전문가 정답과 비교 평가하는 구조입니다. 초록의 성과 수치는 발표자의 사례 주장입니다.

### CLI 에이전트와 스킬 워크플로

- **OPN310-R — CLI Agent Orchestrator: Open source multi-agent AI for developer CLIs:** Codex·Claude Code·Kiro 등 CLI를 MCP와 tmux로 연결하는 실습. 기존 오케스트레이션 구조와 비교하기 좋습니다.
- **DVT339-R — Best practices for making coding agent orchestration more deterministic:** 긴 작업에서 계획과 실행 맥락이 무너지는 문제, 멀티에이전트 신뢰성 패턴을 다룹니다.
- **DVT415-R — Mastering agentic development: skills, custom agents, and steering:** 유용한 스킬과 불필요한 지침을 구분하고 팀의 관례를 지속적으로 전달하는 방법을 다룹니다.

## 향후 6~12개월의 트렌드 전망

카탈로그의 반복 출현, 여러 분야에 걸친 적용, 실습 세션의 구체성을 바탕으로 한 전망입니다. AWS 행사이므로 산업 전체의 도입률을 뜻하지는 않습니다. 확신은 정성적인 판단입니다.

| 예상 트렌드 | 확신 | 근거와 예상 변화 | 관련 세션 |
|---|---|---|---|
| 평가가 관측·배포 과정에 들어옴 | 높음 | HTTP 오류율만으로 잘못된 답변·도구 선택·업무 규칙 위반을 잡을 수 없습니다. 운영 trace → 평가 데이터 → 수정 → 배포 검증이 하나의 과정이 됩니다. | COP401-R, AIM440, COP323-R |
| 업무별로 자율성을 다르게 부여함 | 높음 | 일상적인 동작은 자동 승인하고 모호하거나 영향이 큰 동작은 사람에게 넘기는 설계가 운영·보안 양쪽에 등장합니다. | SEC349, COP353, SEC407-R |
| MCP·에이전트 신원이 보안의 주요 대상이 됨 | 높음 | 도구 정의 변조, 사용자 권한 위임, 에이전트 간 권한 전파를 함께 관리해야 합니다. | SEC343, SEC344, SEC419 |
| 컨텍스트·스킬·메모리를 평가하며 관리함 | 높음 | 같은 모델도 제공한 정보와 도구 구성에 따라 결과가 달라집니다. 스킬 버전과 컨텍스트 구성을 실험·평가하게 됩니다. | AIM446-R, AIM450-R, DVT415-R |
| 코딩 자동화가 릴리스·운영 자동화로 확장됨 | 중상 | PR 생성량이 늘면 리뷰·검증·배포가 병목이 됩니다. 운영 상태를 이용한 배포 판단과 개발 시점의 운영 정보 생성이 중요해집니다. | COP406-R, COP407, DVT227 |
| 에이전트 비용을 사용자·업무 결과 단위로 관리함 | 높음 | 반복 호출·장기 컨텍스트·도구 사용으로 비용이 크게 달라집니다. 예산 제한, 비용 귀속, 완료한 업무당 비용을 관리하게 됩니다. | AIM3321, PEX303-R, COP311-R |

2026-11-05에 확인한 AgentCore 공식 제품 구성에도 Identity·Policy·Evaluations·Observability가 함께 등장합니다. 권한 통제와 품질 운영이 에이전트 플랫폼의 기본 구성으로 묶이는 방향은 카탈로그 밖에서도 확인됩니다. 당시 공식 페이지는 Policy와 Evaluations를 Preview로 표시했습니다. [AgentCore 공식 설명](https://aws.amazon.com/ko/bedrock/agentcore/)

사람 없이 프로덕션 전체를 운영하는 것과 복잡한 멀티에이전트 구성을 모든 문제에 적용하는 것은 단기 도입 우선순위를 낮게 둡니다. 카탈로그 자체에서도 복구·승인·평가·비용 문제를 해결하는 세션이 반복됩니다.

## 여섯 세션의 학습 경로

**COP401-R → OPN304-R → COP317-R → SEC321-R → SEC343 → SEC407-R**

이 조합에서 가져올 결과물은 실패를 재현하는 평가셋, 에이전트 실행 trace, 스킬 기반 운영 런북, 개발 단계별 보안 통제, MCP 변경 검사, 실제 실행 권한 경계입니다. 추천 순서는 시간표가 아니며 `python3 scripts/catalog.py show CODE --repeats`로 회차를 확인할 수 있습니다.
