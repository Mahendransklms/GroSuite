const FORM_ENDPOINT="https://formsubmit.app/f/fhydgy6ynj";

// Keep the request below FormSubmit's approximately
// 4.5 MB total multipart request limit.
const MAX_RESUME_BYTES = 4 * 1024 * 1024;


/* ========================================
   MOBILE NAVIGATION
======================================== */

const menuToggle = document.querySelector(".nav__toggle");
const menu = document.getElementById("menu");

if (menuToggle && menu) {

  menuToggle.addEventListener("click", () => {

    const isOpen = menu.classList.toggle("open");

    menuToggle.setAttribute(
      "aria-expanded",
      String(isOpen)
    );

    menuToggle.setAttribute(
      "aria-label",
      isOpen ? "Close navigation menu" : "Open navigation menu"
    );

  });

  menu.addEventListener("click", (event) => {

    if (
      event.target instanceof Element &&
      event.target.closest("a")
    ) {

      menu.classList.remove("open");

      menuToggle.setAttribute("aria-expanded", "false");

      menuToggle.setAttribute(
        "aria-label",
        "Open navigation menu"
      );

    }

  });

  document.addEventListener("keydown", (event) => {

    if (
      event.key === "Escape" &&
      menu.classList.contains("open")
    ) {

      menu.classList.remove("open");

      menuToggle.setAttribute("aria-expanded", "false");

      menuToggle.setAttribute(
        "aria-label",
        "Open navigation menu"
      );

      menuToggle.focus();

    }

  });

}


/* ========================================
   REVEAL ANIMATIONS
======================================== */

const revealItems = document.querySelectorAll(".reveal");

const reduceMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
).matches;

if (
  reduceMotion ||
  !("IntersectionObserver" in window)
) {

  revealItems.forEach((item) => {
    item.classList.add("in");
  });

} else {

  const revealObserver = new IntersectionObserver(
    (entries, observer) => {

      entries.forEach((entry) => {

        if (entry.isIntersecting) {

          entry.target.classList.add("in");

          observer.unobserve(entry.target);

        }

      });

    },
    {
      threshold: 0.12,
      rootMargin: "0px 0px -30px 0px"
    }
  );

  revealItems.forEach((item, index) => {

    item.style.transitionDelay =
      `${(index % 5) * 55}ms`;

    revealObserver.observe(item);

  });

}


/* ========================================
   FOOTER YEAR
======================================== */

document.querySelectorAll("[data-year]").forEach((element) => {

  element.textContent = String(
    new Date().getFullYear()
  );

});


/* ========================================
   FORM STATUS MESSAGE
======================================== */

function showFormMessage(form, message, type = "") {

  let status = form.querySelector(".form-status");

  if (!status) {

    status = document.createElement("p");

    status.className = "form-status";

    status.setAttribute("role", "status");

    status.setAttribute("aria-live", "polite");

    form.appendChild(status);

  }

  status.hidden = false;

  status.textContent = message;

  status.classList.remove("success", "error");

  if (type) {
    status.classList.add(type);
  }

}


/* ========================================
   ENQUIRY MESSAGE PREFILL
======================================== */

function prefillEnquiryMessage(form) {

  const parameters = new URLSearchParams(
    window.location.search
  );

  const interest = parameters.get("interest");

  const messageField = form.querySelector(
    '[name="message"]'
  );

  if (
    interest &&
    messageField &&
    !messageField.value
  ) {

    messageField.value =
      `I'm interested in: ${interest}. ` +
      "Please contact me with more information.";

  }

}


/* ========================================
   RESUME VALIDATION
======================================== */

