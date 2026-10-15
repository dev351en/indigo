# Section 01: Header & Navigation

## Overview
The header of `uchicago.edu` consists of a 2-tier dual-wing desktop layout that gracefully transforms into an accessible off-canvas slide drawer on mobile and tablet screens (<900px).

## Structure & Hierarchy

```text
Header Container (#header)
 ├── Skip Link (#maincontent)
 ├── Logo Container (.logoContainer)
 │    ├── Desktop Shield & Wordmark (assets/logo-background.svg)
 │    └── Mobile Shield & Wordmark (assets/logo-background-mobile.svg)
 ├── Brand Bar (.brandBar) [Top Tier]
 │    ├── Left Utilities: News, Events, Careers
 │    ├── "Info For" Dropdown: Students, Faculty, Staff, Alumni, Parents, Media
 │    ├── Right Utilities: Visit, Contact Us, Directory
 │    └── Search Toggle Button (.searchToggleBtn)
 ├── Search Flyout Overlay (.searchFlyout)
 │    ├── Search Input ("Search UChicago")
 │    ├── People Directory Search Link ("Search for People")
 │    └── Close Button (.closeSearchBtn)
 └── Main Navigation (.mainNav) [Bottom Tier]
      ├── Left Wing:
      │    ├── Who We Are (Dropdown: Community Impact, Global Impact, History, Facts, Leadership, Admin)
      │    ├── Academics (Dropdown: Schools & Divisions, Departments, Undergrad, Grad, N-12, Calendar)
      │    ├── Research (Dropdown: Breakthroughs, Centers, Labs, Global Centers, Provost, Research Office)
      │    └── Admissions (Dropdown: Undergrad, Grad, International, Affordability, Continuing Ed, Summer, Aid)
      └── Right Wing:
           ├── Life at UChicago (Dropdown: Hyde Park, Student Life, Resources, Arts, Diversity, Health, Safety)
           ├── UChicago Medicine (Direct Highlight Link)
           └── Give (Signature Maroon Pill CTA)
```

## Styling & Tokens
- **Background**: `#ffffff` with subtle bottom border `#d9d9d9`.
- **Top Brand Bar Background**: `#000000` / deep charcoal with light typography.
- **Active / Give Accent**: `#800000` (Chicago Maroon) with white uppercase text.
- **Dropdown Hover Card**: White surface with `box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15)` and red hover indicator bar.
