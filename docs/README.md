# The University of Chicago — Website Replica & Redesign Suite

Welcome to the comprehensive reverse-engineering and replica package for **The University of Chicago** official website ([uchicago.edu](https://www.uchicago.edu/)).

This repository contains everything required to demonstrate to your client that you can scrape, dissect, recreate, and elevate the University of Chicago website with pixel-perfect precision and modern engineering best practices.

---

## 📁 Repository Structure

```text
uchicago_replica/
├── assets/                           # Real downloaded media assets from uchicago.edu
│   ├── 2023-fall-video-update-1116.mp4 # Full HD background hero campus video (10.5 MB)
│   ├── logo-background.svg           # Primary official desktop SVG shield & wordmark
│   ├── logo-background-mobile.svg    # Compact mobile SVG shield & wordmark
│   ├── phoenix.png                   # Official watermark Phoenix crest background
│   ├── chicago-minds-gray-bg.jpg     # "Chicago Minds" campaign feature photography
│   └── footerlogo.jpg                # Institutional footer crest wordmark
├── css/                              # 15 original modular CSS chunks extracted from production
│   ├── EduHeader.0831b491.chunk.css  # Header, brand bar, and mega-menu styles
│   ├── VideoSpotlight.959d1aa1.chunk.css # Fullscreen background video styling
│   ├── CTABarSpotlight.a8390392.chunk.css # Primary action buttons
│   ├── NewsFeatured.030ee8bf.chunk.css   # Latest news card grid styling
│   ├── CalloutBannerList.7b5c1658.chunk.css # Campaign banner & carousel styling
│   ├── CalloutTiles.27d841b2.chunk.css   # Pillars feature cards
│   ├── HeadlineBar.8eeb7507.chunk.css    # Editorial headline & text layouts
│   ├── SectionWrap.7a4d0c6c.chunk.css    # Background motif & wrappers
│   ├── Footer.6e030fa0.chunk.css         # Footer & legal links
│   └── main.316e8eaf.chunk.css          # Global typography, resets, grids
├── docs/                             # Exhaustive Markdown documentation
│   ├── README.md                     # Master project guide & presentation blueprint
│   ├── DESIGN_SYSTEM.md              # Color tokens, typography scale, spacing, a11y
│   ├── COMPONENTS.md                 # UI component catalog, props, markup & state
│   ├── SITE_STRUCTURE_AND_LINKS.md   # Sitemap, mega-menu trees, and 150+ links directory
│   ├── CONTENT_AUDIT.md              # Full verbatim copy, headings, and SEO metadata
│   └── sections/                     # Granular Markdown breakdowns for every section
│       ├── 01_header_and_navigation.md
│       ├── 02_hero_video_spotlight.md
│       ├── 03_cta_bar.md
│       ├── 04_featured_news.md
│       ├── 05_chicago_minds_campaign.md
│       ├── 06_rigorous_inquiry.md
│       ├── 07_independent_thinking_and_research.md
│       ├── 08_ideas_humanity_and_impact.md
│       ├── 09_chicago_home.md
│       └── 10_institutional_footer.md
├── pages/                            # Full scraped HTML of all primary section landing pages
│   ├── who-we-are.html               # /who-we-are (143 KB)
│   ├── academics.html                 # /academics (132 KB)
│   ├── research-and-scholarship.html # /research-and-scholarship (267 KB)
│   ├── admissions.html                # /admissions (148 KB)
│   ├── life-at-uchicago.html          # /life-at-uchicago (135 KB)
│   ├── visit.html                     # /visit (217 KB)
│   └── contact-us.html                # /contact-us (125 KB)
└── site/                             # Fully functional, standalone Interactive Web Replica
    ├── index.html                    # Semantic, accessible HTML replica
    ├── styles.css                    # Production-grade responsive CSS matching design tokens
    └── app.js                        # Interactive JavaScript (menus, video, search, drawer)
```

---

## 🚀 How to Run & Present to the Client

### Option 1: Instant Browser Preview (Zero Installation)
Simply open the `site/index.html` file directly in any modern browser:
```powershell
Start-Process "d:\Microvirt\OBSIDIAN\uchicago_replica\site\index.html"
```

### Option 2: Local HTTP Server
Run a local static file server using Python or Node.js:
```powershell
# Using Python
cd d:\Microvirt\OBSIDIAN\uchicago_replica\site
py -m http.server 3000

# Or using Node npx
npx serve d:\Microvirt\OBSIDIAN\uchicago_replica\site
```
Then navigate to `http://localhost:3000`.

---

## 🎯 Key Client Presentation Talking Points

When presenting this replica and proposal to your client:

1. **Precision Reverse-Engineering**:
   - You have captured every single design token, color shade (Chicago Maroon `#800000`, Deep Maroon `#670a0a`), font pairing (classic serif with clean geometric sans-serif), and micro-interaction.
2. **Interactive Functionality**:
   - Show the working **Mega-Menu Dropdowns** on hover and focus.
   - Click the **Search Icon** in the top-right to reveal the live **Search Flyout Overlay** with quick link to the People Directory.
   - Demonstrate the **Hero Video Spotlight** with functional **Play/Pause controls** and accessible screen-reader narration.
   - Resize the window to mobile width (<900px) to showcase the responsive **Hamburger Drawer** and nested mobile navigation accordion.
   - Demonstrate the **Latest News** grid with Phoenix watermark background and hover elevation effects.
3. **Modernization & Redesign Opportunities**:
   - The current production site relies on legacy Sitecore and heavy chunked bundles (~1 MB JS).
   - Propose rebuilding with **Next.js 15 / Astro / Vite + Tailwind CSS**, reducing bundle size by 80%, achieving 100/100 Lighthouse performance, sub-second LCP (Largest Contentful Paint), and enhanced WCAG 2.2 AAA accessibility.