function validateResume(form) {

  const resumeInput = form.querySelector(
    'input[type="file"][name="attachment"]'
  );

  // Enquiry form does not have a resume field.

  if (!resumeInput) {
    return true;
  }

  if (
    !resumeInput.files ||
    resumeInput.files.length === 0
  ) {

    showFormMessage(
      form,
      "Please upload your resume.",
      "error"
    );

    resumeInput.focus();

    return false;

  }

  const file = resumeInput.files[0];

  // Validate PDF extension and MIME type.

  const isPdf =
    file.name.toLowerCase().endsWith(".pdf") &&
    (
      !file.type ||
      file.type === "application/pdf"
    );

  if (!isPdf) {

    showFormMessage(
      form,
      "Please upload your resume as a PDF file.",
      "error"
    );

    resumeInput.focus();

    return false;

  }

  // Validate maximum file size.

  if (file.size > MAX_RESUME_BYTES) {

    showFormMessage(
      form,
      "Resume file must be 4 MB or smaller.",
      "error"
    );

    resumeInput.focus();

    return false;

  }

  return true;

}


/* ========================================
   FORMSUBMIT.APP CONFIGURATION
======================================== */

document.querySelectorAll(
  "form[data-email-form]"
).forEach((form) => {

  const formType = form.dataset.emailForm;

  let isSubmitting = false;


  // Check supported form type.

  if (!["careers", "enquiry"].includes(formType)) {

    console.error(
      "Unknown form type:",
      formType
    );

    return;

  }


  // Configure the endpoint.

  form.action = FORM_ENDPOINT;

  form.method = "POST";


  // Enable multipart upload.

  form.enctype = "multipart/form-data";


  // Set spam protection timestamp.

  const timestampField = form.querySelector(
    '[name="_ts"]'
  );

  function updateTimestamp() {

    if (timestampField) {
      timestampField.value = String(Date.now());
    }

  }

  updateTimestamp();


  // Configure enquiry message.

  if (formType === "enquiry") {
    prefillEnquiryMessage(form);
  }


  /* ========================================
     FORM SUBMISSION
  ======================================== */

  form.addEventListener("submit", async (event) => {

    event.preventDefault();


    // Prevent duplicate submissions.

    if (isSubmitting) {
      return;
    }


    // Check browser validation.

    if (!form.reportValidity()) {
      return;
    }


    // Validate resume for Careers.

    if (!validateResume(form)) {
      return;
    }


    // Set Reply-To address.

    const emailField = form.querySelector(
      '[name="email"]'
    );

    const replyToField = form.querySelector(
      '[name="_replyto"]'
    );

    if (emailField && replyToField) {

      replyToField.value = emailField.value.trim();

    }


    // Set submission subject.

    const subjectField = form.querySelector(
      '[name="_subject"]'
    );

    if (subjectField) {

      subjectField.value =
        formType === "careers"
          ? "New Careers Application - GroSuite"
          : "New Website Enquiry - GroSuite";

    }


    // Update timestamp immediately before submission.

    updateTimestamp();


    // Get submit button.

    const submitButton = form.querySelector(
      'button[type="submit"], input[type="submit"]'
    );

    let originalButtonText = "";

    if (submitButton) {

      originalButtonText =
        submitButton.tagName === "INPUT"
          ? submitButton.value
          : submitButton.textContent;

    }


    // Loading state.

    isSubmitting = true;

    if (submitButton) {

      submitButton.disabled = true;

      if (submitButton.tagName === "INPUT") {

        submitButton.value = "Sending...";

      } else {

        submitButton.textContent = "Sending...";

      }

    }

    form.setAttribute("aria-busy", "true");


    showFormMessage(
      form,
      "Please wait. Your submission is being sent..."
    );


    try {

      // Collect form fields and uploaded files.

      const formData = new FormData(form);


      // Send request to FormSubmit.app.

      const response = await fetch(FORM_ENDPOINT, {

        method: "POST",

        headers: {
          Accept: "application/json"
        },

        body: formData

      });


      // Read JSON response.

      const result = await response
        .json()
        .catch(() => null);


      // Check server response.

      if (!response.ok || !result || !result.ok) {

        const message =
          result?.error?.message ||
          `Submission failed. HTTP status: ${response.status}`;

        const error = new Error(message);

        error.code = result?.error?.code || "";

        throw error;

      }


      // Show successful submission message.

      if (formType === "careers") {

        showFormMessage(
          form,
          "Your job application was submitted successfully. Thank you!",
          "success"
        );

      } else {

        showFormMessage(
          form,
          "Your enquiry was submitted successfully. Our team will contact you soon.",
          "success"
        );

      }


      // Reset form fields.

      form.reset();


      // Refresh spam protection timestamp.

      updateTimestamp();


      // Restore enquiry prefill.

      if (formType === "enquiry") {
        prefillEnquiryMessage(form);
      }


      console.log(
        "Form submitted successfully. Submission ID:",
        result.id
      );


    } catch (error) {

      console.error(
        "Form submission error:",
        error
      );

      let message =
        "Unable to submit your form. Please try again.";

      if (!navigator.onLine) {

        message =
          "No internet connection. Please check your network.";

      } else if (error.code === "domain_not_allowed") {

        message =
          "This website domain is not authorized in FormSubmit settings.";

      } else if (error.code === "form_not_found") {

        message =
          "The FormSubmit form endpoint is invalid.";

      } else if (error.code === "payload_too_large") {

        message =
          "The uploaded request is too large. Please upload a smaller resume.";

      } else if (error.code === "file_too_large") {

        message =
          "The resume exceeds the maximum file size allowed.";

      } else if (error.code === "storage_quota_exceeded") {

        message =
          "FormSubmit storage is full. Please contact the website administrator.";

      } else if (error.code === "rate_limited") {

        message =
          "Too many submissions. Please try again later.";

      } else if (error instanceof TypeError) {

        message =
          "Network error. Check your internet connection and run the website using Live Server.";

      } else if (error.message) {

        message = error.message;

      }


      showFormMessage(
        form,
        message,
        "error"
      );

    } finally {

      // Restore submit button.

      isSubmitting = false;

      if (submitButton) {

        submitButton.disabled = false;

        if (submitButton.tagName === "INPUT") {

          submitButton.value = originalButtonText;

        } else {

          submitButton.textContent = originalButtonText;

        }

      }

      form.removeAttribute("aria-busy");

    }

  });

});


