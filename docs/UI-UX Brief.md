# UI/UX Brief

# GramVikas AI
### AI-Driven Hyper-Local Business Advisory & Financial Structuring Assistant

---

# 1. Design Vision

GramVikas AI should feel like a modern government-backed digital advisory platform that is:

- Professional
- Trustworthy
- Accessible
- Data-driven
- Mobile-first
- Multilingual

The interface should simplify complex business and financial information for first-time entrepreneurs while maintaining a clean and modern appearance.

---

# 2. Design Principles

## Simplicity First

Most users may not have prior experience with:

- Business consulting
- Financial planning
- Loan calculations
- Market research

The UI should prioritize clarity over complexity.

---

## Guided Experience

Users should never face large forms.

Instead:

- Step-by-step inputs
- Guided workflows
- Smart defaults
- Progressive disclosure

---

## Visual Decision Support

Information should be represented through:

- Score cards
- Maps
- Charts
- Progress indicators
- Color-coded insights

instead of large blocks of text.

---

## Mobile-First Design

Target users may primarily access the platform through smartphones.

All screens must be:

- Responsive
- Touch-friendly
- Lightweight

---

# 3. Design System

## Framework

- React
- TailwindCSS
- shadcn/ui
- 21st.dev Components

---

## Typography

Primary Font:

```text
Inter
```

Fallback:

```text
System UI
```

---

## Spacing

Use 8px spacing system.

```text
8px
16px
24px
32px
48px
64px
```

---

## Border Radius

```text
12px
16px
20px
```

Used across:

- Cards
- Inputs
- Dialogs
- Buttons

---

# 4. Color Palette

## Primary

```text
Emerald Green
```

Represents:

- Growth
- Development
- Agriculture
- Entrepreneurship

---

## Secondary

```text
Blue
```

Represents:

- Trust
- Finance
- Government Services

---

## Accent

```text
Amber
```

Represents:

- Opportunities
- Insights
- Recommendations

---

## Status Colors

Success:

```text
Green
```

Warning:

```text
Yellow
```

Error:

```text
Red
```

Info:

```text
Blue
```

---

# 5. Application Layout

```text
┌─────────────────────────────┐
│ Header                      │
├─────────────────────────────┤
│ Sidebar Navigation          │
├─────────────────────────────┤
│ Main Content Area           │
├─────────────────────────────┤
│ Footer                      │
└─────────────────────────────┘
```

---

# 6. Main Pages

---

## Landing Page

Purpose:

Introduce platform capabilities.

Sections:

### Hero Section

Contains:

- Product Introduction
- Call To Action
- Start Analysis Button

---

### Feature Cards

Display:

- Business Advisory
- Financial Calculator
- Competitor Mapping
- AI Assistant

---

### Process Flow

```text
Enter Location
       ↓
Select Business
       ↓
Enter Capital
       ↓
Generate Report
```

---

## Business Analysis Page

Purpose:

Generate hyper-local business feasibility reports.

---

### Input Section

Fields:

- District
- Village
- Business Category
- Available Margin Capital

---

### Analysis Dashboard

Displays:

- Opportunity Score
- Competition Score
- Risk Score
- Recommendation Score

---

## Financial Calculator Page

Purpose:

Show financial eligibility.

---

### Input Card

Field:

```text
Available Margin Capital
```

---

### Output Cards

Show:

- Project Cost
- Eligible Loan Amount
- Scheme Name
- Interest Rate
- Moratorium
- EMI

---

## GIS Map Page

Purpose:

Visualize geographic insights.

---

### Map Features

Uses:

- Leaflet.js
- OpenStreetMap

Displays:

- Village Boundary
- 5 km Radius
- 10 km Radius
- Nearby Villages
- Competitor Clusters

---

## AI Advisory Chat Page

Purpose:

Conversational business assistant.

Features:

- Multilingual Chat
- Context-Aware Responses
- Follow-up Questions

---

## Report Page

Purpose:

Display final advisory report.

Sections:

- Executive Summary
- Market Reach
- Opportunity Analysis
- SWOT Analysis
- Financial Plan
- Risk Assessment
- Recommendations

---

# 7. Core Components

---

## Navigation Sidebar

Contains:

- Dashboard
- Business Analysis
- Financial Calculator
- GIS Map
- AI Advisor
- Reports

---

## KPI Cards

Display:

- Opportunity Score
- Competition Score
- Risk Score
- Market Potential

---

## SWOT Cards

Separate cards for:

- Strengths
- Weaknesses
- Opportunities
- Threats

---

## Financial Cards

Display:

- Loan Amount
- EMI
- Interest
- Repayment Schedule

---

## Competitor Cards

Display:

- Competition Density
- Market Saturation
- Opportunity Gap

---

## Report Download Card

Actions:

- Download PDF
- Print Report

---

# 8. Charts & Visualizations

Use:

- Recharts

---

## Competition Analysis

Chart Type:

```text
Bar Chart
```

---

## Market Opportunity

Chart Type:

```text
Radar Chart
```

---

## Financial Breakdown

Chart Type:

```text
Pie Chart
```

---

## Repayment Schedule

Chart Type:

```text
Line Chart
```

---

# 9. Animation Guidelines

Animations should enhance usability and never distract users.

---

## Approved 21st.dev Animations

### Fade-In Sections

Used when loading pages.

---

### Animated KPI Counters

Used for:

- Opportunity Score
- Loan Amount
- Market Reach

---

### Hover Cards

Used on:

- Feature Cards
- Dashboard Cards

---

### Accordion Animations

Used for:

- SWOT Sections
- Report Sections

---

### Smooth Page Transitions

Used between pages.

---

### Skeleton Loaders

Displayed during:

- AI Processing
- Report Generation

---

### Progress Indicators

Shown during:

```text
Data Collection
↓
Analysis
↓
AI Advisory
↓
Report Generation
```

---

## Avoid

❌ Particle Effects

❌ 3D Animations

❌ WebGL Effects

❌ Heavy Motion Graphics

❌ Auto-Playing Visual Effects

❌ Complex Landing Page Animations

---

# 10. Accessibility

Requirements:

- WCAG Compliant
- Keyboard Navigation
- Screen Reader Support
- High Contrast Support
- Responsive Design

---

# 11. Multilingual Support

Supported Languages:

- English
- Hindi
- Telugu

Future:

- Marathi
- Kannada
- Tamil

---

# 12. Responsive Breakpoints

Mobile:

```text
< 768px
```

Tablet:

```text
768px - 1024px
```

Desktop:

```text
> 1024px
```

---

# 13. User Flow

```text
Landing Page
      ↓

Business Analysis Form
      ↓

Financial Calculation
      ↓

GIS Market Analysis
      ↓

AI Advisory Generation
      ↓

Report Dashboard
      ↓

PDF Export
```

---

# 14. MVP UI Deliverables

✅ Landing Page

✅ Dashboard

✅ Business Analysis Form

✅ Financial Calculator

✅ GIS Map Module

✅ AI Chat Assistant

✅ SWOT Dashboard

✅ Competitor Analysis Dashboard

✅ Report Viewer

✅ PDF Download

✅ Responsive Design

✅ Multilingual UI

✅ 21st.dev Micro-Animations

✅ shadcn/ui Design System

---

# 15. Future Enhancements

- Dark Mode
- Voice Assistant
- WhatsApp Integration
- Mobile App
- Offline Mode
- Advanced GIS Heatmaps
- District Analytics Dashboard