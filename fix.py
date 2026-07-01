import re

def main():
    with open('site3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix CSS
    css_old = r'''  \.feature-card \{.*?\}'''
    css_new = '''  .feature-card {
    background: var(--black);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 40px 32px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: transform 0.3s ease, border-color 0.3s ease;
  }'''
    content = re.sub(css_old, css_new, content, flags=re.DOTALL)

    # Fix HTML block
    cards_html = '''<section id="content" style="padding-top: 64px; padding-bottom: 64px;">
  <div class="eyebrow" style="justify-content:center">
    <div class="eyebrow-line"></div>
    <span class="eyebrow-text">Content</span>
    <div class="eyebrow-line"></div>
  </div>
  <div class="cards-grid">
    <div class="feature-card">
      <div class="card-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="6" y="6" width="12" height="12" rx="2" ry="2"></rect>
          <circle cx="9.5" cy="9.5" r="1.5" fill="var(--white)" stroke="none"></circle>
          <path d="M6 14l3.5-3.5a1.5 1.5 0 0 1 2.1 0L14 13"></path>
          <path d="M12 15l2-2a1.5 1.5 0 0 1 2.1 0L18 15"></path>
          <path d="M12 2v2"></path><path d="M12 2l-1.5 1.5"></path><path d="M12 2l1.5 1.5"></path>
          <path d="M12 20v2"></path><path d="M12 22l-1.5-1.5"></path><path d="M12 22l1.5-1.5"></path>
          <path d="M2 12h2"></path><path d="M2 12l1.5-1.5"></path><path d="M2 12l1.5 1.5"></path>
          <path d="M20 12h2"></path><path d="M22 12l-1.5-1.5"></path><path d="M22 12l-1.5 1.5"></path>
          <path d="M4 4l1.5 1.5"></path><path d="M4 4l0 2"></path><path d="M4 4l2 0"></path>
          <path d="M20 20l-1.5-1.5"></path><path d="M20 20l-2 0"></path><path d="M20 20l0-2"></path>
          <path d="M20 4l-1.5 1.5"></path><path d="M20 4l-2 0"></path><path d="M20 4l0 2"></path>
          <path d="M4 20l1.5-1.5"></path><path d="M4 20l0-2"></path><path d="M4 20l2 0"></path>
        </svg>
      </div>
      <h3 class="card-title">Viral by Design</h3>
      <p class="card-desc">Every post is engineered to spark emotion, conversation, and shares at scale.</p>
    </div>
    
    <div class="feature-card">
      <div class="card-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 18l-3 4 1-3.5L4 16l4 0"></path>
          <path d="M16 18l3 4-1-3.5L20 16l-4 0"></path>
          <circle cx="12" cy="11" r="7"></circle>
          <circle cx="12" cy="11" r="5"></circle>
          <polygon fill="var(--white)" stroke="none" points="12 9.5 11.2 11.2 9.5 11.5 10.8 12.8 10.4 14.5 12 13.5 13.6 14.5 13.2 12.8 14.5 11.5 12.8 11.2"></polygon>
        </svg>
      </div>
      <h3 class="card-title">AI Relevant</h3>
      <p class="card-desc">Trend-aware content that speaks directly to AI enthusiasts and learners of today.</p>
    </div>

    <div class="feature-card">
      <div class="card-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="var(--white)">
          <path d="M6 3a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v19l-6-4.5L6 22V3z"></path>
          <polygon fill="var(--black)" points="12 11 9.5 12.5 10 9.5 8 7.5 11 7.5 12 5 13 7.5 16 7.5 14 9.5 14.5 12.5"></polygon>
        </svg>
      </div>
      <h3 class="card-title">Visually Elite</h3>
      <p class="card-desc">Clean, modern, and aesthetic visuals tailored for high-performing digital platforms.</p>
    </div>

    <div class="feature-card">
      <div class="card-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--white)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 10h14l-7 9-7-9z"></path>
          <path d="M5 10l3-4h8l3 4"></path>
          <path d="M8 6l4 13"></path>
          <path d="M16 6l-4 13"></path>
          <path d="M12 6v4"></path>
          <path d="M12 1v2"></path>
          <path d="M16 2.5l-1.5 1.5"></path>
          <path d="M8 2.5l1.5 1.5"></path>
        </svg>
      </div>
      <h3 class="card-title">Value-Driven</h3>
      <p class="card-desc">We post for attention as well as to educate, empower, and elevate.</p>
    </div>
  </div>
</section>'''
    
    content = re.sub(r'<section id="content".*?</section>', cards_html, content, flags=re.DOTALL)
    
    with open('site3.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
