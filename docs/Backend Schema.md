# Backend Schema Document

# GramVikas AI
### FastAPI Backend Specification

---

# 1. Backend Overview

Backend Framework:

- FastAPI
- Pydantic
- Uvicorn

Responsibilities:

- Business Analysis
- Financial Structuring
- AI Advisory
- GIS Processing
- Report Generation
- Authentication
- Database Operations

---

# 2. Backend Folder Structure

```text id="backend1"
backend/

├── app.py
│
├── api/
│   ├── advisory.py
│   ├── finance.py
│   ├── gis.py
│   ├── reports.py
│   └── chat.py
│
├── schemas/
│
├── models/
│
├── services/
│
├── repositories/
│
├── analytics/
│
├── financial/
│
├── ai/
│
├── gis/
│
├── reports/
│
└── core/
```

---

# 3. Pydantic Schemas

---

## AnalyzeBusinessRequest

```python id="schema1"
from pydantic import BaseModel

class AnalyzeBusinessRequest(BaseModel):
    district: str
    village: str
    business_category: str
    margin_capital: float
```

---

## AnalyzeBusinessResponse

```python id="schema2"
class AnalyzeBusinessResponse(BaseModel):
    opportunity_score: float
    competition_score: float
    risk_score: float

    swot: dict

    pricing_strategy: dict

    recommendation: str
```

---

## FinancialCalculationRequest

```python id="schema3"
class FinancialCalculationRequest(BaseModel):
    margin_capital: float
```

---

## FinancialCalculationResponse

```python id="schema4"
class FinancialCalculationResponse(BaseModel):

    project_cost: float

    loan_amount: float

    scheme: str

    interest_rate: float

    tenure_years: int

    moratorium_months: int

    monthly_emi: float

    quarterly_emi: float

    total_interest: float

    total_repayment: float
```

---

## AIChatRequest

```python id="schema5"
class AIChatRequest(BaseModel):
    query: str
```

---

## AIChatResponse

```python id="schema6"
class AIChatResponse(BaseModel):
    answer: str
```

---

## ReportGenerationRequest

```python id="schema7"
class ReportGenerationRequest(BaseModel):
    report_id: str
```

---

## ReportGenerationResponse

```python id="schema8"
class ReportGenerationResponse(BaseModel):
    pdf_url: str
```

---

# 4. Database Models

---

## User Model

```python id="model1"
class User:
    id: UUID
    full_name: str
    phone: str
    language: str
```

---

## Village Model

```python id="model2"
class Village:
    id: UUID
    district: str
    mandal: str
    village_name: str
    latitude: float
    longitude: float
```

---

## DistrictMSME Model

```python id="model3"
class DistrictMSME:
    id: UUID
    district_name: str
    total_msmes: int
    competition_score: float
```

---

## BusinessReport Model

```python id="model4"
class BusinessReport:
    id: UUID

    user_id: UUID

    district: str

    village: str

    business_category: str

    opportunity_score: float

    competition_score: float

    risk_score: float

    swot: dict

    recommendations: dict
```

---

## FinancialReport Model

```python id="model5"
class FinancialReport:
    id: UUID

    user_id: UUID

    margin_capital: float

    project_cost: float

    loan_amount: float

    scheme: str

    interest_rate: float

    monthly_emi: float

    quarterly_emi: float
```

---

# 5. API Contracts

---

# POST /api/analyze-business

## Request

```json id="api1"
{
  "district": "Nalgonda",
  "village": "Chityal",
  "business_category": "Dairy",
  "margin_capital": 100000
}
```

---

## Response

```json id="api2"
{
  "opportunity_score": 82,
  "competition_score": 41,
  "risk_score": 28,

  "swot": {},

  "pricing_strategy": {},

  "recommendation": "Proceed"
}
```

---

# POST /api/calculate-finance

## Request

```json id="api3"
{
  "margin_capital": 100000
}
```

---

## Response

