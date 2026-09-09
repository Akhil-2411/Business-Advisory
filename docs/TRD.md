# Technical Requirements Document (TRD)

# GramVikas AI
### AI-Driven Hyper-Local Business Advisory & Financial Structuring Assistant for Rural Micro-Entrepreneurs

---

# 1. Technical Overview

GramVikas AI is a full-stack AI-powered platform that provides:

- Hyper-local business intelligence
- Geographic market analysis
- Competition analysis
- Opportunity discovery
- Financial structuring
- Government scheme routing
- AI-generated feasibility reports

The platform combines:

- GIS Intelligence
- Business Analytics
- Financial Modeling
- OpenAI-powered Advisory
- Interactive Mapping

into a unified decision-support platform for rural entrepreneurs.

---

# 2. System Architecture

```text
┌─────────────────────────────────────┐
│             Frontend                │
│ React + Tailwind + shadcn/ui        │
└─────────────────┬───────────────────┘
                  │
                  ▼

┌─────────────────────────────────────┐
│             FastAPI                 │
│          REST API Layer             │
└─────────────────┬───────────────────┘
                  │

 ┌────────────────┼─────────────────┐
 ▼                ▼                 ▼

Business      Financial        AI Advisory
Engine        Engine           Engine

 │                │                 │
 └────────────────┼─────────────────┘
                  │
                  ▼

        Supabase PostgreSQL
      + Vector Embedding Store

                  │
                  ▼

             OpenAI API

                  │
                  ▼

      Telangana Village GeoJSON
      Telangana Village Centroids
      District MSME Dataset
      Cleaned MSME Dataset
```

---

# 3. Technology Stack

## Frontend

### React

Frontend SPA Framework

### JavaScript

Application Logic

### TailwindCSS

Responsive Styling

### shadcn/ui

Reusable Components

### 21st.dev

Production UI Blocks

### Leaflet.js

GIS Visualization

### OpenStreetMap

Map Tile Provider

---

## Backend

### FastAPI

REST APIs

### Pydantic

Validation

### Uvicorn

ASGI Runtime

---

## Database

### Supabase PostgreSQL

Primary Relational Database

### pgvector

Embedding Storage

---

## AI Layer

### OpenAI

Business Intelligence Generation

### Embeddings

Semantic Search

### RAG Retrieval

Context-Aware Advisory

---

## Deployment

### Frontend

Vercel

### Backend

Render / Railway

### Database

Supabase Cloud

---

# 4. Frontend Architecture

```text
src/

├── pages/
├── components/
├── features/
│   ├── advisory/
│   ├── finance/
│   ├── maps/
│   └── reports/
├── services/
├── hooks/
├── utils/
├── layouts/
└── assets/
```

---

# 5. Backend Architecture

```text
backend/

├── app/
├── api/
├── services/
├── schemas/
├── models/
├── repositories/
├── analytics/
├── gis/
├── financial/
├── ai/
└── reports/
```

---

# 6. Data Sources

The platform strictly relies on curated datasets present within the project repository.

No external or unverified datasets are used during business analysis.

---

## Dataset 1: Telangana Villages GeoJSON

**File:** `telangana_villages.geojson`

### Purpose

- Village boundary visualization
- GIS rendering
- Radius analysis
- Market reach estimation
- Neighbor village discovery

### Used By

- Leaflet.js
- OpenStreetMap Layer
- Market Reach Engine

---

## Dataset 2: Telangana Village Centroids

**File:** `telangana_village_centroids.csv`

### Purpose

- Latitude & longitude reference
- Distance calculations
- Radius calculations
- Nearby village discovery
- Consumer reach estimation

### Used By

- GIS Engine
- Market Reach Module

---

## Dataset 3: District MSME Analytics Dataset

**File:** `district_msme_final.csv`

### Purpose

- Competition analysis
- Market saturation estimation
- Opportunity discovery
- District business intelligence

### Used By

- Competitor Mapping Engine
- Opportunity Discovery Engine

---

## Dataset 4: Cleaned MSME Master Dataset

**File:** `cleaned_msme_final.xls`

### Purpose

- Industry distribution analysis
- Sector-wise trends
- Enterprise classification
- Business recommendations

### Used By

- AI Advisory Engine
- Business Intelligence Engine

---

# 7. Data Governance Policy

The platform performs analysis only on validated datasets.

Future datasets must pass:

- Data Cleaning
- Duplicate Removal
- Schema Validation
- Geographic Validation
- Consistency Checks

Raw or unverified datasets are never used directly for AI recommendations.

---

# 8. Database Design

## users

```sql
id UUID PRIMARY KEY
name TEXT
phone TEXT
language TEXT
created_at TIMESTAMP
```

---

## villages

```sql
id UUID PRIMARY KEY
district TEXT
mandal TEXT
village_name TEXT
latitude FLOAT
longitude FLOAT
geojson JSONB
```

---

## district_msme

```sql
id UUID PRIMARY KEY
district_name TEXT
total_msme INTEGER
competition_score FLOAT
updated_at TIMESTAMP
```

---

## business_reports

