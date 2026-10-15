# Design System: The University of Chicago

> Extracted and reverse-engineered from the live production stylesheets of `https://www.uchicago.edu/`.

---

## 1. Color Palette & Tokens

The University of Chicago visual identity relies on a distinguished heritage palette anchored by Chicago Maroon, supported by crisp neutrals and a rich secondary palette representing diverse schools and academic units.

### 1.1 Primary & Heritage Colors

| Token Name | Hex Code | RGB | Role / Usage |
| :--- | :--- | :--- | :--- |
| `--color-maroon-primary` | `#800000` | `rgb(128, 0, 0)` | Primary University brand color, Give button, key CTAs |
| `--color-maroon-deep` | `#670a0a` | `rgb(103, 10, 10)` | Active button states, deep maroon borders, badge accents |
| `--color-maroon-dark` | `#4a0707` | `rgb(74, 7, 7)` | Hover dark state for maroon elements |
| `--color-black` | `#000000` | `rgb(0, 0, 0)` | Primary headings, brand bar backgrounds, high contrast text |
| `--color-charcoal-body` | `#4d4d4d` | `rgb(77, 77, 77)` | Primary body copy, article text, sub-descriptions |
| `--color-gray-subtle` | `#666666` | `rgb(102, 102, 102)` | Secondary metadata, dates, news source labels |
| `--color-white` | `#ffffff` | `rgb(255, 255, 255)` | Backgrounds, light card fills, reverse text |

### 1.2 Surface & Border Neutrals

| Token Name | Hex Code | RGB | Role / Usage |
| :--- | :--- | :--- | :--- |
| `--color-surface-light` | `#f3f3f3` | `rgb(243, 243, 243)` | Section background fill, card background hover |
| `--color-surface-offwhite` | `#fbfbfb` | `rgb(251, 251, 251)` | Subtle alternating card fills |
| `--color-border-light` | `#d9d9d9` | `rgb(217, 217, 217)` | Container dividing lines, subtle borders |
| `--color-border-subtle` | `#e5e5e5` | `rgb(229, 229, 229)` | Nav dropdown divider borders |

### 1.3 Secondary & Departmental Accent Palette

| Accent Name | Hex Code | RGB | Associated Theme / Use Case |
| :--- | :--- | :--- | :--- |
| Deep Navy | `#002a3a` | `rgb(0, 42, 58)` | Global programs, institutional reports |
| Academic Blue | `#007396` | `rgb(0, 115, 150)` | Research, scholarship tags |
| Green | `#789d4a` | `rgb(120, 157, 74)` | Environmental, life sciences, sustainability |
| Gold / Amber | `#eaaa00` | `rgb(234, 170, 0)` | Highlights, awards, honors |
| Terracotta Orange | `#a9431e` | `rgb(169, 67, 30)` | Arts, culture, Hyde Park features |
| Plum / Violet | `#59315f` | `rgb(89, 49, 95)` | Humanities, interdisciplinary centers |

---

## 2. Typography Hierarchy

The University typography pairs a classic scholarly serif typeface for major headlines with a clean, geometric sans-serif for functional UI navigation and editorial body reading.

### 2.1 Font Families

```css
:root {
  --font-serif: "UChicagoSerif", Georgia, "Times New Roman", Garamond, serif;
  --font-sans: "UChicagoSansSerif-Regular", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-sans-semibold: "UChicagoSansSerif-SemiBold", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-sans-bold: "UChicagoSansSerif-Bold", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-icons: "Font Awesome 6 Pro", "Font Awesome 6 Brands", "FontAwesome", sans-serif;
}
```

### 2.2 Scale & Typographic Styles