/* ========================================
   OUR PARTNERS SECTION ANIMATIONS
======================================== */

(() => {

  const partnerSection = document.querySelector(
    "#our-partners"
  );

  if (!partnerSection) return;


  const revealElements =
    partnerSection.querySelectorAll(".reveal");


  // Reveal partner content.

  if (
    reduceMotion ||
    !("IntersectionObserver" in window)
  ) {

    revealElements.forEach((element) => {

      element.classList.add("is-visible");

    });

  } else {

    const partnerObserver = new IntersectionObserver(
      (entries, observer) => {

        entries.forEach((entry) => {

          if (entry.isIntersecting) {

            entry.target.classList.add("is-visible");

            observer.unobserve(entry.target);

          }

        });

      },
      {
        threshold: 0.15,
        rootMargin: "0px 0px -30px 0px"
      }
    );

    revealElements.forEach((element) => {

      partnerObserver.observe(element);

    });

  }


  // Pause moving logos when keyboard focus enters.

  const marquee = partnerSection.querySelector(
    ".partner-marquee"
  );

  if (marquee) {

    marquee.addEventListener("focusin", () => {

      marquee.classList.add("is-paused");

    });

    marquee.addEventListener("focusout", (event) => {

      if (!marquee.contains(event.relatedTarget)) {

        marquee.classList.remove("is-paused");

      }

    });

  }

})();


/* ========================================
   END OF GROSUITE MAIN.JS
======================================== */


