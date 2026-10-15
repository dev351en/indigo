# Component Architecture & Catalog

> Complete structural, interactive, and styling specifications for all UI components on the University of Chicago website ([uchicago.edu](https://www.uchicago.edu/)).

---

## Component Inventory Overview

| # | Component Name | Original React/CSS Chunk Name | Primary Function | Location |
|---|---|---|---|---|
| 1 | **EduHeader** | `EduHeader.chunk.css` | Institutional branding, Skip link, Logo, Mobile trigger | Top of page |
| 2 | **EduBrandBar** | `EduHeader.chunk.css` | Utility links, "Info For" dropdown, Search flyout | Header top tier |
| 3 | **EduNavigation** | `EduHeader.chunk.css` | 2-tier primary mega-menu navigation | Header bottom tier |
| 4 | **VideoSpotlight** | `VideoSpotlight.chunk.css` | Full-width looping video banner with accessible controls | Hero |
| 5 | **CTABarSpotlight** | `CTABarSpotlight.chunk.css` | 3 primary action buttons (Apply, Contact, Visit) | Directly below Hero |
| 6 | **SectionWrap** | `SectionWrap.chunk.css` | Section background wrapper with Phoenix crest watermark | News wrapper |
| 7 | **HeadlineTextBold** | `HeadlineTextBold.chunk.css` | Bold uppercase section headers ("LATEST NEWS") | Section header |
| 8 | **NewsFeatured** & **NewsItem** | `NewsFeatured.chunk.css` | 4-column responsive grid of curated stories + CTA | News section |
| 9 | **CalloutBannerList** | `CalloutBannerList.chunk.css` | Campaign highlight ("Chicago Minds") with image & copy | Mid-page |
| 10 | **HeadlineBar** | `HeadlineBar.chunk.css` | High-impact mission statements with editorial typography | Informational |
| 11 | **CalloutTiles** | `CalloutTiles.chunk.css` | Multicolumn feature cards with description & chevron CTA | Pillars grid |
| 12 | **PhotoTabs** | `PhotoTabs.chunk.css` | Tabbed image & caption component | Interstitial |
| 13 | **ImageTileGrid** | `ImageTileGrid.chunk.css` | Grid layout for photography and stories | Interstitial |
| 14 | **Footer** | `Footer.chunk.css` | Campus contact, legal compliance, utility links, social icons | Bottom of page |

---

## Detailed Component Specifications

### 1. `EduHeader` & `EduBrandBar`

#### Markup Blueprint
```html
<header class="EduHeader_container" id="header" data-mobilenavisopen="false" data-scrolldown="false">
  <a href="#maincontent" class="skipLink">Skip to main content</a>
  
  <div class="header-inner">
    <!-- Brand Logo -->
    <a class="logoContainer" href="/" aria-label="The University of Chicago Homepage">
      <img src="assets/logo-background.svg" class="desktopLogo" alt="The University of Chicago Logo" />
      <img src="assets/logo-background-mobile.svg" class="mobileLogo" alt="The University of Chicago Logo" />
    </a>

    <!-- Brand Bar (Top Utility Tier) -->
    <div class="brandBar">
      <ul class="utilityNav left">
        <li><a href="https://news.uchicago.edu">News</a></li>
        <li><a href="https://events.uchicago.edu/">Events</a></li>
        <li><a href="/careers">Careers</a></li>
        <li class="infoDropdownContainer">
          <button class="infoDropdownBtn" aria-expanded="false" aria-controls="infoMenu">
            Info For <i class="fa fa-chevron-down"></i>
          </button>
          <ul id="infoMenu" class="infoDropdownMenu" hidden>
            <li><a href="/students">Students</a></li>
            <li><a href="https://intranet.uchicago.edu/info-for-faculty">Faculty</a></li>
            <li><a href="https://intranet.uchicago.edu/info-for-staff">Staff</a></li>
            <li><a href="https://alumniandfriends.uchicago.edu/">Alumni</a></li>
            <li><a href="https://college.uchicago.edu/about/parents">Parents</a></li>
            <li><a href="https://news.uchicago.edu/media-resources">Media</a></li>
          </ul>
        </li>
      </ul>

      <ul class="utilityNav right">
        <li><a href="/visit">Visit</a></li>
        <li><a href="/contact-us">Contact Us</a></li>
        <li><a href="https://directory.uchicago.edu">Directory</a></li>
        <li>
          <button class="searchToggleBtn" aria-label="Open search flyout" aria-expanded="false">
            <i class="fa fa-search"></i>
          </button>
        </li>
      </ul>
    </div>

    <!-- Search Flyout Overlay -->
    <div class="searchFlyout" hidden>
      <form class="searchForm" role="search" action="/search" method="GET">
        <label for="siteSearchInput">Search UChicago</label>
        <div class="searchInputWrap">
          <input type="search" id="siteSearchInput" name="q" placeholder="What are you looking for?" autocomplete="off" />
          <button type="submit" aria-label="Submit search"><i class="fa fa-search"></i></button>
        </div>
        <a href="https://directory.uchicago.edu" class="peopleSearchLink">
          Search for People <i class="fa fa-arrow-right"></i>
        </a>
      </form>
      <button class="closeSearchBtn" aria-label="Close search flyout"><i class="fa fa-times"></i></button>
    </div>
  </div>
</header>
```

#### Behavior & State Management
- **Scroll Detection**: The header sets `data-scrolldown="true"` when the user scrolls past `120px`, condensing padding and subtly increasing shadow.
- **Search Flyout**: Clicking `.searchToggleBtn` removes the `hidden` attribute from `.searchFlyout`, traps focus inside the input, and supports `Esc` key to close.
- **Info For Dropdown**: Clicking or focusing on `.infoDropdownBtn` toggles `aria-expanded="true|false"` and shows the floating menu with smooth fade-in.

---

### 2. `EduNavigation` (Mega-Menu)

#### Navigation Structure
The primary navigation splits into two symmetrical clusters around the shield/logo:

1. **Left Wing**:
   - **Who We Are**: 3 columns (Community Impact, Global Impact | History & Traditions, Facts & Figures | Leadership, Administration)
   - **Academics**: 2 columns (Schools & Divisions, Departments, Undergraduate | Graduate, N-12 Education, Academic Calendar)
   - **Research**: 2 columns (Breakthroughs, Institutes & Centers, Affiliated Labs, Global Centers | Other Academic Units, Provost, Office of Research)
   - **Admissions**: 2 columns (Undergrad, Grad, International, Affordability | Continuing Ed, Summer Programs, Financial Aid)
2. **Right Wing**:
   - **Life at UChicago**: 2 columns (Hyde Park, Student Life, Campus Resources, Arts | Diversity, Health & Wellness, Safety)
   - **UChicago Medicine**: Direct link styled with highlight
   - **Give**: Red pill CTA button (`#800000`) linking to giving portal

---

### 3. `VideoSpotlight` (Hero)

#### Markup Blueprint
```html
<section class="videoSpotlight" style="height: 600px;">
  <video class="bgVideo" autoplay muted loop playsinline aria-describedby="videoDesc">
    <source src="assets/2023-fall-video-update-1116.mp4" type="video/mp4" />
  </video>
  <div class="videoOverlay">
    <div class="videoText">
      <p class="tagline">Field-Defining Scholarship</p>
      <p class="tagline">Transformative Education</p>
      <p class="tagline">World-Changing Ideas</p>
      <h1 class="universityName">The University of Chicago</h1>
    </div>
  </div>
  <button class="videoPlayPauseBtn" aria-label="Pause spotlight video" aria-pressed="false">
    <i class="fa fa-pause"></i>
  </button>
  <div id="videoDesc" class="sr-only">
    Video showing various dynamic scenes across the University of Chicago campus including aerial gothic architecture, laboratories, libraries, and scholarly collaboration.
  </div>
</section>
```

---

### 4. `CTABarSpotlight`

Positioned immediately below the hero video, offering high-priority gateway links to primary user journeys:
1. **How to apply** -> `/admissions`
2. **Contact Us** -> `/contact-us`
3. **Visit Our Campus** -> `/visit`

- Background: `#670a0a` / Deep Chicago Maroon gradient bar or dark charcoal borderless container.
- Button Style: Bold white background with dark typography, turning Maroon with white text on hover.

---

### 5. `NewsFeatured` & `NewsItem`

Displays four high-impact recent stories from across the university research ecosystem:

```html
<section class="newsFeaturedSection" style="background-image: url('assets/phoenix.png');">
  <div class="container">
    <div class="sectionHeader">
      <h2 class="sectionTitle">LATEST NEWS</h2>
    </div>
    <div class="newsGrid">
      <!-- Article 1 -->
      <article class="newsCard">
        <div class="newsCardContent">
          <small class="newsCategory">ECONOMICS & HONORS</small>
          <h3 class="newsTitle">
            <a href="https://news.uchicago.edu/story/michael-woodford-uchicago-alum-and-former-faculty-member-shares-nobel-prize">
              Michael Woodford, UChicago alum and former faculty member, shares Nobel Prize
            </a>
          </h3>
          <span class="newsSource">Source: UChicago News</span>
        </div>
      </article>

      <!-- Article 2 -->
      <article class="newsCard">
        <div class="newsCardContent">
          <small class="newsCategory">PHYSICS & DISCOVERY</small>
          <h3 class="newsTitle">
            <a href="https://news.uchicago.edu/big-brains-podcast-neutrino-hunters-searching-ghostly-particles-antarctic-ice-abby-vieregg">
              Neutrino hunters: Searching for ghostly particles in Antarctic ice, with Abby Vieregg
            </a>
          </h3>
          <span class="newsSource">Source: Big Brains Podcast</span>
        </div>
      </article>

      <!-- Article 3 -->
      <article class="newsCard">
        <div class="newsCardContent">
          <small class="newsCategory">COMMUNITY & STEM</small>
          <h3 class="newsTitle">
            <a href="https://news.uchicago.edu/story/learning-blast-literally-south-side-science-festival">
              Learning is a blast—literally—at the South Side Science Festival
            </a>
          </h3>
          <span class="newsSource">Source: Science & Outreach</span>
        </div>
      </article>

      <!-- Article 4 -->
      <article class="newsCard">
        <div class="newsCardContent">
          <small class="newsCategory">LAW & SOCIETY</small>
          <h3 class="newsTitle">
            <a href="https://news.uchicago.edu/story/book-bans-are-surging-so-are-efforts-let-books-be">
              Book bans are surging. So are efforts to ‘let books be’
            </a>
          </h3>
          <span class="newsSource">Source: Humanities & Culture</span>
        </div>
      </article>
    </div>

    <div class="newsSeeMoreWrap">
      <a href="https://news.uchicago.edu" class="btn-maroon">See More News</a>
    </div>
  </div>
</section>
```

---

### 6. `CalloutBannerList` (Campaign Feature)

Showcases major institutional milestones and fundraising initiatives (e.g. *Chicago Minds*):
- Left Column: Featured hero image (`assets/chicago-minds-gray-bg.jpg`).
- Right Column: Dark accented card with red border, containing:
  - Heading: `Explore the "Chicago Minds" campaign`
  - Body: `Learn about the ambitious initiative to expand UChicago's global impact through research and education.`
  - Pagination / Dot Indicators: Interactive dots indicating slide active state.

---

### 7. `HeadlineBar` & `CalloutTiles`

Represents UChicago's core intellectual pillars:
1. **We value rigorous inquiry** (`/who-we-are`)
2. **We foster independent thinking** (`/academics`)
3. **Field-defining research** (`/research-and-scholarship`)
4. **Transformative education** (`/academics`)
5. **We advance ideas and humanity** (`/research-and-scholarship/breakthroughs`)
6. **A history of groundbreaking discoveries** (`/research-and-scholarship/breakthroughs`)
7. **Community impact** (`/who-we-are/community-impact`)
8. **Global impact** (`/who-we-are/global-impact`)
9. **We call Chicago home** (`/life-at-uchicago/hyde-park`)

---

### 8. `Footer`

Features the university signature footer:
- University Wordmark (`footerlogo.jpg`)
- Address: `Hyde Park Campus | 5801 S. Ellis Ave. Chicago, IL 60637`
- 3 Column Quick Nav (Accreditation, Careers, Make a gift, Title IX, Privacy, Accessibility)
- Social channel icons (Facebook, Instagram, LinkedIn, X/Twitter, YouTube)
- Copyright and non-discrimination disclosure statement
