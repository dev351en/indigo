# Section 02: Hero Video Spotlight

## Overview
The Hero section is a full-width high-definition background video player demonstrating university campus life, world-class research laboratories, and scholarly collaboration.

## Asset Reference
- **Source Video**: `assets/2023-fall-video-update-1116.mp4` (Downloaded, 10.5 MB, 1080p MP4)
- **Original CDN URL**: `https://www.uchicago.edu/-/media/project/uchicago-tenant/www/videos/2023-fall-video-update-1116.mp4`

## Core Functional Requirements
1. **Autoplay & Muting**: `autoplay`, `muted`, `playsinline`, `loop` attributes are mandatory to ensure consistent cross-browser mobile and desktop auto-playback without sound disruption.
2. **Accessible Controls**:
   - Floating Play/Pause toggle button in bottom corner.
   - Updates `aria-pressed="false|true"` dynamically.
   - Keyboard accessible via `Tab` and `Space`/`Enter`.
3. **Screen Reader Description (`#video-spotlight-desc`)**:
   - `sr-only` element providing descriptive narrative of campus scenes:
     `"video showing various scenes around UChicago campus with overlay text: Field-Defining Scholarship, Transformative Education, World-Changing Ideas, The University of Chicago"`
4. **Dimensions**:
   - Desktop height: `600px` fixed or `calc(100vh - 120px)`.
   - Object fit: `object-fit: cover` to preserve aspect ratio regardless of viewport width.