```sql
id UUID PRIMARY KEY
user_id UUID
district TEXT
village TEXT
business_category TEXT
opportunity_score FLOAT
competition_score FLOAT
risk_score FLOAT
swot JSONB
report_json JSONB
created_at TIMESTAMP
```

---

## financial_reports

```sql
id UUID PRIMARY KEY
user_id UUID
margin_capital FLOAT
project_cost FLOAT
loan_amount FLOAT
scheme TEXT
emi FLOAT
created_at TIMESTAMP
```

---

## embeddings

```sql
id UUID PRIMARY KEY
content TEXT
embedding VECTOR
source TEXT
metadata JSONB
```

---

# 9. GIS Architecture

## Mapping Stack

- Leaflet.js
- OpenStreetMap

---

## Village Boundary Rendering

Uses:

`telangana_villages.geojson`

Capabilities:

- Polygon rendering
- Village selection
- Boundary highlighting

---

## Radius Engine

Generates:

- 5 km Radius
- 10 km Radius

around selected village.

---

## Market Reach Analysis

Calculates:

- Reachable villages
- Service area coverage
- Estimated consumer reach

---

## Competitor Visualization

Displays:

- Cluster markers
- Competition heatmaps
- Opportunity zones

---

# 10. Business Intelligence Engine

Responsible For:

- Competition analysis
- Opportunity discovery
- Threat identification
- Pricing recommendations
- Market saturation analysis

### Inputs

- District
- Village
- Business Category

### Outputs

```json
{
  "opportunity_score": 82,
  "competition_score": 45,
  "risk_score": 31,
  "recommendation": "Proceed"
}
```

---

# 11. Financial Structuring Engine

### Inputs

```json
{
  "margin_capital": 100000
}
```

### Calculations

```text
Project Cost = Margin Capital ÷ 10%

Loan Amount = Project Cost × 90%
```

### Scheme Routing

#### Micro Finance Scheme

Project Cost ≤ ₹1.40 Lakh

- Interest Rate: 6.5%
- Tenure: 3 Years
- Moratorium: 3 Months

#### Term Loan Scheme

₹1.40 Lakh < Project Cost ≤ ₹50 Lakh

- Interest Rate: 8%
- Tenure: 7 Years
- Moratorium: 6 Months

#### Not Eligible

Project Cost > ₹50 Lakh

### Outputs

- Project Cost
- Loan Amount
- Scheme
- EMI
- Quarterly Repayment
- Total Interest
- Total Repayment

---

# 12. AI Advisory Engine

Uses OpenAI to generate:

- SWOT Analysis
- Threat Analysis
- Opportunity Analysis
- Pricing Guidance
- Business Recommendations

### Inputs

```json
{
  "district": "Nalgonda",
  "village": "Chityal",
  "business": "Dairy",
  "capital": 100000
}
```

### Outputs

```json
{
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": []
}
```

---

# 13. RAG Architecture

## Retrieval Flow

```text
User Query
      ↓
Embedding Creation
      ↓
Vector Search
      ↓
Relevant Dataset Context
      ↓
Prompt Augmentation
      ↓
OpenAI Response
```

### Knowledge Sources

- district_msme_final.csv
- cleaned_msme_final.xls
- telangana_village_centroids.csv
- telangana_villages.geojson

---

# 14. API Design

## POST /api/analyze-business

```json
{
  "district": "Nalgonda",
  "village": "Chityal",
  "business": "Dairy",
  "margin_capital": 100000
}
```

---

## POST /api/calculate-finance

```json
{
  "margin_capital": 100000
}
```

---

## POST /api/chat

```json
{
  "query": "Is dairy business viable in my district?"
}
```

---

# 15. Report Generation Pipeline

```text
Business Analysis
        +
Financial Analysis
        +
GIS Analysis
        +
AI Recommendations
        ↓
Generate PDF
        ↓
Store in Supabase
        ↓
Download
```

---

# 16. Security Requirements

## Authentication

JWT Authentication

### Security Controls

- HTTPS
- Rate Limiting
- Input Validation
- Row Level Security (RLS)

---

# 17. Performance Requirements

- API Response < 3 Seconds
- Map Load < 2 Seconds
- Report Generation < 10 Seconds

---

# 18. Deployment Architecture

```text
Frontend (Vercel)
        │
        ▼

FastAPI Backend
(Render / Railway)
        │
        ▼

Supabase Cloud
        │
        ▼

OpenAI API
```

---

# 19. MVP Deliverables

✅ Hyper-Local Business Intelligence

✅ GIS Market Reach Analysis

✅ Competitor Mapping

✅ Opportunity Discovery

✅ Threat Analysis

✅ Product Market Value Engine

✅ Smart Financial Calculator

✅ Scheme Router

✅ EMI Planner

✅ Interactive GIS Map

✅ AI Advisory Assistant

✅ PDF Report Generator

✅ FastAPI Backend

✅ Supabase PostgreSQL

✅ OpenAI Integration

✅ React Frontend

✅ Multilingual Support

---

# 20. Future Scope

- Voice-based advisory
- WhatsApp integration
- Mobile application
- District analytics dashboard
- Government monitoring portal
- Predictive opportunity forecasting