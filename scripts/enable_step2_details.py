import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Uncomment Progress Indicator
old_progress = '''            <!-- Step Progress Indicator -->
            <!-- <div class="pricing-step-progress" id="pricingStepProgress">
              <div class="pricing-step-item active" id="stepIndicator1">
                <span class="step-circle" id="circleStep1">1</span>
                <span class="step-text">1. Choose Country &amp; Currency</span>
              </div>
              <div class="pricing-step-line" id="stepLine1"></div>
              <div class="pricing-step-item" id="stepIndicator2">
                <span class="step-circle" id="circleStep2">2</span>
                <span class="step-text">2. Company &amp; Contact Details</span>
              </div>
              <div class="pricing-step-line" id="stepLine2"></div>
              <div class="pricing-step-item" id="stepIndicator3">
                <span class="step-circle" id="circleStep3">3</span>
                <span class="step-text">3. Price Details</span>
              </div>
            </div> -->'''

new_progress = '''            <!-- Step Progress Indicator -->
            <div class="pricing-step-progress" id="pricingStepProgress">
              <div class="pricing-step-item active" id="stepIndicator1">
                <span class="step-circle" id="circleStep1">1</span>
                <span class="step-text">1. Choose Country &amp; Currency</span>
              </div>
              <div class="pricing-step-line" id="stepLine1"></div>
              <div class="pricing-step-item" id="stepIndicator2">
                <span class="step-circle" id="circleStep2">2</span>
                <span class="step-text">2. Company &amp; Contact Details</span>
              </div>
              <div class="pricing-step-line" id="stepLine2"></div>
              <div class="pricing-step-item" id="stepIndicator3">
                <span class="step-circle" id="circleStep3">3</span>
                <span class="step-text">3. Price Details</span>
              </div>
            </div>'''

assert old_progress in content, 'old_progress not found'
content = content.replace(old_progress, new_progress)

# 2. Uncomment step badge in Step 1
old_step1_badge = '''                <div class="pricing-gate-header">
                  <!-- <span class="pricing-gate-step-badge">STEP 1 OF 2</span> -->'''
new_step1_badge = '''                <div class="pricing-gate-header">
                  <span class="pricing-gate-step-badge">STEP 1 OF 2</span>'''
assert old_step1_badge in content, 'old_step1_badge not found'
content = content.replace(old_step1_badge, new_step1_badge)

# 3. Update Step 1 submit button text & note
old_step1_btn = '''                <!-- Submit Step 1 Button (Directly unlocks pricing while Step 2 is temporarily disabled) -->
                <div class="pricing-gate-actions">
                  <button type="button" id="btnSubmitStep1" class="btn-pricing-submit">
                    <span>View Pricing Plans</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    Country &amp; Currency choice configures your transparent billing rates instantly.
                  </p>
                </div>'''

new_step1_btn = '''                <!-- Submit Step 1 Button -->
                <div class="pricing-gate-actions">
                  <button type="button" id="btnSubmitStep1" class="btn-pricing-submit">
                    <span>Continue to Step 2</span>
                    <span class="btn-arrow" aria-hidden="true">→</span>
                  </button>
                  <p class="pricing-gate-privacy">
                    Step 1 of 2: Country &amp; Currency choice configures your billing rates.
                  </p>
                </div>'''
assert old_step1_btn in content, 'old_step1_btn not found'
content = content.replace(old_step1_btn, new_step1_btn)

# 4. Uncomment Step 2 block and make required fields required
pattern_step2 = r'<!-- STEP 2: Company & Contact Details Block \(Disabled / commented out per request - can be re-enabled anytime\)\s+<div id="pricingStep2Block".*?</div>\s+-->\s+'
match = re.search(pattern_step2, content, re.DOTALL)
assert match, 'pattern_step2 not matched'

step2_html = '''              <!-- STEP 2: Company & Contact Details Block (Hidden initially) -->
              <div id="pricingStep2Block" class="pricing-step-container" style="display: none;">
                <div class="pricing-gate-header">
                  <span class="pricing-gate-step-badge">STEP 2 OF 2</span>
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
                      <input type="text" id="pricingCompanyName" name="company_name" class="pricing-input" placeholder="e.g. Acme Technologies" required>
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingFullName">Your Full Name *</label>
                      <input type="text" id="pricingFullName" name="full_name" class="pricing-input" placeholder="e.g. Rahul Sharma" required>
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingWorkEmail">Work Email *</label>
                      <input type="email" id="pricingWorkEmail" name="work_email" class="pricing-input" placeholder="e.g. rahul@company.com" required>
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingPhone">Phone / WhatsApp Number *</label>
                      <input type="tel" id="pricingPhone" name="phone" class="pricing-input" placeholder="e.g. +91 98765 43210" required>
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
'''

