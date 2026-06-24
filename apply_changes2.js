const fs = require('fs');
const path = require('path');

const siteHtmlPath = path.join(__dirname, 'site.html');
const site2HtmlPath = path.join(__dirname, 'site2.html');
const site3HtmlPath = path.join(__dirname, 'site3.html');

console.log('Loading files...');
const siteHtml = fs.readFileSync(siteHtmlPath, 'utf8');
let site2Html = fs.readFileSync(site2HtmlPath, 'utf8');

// ----------------------------------------------------
// 1. EXTRACT PARTNERSHIPS SECTION FROM site.html
// ----------------------------------------------------
console.log('Extracting partnerships section from site.html...');
const pStartMarker = '<!-- PARTNERSHIPS — REDESIGNED MARQUEE -->';
const pEndMarker = '<!-- ANALYTICS -->';
const pStartIndex = siteHtml.indexOf(pStartMarker);
const pEndIndex = siteHtml.indexOf(pEndMarker);

if (pStartIndex === -1 || pEndIndex === -1) {
  console.error('Could not find partnerships markers in site.html!');
  process.exit(1);
}
const partnershipsHtml = siteHtml.substring(pStartIndex, pEndIndex);

// ----------------------------------------------------
// 2. CSS STYLES REPLACEMENT
// ----------------------------------------------------
console.log('Updating CSS styles in site2.html...');

// Remove the phone mockup styling (from .hero-visual to the end of ticker)
const cssStartMarker = '/* Phone mockup */';
const cssEndMarker = '/* ── ABOUT ── */';
const cssStartIndex = site2Html.indexOf(cssStartMarker);
const cssEndIndex = site2Html.indexOf(cssEndMarker);

const newCss = `/* Hero Image Container */
  .hero-image-container {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    max-width: 600px;
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 1.2s cubic-bezier(0.22, 1, 0.36, 1), transform 1.2s cubic-bezier(0.22, 1, 0.36, 1);
    will-change: transform, opacity;
  }
  .hero-image-container.visible {
    opacity: 1;
    transform: translateY(0);
  }
  .hero-image {
    width: 100%;
    height: auto;
    max-height: 520px;
    object-fit: contain;
    background: transparent;
    animation: hero-float 12s ease-in-out infinite alternate;
    will-change: transform;
  }
  @keyframes hero-float {
    0% { transform: translateY(0) translateX(0) scale(0.98); }
    50% { transform: translateY(-12px) translateX(8px) scale(1.02); }
    100% { transform: translateY(0) translateX(0) scale(0.98); }
  }

  /* ── STATS TICKER ── */
  .stats-bar {
    background: #0D0D0D;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    overflow: hidden; position: relative;
    padding: 20px 0;
  }
  .stats-track {
    display: flex; gap: 60px;
    animation: scroll-left 22s linear infinite;
    width: max-content;
  }
  @keyframes scroll-left { from{transform:translateX(0)} to{transform:translateX(-50%)} }
  .stat-item {
    display: flex; align-items: center; gap: 12px;
    white-space: nowrap; flex-shrink: 0;
  }
  .stat-num {
    font-family: var(--font-display);
    font-size: 20px; font-weight: 700;
    color: var(--lime);
  }
  .stat-label { font-size: 13px; color: var(--muted); letter-spacing: 0.06em; text-transform: uppercase; font-family: var(--font-body); }
  .stat-sep { color: rgba(255,255,255,0.15); font-size: 20px; }

  /* ── PARTNER MARQUEE ── */
  .partners-glass {
    position: relative;
    max-width: 1400px;
    margin: 0 auto;
    padding: 36px 0;
    background: linear-gradient(180deg, rgba(255,255,255,0.035), rgba(255,255,255,0.015));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 28px;
    backdrop-filter: blur(14px);
    box-shadow:
      0 30px 80px -30px rgba(0,0,0,0.6),
      inset 0 1px 0 rgba(255,255,255,0.06);
    overflow: hidden;
  }
  .marquee-wrapper {
    overflow: hidden;
    position: relative;
    padding: 4px 0;
  }
  .marquee-wrapper::before,
  .marquee-wrapper::after {
    content: '';
    position: absolute; top: 0; bottom: 0; z-index: 2;
    width: 160px;
    pointer-events: none;
  }
  .marquee-wrapper::before { left: 0;
    background: linear-gradient(90deg, rgba(8,8,8,0.96), rgba(8,8,8,0));
  }
  .marquee-wrapper::after  { right: 0;
    background: linear-gradient(-90deg, rgba(8,8,8,0.96), rgba(8,8,8,0));
  }
  .marquee-track {
    display: flex;
    align-items: center;
    gap: 72px;
    animation: marquee-scroll 45s linear infinite;
    width: max-content;
    will-change: transform;
  }
  .marquee-track:hover { animation-play-state: paused; }
  @keyframes marquee-scroll { from{transform:translateX(0)} to{transform:translateX(-50%)} }

  .partner-logo-item {
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    height: 90px;
    width: 180px;
    padding: 0 12px;
    background: transparent;
    border: none;
    transition: transform 0.4s cubic-bezier(0.22,1,0.36,1);
  }
  .partner-logo-item img {
    max-height: 64px;
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    background: transparent;
    opacity: 0.55;
    transition: opacity 0.2s, transform 0.2s;
    filter: brightness(0) invert(1);
  }
  .partner-logo-item:hover img {
    opacity: 0.9;
    transform: scale(1.08);
  }

  `;

