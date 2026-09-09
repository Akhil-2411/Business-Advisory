# Product Requirements Document (PRD)

# GramVikas AI
### AI-Driven Hyper-Local Business Advisory & Financial Structuring Assistant for Rural Micro-Entrepreneurs

---

# 1. Product Overview

## Product Name

GramVikas AI

## Problem Statement ID

26091

## Organization

Ministry of Social Justice and Empowerment (MoSJE)

## Theme

Agriculture, FoodTech & Rural Development

---

# Vision

To empower rural and semi-urban entrepreneurs with AI-driven business intelligence, geographic insights, and financial planning tools that help them identify viable business opportunities, understand local market conditions, calculate loan eligibility, and make informed decisions before applying for government-backed concessional loans.

The platform acts as a digital business consultant, market analyst, and financial advisor specifically designed for grassroots entrepreneurs.

---

# 2. Problem Statement

Many first-time rural entrepreneurs face business failure despite receiving financial assistance because they:

- Lack access to formal market research
- Choose businesses based on assumptions rather than data
- Do not understand loan eligibility requirements
- Struggle with financial planning and repayment calculations
- Have limited access to professional business consulting
- Cannot evaluate local competition and opportunities
- Lack visibility into nearby markets and customer reach

As a result, many funded enterprises stagnate or fail to scale.

---

# 3. Product Goals

## Business Goals

- Improve success rates of newly funded micro-enterprises
- Promote data-driven entrepreneurship
- Increase informed participation in government schemes
- Reduce financial planning mistakes among beneficiaries
- Improve loan repayment success rates

---

## User Goals

- Discover suitable business opportunities
- Understand local business ecosystems
- Assess competition levels
- Evaluate business feasibility
- Calculate loan eligibility instantly
- Understand repayment obligations
- Generate professional business reports
- Visualize business opportunities on maps

---

# 4. Target Users

## Primary Users

### Rural Entrepreneurs

- First-time business owners
- Self-employed individuals
- Small traders
- Farmers diversifying into businesses

### Youth Entrepreneurs

- Dairy entrepreneurs
- Retail shop owners
- Textile business owners
- Service providers
- Food processing entrepreneurs

---

## Secondary Users

### Government Agencies

- State Channelizing Agencies (SCAs)
- District Officers
- Development Officers

### Financial Institutions

- Loan processing authorities
- Scheme evaluators

### NGOs & Mentors

- Entrepreneurship support organizations
- Rural business consultants

---

# 5. User Journey

```text
User Visits Platform
        ↓
Select Preferred Language
        ↓
Select District
        ↓
Select Village
        ↓
Enter Available Margin Capital
        ↓
Select Business Category
        ↓
Generate Analysis
        ↓
Hyper-Local Business Report
+
Financial Structuring Report
        ↓
Interactive Map Visualization
        ↓
Download PDF Report
```

---

# 6. Core Modules

---

# Module 1: Hyper-Local Business Intelligence Engine

Generates a localized business feasibility report using geographic intelligence, MSME analytics, AI insights, and financial data.

---

## Feature 1: User Input Module

### Geographic Inputs

- District
- Block / Mandal
- Village

### Financial Inputs

Available Margin Capital

Example:

₹1,00,000

### Business Category

Examples:

- Dairy
- Poultry
- Retail Store
- Textile Shop
- Tailoring
- Mobile Repair
- Food Processing
- Agriculture Services
- Handicrafts

---

## Feature 2: Geo-Spatial Market Reach Analysis

Uses:

- Telangana Village GeoJSON
- OpenStreetMap
- Leaflet.js

Capabilities:

- Display village boundaries
- Show neighboring villages
- Generate 5 km radius analysis
- Generate 10 km radius analysis
- Estimate reachable consumer base
- Suggest local distribution routes

### Outputs

- Reachable Villages
- Service Coverage Radius
- Estimated Customer Reach
- Distribution Recommendations

---

## Feature 3: Local Business Ecosystem Analysis

Analyzes district-level MSME and enterprise activity.

### Outputs

- Dominant industries
- Existing business concentration
- Sector-wise enterprise distribution
- Emerging sectors
- Potential business clusters
- Local economy overview

---

## Feature 4: Opportunity Discovery Engine

Identifies:

- Underserved business categories
- Low-competition sectors
- Emerging business opportunities
- High-growth sectors
- Recommended sectors for investment

### Outputs

- Opportunity Score (0-100)
- Recommended Business Categories
- Growth Potential Indicators

---

## Feature 5: AI SWOT Analysis

Generates customized SWOT analysis based on:

- Location
- Business category
- Available capital
- Local market conditions

### Outputs

#### Strengths

#### Weaknesses