content = content[:match.start()] + step2_html + content[match.end():]

# 5. Enable STEP_2_ENABLED in JS
old_step2_flag = 'const STEP_2_ENABLED = false; // Step 2 (Company Details) temporarily disabled per request; Step 1 unlocks pricing directly'
new_step2_flag = 'const STEP_2_ENABLED = true; // Step 2 (Company & Contact Details) enabled'
assert old_step2_flag in content, 'old_step2_flag not found'
content = content.replace(old_step2_flag, new_step2_flag)

# 6. Update Step 1 handler, BackToStep1, EditDetails, and Form Submit handlers
old_handlers = '''      // 4. Step 1 Submit Handler (Country & Currency -> Directly Unlocks Pricing)
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
      }'''

new_handlers = '''      // 4. Step 1 Submit Handler (Country & Currency -> Advance to Step 2)
      if (btnSubmitStep1) {
        btnSubmitStep1.addEventListener('click', () => {
          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
          const currencyVal = pricingCurrency ? pricingCurrency.value : 'INR';
          currentCurrency = currencyVal;

          const curData = currencyRates[currentCurrency] || currencyRates.INR;
          const countryOptText = pricingCountry.options[pricingCountry.selectedIndex]?.text || countryVal;

          if (STEP_2_ENABLED && pricingStep2Block) {
            // Advance to Step 2
            if (pricingStep1Block) pricingStep1Block.style.display = 'none';
            pricingStep2Block.style.display = 'block';
            if (step2SelectedRegion) {
              step2SelectedRegion.textContent = `${countryOptText} · ${currentCurrency} (${curData.symbol.trim()})`;
            }

            if (stepIndicator1) {
              stepIndicator1.classList.remove('active');
              stepIndicator1.classList.add('completed');
            }
            if (circleStep1) circleStep1.innerHTML = '✓';
            if (stepLine1) stepLine1.classList.add('completed');
            if (stepIndicator2) stepIndicator2.classList.add('active');

            pricingStep2Block.scrollIntoView({ behavior: 'smooth', block: 'start' });
          } else {
            // Fallback if Step 2 is ever disabled
            if (summaryCompany) summaryCompany.textContent = 'GroSuite Products';
            if (summaryCountry) summaryCountry.textContent = curData.countryName;
            if (summaryCurrency) summaryCurrency.textContent = curData.code + ' - ' + curData.symbol.trim();
            if (quickCurrencySwitch) quickCurrencySwitch.value = currentCurrency;

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

          if (stepIndicator2) stepIndicator2.classList.remove('active');
          if (stepLine1) stepLine1.classList.remove('completed');
          if (stepIndicator1) {
            stepIndicator1.classList.remove('completed');
            stepIndicator1.classList.add('active');
          }
          if (circleStep1) circleStep1.textContent = '1';

          pricingGateForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }

      // 6. Edit Details Button (Change Country/Currency from banner)
      if (btnEditDetails) {
        btnEditDetails.addEventListener('click', () => {
          if (pricingGateForm) pricingGateForm.style.display = 'block';
          if (pricingStep2Block) pricingStep2Block.style.display = 'none';
          if (pricingStep1Block) pricingStep1Block.style.display = 'block';
          if (pricingSuccessBanner) pricingSuccessBanner.style.display = 'none';

          if (stepIndicator3) stepIndicator3.classList.remove('active', 'completed');
          if (stepIndicator2) stepIndicator2.classList.remove('active', 'completed');
          if (stepIndicator1) {
            stepIndicator1.classList.remove('completed');
            stepIndicator1.classList.add('active');
          }
          if (circleStep1) circleStep1.textContent = '1';
          if (circleStep2) circleStep2.textContent = '2';
          if (circleStep3) circleStep3.textContent = '3';
          if (stepLine1) stepLine1.classList.remove('completed');
          if (stepLine2) stepLine2.classList.remove('completed');

          pricingGateForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }

      // 7. Step 2 Form Submission Handler (Company Details -> Reveal Pricing)
      if (pricingGateForm) {
        pricingGateForm.addEventListener('submit', async (e) => {
          e.preventDefault();

          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
          const currencyVal = pricingCurrency ? pricingCurrency.value : 'INR';
          const companyVal = document.getElementById('pricingCompanyName')?.value.trim();
          const nameVal = document.getElementById('pricingFullName')?.value.trim();
          const emailVal = document.getElementById('pricingWorkEmail')?.value.trim();
          const phoneVal = document.getElementById('pricingPhone')?.value.trim();
          const teamVal = document.getElementById('pricingTeamSize')?.value;
          const interestVal = document.getElementById('pricingInterest')?.value || 'All Solutions';

          if (!companyVal || !nameVal || !emailVal || !phoneVal || !teamVal) {
            if (pricingFormStatus) {
              pricingFormStatus.style.color = '#dc2626';
              pricingFormStatus.textContent = 'Please fill in all required fields marked with *.';
            }
            return;
          }

          // Email format check
          if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(emailVal)) {
            if (pricingFormStatus) {
              pricingFormStatus.style.color = '#dc2626';
              pricingFormStatus.textContent = 'Please enter a valid work email address.';
            }
            return;
          }

          // UI Progress
          if (pricingSubmitBtn) {
            pricingSubmitBtn.disabled = true;
            pricingSubmitBtn.innerHTML = '<span>Sending Details &amp; Unlocking...</span>';
          }
          if (pricingFormStatus) {
            pricingFormStatus.style.color = '#2563eb';
            pricingFormStatus.textContent = 'Submitting your quotation request...';
          }

          currentCurrency = currencyVal;
          const curData = currencyRates[currentCurrency] || currencyRates.INR;
          const countryOptText = pricingCountry.options[pricingCountry.selectedIndex]?.text || countryVal;

          // Prepare FormData for FormSubmit.app
          const formData = new FormData();
          formData.append('_subject', `Pricing & Quotation Request - ${companyVal} (${countryVal} / ${currentCurrency})`);
          formData.append('Company Name', companyVal);
          formData.append('Contact Name', nameVal);
          formData.append('Work Email', emailVal);
          formData.append('Phone Number', phoneVal);
          formData.append('Country', countryOptText);
          formData.append('Currency', currentCurrency + ' (' + curData.symbol.trim() + ')');
          formData.append('Team Size', teamVal);
          formData.append('Solution Interest', interestVal);
          formData.append('Submission Time', new Date().toLocaleString());
          formData.append('_ts', String(Date.now()));

          // Send email notification with quotation details in background
          try {
            fetch(FORM_ENDPOINT, {
              method: 'POST',
              headers: { 'Accept': 'application/json' },
              body: formData
            }).catch(err => console.warn('Quotation submission notice:', err));
          } catch (err) {
            console.warn('Form submission notice:', err);
          }

          // Update Summary Banner
          if (summaryCompany) summaryCompany.textContent = companyVal;
          if (summaryEmail) summaryEmail.textContent = emailVal;
          if (summaryCountry) summaryCountry.textContent = curData.countryName;
          if (summaryCurrency) summaryCurrency.textContent = curData.code + ' - ' + curData.symbol.trim();
          if (quickCurrencySwitch) quickCurrencySwitch.value = currentCurrency;

          // Update Progress Indicator to Step 3 Completed
          if (stepIndicator2) {
            stepIndicator2.classList.remove('active');
            stepIndicator2.classList.add('completed');
          }
          if (circleStep2) circleStep2.innerHTML = '✓';
          if (stepLine2) stepLine2.classList.add('completed');
          if (stepIndicator3) {
            stepIndicator3.classList.add('active', 'completed');
          }
          if (circleStep3) circleStep3.innerHTML = '✓';

          // Hide Form, Show Banner, Show Price Details
          pricingGateForm.style.display = 'none';
          if (pricingSuccessBanner) pricingSuccessBanner.style.display = 'flex';
          if (pricingDetailsContainer) {
            pricingDetailsContainer.style.display = 'block';
            pricingDetailsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }

          // Render prices in chosen currency
          renderPricing();

          // Reset button
          if (pricingSubmitBtn) {
            pricingSubmitBtn.disabled = false;
            pricingSubmitBtn.innerHTML = '<span>Show Price</span> <span class="btn-arrow" aria-hidden="true">→</span>';
          }
          if (pricingFormStatus) pricingFormStatus.textContent = '';
        });
      }'''

assert old_handlers in content, 'old_handlers not found'
content = content.replace(old_handlers, new_handlers)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully enabled Step 2 in pricing.html!')