site2Html = site2Html.substring(0, cssStartIndex) + newCss + site2Html.substring(cssEndIndex);

// Update lead paragraph styling in site2.html
site2Html = site2Html.replace(
  `  p.lead {
    font-size: 15px;
    color: var(--mid);
    line-height: 1.75;
    max-width: 480px;
    margin-top: 20px;
  }`,
  `  p.lead {
    font-size: 17px;
    font-weight: 500;
    color: var(--mid);
    line-height: 1.75;
    max-width: 480px;
    margin-top: 20px;
  }`
);

// Update Media Queries in site2.html to replace phone mockup settings with hero image container
site2Html = site2Html.replace(
  `    .hero-visual { height: 320px; }
    .phone { width: 160px; height: 300px; }
    .phone2 { display: none; }
    .ticker { grid-template-columns: repeat(2, 1fr); gap: 1px; background: var(--border); padding: 0; }
    .ticker-item { padding: 24px; border-right: none; background: var(--black); }`,
  `    .hero-image-container { max-width: 80%; margin: 0 auto; }`
);

// ----------------------------------------------------
// 3. HTML BODY REPLACEMENTS
// ----------------------------------------------------
console.log('Replacing HTML markup in site2.html...');

// Replace lead subheading text (remove em-dash, add comma)
site2Html = site2Html.replace(
  '<p class="lead">Millions of reach across Facebook and Instagram — we break the biggest stories in artificial intelligence, robotics, and emerging technology.</p>',
  '<p class="lead">Millions of reach across Facebook and Instagram, we break the biggest stories in artificial intelligence, robotics, and emerging technology.</p>'
);

// Replace hero visual with hero image container
const heroVisualStart = site2Html.indexOf('<div class="hero-visual">');
const heroVisualEnd = site2Html.indexOf('</section>', heroVisualStart);
if (heroVisualStart === -1 || heroVisualEnd === -1) {
  console.error('Could not find hero visual markers!');
  process.exit(1);
}
const visualMarkup = `  <div class="hero-image-container" id="heroImageContainer">
    <img src="phones.png" class="hero-image" alt="Inteliviz and ArtificialIntelligence.co Instagram Feed Preview on Mobile Phones" loading="lazy">
  </div>\n</section>`;
site2Html = site2Html.substring(0, heroVisualStart) + visualMarkup + site2Html.substring(heroVisualEnd + 10);

// Replace static ticker with scrolling stats ticker
const tickerStart = site2Html.indexOf('<!-- TICKER -->');
const tickerEnd = site2Html.indexOf('<!-- ABOUT -->');
if (tickerStart === -1 || tickerEnd === -1) {
  console.error('Could not find ticker markers!');
  process.exit(1);
}
const statsTickerMarkup = `<!-- STATS TICKER -->
<div class="stats-bar" aria-label="Key statistics">
  <div class="stats-track">
    <div class="stat-item"><span class="stat-num">400K+</span><span class="stat-label">Instagram Audience</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">40M+</span><span class="stat-label">Quarterly Reach</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">100K+</span><span class="stat-label">Facebook Followers</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">30+</span><span class="stat-label">Brand Collaborations</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <!-- Duplicate for seamless loop -->
    <div class="stat-item"><span class="stat-num">400K+</span><span class="stat-label">Instagram Audience</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">40M+</span><span class="stat-label">Quarterly Reach</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">100K+</span><span class="stat-label">Facebook Followers</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
    <div class="stat-item"><span class="stat-num">30+</span><span class="stat-label">Brand Collaborations</span></div>
    <div class="stat-item stat-sep" aria-hidden="true">·</div>
  </div>
</div>\n\n`;
site2Html = site2Html.substring(0, tickerStart) + statsTickerMarkup + site2Html.substring(tickerEnd);

// Replace collaborations section logo items list with base64 wrapper extracted from site.html
const collabStart = site2Html.indexOf('<!-- COLLABORATIONS -->');
const collabEnd = site2Html.indexOf('<!-- ANALYTICS -->');
if (collabStart === -1 || collabEnd === -1) {
  console.error('Could not find collaborations markers!');
  process.exit(1);
}
site2Html = site2Html.substring(0, collabStart) + partnershipsHtml + site2Html.substring(collabEnd);


// ----------------------------------------------------
// 4. JAVASCRIPT ANIMATION HANDLERS
// ----------------------------------------------------
console.log('Adding JavaScript event listeners in site2.html...');

const jsCode = `  // Reveal hero image container on load
  document.addEventListener("DOMContentLoaded", () => {
    const heroImageContainer = document.getElementById("heroImageContainer");
    if (heroImageContainer) {
      setTimeout(() => {
        heroImageContainer.classList.add("visible");
      }, 150);
    }
  });

  // Parallax effect on scroll for hero image
  window.addEventListener("scroll", () => {
    const heroImageContainer = document.getElementById("heroImageContainer");
    if (heroImageContainer) {
      const scrollY = window.scrollY;
      if (scrollY < window.innerHeight) {
        heroImageContainer.style.transform = 'translateY(' + (scrollY * 0.12) + 'px)';
      }
    }
  }, { passive: true });
</script>`;

site2Html = site2Html.replace('</script>', jsCode);

// Write modified HTML back to site2.html and site3.html
console.log('Writing output files...');
fs.writeFileSync(site2HtmlPath, site2Html, 'utf8');
fs.writeFileSync(site3HtmlPath, site2Html, 'utf8');

fs.unlinkSync(__filename);
console.log('All changes applied successfully to site2.html and site3.html!');
