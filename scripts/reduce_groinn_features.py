import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the updated Prime and Custom Quote features
prime_and_quote_replacement = """            <!-- Category 3: Prime -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Prime</h3>
                <p class="pricing-card__desc">Advanced hotel management for large hotels &amp; luxury resorts.</p>
              </div>
              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGroinn3">₹</span>
                <span class="pricing-card__amount" id="cardAmountGroinn3" data-monthly="1000"
                  data-annual="12000">1000</span>
                <span class="pricing-card__original-price" id="cardOriginalGroinn3" style="display: none;">1000</span>
                <span class="pricing-card__period" id="cardPeriodGroinn3">/ month</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGroinn3"
                data-monthly-note="Yearly: ₹12,000 / year (Billed monthly)"
                data-annual-note="Yearly: ₹12,000 / year (Billed Annually)">
                Yearly: ₹12,000 / year (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in Standard, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Dashboard</b> – Advanced analytics</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Calendar</b> – Advanced room planning</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Inventory</b> – Advanced stock tracking</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Banquet Halls</b> – Advanced event management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Accounts</b> – Advanced financial reports</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Reports</b> – Revenue and occupancy analytics</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Staff</b> – Advanced role-based permissions</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Cards &amp; Readers</b> – Hardware integration</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Website</b> – Advanced booking configuration</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-prime">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Category 4: Custom Quote -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Enterprise</h3>
                <p class="pricing-card__desc">For hotel chains, luxury resorts, and organizations requiring customized hotel management solutions.</p>
              </div>

              <div class="pricing-card__price-box pricing-card__price-box--quote">
                <span class="pricing-card__amount pricing-card__amount--quote">Custom Quote</span>
              </div>
              <p class="pricing-card__billing-note">Tailored per-property pricing &amp; volume tiers</p>

              <p class="pricing-card__features-title">Everything in Prime, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Multi-property and multi-branch management</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Centralized hotel dashboard</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Central Reservation System (CRS)</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Centralized inventory management</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Multi-property financial consolidation</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>OTA channel integrations</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Custom ERP / CRM integration</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Advanced API and webhook integration</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Private cloud / on-premise deployment</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Dedicated technical support &amp; custom SLA</b></span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-enterprise">
                Contact Hospitality Team <span>→</span>
              </a>
            </article>"""

pattern = r'(<!-- Category 3: Prime -->[\s\S]*?<!-- Category 4: Custom Quote -->[\s\S]*?</article>)'

match = re.search(pattern, html)
if not match:
    print("Match FAILED!")
else:
    print("Match SUCCESS!")
    updated_html = html[:match.start(1)] + prime_and_quote_replacement + html[match.end(1):]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("pricing.html updated successfully!")
