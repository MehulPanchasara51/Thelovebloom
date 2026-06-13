import re

with open('page.html', 'r') as f:
    html = f.read()

# 1. Update Hamburger to have an onclick event
html = html.replace(
    '<svg class="hamburger" viewBox="0 0 24 24"',
    '<svg class="hamburger" onclick="toggleMobileMenu()" viewBox="0 0 24 24"'
)

# Add a mobile-only Sign In link
html = html.replace(
    '<a href="#">Offers</a>\n        </nav>',
    '<a href="#">Offers</a>\n            <a href="#" class="mobile-only" style="display:none;">Sign In</a>\n        </nav>'
)

# 2. Add toggleMobileMenu script
script_addition = """
        function toggleMobileMenu() {
            document.querySelector('.main-nav').classList.toggle('active');
        }
        
        // ── Product cards ──
"""
html = html.replace('        // ── Product cards ──', script_addition)

# 3. Social Icons Replacement
new_socials = """                <div class="social-row">
                    <div class="social-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></div>
                    <div class="social-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></div>
                    <div class="social-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
                    <div class="social-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"/></svg></div>
                    <div class="social-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg></div>
                </div>"""

html = re.sub(r'<div class="social-row">.*?</div>\s*</div>\s*<div class="footer-col about-desktop">', new_socials + '\n            </div>\n            <div class="footer-col about-desktop">', html, flags=re.DOTALL)

# 4. CSS Media Query Updates
css_768 = """
        @media (max-width: 768px) {
            .top-bar { flex-wrap: wrap; padding: 16px 20px; }
            .hamburger { display: block; order: 1; flex: 1; margin: 0; }
            .logo { order: 2; flex: 2; }
            .header-icons { order: 3; flex: 1; justify-content: flex-end; gap: 14px; }
            .search-wrap { order: 4; flex: 0 0 100%; margin-top: 16px; justify-content: flex-start; }
            .search-icon { position: absolute; left: 14px; top: 12px; width: 16px; height: 16px; stroke: #888; }
            .search-input { display: block; width: 100%; max-width: 100%; height: 40px; padding-left: 36px; text-align: left; }
            .logo img { height: 32px; }
            .header-icons svg { width: 18px; height: 18px; }
            
            .main-nav { display: none; flex-direction: column; position: absolute; top: 100%; left: 0; width: 100%; background: #fff; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 1px solid var(--border); }
            .main-nav.active { display: flex; }
            .mobile-only { display: block !important; margin-top: 10px; border-top: 1px solid #eee; padding-top: 10px; }

            .hero { height: 500px; }
            .hero-slide { align-items: flex-end; padding-bottom: 60px; }
            .hero-slide h1 { font-size: 22px; letter-spacing: 1px; margin-bottom: 20px; }
            .hero-btn { font-size: 14px; padding: 0 24px; }
            .hero-arrow { display: none; }

            .explore-wrap { padding: 0; }
            .explore-track { flex-wrap: nowrap; overflow-x: auto; scroll-snap-type: x mandatory; gap: 12px; padding: 0 20px 20px; justify-content: flex-start; }
            .explore-item { flex: 0 0 calc(33.333% - 8px); scroll-snap-align: start; }
            .explore-box { width: 100%; height: auto; aspect-ratio: 1; }
            .explore-label { font-size: 11px; }

            .products-section { padding: 0 20px 10px; }
            .products-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
            .footer { padding: 40px 20px 20px; }
            .footer-grid { grid-template-columns: 1fr; gap: 32px; }
            
            .email-row { flex-direction: row; }
            .email-row input { flex: 1; width: auto; }
            .email-row button { width: auto; padding: 0 16px; font-size: 12px; }
            .social-icon svg { stroke: #222; fill: none !important; }
        }
"""

html = re.sub(r'@media \(max-width: 768px\) \{.*?(?=@media \(max-width: 480px\))', css_768, html, flags=re.DOTALL)

with open('page.html', 'w') as f:
    f.write(html)

print("Updates applied")