/* ========================================
   ENQUIRE PAGE URL PREFILL HELPER
======================================== */
(function() {
  const urlParams = new URLSearchParams(window.location.search);
  const solution = urlParams.get('solution');
  const plan = urlParams.get('plan');
  const messageBox = document.getElementById('enquire-message');
  const solutionSelect = document.getElementById('enquire-solution');

  if (solutionSelect && solution) {
    const s = solution.toLowerCase();
    for (let i = 0; i < solutionSelect.options.length; i++) {
      if (solutionSelect.options[i].value.toLowerCase() === s) {
        solutionSelect.selectedIndex = i;
        break;
      }
    }
  }

  if (messageBox && !messageBox.value) {
    if (solution && solution.toLowerCase() === 'hrms') {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to start a 15-day Free Trial for GroSuite HRMS Solutions. Please set up our trial access and share the onboarding details.';
    } else if (solution && solution.toLowerCase() === 'erp') {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to start a 15-day Free Trial for GroSuite ERP Solutions. Please set up our trial access and share the onboarding details.';
    } else if (solution && solution.toLowerCase() === 'crm') {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to start a 15-day Free Trial for GroSuite CRM Solutions. Please set up our trial access and share the onboarding details.';
    } else if (solution && (solution.toLowerCase() === 'automation' || solution.toLowerCase() === 'business-automation')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to start a 15-day Free Trial for GroSuite Business Automation Solutions. Please set up our trial access and share the onboarding details.';
    } else if (solution && (solution.toLowerCase() === 'integration' || solution.toLowerCase() === 'system-integration')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to start a 15-day Free Trial for GroSuite System Integration Solutions. Please set up our trial access and share the onboarding details.';
    } else if (solution && (solution.toLowerCase() === 'domain-management' || solution.toLowerCase() === 'domain' || solution.toLowerCase() === 'website-development')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about GroSuite Website Development, Design & Domain Management Services. Please share information regarding custom web design, web apps, and enterprise domain hosting.';
    } else if (solution && (solution.toLowerCase() === 'website-design-development' || solution.toLowerCase() === 'web-design')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss a custom Website Development & Website Design project for our company. Please schedule an introductory consultation.';
    } else if (solution && (solution.toLowerCase() === 'web-application-development' || solution.toLowerCase() === 'web-app')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss our requirements for Website Application Development (SaaS portal, client dashboard, or custom web app).';
    } else if (solution && (solution.toLowerCase() === 'business-website')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI am interested in developing a professional Business Website with product/service showcases, lead capture, and customer engagement features.';
    } else if (solution && (solution.toLowerCase() === 'ecommerce-website' || solution.toLowerCase() === 'ecommerce')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss developing a modern E-Commerce Website with product catalogs, shopping cart, and secure payment gateway integration.';
    } else if (solution && (solution.toLowerCase() === 'portfolio-website' || solution.toLowerCase() === 'portfolio')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about building a high-impact Portfolio Website to showcase our projects, case studies, and creative works.';
    } else if (solution && (solution.toLowerCase() === 'informational-website' || solution.toLowerCase() === 'informational')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss building an Informational Website with a resource library, knowledge base, and search capabilities.';
    } else if (solution && (solution.toLowerCase() === 'api-integration' || solution.toLowerCase() === 'api')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss a project for GroSuite API & System Integration Services. Please share details on custom API architecture and data bridge capabilities.';
    } else if (solution && (solution.toLowerCase() === 'whatsapp-integration' || solution.toLowerCase() === 'whatsapp')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about API & WhatsApp Business Integration. Please share details on automated notifications, messaging webhooks, and conversational bot setup.';
    } else if (solution && (solution.toLowerCase() === 'database-integration' || solution.toLowerCase() === 'database')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Database Integration and data pipeline synchronization (SQL, NoSQL, Cache, Vector DB) for our application infrastructure.';
    } else if (solution && (solution.toLowerCase() === 'cloud-platform-integration' || solution.toLowerCase() === 'cloud-integration')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Cloud & Platform Integration across AWS, Azure, GCP, and enterprise SaaS platforms.';
    } else if (solution && (solution.toLowerCase() === 'api-security')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss API Security, tokenized authentication (OAuth 2.0/mTLS), rate limiting, and endpoint vulnerability protection.';
    } else if (solution && (solution.toLowerCase() === 'api-testing' || solution.toLowerCase() === 'api-monitoring')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss API Testing & Real-Time Monitoring solutions to ensure endpoint uptime, synthetic testing, and latency alerting.';
    } else if (solution && (solution.toLowerCase() === 'ai-chatbots' || solution.toLowerCase() === 'ai')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI am interested in GroSuite AI & Chatbot Development Services. Please connect with us to discuss conversational AI bots and LLM integration for our workflows.';
    } else if (solution && (solution.toLowerCase() === 'ai-application-development' || solution.toLowerCase() === 'ai-app')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss a custom AI Application Development project with autonomous AI agents, LLM pipelines, and vector embeddings.';
    } else if (solution && (solution.toLowerCase() === 'chatbot-development' || solution.toLowerCase() === 'chatbot')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Chatbot Development for omnichannel conversational AI across WhatsApp, web, and mobile.';
    } else if (solution && (solution.toLowerCase() === 'ai-integration-automation' || solution.toLowerCase() === 'ai-automation')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss AI Integration & Automation to embed generative AI models into our existing software and operational workflows.';
    } else if (solution && (solution.toLowerCase() === 'voice-ai-speech' || solution.toLowerCase() === 'voice-ai')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Voice AI & Speech Solutions (real-time speech recognition, voice bots, and text-to-speech synthesis).';
    } else if (solution && (solution.toLowerCase() === 'ai-analytics-reporting' || solution.toLowerCase() === 'ai-analytics')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss AI Analytics & Reporting solutions for predictive insights, automated data summaries, and executive intelligence.';
    } else if (solution && (solution.toLowerCase() === 'mobile-apps' || solution.toLowerCase() === 'mobile')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss our requirements for GroSuite Mobile App Development Services (iOS/Android/Cross-Platform). Please schedule an introductory call.';
    } else if (solution && (solution.toLowerCase() === 'android-app-development' || solution.toLowerCase() === 'android-app')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss native Android App Development (Kotlin, Jetpack Compose, Android SDK) and cross-platform mobile solutions.';
    } else if (solution && (solution.toLowerCase() === 'mobile-backend-api' || solution.toLowerCase() === 'backend-api-integration')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Backend & API Integration for mobile apps, real-time sync, and push notification architecture.';
    } else if (solution && (solution.toLowerCase() === 'app-testing-qa' || solution.toLowerCase() === 'app-testing')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss App Testing & Quality Assurance across physical Android & iOS device matrix, automated UI tests, and performance benchmarking.';
    } else if (solution && (solution.toLowerCase() === 'app-maintenance-support' || solution.toLowerCase() === 'app-maintenance')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about App Maintenance & 24/7 Support packages, OS version updates, crash analytics, and SLA monitoring.';
    } else if (solution && (solution.toLowerCase() === 'cloud-development' || solution.toLowerCase() === 'cloud')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss GroSuite Cloud Development & DevOps Services. Please share more details on cloud migration, containerization, and infrastructure architecture.';
    } else if (solution && (solution.toLowerCase() === 'business-integration' || solution.toLowerCase() === 'business')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about GroSuite Business Integration Services to harmonize our enterprise systems, data pipelines, and departmental workflows.';
    } else if (solution && (solution.toLowerCase() === 'data-analytics')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Data Analytics solutions, real-time KPI dashboards, and predictive business intelligence for our organization.';
    } else if (solution && (solution.toLowerCase() === 'data-engineering')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Data Engineering services, streaming ETL pipelines, data lakehouse architecture, and warehouse integration.';
    } else if (solution && (solution.toLowerCase() === 'financial-integration' || solution.toLowerCase() === 'financial')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Financial Integration solutions for automated ledger sync, ERP/accounting bridging, and payment reconciliation.';
    } else if (solution && (solution.toLowerCase() === 'business-analytics-reporting' || solution.toLowerCase() === 'business-analytics')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Business Analytics & Reporting services, executive KPI scorecards, and automated operational intelligence.';
    } else if (solution && (solution.toLowerCase() === 'cyber-security' || solution.toLowerCase() === 'security')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss GroSuite Cyber Security Services, threat defense, and security assessment for our digital infrastructure.';
    } else if (solution && (solution.toLowerCase() === 'security-testing' || solution.toLowerCase() === 'testing')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Security Testing services, including Vulnerability Assessments, Penetration Testing (VAPT), and code security reviews.';
    } else if (solution && (solution.toLowerCase() === 'firewall-management' || solution.toLowerCase() === 'firewall')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Firewall Management, Next-Gen Firewall (NGFW) policies, WAF deployment, and DDoS mitigation strategies.';
    } else if (solution && (solution.toLowerCase() === 'network-security')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Network Security architecture, zero-trust network access (ZTNA), VPNs, and micro-segmentation.';
    } else if (solution && (solution.toLowerCase() === 'endpoint-security')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Endpoint Security solutions, Endpoint Detection & Response (EDR), device compliance, and malware defense.';
    } else if (solution && (solution.toLowerCase() === 'report-security' || solution.toLowerCase() === 'security-reporting')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Security Reporting & Compliance Audits (ISO 27001, SOC 2, GDPR, HIPAA) and executive threat reports.';
    } else if (solution && (solution.toLowerCase() === 'data-protection')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to discuss Data Protection services, end-to-end encryption, data loss prevention (DLP), and database access governance.';
    } else if (solution && (solution.toLowerCase() === 'domain-security')) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about Domain Security solutions, DNSSEC enforcement, anti-spoofing protocols (DMARC, SPF, DKIM), and brand protection.';
    } else if (plan) {
      messageBox.value = 'Hi GroSuite Team,\n\nI would like to inquire about the ' + plan + ' plan for GroSuite. Please share more details.';
    }
  }
})();


