import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

groinn_grid_perfect = """          <div class="pricing-grid">

            <!-- Category 1: Basic -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Basic</h3>
                <p class="pricing-card__desc">Essential hotel management for small hotels &amp; lodges.</p>
              </div>
              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGroinn1">₹</span>
                <span class="pricing-card__amount" id="cardAmountGroinn1" data-monthly="1000"
                  data-annual="12000">1000</span>
                <span class="pricing-card__original-price" id="cardOriginalGroinn1" style="display: none;">1000</span>
                <span class="pricing-card__period" id="cardPeriodGroinn1">/ month</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGroinn1"
                data-monthly-note="Yearly: ₹12,000 / year (Billed monthly)"
                data-annual-note="Yearly: ₹12,000 / year (Billed Annually)">
                Yearly: ₹12,000 / year (Billed monthly)
              </p>

              <p class="pricing-card__features-title">What's included:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Dashboard</b> – Basic overview</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Calendar</b> – Room availability check</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Front Desk</b> – Check-in / Check-out</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Bookings</b> – Reservation management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Guests</b> – Guest profiles management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Housekeeping</b> – Room cleaning status</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Rates</b> – Room pricing</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Enquiries</b> – Customer enquiries</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Reports</b> – Basic reports</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-basic">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Category 2: Standard -->
            <article class="pricing-card pricing-card--popular">
              <span class="popular-badge">Most Popular</span>

              <div class="pricing-card__header">
                <h3>Standard</h3>
                <p class="pricing-card__desc">Complete hotel management for growing hotels &amp; resorts.</p>
              </div>
              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGroinn2">₹</span>
                <span class="pricing-card__amount" id="cardAmountGroinn2" data-monthly="1000"
                  data-annual="12000">1000</span>
                <span class="pricing-card__original-price" id="cardOriginalGroinn2" style="display: none;">1000</span>
                <span class="pricing-card__period" id="cardPeriodGroinn2">/ month</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGroinn2"
                data-monthly-note="Yearly: ₹12,000 / year (Billed monthly)"
                data-annual-note="Yearly: ₹12,000 / year (Billed Annually)">
                Yearly: ₹12,000 / year (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in Basic, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Inventory</b> – Stock management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Banquet Halls</b> – Hall booking</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Deposits</b> – Advance payment tracking</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Accounts</b> – Financial management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>GST Register</b> – GST records</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Room Movements</b> – Room transfers</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Staff</b> – Staff management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Website</b> – Website management</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Reports</b> – Advanced reports</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Housekeeping</b> – Task assignment</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--primary" href="enquire.html?plan=groinn-standard">
                Start 15-Day Free Trial <span>→</span>
              </a>
            </article>

            <!-- Category 3: Prime -->
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
                <p class="pricing-card__desc">For hotel chains, luxury resorts, and organizations requiring customized
                  hotel management solutions.</p>
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
                  <span><b>Dedicated technical support &amp; custom SLA</b></span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-enterprise">
                Contact Hospitality Team <span>→</span>
              </a>
            </article>

          </div>"""

# Replace the whole <div class="pricing-grid"> ... </div> inside GroInn precisely
start_marker = '<section class="pricing-section" id="groinn-pricing"'
end_marker = '<!-- Trust Badges Strip -->'

sec_start = html.find(start_marker)
sec_end = html.find(end_marker, sec_start)

grid_start = html.find('<div class="pricing-grid">', sec_start)
grid_end = html.rfind('</div>', grid_start, sec_end) + len('</div>')

new_html = html[:grid_start] + groinn_grid_perfect + html[grid_end:]

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Groinn grid replaced cleanly and perfectly!")