#### Opportunities

#### Threats

---

## Feature 6: Competitor Mapping Engine

Uses district MSME competition data.

### Outputs

- Estimated competitor density
- Competition score
- Market saturation score
- Sector concentration analysis
- District ranking

---

## Feature 7: Threat Analysis Engine

Identifies:

- Supply chain bottlenecks
- Seasonal demand fluctuations
- Transportation limitations
- Dependency on single buyers
- Local competition risks
- Pricing pressure

### Outputs

- Threat Score
- Risk Category
  - Low
  - Medium
  - High

---

## Feature 8: Product Market Value Engine

Uses:

- Competition score
- Business category
- Local economic indicators

### Outputs

- Suggested selling price
- Local market value
- Revenue projections
- Expected profit margins

---

## Feature 9: Risk Assessment Engine

Calculates overall business risk.

Factors:

- Competition
- Capital adequacy
- Market demand
- Threat score

### Outputs

Risk Score

Categories:

- Low
- Medium
- High

---

# Module 2: Smart Financial Structuring Engine

Automatically calculates financial feasibility and loan eligibility.

---

## Feature 10: Financial Calculator

### User Input

Available Margin Capital

Example:

₹1,00,000

### Project Cost Formula

```text
Project Cost = Available Margin Capital ÷ 10%
```

Example:

```text
₹1,00,000 ÷ 10%
= ₹10,00,000
```

### Maximum Loan Formula

```text
Maximum Loan Amount = Project Cost × 90%
```

Example:

```text
₹10,00,000 × 90%
= ₹9,00,000
```

### Outputs

- Total Project Cost
- Maximum Loan Amount
- User Contribution
- Eligibility Status

---

## Feature 11: Government Scheme Router

Automatically selects the correct scheme.

### Micro Finance Scheme

#### Eligibility

Project Cost ≤ ₹1.40 Lakh

#### Benefits

- Loan Coverage: 90%
- Maximum Loan: ₹1.25 Lakh
- Interest Rate: 6.5%
- Tenure: 3 Years
- Moratorium: 3 Months

---

### Term Loan Scheme

#### Eligibility

₹1.40 Lakh < Project Cost ≤ ₹50 Lakh

#### Benefits

- Loan Coverage: 90%
- Maximum Loan: ₹45 Lakh
- Interest Rate: 8%
- Tenure: 7 Years
- Moratorium: 6 Months

---

### Not Eligible

```text
Project Cost > ₹50 Lakh
```

---

## Feature 12: EMI & Repayment Planner

Generates:

- Monthly EMI
- Quarterly EMI
- Total Interest Payable
- Total Repayment Amount
- Moratorium Information
- First EMI Date

---

## Feature 13: Working Capital Planner

Provides guidance regarding:

- Initial operational expenses
- Working capital requirements
- Cash reserve recommendations
- Sustainability planning

---

# Feature 14: Interactive Village Intelligence Map

Built Using:

- Leaflet.js
- OpenStreetMap

Capabilities:

- Village Boundary Visualization
- Nearby Village Discovery
- Radius Overlay (5 km / 10 km)
- Competitor Density Heatmap
- Opportunity Zones
- Consumer Reach Visualization

---

# Feature 15: AI Advisory Chat Assistant

Supports:

- English
- Hindi
- Telugu
- Tamil
- Kannada
- Marathi

Capabilities:

- Business consultation
- Opportunity discovery
- Competition analysis
- Financial guidance
- Loan explanation
- Risk assessment
- Pricing recommendations

---

# Feature 16: Report Generation

Generate downloadable reports.

### Business Advisory Report

Includes:

- Market Reach Analysis
- Opportunity Analysis
- SWOT Analysis
- Competition Analysis
- Threat Assessment
- Pricing Recommendations

### Financial Structuring Report

Includes:

- Project Cost
- Loan Eligibility
- Scheme Selection
- EMI Schedule
- Repayment Details

### Export Formats

- PDF
- Print Ready Format

---

# 7. Datasets

## Dataset 1: Telangana Village GeoJSON

Used For:

- Village Boundary Mapping
- Radius Analysis
- Market Reach Estimation
- Service Area Visualization

---

## Dataset 2: District MSME Competition Dataset

Used For:

- Competitor Mapping
- Competition Analysis
- Market Saturation Analysis
- Opportunity Discovery

---

## Dataset 3: Financial Structuring Dataset

Used For:

- Loan Eligibility
- Scheme Routing
- EMI Planning
- Working Capital Recommendations

---

# 8. AI Architecture