/* ========================================
   CAREER PAGE AUTO-SELECTION HELPER
======================================== */
(function() {
  document.querySelectorAll('[data-apply-type]').forEach(btn => {
    btn.addEventListener('click', function() {
      const type = this.getAttribute('data-apply-type');
      const catSelect = document.getElementById('career-category');
      if (catSelect && type) {
        for (let i = 0; i < catSelect.options.length; i++) {
          if (catSelect.options[i].value.toLowerCase() === type.toLowerCase()) {
            catSelect.selectedIndex = i;
            break;
          }
        }
      }
    });
  });

  document.querySelectorAll('[data-role-select]').forEach(btn => {
    btn.addEventListener('click', function() {
      const role = this.getAttribute('data-role-select');
      const roleSelect = document.getElementById('career-role');
      const catSelect = document.getElementById('career-category');
      if (roleSelect && role) {
        for (let i = 0; i < roleSelect.options.length; i++) {
          if (roleSelect.options[i].value.toLowerCase() === role.toLowerCase()) {
            roleSelect.selectedIndex = i;
            break;
          }
        }
      }
      if (catSelect && role.toLowerCase().includes('trainee')) {
        for (let i = 0; i < catSelect.options.length; i++) {
          if (catSelect.options[i].value.toLowerCase() === 'internship') {
            catSelect.selectedIndex = i;
            break;
          }
        }
      }
    });
  });
})();


