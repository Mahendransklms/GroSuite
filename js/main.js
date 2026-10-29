const FORM_RECIPIENTS = {
  careers: "support@grosuite.in",
  enquiry: "support@grosuite.in"
};

const FORM_ENDPOINT = "https://formsubmit.co/";
const DEMO_DOMAIN = "example.com";
const MAX_RESUME_BYTES = 10 * 1024 * 1024;

// Mobile navigation
const menuToggle = document.querySelector(".nav__toggle");
const menu = document.getElementById("menu");

if (menuToggle && menu) {
  menuToggle.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("open");

    menuToggle.setAttribute("aria-expanded", String(isOpen));

    menuToggle.setAttribute(
      "aria-label",
      isOpen ? "Close navigation menu" : "Open navigation menu"
    );
  });

  menu.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      menu.classList.remove("open");

      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.setAttribute(
        "aria-label",
        "Open navigation menu"
      );
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.classList.contains("open")) {
      menu.classList.remove("open");

      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.focus();
    }
  });
}

// Reveal content as it enters the viewport.
// Respect the visitor's reduced-motion preference.
const revealItems = document.querySelectorAll(".reveal");

const reduceMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
).matches;

if (reduceMotion || !("IntersectionObserver" in window)) {
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
    item.style.transitionDelay = `${(index % 5) * 55}ms`;
    revealObserver.observe(item);
  });
}

// Automatically update the footer year.
document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

// Configure email forms.
document.querySelectorAll("form[data-email-form]").forEach((form) => {
  const formType = form.dataset.emailForm;
  const recipient = FORM_RECIPIENTS[formType];
  const notice = form.querySelector(".form-demo-notice");

  if (!recipient) {
    console.error(
      `No recipient email configured for form type: ${formType}`
    );

    form.addEventListener("submit", (event) => {
      event.preventDefault();
    });

    return;
  }

  // Configure the external form-processing endpoint.
  form.action = `${FORM_ENDPOINT}${recipient}`;
  form.noValidate = false;

  // Avoid sending real form data to a demo recipient.
  const isDemoRecipient = recipient
    .toLowerCase()
    .endsWith(`@${DEMO_DOMAIN}`);

  if (notice && isDemoRecipient) {
    notice.hidden = false;
  }

  // Prefill the enquiry message for partnership enquiries.
  if (formType === "enquiry") {
    const parameters = new URLSearchParams(window.location.search);
    const interest = parameters.get("interest");

    const messageField = form.querySelector('[name="message"]');

    if (interest && messageField && !messageField.value) {
      messageField.value =
        `I'm interested in: ${interest}. ` +
        "Please contact me with more information.";
    }
  }

  form.addEventListener("submit", (event) => {
    // Let the company reply directly to the applicant or enquirer.
    const emailField = form.querySelector('[name="email"]');
    const replyToField = form.querySelector('[name="_replyto"]');

    if (replyToField && emailField) {
      replyToField.value = emailField.value.trim();
    }

    // Validate the career resume.
    const resumeInput = form.querySelector(
      'input[type="file"][name="attachment"]'
    );

    if (
      resumeInput &&
      resumeInput.files &&
      resumeInput.files.length > 0
    ) {
      const file = resumeInput.files[0];

      const isPdf =
        file.type === "application/pdf" ||
        file.name.toLowerCase().endsWith(".pdf");

      if (!isPdf) {
        event.preventDefault();

        window.alert("Please upload your resume as a PDF file.");

        resumeInput.focus();
        return;
      }

      if (file.size > MAX_RESUME_BYTES) {
        event.preventDefault();

        window.alert(
          "The resume file must be 10 MB or smaller."
        );

        resumeInput.focus();
        return;
      }
    }

    // Stop submission while a demo email address is configured.
    if (isDemoRecipient) {
      event.preventDefault();

      window.alert(
        `This form is still configured for a demo address (${recipient}). ` +
        "Replace it in js/main.js with your real company email " +
        "before submitting or publishing the form."
      );
    }
  });
});

/* ========================================
   OUR PARTNERS SECTION ANIMATIONS
======================================== */

(() => {
  const partnerSection = document.querySelector("#our-partners");

  if (!partnerSection) return;

  const revealElements =
    partnerSection.querySelectorAll(".reveal");

  // Reveal content when it enters the viewport
  if ("IntersectionObserver" in window) {
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
  } else {
    // Fallback for browsers without IntersectionObserver
    revealElements.forEach((element) => {
      element.classList.add("is-visible");
    });
  }

  // Pause the moving logos when keyboard focus enters
  const marquee = partnerSection.querySelector(".partner-marquee");

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