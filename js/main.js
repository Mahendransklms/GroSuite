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
          "Your job application was submitted successfully. Our team will contact you soon. Thank you!",
          "success"
        );

      } else {

        showFormMessage(
          form,
          "Your enquiry was submitted successfully. Our team will contact you soon. Thank you!",
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
