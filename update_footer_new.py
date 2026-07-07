import re

with open('site3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS for the new footer
new_css = """
    /* ⚡ NEW FOOTER ⚡ */
    .new-footer {
      background-color: #0E0E0E;
      color: #FFFFFF;
      padding: 64px 48px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      font-family: var(--font-body);
    }
    
    .footer-inner {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 48px;
    }

    .footer-left {
      flex: 1;
      max-width: 500px;
    }

    .footer-heading {
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 500;
      margin-bottom: 32px;
      position: relative;
      padding-bottom: 12px;
      display: inline-block;
    }

    .footer-heading::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: 0;
      height: 2px;
      width: 100%;
      background-color: var(--lime); /* Replacing orange with yellow */
    }

    .footer-links {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: 32px;
      row-gap: 24px;
      margin-top: 24px;
    }

    .footer-links a {
      color: #b0b0b0;
      text-decoration: none;
      font-size: 11px;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 600;
      transition: color 0.2s;
    }

    .footer-links a:hover {
      color: #FFFFFF;
    }

    .footer-divider {
      width: 1px;
      background-color: rgba(255, 255, 255, 0.1);
      align-self: stretch;
      min-height: 200px;
    }

    .footer-right {
      flex: 1;
      max-width: 400px;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      text-align: right;
    }

    .footer-logo-box {
      border: 2px solid var(--lime);
      color: #FFFFFF;
      padding: 12px 16px;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 24px;
      letter-spacing: 1px;
      margin-bottom: 24px;
      display: inline-block;
    }

    .footer-bio {
      color: #b0b0b0;
      font-size: 13px;
      line-height: 1.6;
      margin-bottom: 48px;
    }

    .footer-copy {
      color: #777777;
      font-size: 12px;
    }

    @media (max-width: 768px) {
      .footer-inner {
        flex-direction: column;
        align-items: flex-start;
      }
      .footer-divider {
        display: none;
      }
      .footer-right {
        align-items: flex-start;
        text-align: left;
        margin-top: 48px;
      }
    }
"""

# HTML for the new footer
new_html = """
  <!-- NEW FOOTER -->
  <footer class="site-footer new-footer">
    <div class="footer-inner">
      <div class="footer-left">
        <h3 class="footer-heading">Follow Inteliviz</h3>
        <div class="footer-links">
          <a href="#">INSTAGRAM</a>
          <a href="#">TELEGRAM</a>
          <a href="#">FACEBOOK</a>
          <a href="mailto:collabaico@gmail.com">CONTACT US</a>
        </div>
      </div>
      <div class="footer-divider"></div>
      <div class="footer-right">
        <div class="footer-logo-box">IM</div>
        <p class="footer-bio">Inteliviz Media is a digital publishing network. You can find our work across Facebook, Instagram, and other major platforms covering the AI revolution in real time.</p>
        <p class="footer-copy">© Inteliviz Media 2026</p>
      </div>
    </div>
  </footer>
"""

# Insert CSS right before </style>
content = content.replace('</style>', new_css + '\n</style>')

# Replace the existing footer HTML
import re
# Regex to match the existing footer structure
# From <!-- FOOTER --> to </footer>
pattern = re.compile(r'<!-- FOOTER -->\s*<footer class="site-footer">.*?</footer>', re.DOTALL)
content = pattern.sub(new_html.strip(), content)

with open('site3.html', 'w', encoding='utf-8') as f:
    f.write(content)
