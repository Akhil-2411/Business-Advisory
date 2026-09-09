# Database Architecture

# GramVikas AI
### AI-Driven Hyper-Local Business Advisory & Financial Structuring Assistant

---

# 1. Database Overview

Database Platform:

**Supabase PostgreSQL**

Extensions:

- pgvector
- PostGIS (Optional Future Enhancement)

Purpose:

- User Management
- Village Data Storage
- MSME Analytics
- Financial Reports
- Business Reports
- AI Advisory History
- Embedding Storage

---

# 2. Database Architecture

```text
                    ┌─────────────────────┐
                    │      Users          │
                    └──────────┬──────────┘
                               │
                               ▼

                    ┌─────────────────────┐
                    │ Business Reports    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼

      Financial Reports   AI Chats      Generated Reports

                               │
                               ▼

                    ┌─────────────────────┐
                    │   Embeddings Store  │
                    └─────────────────────┘

                               ▲

             ┌─────────────────┼─────────────────┐

             ▼                                   ▼

     District MSME Data              Village Data

```

---

# 3. Core Tables

---

# users

Stores registered users.

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    full_name TEXT,
    phone TEXT,
    language TEXT DEFAULT 'English',
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| full_name | TEXT |
| phone | TEXT |
| language | TEXT |
| created_at | TIMESTAMP |

---

# villages

Stores Telangana village metadata.

```sql
CREATE TABLE villages (
    id UUID PRIMARY KEY,
    district TEXT,
    mandal TEXT,
    village_name TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    geojson JSONB
);
```

---

## Source

telangana_village_centroids.csv

telangana_villages.geojson

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| district | TEXT |
| mandal | TEXT |
| village_name | TEXT |
| latitude | FLOAT |
| longitude | FLOAT |
| geojson | JSONB |

---

# district_msme

Stores district-level MSME analytics.

```sql
CREATE TABLE district_msme (
    id UUID PRIMARY KEY,
    district_name TEXT,
    total_msmes INTEGER,
    competition_score NUMERIC,
    updated_at TIMESTAMP
);
```

---

## Source

district_msme_final.csv

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| district_name | TEXT |
| total_msmes | INTEGER |
| competition_score | NUMERIC |
| updated_at | TIMESTAMP |

---

# business_reports

Stores generated business feasibility reports.

```sql
CREATE TABLE business_reports (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),

    district TEXT,
    village TEXT,

    business_category TEXT,

    opportunity_score NUMERIC,

    competition_score NUMERIC,

    risk_score NUMERIC,

    swot JSONB,

    recommendations JSONB,

    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| user_id | UUID |
| district | TEXT |
| village | TEXT |
| business_category | TEXT |
| opportunity_score | NUMERIC |
| competition_score | NUMERIC |
| risk_score | NUMERIC |
| swot | JSONB |
| recommendations | JSONB |
| created_at | TIMESTAMP |

---

# financial_reports

Stores financial calculations.

```sql
CREATE TABLE financial_reports (
    id UUID PRIMARY KEY,

    user_id UUID REFERENCES users(id),

    margin_capital NUMERIC,

    project_cost NUMERIC,

    loan_amount NUMERIC,

    scheme TEXT,

    interest_rate NUMERIC,

    tenure_years INTEGER,

    moratorium_months INTEGER,

    monthly_emi NUMERIC,

    quarterly_emi NUMERIC,

    total_interest NUMERIC,

    total_repayment NUMERIC,

    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| user_id | UUID |
| margin_capital | NUMERIC |
| project_cost | NUMERIC |
| loan_amount | NUMERIC |
| scheme | TEXT |
| interest_rate | NUMERIC |
| tenure_years | INTEGER |
| moratorium_months | INTEGER |
| monthly_emi | NUMERIC |
| quarterly_emi | NUMERIC |
| total_interest | NUMERIC |
| total_repayment | NUMERIC |
| created_at | TIMESTAMP |

---

# ai_chat_history

Stores conversations with the AI advisor.

```sql
CREATE TABLE ai_chat_history (
    id UUID PRIMARY KEY,

    user_id UUID REFERENCES users(id),

    query TEXT,

    response TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Fields

| Field | Type |
|---------|---------|
| id | UUID |
| user_id | UUID |
| query | TEXT |
| response | TEXT |
| created_at | TIMESTAMP |

---

# generated_reports

Stores downloadable reports.

```sql
CREATE TABLE generated_reports (
    id UUID PRIMARY KEY,

    user_id UUID REFERENCES users(id),

    report_type TEXT,

    report_url TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Report Types

- Business Advisory
- Financial Structuring
- Combined Report

---

# embeddings

Stores vector embeddings for RAG.

```sql
CREATE TABLE embeddings (
    id UUID PRIMARY KEY,

    content TEXT,

    embedding VECTOR(1536),

    source TEXT,

    metadata JSONB
);
```

---

## Sources

- district_msme_final.csv
- cleaned_msme_final.xls
- telangana_village_centroids.csv
- telangana_villages.geojson

---

# 4. Relationships

```text
users
│
├── business_reports
│
├── financial_reports
│
├── ai_chat_history
│
└── generated_reports

business_reports
│
├── villages
│
└── district_msme

embeddings
│
├── district_msme
├── villages
└── cleaned_msme
```

---

# 5. Indexing Strategy

## villages

```sql
CREATE INDEX idx_village_name
ON villages(village_name);
```

---

## district_msme

```sql
CREATE INDEX idx_district_name
ON district_msme(district_name);
```

---

## business_reports

```sql
CREATE INDEX idx_business_category
ON business_reports(business_category);
```

---

## embeddings

```sql
CREATE INDEX embeddings_vector_idx
ON embeddings
USING ivfflat (embedding vector_cosine_ops);
```

---

# 6. Storage Architecture

## PostgreSQL Tables

Stores:

- Users
- Reports
- MSME Analytics
- Village Data

---

## Supabase Storage Bucket

Stores:

- Generated PDFs
- Exported Reports
- Future Attachments

Bucket Name:

```text
reports
```

---

# 7. Data Flow

```text
User Input
      ↓

Business Analysis Request
      ↓

FastAPI Backend
      ↓

Village Lookup
+
MSME Lookup
+
Financial Engine
      ↓

OpenAI Advisory Engine
      ↓

Business Report
      ↓

Store in PostgreSQL
      ↓

Generate PDF
      ↓

Store in Supabase Storage
```

---

# 8. Scalability Strategy

### Current

Supabase PostgreSQL

### Future

- Read Replicas
- PostGIS Spatial Queries
- Redis Cache
- Analytics Warehouse

---

# 9. Security

## Authentication

Supabase Auth

---

## Authorization

Row Level Security (RLS)

---

## Data Protection

- HTTPS
- JWT Tokens
- Encrypted Connections

---

# Final Database Components

✅ users

✅ villages

✅ district_msme

✅ business_reports

✅ financial_reports

✅ ai_chat_history

✅ generated_reports

✅ embeddings

✅ Supabase Storage