/* ==========================================================================
   SUBHEADINGS RESPECTIVE COLOR INTERACTION (INDUSTRIES & RESOURCES)
   ========================================================================== */
(function() {
  function initSubheadingsColorSync() {
    // 1. Header Dropdown Submenu Click Handling
    document.querySelectorAll('.nav__submenu a').forEach(function(link) {
      link.addEventListener('click', function() {
        const submenu = this.closest('.nav__submenu');
        if (submenu) {
          submenu.querySelectorAll('a').forEach(function(a) {
            a.classList.remove('is-active');
          });
          this.classList.add('is-active');
        }

        const href = this.getAttribute('href') || '';
        // If clicking an industry hash on index.html
        if (href.includes('#industry-')) {
          const hashId = href.split('#')[1];
          const targetCard = document.getElementById(hashId);
          if (targetCard) {
            document.querySelectorAll('.industry').forEach(function(c) {
              c.classList.remove('is-active');
            });
            targetCard.classList.add('is-active');
            setTimeout(function() {
              targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 100);
          }
        }
      });
    });

    // 2. Direct Click on Industry Cards (index.html)
    const industryCards = document.querySelectorAll('.industry');
    if (industryCards.length > 0) {
      industryCards.forEach(function(card) {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function() {
          industryCards.forEach(function(c) {
            c.classList.remove('is-active');
          });
          this.classList.add('is-active');
          if (this.id) {
            try {
              history.replaceState(null, '', '#' + this.id);
            } catch (err) {}
            // Also sync active state in navbar submenu if present
            const navSub = document.querySelector('.nav__submenu a[href*="' + this.id + '"]');
            if (navSub) {
              const p = navSub.closest('.nav__submenu');
              if (p) {
                p.querySelectorAll('a').forEach(function(a) { a.classList.remove('is-active'); });
                navSub.classList.add('is-active');
              }
            }
          }
        });
      });

      // Synchronize hash on page load / hash change
      function activateIndustryFromHash() {
        const hash = window.location.hash;
        if (hash && hash.startsWith('#industry-')) {
          const targetCard = document.querySelector(hash);
          if (targetCard) {
            industryCards.forEach(function(c) { c.classList.remove('is-active'); });
            targetCard.classList.add('is-active');
            const navSub = document.querySelector('.nav__submenu a[href*="' + hash.substring(1) + '"]');
            if (navSub) {
              const p = navSub.closest('.nav__submenu');
              if (p) {
                p.querySelectorAll('a').forEach(function(a) { a.classList.remove('is-active'); });
                navSub.classList.add('is-active');
              }
            }
          }
        }
      }

      window.addEventListener('hashchange', activateIndustryFromHash);
      if (window.location.hash && window.location.hash.startsWith('#industry-')) {
        setTimeout(activateIndustryFromHash, 250);
      }
    }

    // 3. Resource Page Subheadings & Filter Tabs (resource.html)
    const resourceTabs = document.querySelectorAll('.resource-tab');
    if (resourceTabs.length > 0) {
      function syncResourceHash() {
        const hash = window.location.hash;
        if (!hash) return;
        resourceTabs.forEach(function(tab) {
          const href = tab.getAttribute('href');
          if (href === hash || (href && href.endsWith(hash))) {
            resourceTabs.forEach(function(t) { t.classList.remove('active'); });
            tab.classList.add('active');
            // Trigger tab filter display
            const filter = tab.getAttribute('data-filter');
            const items = document.querySelectorAll('[data-resource-item]');
            if (items.length > 0 && filter) {
              if (filter === 'all') {
                items.forEach(function(item) { item.style.display = ''; });
              } else {
                items.forEach(function(item) {
                  const itemCat = item.getAttribute('data-category') || '';
                  item.style.display = (itemCat === filter) ? '' : 'none';
                });
              }
            }
          }
        });

        // Pulse / activate section block
        const targetSec = document.querySelector(hash);
        if (targetSec && targetSec.classList.contains('resource-block')) {
          document.querySelectorAll('.resource-block').forEach(function(b) {
            b.classList.remove('is-active');
          });
          targetSec.classList.add('is-active');
        }
      }

      window.addEventListener('hashchange', syncResourceHash);
      if (window.location.hash) {
        setTimeout(syncResourceHash, 250);
      }
    }

    // Ensure Free Trial nav button active indicator on enquire.html
    const pathname = window.location.pathname.toLowerCase();
    if (pathname.includes('enquire')) {
      const trialBtn = document.querySelector('.nav__trial');
      if (trialBtn) {
        trialBtn.setAttribute('aria-current', 'page');
        trialBtn.classList.add('active');
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSubheadingsColorSync);
  } else {
    initSubheadingsColorSync();
  }
})();
