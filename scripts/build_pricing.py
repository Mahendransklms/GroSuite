import os
import re

PRICING_FILE = r'pricing.html'
STYLE_FILE = r'css/style.css'

with open(PRICING_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Step 1 Submit Button & Step 2 comment-out
step1_old_submit = '''                <!-- Submit Step 1 Button -->
                <div class="pricing-gate-actions">
                  <button type="button" id="btnSubmitStep1" class="btn-pricing-submit">
                    <span>Submit</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    Step 1 of 2: Country &amp; Currency choice configures your billing rates.
                  </p>
                </div>
              </div>

              <!-- STEP 2: Company & Contact Details Block (Hidden initially) -->
              <div id="pricingStep2Block" class="pricing-step-container" style="display: none;">
                <div class="pricing-gate-header">
                  <!-- <span class="pricing-gate-step-badge">STEP 2 OF 2</span> -->
                  <h2>Fill Company &amp; Contact Details</h2>
                  <p>Provide your business and contact information to unlock transparent pricing and receive an official
                    quotation.</p>
                </div>

                <!-- Selected Summary Bar -->
                <div class="step2-selection-bar">
                  <span>Selected Region: <strong id="step2SelectedRegion">🇮🇳 India · INR (₹)</strong></span>
                  <button type="button" id="btnBackToStep1" class="btn-step-edit">Change Country / Currency ✎</button>
                </div>

                <div class="pricing-gate-subblock">
                  <div class="pricing-gate-grid-2">
                    <div class="pricing-field-group">
                      <label for="pricingCompanyName">Company Name *</label>
                      <input type="text" id="pricingCompanyName" name="company_name" class="pricing-input"
                        placeholder="e.g. Acme Technologies" required>
                    </div>

                    <div class="pricing-field-group">
                      <label for="pricingFullName">Your Full Name *</label>
                      <input type="text" id="pricingFullName" name="full_name" class="pricing-input"
                        placeholder="e.g. Rahul Sharma" required>
                    </div>

                    <div class="pricing-field-group">
                      <label for="pricingWorkEmail">Work Email *</label>
                      <input type="email" id="pricingWorkEmail" name="work_email" class="pricing-input"
                        placeholder="e.g. rahul@company.com" required>
                    </div>

                    <div class="pricing-field-group">
                      <label for="pricingPhone">Phone / WhatsApp Number *</label>
                      <input type="tel" id="pricingPhone" name="phone" class="pricing-input"
                        placeholder="e.g. +91 98765 43210" required>
                    </div>

                    <div class="pricing-field-group">
                      <label for="pricingTeamSize">Number of Employees *</label>
                      <select id="pricingTeamSize" name="employee_count" class="pricing-input pricing-select" required>
                        <option value="" disabled selected>Select employee count</option>
                        <option value="1-10">1 - 10 Employees</option>
                        <option value="11-50">11 - 50 Employees</option>
                        <option value="51-200">51 - 200 Employees</option>
                        <option value="201-500">201 - 500 Employees</option>
                        <option value="500+">500+ Employees</option>
                      </select>
                    </div>

                    <div class="pricing-field-group">
                      <label for="pricingInterest">Solution of Interest *</label>
                      <select id="pricingInterest" name="solution_interest" class="pricing-input pricing-select"
                        required>
                        <option value="All GroSuite Solutions">All GroSuite Solutions (HRMS, ERP, CRM)</option>
                        <option value="HRMS Solutions">HRMS Solutions</option>
                        <option value="ERP Solutions">ERP Solutions</option>
                        <option value="CRM Solutions">CRM Solutions</option>
                        <option value="Business Automation">Business Automation</option>
                        <option value="System Integration">System Integration</option>
                        <option value="Cyber Security">Cyber Security</option>
                        <option value="Custom Architecture">Custom Enterprise Architecture</option>
                      </select>
                    </div>
                  </div>
                </div>

                <!-- Submit Step 2 Button -->
                <div class="pricing-gate-actions">
                  <button type="submit" id="pricingSubmitBtn" class="btn-pricing-submit">
                    <span>Show Price</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    🔒 We respect your privacy. Details will be delivered to your email and our sales desk.
                  </p>
                  <div id="pricingFormStatus" class="pricing-form-status" role="status" aria-live="polite"></div>
                </div>
              </div>'''

step1_new_submit = '''                <!-- Submit Step 1 Button (Directly unlocks pricing while Step 2 is temporarily disabled) -->
                <div class="pricing-gate-actions">
                  <button type="button" id="btnSubmitStep1" class="btn-pricing-submit">
                    <span>View Pricing Plans</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    Country &amp; Currency choice configures your transparent billing rates instantly.
                  </p>
                </div>
              </div>

              <!-- STEP 2: Company & Contact Details Block (Disabled / commented out per request - can be re-enabled anytime)
              <div id="pricingStep2Block" class="pricing-step-container" style="display: none;">
                <div class="pricing-gate-header">
                  <h2>Fill Company &amp; Contact Details</h2>
                  <p>Provide your business and contact information to unlock transparent pricing and receive an official quotation.</p>
                </div>

                <div class="step2-selection-bar">
                  <span>Selected Region: <strong id="step2SelectedRegion">🇮🇳 India · INR (₹)</strong></span>
                  <button type="button" id="btnBackToStep1" class="btn-step-edit">Change Country / Currency ✎</button>
                </div>

                <div class="pricing-gate-subblock">
                  <div class="pricing-gate-grid-2">
                    <div class="pricing-field-group">
                      <label for="pricingCompanyName">Company Name *</label>
                      <input type="text" id="pricingCompanyName" name="company_name" class="pricing-input" placeholder="e.g. Acme Technologies">
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingFullName">Your Full Name *</label>
                      <input type="text" id="pricingFullName" name="full_name" class="pricing-input" placeholder="e.g. Rahul Sharma">
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingWorkEmail">Work Email *</label>
                      <input type="email" id="pricingWorkEmail" name="work_email" class="pricing-input" placeholder="e.g. rahul@company.com">
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingPhone">Phone / WhatsApp Number *</label>
                      <input type="tel" id="pricingPhone" name="phone" class="pricing-input" placeholder="e.g. +91 98765 43210">
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingTeamSize">Number of Employees *</label>
                      <select id="pricingTeamSize" name="employee_count" class="pricing-input pricing-select">
                        <option value="" disabled selected>Select employee count</option>
                        <option value="1-10">1 - 10 Employees</option>
                        <option value="11-50">11 - 50 Employees</option>
                        <option value="51-200">51 - 200 Employees</option>
                        <option value="201-500">201 - 500 Employees</option>
                        <option value="500+">500+ Employees</option>
                      </select>
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingInterest">Solution of Interest *</label>
                      <select id="pricingInterest" name="solution_interest" class="pricing-input pricing-select">
                        <option value="All GroSuite Solutions">All GroSuite Solutions (HRMS, ERP, CRM)</option>
                        <option value="HRMS Solutions">HRMS Solutions</option>
                        <option value="ERP Solutions">ERP Solutions</option>
                        <option value="CRM Solutions">CRM Solutions</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div class="pricing-gate-actions">
                  <button type="submit" id="pricingSubmitBtn" class="btn-pricing-submit">
                    <span>Show Price</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    🔒 We respect your privacy. Details will be delivered to your email and our sales desk.
                  </p>
                  <div id="pricingFormStatus" class="pricing-form-status" role="status" aria-live="polite"></div>
                </div>
              </div>
              -->'''

if step1_old_submit in content:
    content = content.replace(step1_old_submit, step1_new_submit, 1)
    print("Step 1 and Step 2 updated successfully.")
else:
    print("ERROR: step1_old_submit not found!")

# 2. Update Success Banner
old_banner = '''            <!-- Success Confirmation Bar (shown after submission) -->
            <div id="pricingSuccessBanner" class="pricing-success-banner" style="display: none;">
              <div class="pricing-success-banner__icon">✓</div>
              <div class="pricing-success-banner__text">
                <h3>Pricing Unlocked for <span id="summaryCompany">Your Company</span>!</h3>
                <p>
                  A formal quotation has been sent to <b id="summaryEmail">email@company.com</b>.
                  Displaying pricing in <b id="summaryCountry">India</b> (<b id="summaryCurrency">INR - ₹</b>).
                </p>
              </div>
              <div class="pricing-success-banner__actions">
                <label for="quickCurrencySwitch"
                  style="font-size: 0.85rem; font-weight: 700; color: #475569;">Currency:</label>
                <select id="quickCurrencySwitch" class="pricing-select pricing-select--compact"
                  aria-label="Change currency">
                  <option value="INR">INR (₹)</option>
                  <option value="USD">USD ($)</option>
                  <option value="GBP">GBP (£)</option>
                  <option value="EUR">EUR (€)</option>
                  <option value="AED">AED (AED)</option>
                  <option value="SGD">SGD (S$)</option>
                  <option value="AUD">AUD (A$)</option>
                  <option value="CAD">CAD (C$)</option>
                </select>
                <button type="button" id="btnEditDetails" class="btn-edit-details">Edit Details ✎</button>
              </div>
            </div>'''

new_banner = '''            <!-- Success Confirmation Bar (shown after submission) -->
            <div id="pricingSuccessBanner" class="pricing-success-banner" style="display: none;">
              <div class="pricing-success-banner__icon">✓</div>
              <div class="pricing-success-banner__text">
                <h3>Pricing Unlocked for <span id="summaryCompany">GroSuite Products</span>!</h3>
                <p>
                  Displaying pricing in <b id="summaryCountry">India</b> (<b id="summaryCurrency">INR - ₹</b>).
                  You can change currency anytime using the selector.
                </p>
              </div>
              <div class="pricing-success-banner__actions">
                <label for="quickCurrencySwitch"
                  style="font-size: 0.85rem; font-weight: 700; color: #475569;">Currency:</label>
                <select id="quickCurrencySwitch" class="pricing-select pricing-select--compact"
                  aria-label="Change currency">
                  <option value="INR">INR (₹)</option>
                  <option value="USD">USD ($)</option>
                  <option value="GBP">GBP (£)</option>
                  <option value="EUR">EUR (€)</option>
                  <option value="AED">AED (AED)</option>
                  <option value="SGD">SGD (S$)</option>
                  <option value="AUD">AUD (A$)</option>
                  <option value="CAD">CAD (C$)</option>
                </select>
                <button type="button" id="btnEditDetails" class="btn-edit-details">Change Country / Currency ✎</button>
              </div>
            </div>'''

if old_banner in content:
    content = content.replace(old_banner, new_banner, 1)
    print("Success Banner updated successfully.")
else:
    print("ERROR: old_banner not found!")

# 3. Replace Pricing Details Container contents (Switcher, Tabs, Grohrms, Groinn, Grolog)
old_pricing_details_start = '''    <!-- Pricing Details Container (Revealed After Submission) -->
    <div id="pricingDetailsContainer" class="pricing-details-container" style="display: none;">

      <!-- Billing Cycle Switcher & Currency Indicator -->
      <section class="pricing-controls-section" style="padding-top: 1.5rem; padding-bottom: 0.5rem;">
        <div class="section-wrap">

          <div class="billing-switcher" role="group" aria-label="Billing cycle selector">
            <span class="billing-switcher__label active" id="labelMonthly">Monthly Billing</span>
            <label class="billing-toggle-switch" for="billingToggle" aria-label="Toggle annual billing discount">
              <input type="checkbox" id="billingToggle">
              <span class="slider"></span>
            </label>
            <span class="billing-switcher__label" id="labelAnnual">Annual Billing</span>
            <span class="discount-pill">Save 20%</span>
          </div>

        </div>
      </section>

      <!-- Pricing Cards Grid -->
      <section class="pricing-section">
        <div class="section-wrap">

          <div class="pricing-grid">

            <!-- Plan 1: Starter HR -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Starter HR</h3>
                <p class="pricing-card__desc">Essential HR directory, leave tracking, and employee self-service for
                  small
                  teams.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyStarter">₹</span>
                <span class="pricing-card__amount" id="cardAmountStarter" data-monthly="60" data-annual="45">60</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" data-monthly-note="Billed monthly (excl. GST)"
                data-annual-note="Billed annually (Save 20%)">
                Billed monthly (excl. GST)
              </p>

              <p class="pricing-card__features-title">What's included:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Centralized employee directory &amp; profiles</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Leave applications &amp; holiday calendars</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Employee Self-Service (ESS) mobile app</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Secure document vault &amp; letters</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Mobile check-in with GPS location</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Email &amp; standard ticket support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=starter">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 2: Professional (Most Popular) -->
            <article class="pricing-card pricing-card--popular">
              <span class="popular-badge">Most Popular</span>

              <div class="pricing-card__header">
                <h3>Professional</h3>
                <p class="pricing-card__desc">Complete HRMS with biometric attendance, automated payroll, shifts, and
                  statutory compliance.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyPro">₹</span>
                <span class="pricing-card__amount" id="cardAmountPro" data-monthly="100" data-annual="75">100</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" data-monthly-note="Billed monthly (excl. GST)"
                data-annual-note="Billed annually (Save 20%)">
                Billed monthly (excl. GST)
              </p>

              <p class="pricing-card__features-title">Everything in Starter, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Biometric machine sync</b> (ZKTeco, eSSL)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Automated 1-click payroll &amp; payslips</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Statutory reports (PF, ESI, PT, TDS)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Shift rosters &amp; overtime calculation</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Geofencing attendance with selfie verification</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>WhatsApp notifications &amp; PDF payslip dispatch</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Priority email &amp; phone onboarding support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--primary" href="enquire.html?plan=professional">
                Start 15-Day Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 3: Enterprise Suite -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Enterprise Suite</h3>
                <p class="pricing-card__desc">For multi-branch companies needing performance reviews, ERP/CRM data sync,
                  and advanced analytics.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyEnterprise">₹</span>
                <span class="pricing-card__amount" id="cardAmountEnterprise" data-monthly="180"
                  data-annual="140">180</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" data-monthly-note="Billed monthly (excl. GST)"
                data-annual-note="Billed annually (Save 20%)">
                Billed monthly (excl. GST)
              </p>

              <p class="pricing-card__features-title">Everything in Professional, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Multi-branch &amp; multi-company</b> support</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Performance appraisals &amp; 360° feedback</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom multi-tier approval workflows</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>ERP &amp; CRM data synchronization connectors</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Advanced business analytics &amp; custom dashboard</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated Technical Account Manager &amp; 99.9% SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=enterprise">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 4: Custom Architecture -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Custom Architecture</h3>
                <p class="pricing-card__desc">Tailored software engineering, on-premise private cloud, bespoke AI
                  workflows, and dedicated pods.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__amount" style="font-size: 2.1rem; line-height: 1.2;">Custom Quote</span>
              </div>
              <p class="pricing-card__billing-note">Tailored project scope &amp; milestones</p>

              <p class="pricing-card__features-title">Tailored deliverables:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Private Cloud or On-Premise dedicated servers</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom ERP/CRM module development</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Bespoke AI assistants, bots &amp; process automations</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Legacy system data migration &amp; custom ETL</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Enterprise security audits &amp; custom compliance</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated senior engineering pod &amp; 24/7 SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=custom">
                Contact Architects <span>→</span>
              </a>
            </article>

          </div>

          <!-- Trust Badges Strip -->'''

gro_ring_svg = '<span class="gro-brand-word" aria-label="{brand}">Gr<svg class="gro-o-ring" viewBox="0 0 40 40" aria-label="o" role="img"><path d="M18.8 4.05 A16 16 0 0 0 4.05 18.8" stroke="var(--red, #d7263d)" fill="none" stroke-width="8" stroke-linecap="butt" /><path d="M21.2 4.05 A16 16 0 0 1 35.95 18.8" stroke="var(--green, #17a34a)" fill="none" stroke-width="8" stroke-linecap="butt" /><path d="M35.95 21.2 A16 16 0 0 1 21.2 35.95" stroke="var(--ring-blue, #2a6df4)" fill="none" stroke-width="8" stroke-linecap="butt" /><path d="M4.05 21.2 A16 16 0 0 0 18.8 35.95" stroke="var(--amber, #dba21e)" fill="none" stroke-width="8" stroke-linecap="butt" /></svg>{suffix}</span>'

ring_grohrms = gro_ring_svg.format(brand="Grohrms", suffix="hrms")
ring_groinn = gro_ring_svg.format(brand="Groinn", suffix="inn")
ring_grolog = gro_ring_svg.format(brand="Grolog", suffix="log")

new_pricing_details = f'''    <!-- Pricing Details Container (Revealed After Submission) -->
    <div id="pricingDetailsContainer" class="pricing-details-container" style="display: none;">

      <!-- Billing Cycle Switcher & Product Tabs -->
      <section class="pricing-controls-section" style="padding-top: 1.5rem; padding-bottom: 0.5rem;">
        <div class="section-wrap">

          <div class="billing-switcher" role="group" aria-label="Billing cycle selector">
            <span class="billing-switcher__label active" id="labelMonthly">Monthly Billing</span>
            <label class="billing-toggle-switch" for="billingToggle" aria-label="Toggle annual billing discount">
              <input type="checkbox" id="billingToggle">
              <span class="slider"></span>
            </label>
            <span class="billing-switcher__label" id="labelAnnual">Annual Billing</span>
            <span class="discount-pill">Save 20%</span>
          </div>

          <!-- Product Switcher Navigation Tabs -->
          <div class="pricing-product-tabs" role="tablist" aria-label="GroSuite Products Pricing">
            <a href="#grohrms-pricing" class="pricing-product-tab active" id="tabGrohrms" role="tab" aria-selected="true">
              {ring_grohrms}
              <span>(HR &amp; Payroll)</span>
            </a>
            <a href="#groinn-pricing" class="pricing-product-tab" id="tabGroinn" role="tab" aria-selected="false">
              {ring_groinn}
              <span>(Hotel Management)</span>
            </a>
            <a href="#grolog-pricing" class="pricing-product-tab" id="tabGrolog" role="tab" aria-selected="false">
              {ring_grolog}
              <span>(Call Log Management)</span>
            </a>
          </div>

        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- PRODUCT 1: GROHRMS (HR & Payroll Management)                              -->
      <!-- ========================================================================= -->
      <section class="pricing-section" id="grohrms-pricing" style="padding-top: 1rem;">
        <div class="section-wrap">

          <div class="pricing-product-header" style="text-align: center; margin-bottom: 2.2rem;">
            <p class="eyebrow" style="color: var(--blue, #2a6df4); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 0.4rem;">HR &amp; PAYROLL MANAGEMENT SUITE</p>
            <h2 style="font-size: 2.2rem; margin: 0 0 0.5rem;">
              {ring_grohrms} Pricing Plans
            </h2>
            <p style="color: var(--muted, #94a3b8); max-width: 620px; margin: 0 auto; font-size: 1rem;">
              Scalable HRMS with employee self-service, biometric attendance, automated payroll &amp; statutory compliance.
            </p>
          </div>

          <div class="pricing-grid">

            <!-- Plan 1: Basic (₹15/user/mo, Yearly: ₹180) -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Basic</h3>
                <p class="pricing-card__desc">Essential HR directory, leave management, and employee self-service for growing teams.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyBasic">₹</span>
                <span class="pricing-card__amount" id="cardAmountBasic" data-monthly="15" data-annual="12">15</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteBasic" data-monthly-note="Yearly: ₹180 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹144 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹180 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">What's included:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Centralized employee directory &amp; profiles</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Leave applications &amp; holiday calendars</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Employee Self-Service (ESS) mobile app</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Secure document vault &amp; letters</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Mobile check-in with GPS location</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Standard email &amp; ticket support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grohrms-basic">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 2: Standard (₹30/user/mo, Yearly: ₹360) (Most Popular) -->
            <article class="pricing-card pricing-card--popular">
              <span class="popular-badge">Most Popular</span>

              <div class="pricing-card__header">
                <h3>Standard</h3>
                <p class="pricing-card__desc">Complete HRMS with biometric attendance, automated payroll, shifts, and statutory compliance.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyStandard">₹</span>
                <span class="pricing-card__amount" id="cardAmountStandard" data-monthly="30" data-annual="24">30</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteStandard" data-monthly-note="Yearly: ₹360 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹288 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹360 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in Basic, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Biometric machine sync</b> (ZKTeco, eSSL)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Automated 1-click payroll &amp; payslips</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Statutory compliance reports (PF, ESI, PT, TDS)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Shift rosters &amp; overtime tracking</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Geofencing attendance with selfie verification</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>WhatsApp notifications &amp; PDF payslip delivery</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Priority email &amp; phone onboarding support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--primary" href="enquire.html?plan=grohrms-standard">
                Start 15-Day Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 3: Prime (₹60/user/mo, Yearly: ₹720) -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Prime</h3>
                <p class="pricing-card__desc">For fast-growing organizations requiring multi-branch control, appraisals, and advanced analytics.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyPrime">₹</span>
                <span class="pricing-card__amount" id="cardAmountPrime" data-monthly="60" data-annual="48">60</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNotePrime" data-monthly-note="Yearly: ₹720 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹576 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹720 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in Standard, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Multi-branch &amp; multi-company hierarchy</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Performance appraisals &amp; 360° review cycles</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom multi-tier approval matrix</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>ERP &amp; CRM data synchronization connectors</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Advanced workforce analytics &amp; custom dashboard</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated Technical Account Manager &amp; 99.9% SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grohrms-prime">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Plan 4: Custom Enterprise Architecture -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Custom Architecture</h3>
                <p class="pricing-card__desc">Tailored software engineering, on-premise private cloud, bespoke AI workflows, and dedicated pods.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__amount" style="font-size: 2.1rem; line-height: 1.2;">Custom Quote</span>
              </div>
              <p class="pricing-card__billing-note">Tailored project scope &amp; milestones</p>

              <p class="pricing-card__features-title">Tailored deliverables:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Private Cloud or On-Premise dedicated servers</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom ERP/CRM module development</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Bespoke AI assistants, bots &amp; process automations</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Legacy system data migration &amp; custom ETL</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Enterprise security audits &amp; custom compliance</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated senior engineering pod &amp; 24/7 SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grohrms-custom">
                Contact Architects <span>→</span>
              </a>
            </article>

          </div>

        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- PRODUCT 2: GROINN (Hotel Management System)                               -->
      <!-- ========================================================================= -->
      <section class="pricing-section" id="groinn-pricing" style="padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.08);">
        <div class="section-wrap">

          <div class="pricing-product-header" style="text-align: center; margin-bottom: 2.2rem;">
            <p class="eyebrow" style="color: var(--blue, #2a6df4); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 0.4rem;">HOTEL &amp; HOSPITALITY MANAGEMENT</p>
            <h2 style="font-size: 2.2rem; margin: 0 0 0.5rem;">
              {ring_groinn} Hotel Management Pricing
            </h2>
            <p style="color: var(--muted, #94a3b8); max-width: 620px; margin: 0 auto; font-size: 1rem;">
              Complete hotel operating system for front desk, reservation bookings, restaurant &amp; bar POS, guest CRM &amp; instant billing.
            </p>
          </div>

          <div class="pricing-grid pricing-grid--2col">

            <!-- Groinn Standard Plan: ₹1000/month (Yearly: ₹12,000) -->
            <article class="pricing-card pricing-card--popular" style="max-width: 540px; margin: 0 auto; width: 100%;">
              <span class="popular-badge">All-In-One Hotel Suite</span>

              <div class="pricing-card__header">
                <h3>Groinn Hotel Suite</h3>
                <p class="pricing-card__desc">Complete software suite designed for independent hotels, boutique resorts, lodges, and restaurants.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGroinn">₹</span>
                <span class="pricing-card__amount" id="cardAmountGroinn" data-monthly="1000" data-annual="800">1000</span>
                <span class="pricing-card__period">/ month</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGroinn" data-monthly-note="Yearly: ₹12,000 / year (Billed monthly)"
                data-annual-note="Yearly: ₹9,600 / year (Save 20% Billed Annually)">
                Yearly: ₹12,000 / year (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything included in Groinn:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Front Desk &amp; Room Management</b> (Check-in/Check-out, Room grid, Housekeeping status)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Direct Booking Engine</b> (Website booking widget, calendar availability)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Restaurant &amp; Bar POS</b> (Table orders, kitchen KOT, split bills)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Guest CRM &amp; History</b> (Guest profiles, preferences, VIP tags, ID upload)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Instant GST Billing &amp; Invoicing</b> (Thermal print, email &amp; WhatsApp bills)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>RevPAR &amp; Occupancy Analytics</b> (Daily revenue, night audit, occupancy rates)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>24/7 Hospitality Support &amp; On-premise / Cloud Deployment</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--primary" href="enquire.html?plan=groinn-suite">
                Start 15-Day Free Hotel Trial <span>→</span>
              </a>
            </article>

            <!-- Groinn Enterprise / Chain Plan -->
            <article class="pricing-card" style="max-width: 540px; margin: 0 auto; width: 100%;">
              <div class="pricing-card__header">
                <h3>Multi-Property &amp; Chains</h3>
                <p class="pricing-card__desc">For hotel chains, luxury resort groups, and franchisees requiring centralized control &amp; channel manager sync.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__amount" style="font-size: 2.1rem; line-height: 1.2;">Custom Quote</span>
              </div>
              <p class="pricing-card__billing-note">Tailored per-property pricing &amp; volume tiers</p>

              <p class="pricing-card__features-title">Enterprise capabilities:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Central Reservation System (CRS)</b> across multi-properties</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>OTA Channel Manager 2-way sync (MakeMyTrip, Booking.com, Agoda)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Centralized Inventory &amp; Procurement across properties</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Keycard door lock integrations (Vingcard, Salto)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom accounting ERP integration &amp; consolidated ledger</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated Hospitality Solution Architect &amp; 99.9% uptime SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=groinn-enterprise">
                Contact Hospitality Team <span>→</span>
              </a>
            </article>

          </div>

        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- PRODUCT 3: GROLOG (Call Log Management Software)                          -->
      <!-- ========================================================================= -->
      <section class="pricing-section" id="grolog-pricing" style="padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.08);">
        <div class="section-wrap">

          <div class="pricing-product-header" style="text-align: center; margin-bottom: 2.2rem;">
            <p class="eyebrow" style="color: var(--blue, #2a6df4); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 0.4rem;">CALL LOG MANAGEMENT SOFTWARE</p>
            <h2 style="font-size: 2.2rem; margin: 0 0 0.5rem;">
              {ring_grolog} Call Log Management Pricing
            </h2>
            <p style="color: var(--muted, #94a3b8); max-width: 650px; margin: 0 auto; font-size: 1rem;">
              Smart Call Tracking, Mobile SIM Sync, AI Transcription &amp; Telephony Analytics for high-performing sales &amp; support teams.
            </p>
          </div>

          <div class="pricing-grid">

            <!-- Tier 1: Up to 5 Users (₹299/user/mo, Yearly: ₹3,588) -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>Up to 5 Users</h3>
                <p class="pricing-card__desc">Ideal for small sales desks, boutique agencies, and startups tracking incoming &amp; outgoing client calls.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGrolog1">₹</span>
                <span class="pricing-card__amount" id="cardAmountGrolog1" data-monthly="299" data-annual="239">299</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGrolog1" data-monthly-note="Yearly: ₹3,588 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹2,868 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹3,588 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">What's included:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>SIM &amp; Mobile Call Sync</b> (Up to 5 devices/SIMs)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Incoming, outgoing &amp; missed call tracking</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Automated call duration &amp; talk-time logging</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Daily agent activity &amp; productivity reports</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Client contact search &amp; 30-day call history</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Email &amp; standard ticketing support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grolog-5users">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Tier 2: 5 - 10 Users (₹249/user/mo, Yearly: ₹2,988) (Most Popular) -->
            <article class="pricing-card pricing-card--popular">
              <span class="popular-badge">Most Popular</span>

              <div class="pricing-card__header">
                <h3>5 – 10 Users</h3>
                <p class="pricing-card__desc">For fast-growing sales teams needing missed call follow-up, recording sync, and agent leaderboards.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGrolog2">₹</span>
                <span class="pricing-card__amount" id="cardAmountGrolog2" data-monthly="249" data-annual="199">249</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGrolog2" data-monthly-note="Yearly: ₹2,988 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹2,388 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹2,988 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in Up to 5 Users, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>5 to 10 company SIM &amp; smartphone connections</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Automatic missed call alerts &amp; callback queue</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Secure cloud call recording sync</b> &amp; playback</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Follow-up management &amp; automated task reminders</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Agent talk-time, idle-time &amp; team performance dashboard</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Priority WhatsApp &amp; phone desk support</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--primary" href="enquire.html?plan=grolog-10users">
                Start 15-Day Free Trial <span>→</span>
              </a>
            </article>

            <!-- Tier 3: 10 - 25 Users (₹199/user/mo, Yearly: ₹2,388) -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>10 – 25 Users</h3>
                <p class="pricing-card__desc">For larger telecalling operations, customer service centers, and high-volume outbound campaigns.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__currency" id="cardCurrencyGrolog3">₹</span>
                <span class="pricing-card__amount" id="cardAmountGrolog3" data-monthly="199" data-annual="159">199</span>
                <span class="pricing-card__period">/ user / mo</span>
              </div>
              <p class="pricing-card__billing-note" id="cardNoteGrolog3" data-monthly-note="Yearly: ₹2,388 / user / yr (Billed monthly)"
                data-annual-note="Yearly: ₹1,908 / user / yr (Save 20% Billed Annually)">
                Yearly: ₹2,388 / user / yr (Billed monthly)
              </p>

              <p class="pricing-card__features-title">Everything in 5–10 Users, plus:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>10 to 25 active agents &amp; multi-SIM tracking</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>AI call summary &amp; sentiment analysis</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Automated CRM lead creation &amp; field mapping</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Supervisor live call monitoring &amp; barge-in capability</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom webhook integrations &amp; REST API access</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated telecommunication support specialist</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grolog-25users">
                Start Free Trial <span>→</span>
              </a>
            </article>

            <!-- Tier 4: 25+ Users / Enterprise Custom -->
            <article class="pricing-card">
              <div class="pricing-card__header">
                <h3>25+ Users / Enterprise</h3>
                <p class="pricing-card__desc">For contact centers, multi-city branches, and enterprises needing IVR sync &amp; private cloud telephony.</p>
              </div>

              <div class="pricing-card__price-box">
                <span class="pricing-card__amount" style="font-size: 2.1rem; line-height: 1.2;">Custom Quote</span>
              </div>
              <p class="pricing-card__billing-note">Volume tiered pricing &amp; enterprise SLA</p>

              <p class="pricing-card__features-title">Enterprise telephony:</p>
              <ul class="pricing-card__features">
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span><b>Dedicated Telephony Gateway &amp; PBX / Cloud IVR sync</b></span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Unlimited historical call audio archiving &amp; custom retention</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Multi-branch privacy boundaries &amp; role-based access</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Custom CRM 2-way dialer sync (Salesforce, Zoho, HubSpot)</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Enterprise security audits &amp; custom data localization</span>
                </li>
                <li>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>Dedicated Senior Telephony Engineer &amp; 99.9% uptime SLA</span>
                </li>
              </ul>

              <a class="pricing-card__btn pricing-card__btn--secondary" href="enquire.html?plan=grolog-enterprise">
                Contact Enterprise Team <span>→</span>
              </a>
            </article>

          </div>

          <!-- Trust Badges Strip -->'''

if old_pricing_details_start in content:
    content = content.replace(old_pricing_details_start, new_pricing_details, 1)
    print("Pricing details container replaced with Grohrms, Groinn, and Grolog!")
else:
    print("ERROR: old_pricing_details_start not found!")

# 4. Update the Script (CurrencyRates, RenderPricing, Event Handlers)
# Find from 'const FORM_ENDPOINT' down to before 'Dynamic Copyright Year'
old_script_block_start = '      const FORM_ENDPOINT = "https://formsubmit.app/f/fhydgy6ynj";'
old_script_block_end = '      // Dynamic Copyright Year'

new_script_block = '''      const FORM_ENDPOINT = "https://formsubmit.app/f/fhydgy6ynj";
      const STEP_2_ENABLED = false; // Step 2 (Company Details) temporarily disabled per request; Step 1 unlocks pricing directly

      // Comprehensive Multi-Currency Rates for Grohrms, Groinn, and Grolog
      const currencyRates = {
        INR: {
          code: 'INR',
          symbol: '₹',
          name: 'Indian Rupee',
          countryName: 'India',
          taxNoteMonthly: 'Billed monthly (excl. GST)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 15, annual: 12 },
            standard: { monthly: 30, annual: 24 },
            prime: { monthly: 60, annual: 48 }
          },
          groinn: {
            monthly: 1000,
            annual: 800
          },
          grolog: {
            tier1: { monthly: 299, annual: 239 },
            tier2: { monthly: 249, annual: 199 },
            tier3: { monthly: 199, annual: 159 }
          },
          addons: {
            whatsapp: '₹999',
            biometric: '₹1,499',
            copilot: '₹1,299',
            telephony: '₹1,999'
          }
        },
        USD: {
          code: 'USD',
          symbol: '$',
          name: 'US Dollar',
          countryName: 'United States / Global',
          taxNoteMonthly: 'Billed monthly (excl. local taxes)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.25, annual: 0.20 },
            standard: { monthly: 0.50, annual: 0.40 },
            prime: { monthly: 1.00, annual: 0.80 }
          },
          groinn: {
            monthly: 15.00,
            annual: 12.00
          },
          grolog: {
            tier1: { monthly: 4.00, annual: 3.20 },
            tier2: { monthly: 3.50, annual: 2.80 },
            tier3: { monthly: 2.80, annual: 2.20 }
          },
          addons: {
            whatsapp: '$14',
            biometric: '$20',
            copilot: '$18',
            telephony: '$25'
          }
        },
        GBP: {
          code: 'GBP',
          symbol: '£',
          name: 'British Pound',
          countryName: 'United Kingdom',
          taxNoteMonthly: 'Billed monthly (excl. VAT)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.20, annual: 0.16 },
            standard: { monthly: 0.40, annual: 0.32 },
            prime: { monthly: 0.80, annual: 0.64 }
          },
          groinn: {
            monthly: 12.00,
            annual: 9.60
          },
          grolog: {
            tier1: { monthly: 3.20, annual: 2.50 },
            tier2: { monthly: 2.80, annual: 2.20 },
            tier3: { monthly: 2.20, annual: 1.80 }
          },
          addons: {
            whatsapp: '£11',
            biometric: '£16',
            copilot: '£14',
            telephony: '£20'
          }
        },
        EUR: {
          code: 'EUR',
          symbol: '€',
          name: 'Euro',
          countryName: 'European Union',
          taxNoteMonthly: 'Billed monthly (excl. VAT)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.22, annual: 0.18 },
            standard: { monthly: 0.45, annual: 0.36 },
            prime: { monthly: 0.90, annual: 0.72 }
          },
          groinn: {
            monthly: 14.00,
            annual: 11.20
          },
          grolog: {
            tier1: { monthly: 3.60, annual: 2.90 },
            tier2: { monthly: 3.10, annual: 2.50 },
            tier3: { monthly: 2.50, annual: 2.00 }
          },
          addons: {
            whatsapp: '€12',
            biometric: '€18',
            copilot: '€16',
            telephony: '€22'
          }
        },
        AED: {
          code: 'AED',
          symbol: 'AED ',
          name: 'UAE Dirham',
          countryName: 'United Arab Emirates',
          taxNoteMonthly: 'Billed monthly (excl. VAT)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 1.00, annual: 0.80 },
            standard: { monthly: 2.00, annual: 1.60 },
            prime: { monthly: 4.00, annual: 3.20 }
          },
          groinn: {
            monthly: 55.00,
            annual: 44.00
          },
          grolog: {
            tier1: { monthly: 15.00, annual: 12.00 },
            tier2: { monthly: 12.00, annual: 10.00 },
            tier3: { monthly: 10.00, annual: 8.00 }
          },
          addons: {
            whatsapp: 'AED 50',
            biometric: 'AED 75',
            copilot: 'AED 65',
            telephony: 'AED 99'
          }
        },
        SGD: {
          code: 'SGD',
          symbol: 'S$',
          name: 'Singapore Dollar',
          countryName: 'Singapore',
          taxNoteMonthly: 'Billed monthly (excl. GST)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.35, annual: 0.28 },
            standard: { monthly: 0.70, annual: 0.56 },
            prime: { monthly: 1.40, annual: 1.12 }
          },
          groinn: {
            monthly: 20.00,
            annual: 16.00
          },
          grolog: {
            tier1: { monthly: 5.50, annual: 4.40 },
            tier2: { monthly: 4.60, annual: 3.70 },
            tier3: { monthly: 3.70, annual: 3.00 }
          },
          addons: {
            whatsapp: 'S$18',
            biometric: 'S$26',
            copilot: 'S$22',
            telephony: 'S$34'
          }
        },
        AUD: {
          code: 'AUD',
          symbol: 'A$',
          name: 'Australian Dollar',
          countryName: 'Australia',
          taxNoteMonthly: 'Billed monthly (excl. GST)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.40, annual: 0.32 },
            standard: { monthly: 0.80, annual: 0.64 },
            prime: { monthly: 1.60, annual: 1.28 }
          },
          groinn: {
            monthly: 22.00,
            annual: 17.60
          },
          grolog: {
            tier1: { monthly: 6.00, annual: 4.80 },
            tier2: { monthly: 5.00, annual: 4.00 },
            tier3: { monthly: 4.00, annual: 3.20 }
          },
          addons: {
            whatsapp: 'A$20',
            biometric: 'A$30',
            copilot: 'A$25',
            telephony: 'A$38'
          }
        },
        CAD: {
          code: 'CAD',
          symbol: 'C$',
          name: 'Canadian Dollar',
          countryName: 'Canada',
          taxNoteMonthly: 'Billed monthly (excl. HST/PST)',
          taxNoteAnnual: 'Billed annually (Save 20%)',
          hrms: {
            basic: { monthly: 0.35, annual: 0.28 },
            standard: { monthly: 0.70, annual: 0.56 },
            prime: { monthly: 1.40, annual: 1.12 }
          },
          groinn: {
            monthly: 20.00,
            annual: 16.00
          },
          grolog: {
            tier1: { monthly: 5.50, annual: 4.40 },
            tier2: { monthly: 4.60, annual: 3.70 },
            tier3: { monthly: 3.70, annual: 3.00 }
          },
          addons: {
            whatsapp: 'C$18',
            biometric: 'C$28',
            copilot: 'C$24',
            telephony: 'C$36'
          }
        }
      };

      // State Management
      let currentCurrency = 'INR';
      let isAnnual = false;

      // DOM Elements - Navigation & Gate
      const pricingGateForm = document.getElementById('pricingGateForm');
      const pricingStep1Block = document.getElementById('pricingStep1Block');
      const pricingStep2Block = document.getElementById('pricingStep2Block');
      const pricingCountry = document.getElementById('pricingCountry');
      const pricingCurrency = document.getElementById('pricingCurrency');
      const btnSubmitStep1 = document.getElementById('btnSubmitStep1');
      const btnBackToStep1 = document.getElementById('btnBackToStep1');
      const btnEditDetails = document.getElementById('btnEditDetails');
      const pricingSubmitBtn = document.getElementById('pricingSubmitBtn');
      const pricingFormStatus = document.getElementById('pricingFormStatus');
      const pricingSuccessBanner = document.getElementById('pricingSuccessBanner');
      const pricingDetailsContainer = document.getElementById('pricingDetailsContainer');
      const step2SelectedRegion = document.getElementById('step2SelectedRegion');
      const quickCurrencySwitch = document.getElementById('quickCurrencySwitch');

      // Product Tabs
      const tabGrohrms = document.getElementById('tabGrohrms');
      const tabGroinn = document.getElementById('tabGroinn');
      const tabGrolog = document.getElementById('tabGrolog');

      // Billing Cycle Switcher
      const billingToggle = document.getElementById('billingToggle');
      const labelMonthly = document.getElementById('labelMonthly');
      const labelAnnual = document.getElementById('labelAnnual');

      // Step Indicators (Progress Bar)
      const stepIndicator1 = document.getElementById('stepIndicator1');
      const stepIndicator2 = document.getElementById('stepIndicator2');
      const stepIndicator3 = document.getElementById('stepIndicator3');
      const circleStep1 = document.getElementById('circleStep1');
      const circleStep2 = document.getElementById('circleStep2');
      const circleStep3 = document.getElementById('circleStep3');
      const stepLine1 = document.getElementById('stepLine1');
      const stepLine2 = document.getElementById('stepLine2');

      // Summary Card Elements
      const summaryCompany = document.getElementById('summaryCompany');
      const summaryEmail = document.getElementById('summaryEmail');
      const summaryCountry = document.getElementById('summaryCountry');
      const summaryCurrency = document.getElementById('summaryCurrency');

      // Grohrms Card Elements
      const cardCurrencyBasic = document.getElementById('cardCurrencyBasic');
      const cardAmountBasic = document.getElementById('cardAmountBasic');
      const cardNoteBasic = document.getElementById('cardNoteBasic');

      const cardCurrencyStandard = document.getElementById('cardCurrencyStandard');
      const cardAmountStandard = document.getElementById('cardAmountStandard');
      const cardNoteStandard = document.getElementById('cardNoteStandard');

      const cardCurrencyPrime = document.getElementById('cardCurrencyPrime');
      const cardAmountPrime = document.getElementById('cardAmountPrime');
      const cardNotePrime = document.getElementById('cardNotePrime');

      // Groinn Card Elements
      const cardCurrencyGroinn = document.getElementById('cardCurrencyGroinn');
      const cardAmountGroinn = document.getElementById('cardAmountGroinn');
      const cardNoteGroinn = document.getElementById('cardNoteGroinn');

      // Grolog Card Elements
      const cardCurrencyGrolog1 = document.getElementById('cardCurrencyGrolog1');
      const cardAmountGrolog1 = document.getElementById('cardAmountGrolog1');
      const cardNoteGrolog1 = document.getElementById('cardNoteGrolog1');

      const cardCurrencyGrolog2 = document.getElementById('cardCurrencyGrolog2');
      const cardAmountGrolog2 = document.getElementById('cardAmountGrolog2');
      const cardNoteGrolog2 = document.getElementById('cardNoteGrolog2');

      const cardCurrencyGrolog3 = document.getElementById('cardCurrencyGrolog3');
      const cardAmountGrolog3 = document.getElementById('cardAmountGrolog3');
      const cardNoteGrolog3 = document.getElementById('cardNoteGrolog3');

      // Add-on Price Elements
      const addonWhatsapp = document.getElementById('addonWhatsappPrice');
      const addonBiometric = document.getElementById('addonBiometricPrice');
      const addonCopilot = document.getElementById('addonCopilotPrice');
      const addonTelephony = document.getElementById('addonTelephonyPrice');

      // Calculator Elements
      const employeeSlider = document.getElementById('employeeSlider');
      const sliderValue = document.getElementById('sliderValue');
      const calcStarterCost = document.getElementById('calcStarterCost');
      const calcStarterPeriod = document.getElementById('calcStarterPeriod');
      const calcProCost = document.getElementById('calcProCost');
      const calcProPeriod = document.getElementById('calcProPeriod');
      const calcEnterpriseCost = document.getElementById('calcEnterpriseCost');
      const calcEnterprisePeriod = document.getElementById('calcEnterprisePeriod');

      // Format Numbers
      function formatNum(val) {
        if (typeof val === 'number') {
          return Number.isInteger(val) ? val.toLocaleString('en-IN') : val.toFixed(2);
        }
        return val;
      }

      // Render Pricing function
      function renderPricing() {
        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        // 1. Grohrms Plans (Basic ₹15, Standard ₹30, Prime ₹60)
        const hrmsBasicMonthly = cur.hrms.basic.monthly;
        const hrmsBasicAnnual = cur.hrms.basic.annual;
        const hrmsBasicActive = isAnnual ? hrmsBasicAnnual : hrmsBasicMonthly;

        const hrmsStdMonthly = cur.hrms.standard.monthly;
        const hrmsStdAnnual = cur.hrms.standard.annual;
        const hrmsStdActive = isAnnual ? hrmsStdAnnual : hrmsStdMonthly;

        const hrmsPrimeMonthly = cur.hrms.prime.monthly;
        const hrmsPrimeAnnual = cur.hrms.prime.annual;
        const hrmsPrimeActive = isAnnual ? hrmsPrimeAnnual : hrmsPrimeMonthly;

        if (cardCurrencyBasic) cardCurrencyBasic.textContent = sym;
        if (cardAmountBasic) cardAmountBasic.textContent = formatNum(hrmsBasicActive);
        if (cardNoteBasic) {
          const yearlyTotal = formatNum(hrmsBasicActive * 12);
          cardNoteBasic.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyStandard) cardCurrencyStandard.textContent = sym;
        if (cardAmountStandard) cardAmountStandard.textContent = formatNum(hrmsStdActive);
        if (cardNoteStandard) {
          const yearlyTotal = formatNum(hrmsStdActive * 12);
          cardNoteStandard.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyPrime) cardCurrencyPrime.textContent = sym;
        if (cardAmountPrime) cardAmountPrime.textContent = formatNum(hrmsPrimeActive);
        if (cardNotePrime) {
          const yearlyTotal = formatNum(hrmsPrimeActive * 12);
          cardNotePrime.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        // 2. Groinn Hotel Management Plan (₹1000/month, ₹12,000/year; Annual save 20%: ₹800/mo, ₹9,600/year)
        const groinnMonthly = cur.groinn.monthly;
        const groinnAnnual = cur.groinn.annual;
        const groinnActive = isAnnual ? groinnAnnual : groinnMonthly;

        if (cardCurrencyGroinn) cardCurrencyGroinn.textContent = sym;
        if (cardAmountGroinn) cardAmountGroinn.textContent = formatNum(groinnActive);
        if (cardNoteGroinn) {
          const yearlyTotal = formatNum(groinnActive * 12);
          cardNoteGroinn.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / year (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / year (Billed monthly)`;
        }

        // 3. Grolog Call Log Management Plans
        // Tier 1 (Up to 5 Users): ₹299 / user / mo, Yearly: ₹3,588 (Annual Save 20%: ₹239 / mo, ₹2,868/yr)
        // Tier 2 (5-10 Users): ₹249 / user / mo, Yearly: ₹2,988 (Annual Save 20%: ₹199 / mo, ₹2,388/yr)
        // Tier 3 (10-25 Users): ₹199 / user / mo, Yearly: ₹2,388 (Annual Save 20%: ₹159 / mo, ₹1,908/yr)
        const grolog1Monthly = cur.grolog.tier1.monthly;
        const grolog1Annual = cur.grolog.tier1.annual;
        const grolog1Active = isAnnual ? grolog1Annual : grolog1Monthly;

        const grolog2Monthly = cur.grolog.tier2.monthly;
        const grolog2Annual = cur.grolog.tier2.annual;
        const grolog2Active = isAnnual ? grolog2Annual : grolog2Monthly;

        const grolog3Monthly = cur.grolog.tier3.monthly;
        const grolog3Annual = cur.grolog.tier3.annual;
        const grolog3Active = isAnnual ? grolog3Annual : grolog3Monthly;

        if (cardCurrencyGrolog1) cardCurrencyGrolog1.textContent = sym;
        if (cardAmountGrolog1) cardAmountGrolog1.textContent = formatNum(grolog1Active);
        if (cardNoteGrolog1) {
          const yearlyTotal = formatNum(grolog1Active * 12);
          cardNoteGrolog1.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog2) cardCurrencyGrolog2.textContent = sym;
        if (cardAmountGrolog2) cardAmountGrolog2.textContent = formatNum(grolog2Active);
        if (cardNoteGrolog2) {
          const yearlyTotal = formatNum(grolog2Active * 12);
          cardNoteGrolog2.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        if (cardCurrencyGrolog3) cardCurrencyGrolog3.textContent = sym;
        if (cardAmountGrolog3) cardAmountGrolog3.textContent = formatNum(grolog3Active);
        if (cardNoteGrolog3) {
          const yearlyTotal = formatNum(grolog3Active * 12);
          cardNoteGrolog3.textContent = isAnnual
            ? `Yearly: ${sym}${yearlyTotal} / user / yr (Save 20% Billed Annually)`
            : `Yearly: ${sym}${yearlyTotal} / user / yr (Billed monthly)`;
        }

        // 4. Add-ons
        if (addonWhatsapp) addonWhatsapp.textContent = cur.addons.whatsapp;
        if (addonBiometric) addonBiometric.textContent = cur.addons.biometric;
        if (addonCopilot) addonCopilot.textContent = cur.addons.copilot;
        if (addonTelephony) addonTelephony.textContent = cur.addons.telephony;

        // 5. Calculator
        updateCalculator();
      }

      // Update Calculator based on slider
      function updateCalculator() {
        if (!employeeSlider) return;
        const users = parseInt(employeeSlider.value, 10);
        if (sliderValue) sliderValue.textContent = users;

        const cur = currencyRates[currentCurrency] || currencyRates.INR;
        const sym = cur.symbol.trim();

        const basicRate = isAnnual ? cur.hrms.basic.annual : cur.hrms.basic.monthly;
        const stdRate = isAnnual ? cur.hrms.standard.annual : cur.hrms.standard.monthly;
        const primeRate = isAnnual ? cur.hrms.prime.annual : cur.hrms.prime.monthly;

        const periodLabel = isAnnual ? 'per month (billed annually)' : 'per month (billed monthly)';

        if (calcStarterCost) calcStarterCost.textContent = `${sym}${formatNum(users * basicRate)}`;
        if (calcStarterPeriod) calcStarterPeriod.textContent = periodLabel;

        if (calcProCost) calcProCost.textContent = `${sym}${formatNum(users * stdRate)}`;
        if (calcProPeriod) calcProPeriod.textContent = periodLabel;

        if (calcEnterpriseCost) calcEnterpriseCost.textContent = `${sym}${formatNum(users * primeRate)}`;
        if (calcEnterprisePeriod) calcEnterprisePeriod.textContent = periodLabel;
      }

      if (employeeSlider) {
        employeeSlider.addEventListener('input', updateCalculator);
      }

      // 1. Country & Currency Selector Linking
      if (pricingCountry) {
        pricingCountry.addEventListener('change', () => {
          const map = {
            IN: 'INR', US: 'USD', GB: 'GBP', EU: 'EUR',
            AE: 'AED', SG: 'SGD', AU: 'AUD', CA: 'CAD', GLOBAL: 'USD'
          };
          const mapped = map[pricingCountry.value] || 'INR';
          if (pricingCurrency) pricingCurrency.value = mapped;
          currentCurrency = mapped;
          if (quickCurrencySwitch) quickCurrencySwitch.value = mapped;
        });
      }

      if (pricingCurrency) {
        pricingCurrency.addEventListener('change', () => {
          currentCurrency = pricingCurrency.value;
          if (quickCurrencySwitch) quickCurrencySwitch.value = currentCurrency;
        });
      }

      if (quickCurrencySwitch) {
        quickCurrencySwitch.addEventListener('change', () => {
          currentCurrency = quickCurrencySwitch.value;
          if (pricingCurrency) pricingCurrency.value = currentCurrency;
          const curData = currencyRates[currentCurrency] || currencyRates.INR;
          if (summaryCurrency) summaryCurrency.textContent = curData.code + ' - ' + curData.symbol.trim();
          if (summaryCountry) summaryCountry.textContent = curData.countryName;
          renderPricing();
        });
      }

      // 2. Billing Toggle Handler
      if (billingToggle) {
        billingToggle.addEventListener('change', () => {
          isAnnual = billingToggle.checked;
          if (labelMonthly) labelMonthly.classList.toggle('active', !isAnnual);
          if (labelAnnual) labelAnnual.classList.toggle('active', isAnnual);
          renderPricing();
        });
      }

      // 3. Product Tabs Switching
      function setActiveProductTab(activeTabId) {
        [tabGrohrms, tabGroinn, tabGrolog].forEach(tab => {
          if (!tab) return;
          const isActive = tab.id === activeTabId;
          tab.classList.toggle('active', isActive);
          tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
      }

      if (tabGrohrms) {
        tabGrohrms.addEventListener('click', (e) => {
          setActiveProductTab('tabGrohrms');
        });
      }
      if (tabGroinn) {
        tabGroinn.addEventListener('click', (e) => {
          setActiveProductTab('tabGroinn');
        });
      }
      if (tabGrolog) {
        tabGrolog.addEventListener('click', (e) => {
          setActiveProductTab('tabGrolog');
        });
      }

      // 4. Step 1 Submit Handler (Country & Currency -> Directly Unlocks Pricing)
      if (btnSubmitStep1) {
        btnSubmitStep1.addEventListener('click', () => {
          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
          const currencyVal = pricingCurrency ? pricingCurrency.value : 'INR';
          currentCurrency = currencyVal;

          const curData = currencyRates[currentCurrency] || currencyRates.INR;
          const countryOptText = pricingCountry.options[pricingCountry.selectedIndex]?.text || countryVal;

          if (STEP_2_ENABLED && pricingStep2Block) {
            // If Step 2 were enabled, advance to Step 2
            if (pricingStep1Block) pricingStep1Block.style.display = 'none';
            pricingStep2Block.style.display = 'block';
            if (step2SelectedRegion) {
              step2SelectedRegion.textContent = `${countryOptText} · ${currentCurrency} (${curData.symbol.trim()})`;
            }
          } else {
            // Step 2 is disabled: immediately unlock pricing details!
            if (summaryCompany) summaryCompany.textContent = 'GroSuite Products';
            if (summaryCountry) summaryCountry.textContent = curData.countryName;
            if (summaryCurrency) summaryCurrency.textContent = curData.code + ' - ' + curData.symbol.trim();
            if (quickCurrencySwitch) quickCurrencySwitch.value = currentCurrency;

            // Update Progress Bar
            if (stepIndicator1) {
              stepIndicator1.classList.remove('active');
              stepIndicator1.classList.add('completed');
            }
            if (circleStep1) circleStep1.innerHTML = '✓';
            if (stepLine1) stepLine1.classList.add('completed');
            if (stepIndicator2) {
              stepIndicator2.classList.remove('active');
              stepIndicator2.classList.add('completed');
            }
            if (circleStep2) circleStep2.innerHTML = '✓';
            if (stepLine2) stepLine2.classList.add('completed');
            if (stepIndicator3) stepIndicator3.classList.add('active', 'completed');
            if (circleStep3) circleStep3.innerHTML = '✓';

            // Hide form, reveal banner and pricing container
            if (pricingGateForm) pricingGateForm.style.display = 'none';
            if (pricingSuccessBanner) pricingSuccessBanner.style.display = 'flex';
            if (pricingDetailsContainer) {
              pricingDetailsContainer.style.display = 'block';
              pricingDetailsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }

            renderPricing();
          }
        });
      }

      // 5. Back to Step 1 Button
      if (btnBackToStep1) {
        btnBackToStep1.addEventListener('click', () => {
          if (pricingStep2Block) pricingStep2Block.style.display = 'none';
          if (pricingStep1Block) pricingStep1Block.style.display = 'block';
          pricingGateForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }

      // 6. Edit Details Button (Change Country/Currency from banner)
      if (btnEditDetails) {
        btnEditDetails.addEventListener('click', () => {
          if (pricingGateForm) pricingGateForm.style.display = 'block';
          if (pricingStep1Block) pricingStep1Block.style.display = 'block';
          if (pricingStep2Block) pricingStep2Block.style.display = 'none';
          if (pricingSuccessBanner) pricingSuccessBanner.style.display = 'none';
          pricingGateForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }

      // 7. Step 2 Form Submission Handler (if re-enabled in the future)
      if (pricingGateForm) {
        pricingGateForm.addEventListener('submit', async (e) => {
          e.preventDefault();
          if (!STEP_2_ENABLED) return;

          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
          const currencyVal = pricingCurrency ? pricingCurrency.value : 'INR';
          const companyVal = document.getElementById('pricingCompanyName')?.value.trim() || 'GroSuite Client';
          const nameVal = document.getElementById('pricingFullName')?.value.trim() || 'Client';
          const emailVal = document.getElementById('pricingWorkEmail')?.value.trim();
          const phoneVal = document.getElementById('pricingPhone')?.value.trim();
          const teamVal = document.getElementById('pricingTeamSize')?.value || '1-10';
          const interestVal = document.getElementById('pricingInterest')?.value || 'All Solutions';

          currentCurrency = currencyVal;
          const curData = currencyRates[currentCurrency] || currencyRates.INR;

          if (summaryCompany) summaryCompany.textContent = companyVal;
          if (summaryCountry) summaryCountry.textContent = curData.countryName;
          if (summaryCurrency) summaryCurrency.textContent = curData.code + ' - ' + curData.symbol.trim();
          if (quickCurrencySwitch) quickCurrencySwitch.value = currentCurrency;

          pricingGateForm.style.display = 'none';
          if (pricingSuccessBanner) pricingSuccessBanner.style.display = 'flex';
          if (pricingDetailsContainer) {
            pricingDetailsContainer.style.display = 'block';
            pricingDetailsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }

          renderPricing();
        });
      }

'''

# Find the slice to replace
start_idx = content.find(old_script_block_start)
end_idx = content.find(old_script_block_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_script_block + content[end_idx:]
    print("Script block replaced successfully!")
else:
    print(f"ERROR: Script slice not found! start_idx={start_idx}, end_idx={end_idx}")

with open(PRICING_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("pricing.html written successfully!")

# 5. Add .pricing-grid--2col CSS rule to css/style.css if not present
with open(STYLE_FILE, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.pricing-grid--2col' not in css_content:
    extra_css = '''
/* 2-Column Centered Grid for Groinn & Dual Offerings */
.pricing-grid--2col {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 520px));
  justify-content: center;
  gap: 1.75rem;
}

@media (max-width: 960px) {
  .pricing-grid--2col {
    grid-template-columns: 1fr;
  }
}
'''
    css_content += extra_css
    with open(STYLE_FILE, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Added .pricing-grid--2col to css/style.css")
else:
    print(".pricing-grid--2col already present in css/style.css")