```text
User Input
      ↓
React Frontend
      ↓
FastAPI Backend
      ↓
Business Intelligence Layer
      ↓
RAG Retrieval Layer
      ↓
OpenAI
      ↓
Village GeoJSON
District MSME Dataset
Financial Rules Dataset
      ↓
AI Advisory Engine
      ↓
Business Feasibility Report
      ↓
Financial Structuring Report
```

---

# 9. Functional Requirements

### FR-1

User can select district and village.

### FR-2

User can enter available margin capital.

### FR-3

User can select business category.

### FR-4

System calculates project cost.

### FR-5

System calculates loan eligibility.

### FR-6

System routes eligible government scheme.

### FR-7

System generates opportunity analysis.

### FR-8

System generates SWOT analysis.

### FR-9

System generates competitor mapping.

### FR-10

System generates threat analysis.

### FR-11

System generates pricing recommendations.

### FR-12

System generates EMI schedules.

### FR-13

System displays interactive maps.

### FR-14

System provides AI recommendations.

### FR-15

System generates downloadable reports.

---

# 10. Non-Functional Requirements

## Performance

- API response time below 5 seconds
- Report generation below 10 seconds

## Scalability

- Support 10,000+ users
- Cloud-native architecture

## Security

- JWT Authentication
- HTTPS Encryption
- Secure API Access
- Role-Based Access Control

## Availability

- 99% uptime target

---

# 11. Technology Stack

## Frontend

### React

Frontend application framework

### JavaScript

Application logic

### TailwindCSS

Responsive UI styling

### shadcn/ui

Reusable UI components

### 21st.dev

Modern AI-generated UI components

### Leaflet.js

Interactive mapping

### OpenStreetMap

Map tiles and geographic visualization

---

## Backend

### FastAPI

REST API development

### Pydantic

Validation and serialization

### Uvicorn

ASGI application server

---

## Database

### Supabase PostgreSQL

Stores:

- Users
- Business Reports
- MSME Analytics
- Scheme Results
- Advisory History

### Supabase Vector Store

Stores:

- Embeddings
- Business Knowledge Base
- Government Scheme Rules
- AI Retrieval Context

---

## AI Layer

### OpenAI

Business intelligence generation

### RAG Pipeline

Context-aware business recommendations

### Embeddings

Semantic retrieval and search

---

## Deployment

### Vercel

Frontend Hosting

### Render / Railway

FastAPI Backend Deployment

### Supabase Cloud

Database & Vector Storage

---

# 12. System Architecture

```text
                    ┌───────────────────────┐
                    │      React App        │
                    │ Tailwind + shadcn/ui  │
                    └───────────┬───────────┘
                                │
                                ▼

                    ┌───────────────────────┐
                    │       FastAPI         │
                    │      Backend API      │
                    └───────────┬───────────┘
                                │
      ┌─────────────────────────┼─────────────────────────┐
      ▼                         ▼                         ▼

┌──────────────┐      ┌────────────────┐      ┌────────────────┐
│ Financial    │      │ Business       │      │ AI Advisory    │
│ Engine       │      │ Intelligence   │      │ Engine         │
└──────────────┘      └────────────────┘      └────────────────┘
                                │
                                ▼

                    ┌────────────────────────┐
                    │ Supabase PostgreSQL    │
                    │ + Vector Embeddings    │
                    └────────────────────────┘
```

---

# 13. Success Metrics

## Business Metrics

- Report generation count
- Scheme routing accuracy
- User engagement rate

## User Metrics

- Monthly Active Users
- Report Downloads
- AI Assistant Usage

## Impact Metrics

- Improved loan readiness
- Better business selection decisions
- Increased entrepreneurship participation
- Reduced business failure rates

---

# MVP Deliverables

✅ Hyper-Local Business Intelligence Engine

✅ Geo-Spatial Market Reach Analysis

✅ Opportunity Discovery Engine

✅ SWOT Analysis Generator

✅ Competitor Mapping

✅ Threat Analysis Engine

✅ Product Market Value Engine

✅ Smart Financial Calculator

✅ Scheme Router

✅ EMI Planner

✅ Working Capital Planner

✅ Interactive GIS Map

✅ AI Advisory Chat Assistant

✅ PDF Report Generator

✅ OpenAI RAG Integration

✅ FastAPI Backend

✅ Supabase Database

✅ React Frontend

✅ Multilingual Support

---

# Final Deliverable

A multilingual AI-powered platform that combines:

- Hyper-Local Business Intelligence
- GIS Mapping
- Market Reach Analysis
- Opportunity Discovery
- Competitor Mapping
- Threat Assessment
- Product Pricing Guidance
- Financial Structuring
- Government Scheme Routing
- EMI Planning

to help rural entrepreneurs make informed, data-driven, and financially sustainable business decisions before applying for concessional funding schemes.