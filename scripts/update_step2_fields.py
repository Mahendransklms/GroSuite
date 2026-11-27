with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Step 2 HTML fields
old_subblock = '''                <div class="pricing-gate-subblock">
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
                </div>'''

new_subblock = '''                <div class="pricing-gate-subblock">
                  <div class="pricing-gate-grid-2">
                    <div class="pricing-field-group">
                      <label for="pricingCompanyName">Company Name *</label>
                      <input type="text" id="pricingCompanyName" name="company_name" class="pricing-input" placeholder="e.g. Acme Technologies" required>
                    </div>
                    <div class="pricing-field-group">
                      <label for="pricingCompanyLocation">Company Location *</label>
                      <input type="text" id="pricingCompanyLocation" name="company_location" class="pricing-input" placeholder="e.g. Chennai, Tamil Nadu" required>
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
                    <div class="pricing-field-group" style="grid-column: 1 / -1;">
                      <label for="pricingInterest">Solution of Interest *</label>
                      <select id="pricingInterest" name="solution_interest" class="pricing-input pricing-select" required>
                        <option value="All GroSuite Solutions" selected>All GroSuite Solutions</option>
                        <option value="Grohrms - Smart HR &amp; Business Solutions">Grohrms - Smart HR &amp; Business Solutions</option>
                        <option value="Grolog - Call Log Management Software">Grolog - Call Log Management Software</option>
                        <option value="Grotrk - Tracking Management System">Grotrk - Tracking Management System</option>
                        <option value="Groinn - Hotel Management Software">Groinn - Hotel Management Software</option>
                        <option value="Grojew - Jewellery Management Software">Grojew - Jewellery Management Software</option>
                        <option value="Grocon - Construction Management Software">Grocon - Construction Management Software</option>
                        <option value="Grohub - Parking Management software">Grohub - Parking Management software</option>
                        <option value="Grofit - Gym Management Software">Grofit - Gym Management Software</option>
                        <option value="Gropro - Textile Billing Software">Gropro - Textile Billing Software</option>
                      </select>
                    </div>
                  </div>
                </div>'''

assert old_subblock in content, "old_subblock not found"
content = content.replace(old_subblock, new_subblock)

# 2. Update JS Form Submission Handler
old_js_submit = '''          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
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
          }'''

new_js_submit = '''          const countryVal = pricingCountry ? pricingCountry.value : 'IN';
          const currencyVal = pricingCurrency ? pricingCurrency.value : 'INR';
          const companyVal = document.getElementById('pricingCompanyName')?.value.trim();
          const locationVal = document.getElementById('pricingCompanyLocation')?.value.trim();
          const nameVal = document.getElementById('pricingFullName')?.value.trim();
          const emailVal = document.getElementById('pricingWorkEmail')?.value.trim();
          const phoneVal = document.getElementById('pricingPhone')?.value.trim();
          const teamVal = document.getElementById('pricingTeamSize')?.value;
          const interestVal = document.getElementById('pricingInterest')?.value || 'All GroSuite Solutions';

          if (!companyVal || !locationVal || !nameVal || !emailVal || !phoneVal || !teamVal || !interestVal) {
            if (pricingFormStatus) {
              pricingFormStatus.style.color = '#dc2626';
              pricingFormStatus.textContent = 'Please fill in all required fields marked with *.';
            }
            return;
          }'''

assert old_js_submit in content, "old_js_submit not found"
content = content.replace(old_js_submit, new_js_submit)

# 3. Update FormData fields
old_formdata = '''          // Prepare FormData for FormSubmit.app
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
          formData.append('_ts', String(Date.now()));'''

new_formdata = '''          // Prepare FormData for FormSubmit.app
          const formData = new FormData();
          formData.append('_subject', `Pricing & Quotation Request - ${companyVal} (${countryVal} / ${currentCurrency})`);
          formData.append('Company Name', companyVal);
          formData.append('Company Location', locationVal);
          formData.append('Contact Name', nameVal);
          formData.append('Work Email', emailVal);
          formData.append('email', emailVal);
          formData.append('_replyto', emailVal);
          formData.append('Phone Number', phoneVal);
          formData.append('Country', countryOptText);
          formData.append('Currency', currentCurrency + ' (' + curData.symbol.trim() + ')');
          formData.append('Team Size', teamVal);
          formData.append('Solution Interest', interestVal);
          formData.append('_autoresponse', 'Thank you for your pricing inquiry! The GroSuite team will review your requirements and follow up with you shortly.');
          formData.append('Submission Time', new Date().toLocaleString());
          formData.append('_ts', String(Date.now()));'''

assert old_formdata in content, "old_formdata not found"
content = content.replace(old_formdata, new_formdata)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Step 2 fields and form submission handling in pricing.html!")
