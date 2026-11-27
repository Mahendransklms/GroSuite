import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new Groinn pricing grid HTML
new_groinn_grid = """          <div class="pricing-grid">

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

              <p class="pricing-card__features-title">Included features:</p>
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
                  <span><b>Calendar</b> – Room availability</span>
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
                  <span><b>Guests</b> – Guest profiles</span>
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
                  <span><b>Offers</b> – Basic discounts</span>
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
                  <span><b>Booking Sources</b> – Source tracking</span>
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
                  <span><b>Booking Sources</b> – Advanced source analysis</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Settings</b> – Advanced configuration</span>
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
                  <span><b>Custom ERP / CRM integration</b></span>
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
                  <span><b>Custom hotel website development</b></span>
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
                  <span><b>Custom reports and dashboards</b></span>
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
                  <span><b>Custom user roles and approval workflows</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Data migration from existing software</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Dedicated technical support</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Custom SLA and uptime commitment</b></span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-enterprise">
                Contact Hospitality Team <span>→</span>
              </a>
            </article>

          </div>"""

# Match the Groinn section grid precisely
pattern = r'(<section class="pricing-section" id="groinn-pricing"[^>]*>[\s\S]*?<div class="pricing-product-header">[\s\S]*?</div>\s*</div>\s*)(<div class="pricing-grid">[\s\S]*?</div>\s*)(<!-- Trust Badges Strip -->)'

match = re.search(pattern, html)
if not match:
    print("Pattern match FAILED!")
else:
    print("Pattern match SUCCESS!")
    updated_html = html[:match.start(2)] + new_groinn_grid + "\n\n          " + html[match.start(3):]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("pricing.html updated successfully!")