| Hierarchy Level | Font Family | Size (Desktop) | Size (Mobile) | Weight | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Spotlight** | Serif | 44px – 56px | 32px – 38px | 700 (Bold) | 1.15 | -0.02em |
| **Section Title (H2)** | Sans-Serif | 28px – 34px | 22px – 26px | 800 (Extrabold) | 1.2 | 0.05em (Caps) |
| **Campaign Head (H1)** | Serif | 36px – 42px | 26px – 30px | 700 (Bold) | 1.2 | -0.01em |
| **Card Headings (H3/H4)** | Sans-Serif | 20px – 24px | 18px – 20px | 700 (Bold) | 1.3 | 0 |
| **HeadlineBar Statement** | Serif / Sans | 22px – 28px | 18px – 22px | 600 / 400 | 1.45 | 0 |
| **Body Copy** | Sans-Serif | 16px – 17px | 15px – 16px | 400 (Regular) | 1.6 | 0 |
| **Nav L1 Links** | Sans-Serif | 15px – 16px | 16px | 600 (SemiBold) | 1.0 | 0.01em |
| **Brand Bar Links** | Sans-Serif | 13px – 14px | 13px | 400 / 500 | 1.0 | 0.02em |
| **Small / Metadata** | Sans-Serif | 12px – 13px | 12px | 500 | 1.4 | 0.04em |

---

## 3. Layout Grid & Spacing

### 3.1 Containers

- **`single-col-inner`**: Standard content wrapper.
  - `max-width: 1200px` (or `1280px` for large displays)
  - `margin: 0 auto`
  - `padding-left: 24px; padding-right: 24px;` (mobile: `16px`)
- **`single-col-wide`**: Full-bleed section container.
  - `width: 100%`
  - `max-width: 100%`
  - Used for Hero Video Spotlight, CTA Bar, and Watermark wrap.

### 3.2 Responsive Breakpoints

| Breakpoint | Viewport Width | Behavior |
| :--- | :--- | :--- |
| **XL Desktop** | `> 1320px` | Maximum container width constraint, relaxed mega-menus |
| **Standard Desktop**| `1101px – 1320px` | Full 2-column header layout (Brand bar + Main Nav) |
| **Medium Desktop / Tablet Landscape** | `901px – 1100px` | Compact navigation spacing, tight padding |
| **Tablet Portrait / Mobile Collapse** | `≤ 900px` | Header converts to mobile menu hamburger button, flyout search stays accessible |
| **Mobile Standard** | `≤ 700px` | Grid collapses to single column, news stacks vertically, CTA buttons full width |
| **Mobile Small** | `≤ 540px` | Ultra-compact typography, full-width touch targets |

---

## 4. Component Design Tokens

### 4.1 Buttons & Interactive Pills

```css
/* Signature Maroon / Red Pill CTA */
.btn-maroon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #800000;
  color: #ffffff;
  padding: 10px 24px;
  border-radius: 4px;
  font-family: var(--font-sans-semibold);
  font-size: 14px;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  transition: background-color 0.25s ease, transform 0.2s ease;
  border: 1px solid transparent;
}
.btn-maroon:hover {
  background-color: #670a0a;
  transform: translateY(-1px);
}

/* White Hero CTA Button (CTA Bar Spotlight) */
.btn-cta-bar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #ffffff;
  color: #111111;
  padding: 14px 28px;
  font-family: var(--font-sans-bold);
  font-size: 15px;
  border: 2px solid #ffffff;
  border-radius: 2px;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.btn-cta-bar:hover {
  background-color: #800000;
  color: #ffffff;
  border-color: #800000;
}
```

### 4.2 News Card & Tile Micro-Interactions

- **Hover Elevation**: Cards feature subtle `box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08)` and `transform: translateY(-2px)` on hover.
- **Red Underline / Chevron Transition**: Link text displays a red underline or shifts `translateX(4px)` when focused or hovered.
- **Watermark Background Motif**: Subtle watermark of the University Phoenix crest (`phoenix.png`) at `background-position: right bottom; background-repeat: no-repeat; opacity: 0.08` overlaid behind the Latest News section.

---

## 5. Accessibility & ARIA Specifications

- **Skip Link**: `<a href="#maincontent" class="skipLink">Skip to main content</a>` positioned off-screen and brought into view on `:focus`.
- **Keyboard Navigation**: All mega-menu dropdowns support keyboard `Tab`, `Shift+Tab`, `Escape` to close, and `Enter`/`Space` to expand.
- **ARIA Roles**:
  - `role="navigation"` on main and utility navs
  - `aria-expanded="false|true"` on dropdown toggles
  - `aria-controls` referencing sub-navigation containers
  - `aria-label` on iconography buttons (e.g. `aria-label="Search UChicago"`, `aria-label="Toggle spotlight video"`)
- **Video Controls**: Pause/Play button with `aria-pressed` state and `#video-spotlight-desc` for screen-reader narration.
