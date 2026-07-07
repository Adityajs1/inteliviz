import sys

html_content = """  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo">Inteliviz Media</div>
        <p class="footer-slogan">Helping you manage and grow your digital business with AI</p>
      </div>
      <div class="footer-newsletter">
        <form class="newsletter-form">
          <input type="email" placeholder="Enter your email" required>
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </div>
    
    <div class="footer-bottom">
      <div class="footer-column">
        <h4>About us</h4>
        <ul>
          <li><a href="#">Our story</a></li>
          <li><a href="#">The Team</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Company</h4>
        <ul>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">News</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Resources</h4>
        <ul>
          <li><a href="#">Papers</a></li>
          <li><a href="#">Documentation</a></li>
          <li><a href="#">Press conferences</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Plans & pricing</h4>
        <ul>
          <li><a href="#">Bronze Tier</a></li>
          <li><a href="#">Silver Tier</a></li>
          <li><a href="#">Gold Tier</a></li>
          <li><a href="#">Platinum</a></li>
        </ul>
      </div>
      <div class="footer-column contact-col">
        <h4>Contact us</h4>
        <ul>
          <li><a href="tel:4805550103">(480) 555-0103</a></li>
          <li><a href="mailto:collabaico@gmail.com">collabaico@gmail.com</a></li>
          <li class="address">1801 Cooks Mine Road,<br>Pleasant Hill, NM, 88101,<br>Contra Costa County</li>
        </ul>
      </div>
    </div>
    <div class="footer-copy-new">
      © 2026 Inteliviz Media · Digital Publishing Media · All rights reserved
    </div>
  </footer>
"""

css_content = """    /* ── FOOTER ── */
    .site-footer {
      padding: 64px 48px 32px 48px;
      background: var(--black);
      border-top: 1px solid var(--border);
      color: var(--white);
    }
    .footer-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 64px;
      flex-wrap: wrap;
      gap: 32px;
    }
    .footer-brand .footer-logo {
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 24px;
      color: var(--white);
      margin-bottom: 8px;
    }
    .footer-brand .footer-slogan {
      font-size: 14px;
      color: var(--mid);
      max-width: 300px;
    }
    .newsletter-form {
      display: flex;
      gap: 16px;
    }
    .newsletter-form input {
      padding: 12px 24px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--white);
      font-family: var(--font-body);
      font-size: 14px;
      width: 250px;
    }
    .newsletter-form button {
      padding: 12px 24px;
      border-radius: 8px;
      border: none;
      background: var(--lime);
      color: var(--black);
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 14px;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    .newsletter-form button:hover {
      opacity: 0.9;
    }
    .footer-bottom {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 32px;
      padding-bottom: 48px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 32px;
    }
    .footer-column h4 {
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 16px;
      margin-bottom: 24px;
      color: var(--white);
    }
    .footer-column ul {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .footer-column ul li a, .footer-column ul li {
      text-decoration: none;
      color: var(--mid);
      font-size: 14px;
      transition: color 0.2s;
      line-height: 1.5;
    }
    .footer-column ul li a:hover {
      color: var(--white);
    }
    .footer-copy-new {
      text-align: left;
      font-size: 12px;
      color: var(--muted);
    }
"""

css_mobile = """      .footer-top {
        flex-direction: column;
        align-items: flex-start;
      }
      .footer-bottom {
        grid-template-columns: 1fr 1fr;
      }
      .newsletter-form {
        flex-direction: column;
        width: 100%;
      }
      .newsletter-form input {
        width: 100%;
      }
"""

with open('site3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Replace HTML
start_html = -1
end_html = -1
for i, line in enumerate(lines):
    if '<!-- FOOTER -->' in line:
        start_html = i
    if start_html != -1 and i > start_html and '</footer>' in line:
        end_html = i
        break

if start_html != -1 and end_html != -1:
    lines = lines[:start_html] + [html_content] + lines[end_html+1:]

# 2. Replace Main CSS
start_css = -1
end_css = -1
for i, line in enumerate(lines):
    if '/* ── FOOTER ── */' in line:
        start_css = i
    if start_css != -1 and i > start_css and '/* ── FEATURE CARDS ── */' in line:
        end_css = i - 1
        break

if start_css != -1 and end_css != -1:
    lines = lines[:start_css] + [css_content] + lines[end_css+1:]

# 3. Replace Mobile CSS
start_mob = -1
end_mob = -1
for i, line in enumerate(lines):
    if '      footer {' in line and i > 800:
        start_mob = i
    if start_mob != -1 and i > start_mob and '      }' in line:
        end_mob = i
        break

if start_mob != -1 and end_mob != -1:
    lines = lines[:start_mob] + [css_mobile] + lines[end_mob+1:]

with open('site3.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