```json id="api4"
{
  "project_cost": 1000000,
  "loan_amount": 900000,
  "scheme": "Term Loan Scheme",
  "interest_rate": 8,
  "monthly_emi": 14000
}
```

---

# POST /api/chat

## Request

```json id="api5"
{
  "query": "Is dairy business viable in my district?"
}
```

---

## Response

```json id="api6"
{
  "answer": "Based on MSME density..."
}
```

---

# POST /api/generate-report

## Request

```json id="api7"
{
  "report_id": "uuid"
}
```

---

## Response

```json id="api8"
{
  "pdf_url": "/reports/report.pdf"
}
```

---

# 6. Service Layer

---

## BusinessAnalysisService

Responsibilities:

- Competition Analysis
- Opportunity Analysis
- SWOT Generation
- Pricing Recommendation

Methods:

```python id="service1"
analyze_business()
generate_swot()
generate_pricing_strategy()
```

---

## FinancialService

Responsibilities:

- Project Cost Calculation
- Loan Calculation
- Scheme Routing
- EMI Generation

Methods:

```python id="service2"
calculate_project_cost()
calculate_loan_amount()
route_scheme()
calculate_emi()
```

---

## GISService

Responsibilities:

- Radius Calculation
- Village Lookup
- Market Reach Analysis

Methods:

```python id="service3"
find_nearby_villages()
calculate_radius()
market_reach_analysis()
```

---

## AIService

Responsibilities:

- OpenAI Calls
- Prompt Construction
- Report Generation

Methods:

```python id="service4"
generate_advisory()
generate_report()
chat()
```

---

# 7. Repository Layer

---

## VillageRepository

```python id="repo1"
get_village()
get_nearby_villages()
```

---

## MSMERepository

```python id="repo2"
get_district_stats()
get_competition_data()
```

---

## ReportRepository

```python id="repo3"
save_report()
fetch_report()
```

---

## FinancialRepository

```python id="repo4"
save_financial_report()
```

---

# 8. Validation Rules

## Business Analysis

```text id="val1"
District Required
Village Required
Business Category Required
Margin Capital > 0
```

---

## Financial Calculation

```text id="val2"
Margin Capital > 0
Margin Capital < ₹5,00,000
```

(₹5 lakh margin corresponds to ₹50 lakh project ceiling.)

---

# 9. Financial Engine Rules

---

## Project Cost

```text id="rule1"
Project Cost = Margin Capital / 0.10
```

---

## Loan Amount

```text id="rule2"
Loan Amount = Project Cost × 0.90
```

---

## Micro Finance

```text id="rule3"
Project Cost ≤ ₹1.40 Lakh
```

Interest: 6.5%

Tenure: 3 Years

Moratorium: 3 Months

---

## Term Loan

```text id="rule4"
₹1.40 Lakh < Project Cost ≤ ₹50 Lakh
```

Interest: 8%

Tenure: 7 Years

Moratorium: 6 Months

---

# 10. External Integrations

### OpenAI

Used For:

- SWOT Analysis
- Threat Detection
- Opportunity Discovery
- Business Recommendations

---

### Supabase

Used For:

- PostgreSQL Database
- Authentication
- Storage
- Vector Embeddings

---

### OpenStreetMap

Used For:

- Map Tiles

---

### Leaflet.js

Used For:

- GIS Visualization
- Radius Mapping
- Village Boundary Rendering

---

# 11. Error Responses

## Validation Error

```json id="error1"
{
  "error": "Invalid Input"
}
```

---

## Village Not Found

```json id="error2"
{
  "error": "Village Not Found"
}
```

---

## Report Not Found

```json id="error3"
{
  "error": "Report Not Found"
}
```

---

# 12. Backend Deliverables

✅ FastAPI APIs

✅ Pydantic Schemas

✅ Financial Engine

✅ GIS Engine

✅ AI Advisory Engine

✅ Report Generator

✅ Supabase Integration

✅ OpenAI Integration

✅ Authentication Layer

✅ Storage Layer