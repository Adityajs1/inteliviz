import re

file_path = r'c:\Users\Aditya Tiwari\Downloads\gazala\site3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the end of the partners-glass section
# It currently ends with:
#           </div>
#     </div>
#   </section>

# Let's find "id="marqueeTrack">" and the first "</section>" after it.
start_idx = content.find('id="marqueeTrack">')
end_section_idx = content.find('</section>', start_idx) + len('</section>')

services_html = """

  <!-- CONTENT FOCUS CARDS -->
  <section id="services" style="padding-top: 64px; padding-bottom: 64px;">
    <div class="eyebrow reveal">
      <div class="eyebrow-line"></div><span class="eyebrow-text">SERVICES</span>
    </div>
    <div class="cards-grid reveal">
      <div class="feature-card">
        <div class="card-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.2"
            stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="7" r="2.5"></circle>
            <circle cx="6" cy="17" r="2.5"></circle>
            <circle cx="18" cy="17" r="2.5"></circle>
            <path d="M10.8 8.9L7.2 15.1"></path>
            <path d="M13.2 8.9l3.6 6.2"></path>
          </svg>
        </div>
        <h3 class="card-title">AI Relevant</h3>
        <p class="card-desc">Trend-aware content that speaks directly to AI enthusiasts and learners of today.</p>
      </div>

      <div class="feature-card">
        <div class="card-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.2"
            stroke-linecap="round" stroke-linejoin="round">
            <rect x="4" y="5" width="16" height="11" rx="2" ry="2"></rect>
            <path d="M9 20h6"></path>
            <path d="M12 16v4"></path>
          </svg>
        </div>
        <h3 class="card-title">Value-Driven</h3>
        <p class="card-desc">We post for attention as well as to educate, empower, and elevate.</p>
      </div>

      <div class="feature-card">
        <div class="card-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.2"
            stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4l16 4-4 16-4-8-8-4z"></path>
            <path d="M14 10l-4 4"></path>
          </svg>
        </div>
        <h3 class="card-title">Visually Elite</h3>
        <p class="card-desc">Clean, modern, and aesthetic visuals tailored for high-performing digital platforms.</p>
      </div>
    </div>
  </section>"""

content = content[:end_section_idx] + services_html + content[end_section_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored services section")
