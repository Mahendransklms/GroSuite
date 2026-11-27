with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """/* 1. Header has uniform min-height so all titles and descriptions line up */
.pricing-card__header {
  min-height: 110px;
  display: flex;
  flex-direction: column;
}

.pricing-card__header h3 {
  font-size: 1.45rem;
  font-weight: 800;
  margin: 0 0 0.45rem;
  color: #ffffff !important;
}

.pricing-card__desc {
  font-size: 0.88rem;
  color: #cbd5e1 !important;
  line-height: 1.5;
  margin-bottom: 0;
  flex-grow: 1;
}

/* 2. Symmetrically Aligned Pricing Box */
.pricing-card__price-box {
  display: flex;
  align-items: baseline;
  gap: 0.35rem;
  margin-top: 1.25rem;
  margin-bottom: 0.35rem;
  min-height: 52px;
}

.pricing-card__currency {
  font-size: 1.65rem;
  font-weight: 800;
  color: #ffffff !important;
  line-height: 1;
}

.pricing-card__amount {
  font-size: 2.85rem;
  font-weight: 900;
  color: #ffffff !important;
  line-height: 1;
  letter-spacing: -0.03em;
}

.pricing-card__original-price {
  font-size: 1.35rem;
  font-weight: 700;
  color: #94a3b8 !important;
  text-decoration: line-through;
  text-decoration-thickness: 2px;
  line-height: 1;
  margin-left: 0.2rem;
  margin-right: 0.15rem;
  opacity: 0.75;
}

.pricing-card__original-price {
  font-size: 1.35rem;
  font-weight: 700;
  color: #94a3b8 !important;
  text-decoration: line-through;
  text-decoration-thickness: 2px;
  line-height: 1;
  margin-left: 0.15rem;
  margin-right: 0.15rem;
  opacity: 0.8;
}

.pricing-card__period {
  font-size: 0.92rem;
  color: #94a3b8 !important;
  font-weight: 600;
}

.pricing-card__price-box--quote {
  align-items: center;
}

.pricing-card__amount--quote {
  font-size: 2.1rem;
  font-weight: 850;
  color: #ffffff !important;
  line-height: 1.15;
}

/* Dedicated Separate Card Annual Discount Pill */
.card-annual-discount {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: #4ade80 !important;
  background: rgba(34, 197, 94, 0.14);
  border: 1px solid rgba(34, 197, 94, 0.4);
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  margin-bottom: 0.6rem;
  width: fit-content;
}

/* 3. Symmetrically Aligned Yearly Billing Note */
.pricing-card__billing-note {
  font-size: 0.82rem;
  min-height: 38px;
  display: flex;
  align-items: center;
  padding: 0.4rem 0.65rem;
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 6px;
  color: #38bdf8 !important;
  font-weight: 600;
  margin-bottom: 1.25rem;
}"""

replacement = """/* 1. Header has uniform min-height so all titles and descriptions line up */
.pricing-card__header {
  min-height: 135px;
  display: flex;
  flex-direction: column;
}

.pricing-card__header h3 {
  font-size: 1.45rem;
  font-weight: 800;
  margin: 0 0 0.45rem;
  color: #ffffff !important;
}

.pricing-card__desc {
  font-size: 0.88rem;
  color: #cbd5e1 !important;
  line-height: 1.5;
  margin-bottom: 0;
  flex-grow: 1;
}

/* 2. Symmetrically Aligned Pricing Box */
.pricing-card__price-box {
  display: flex;
  align-items: baseline;
  gap: 0.25rem;
  margin-top: 1rem;
  margin-bottom: 0.45rem;
  min-height: 52px;
  white-space: nowrap;
}

.pricing-card__currency {
  font-size: 1.45rem;
  font-weight: 800;
  color: #ffffff !important;
  line-height: 1;
  flex-shrink: 0;
}

.pricing-card__amount {
  font-size: 2.15rem;
  font-weight: 900;
  color: #ffffff !important;
  line-height: 1;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.pricing-card__original-price {
  font-size: 1.05rem;
  font-weight: 700;
  color: #94a3b8 !important;
  text-decoration: line-through;
  text-decoration-thickness: 1.5px;
  line-height: 1;
  margin-left: 0.15rem;
  margin-right: 0.1rem;
  opacity: 0.75;
  flex-shrink: 0;
}

.pricing-card__period {
  font-size: 0.82rem;
  color: #94a3b8 !important;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 0;
}

.pricing-card__price-box--quote {
  align-items: center;
}

.pricing-card__amount--quote {
  font-size: 1.85rem;
  font-weight: 850;
  color: #ffffff !important;
  line-height: 1.15;
}

/* Dedicated Separate Card Annual Discount Pill */
.card-annual-discount {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: #4ade80 !important;
  background: rgba(34, 197, 94, 0.14);
  border: 1px solid rgba(34, 197, 94, 0.4);
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  margin-bottom: 0.6rem;
  width: fit-content;
}

/* 3. Symmetrically Aligned Yearly Billing Note */
.pricing-card__billing-note {
  font-size: 0.8rem;
  line-height: 1.35;
  min-height: 48px;
  display: flex;
  align-items: center;
  padding: 0.4rem 0.65rem;
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 6px;
  color: #38bdf8 !important;
  font-weight: 600;
  margin-bottom: 1.25rem;
}"""

assert target in css, "Target not found in css/style.css"
css = css.replace(target, replacement)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css for aligned pricing boxes!")
