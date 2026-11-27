import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})

        file_url = f"file:///{os.path.abspath('pricing.html').replace(os.sep, '/')}"
        print(f"Navigating to {file_url}")
        await page.goto(file_url, wait_until='networkidle')

        # 1. Verify Step 1 initial state
        step1_visible = await page.is_visible('#pricingStep1Block')
        step2_visible = await page.is_visible('#pricingStep2Block')
        progress_visible = await page.is_visible('#pricingStepProgress')
        print(f"Initial: step1={step1_visible}, step2={step2_visible}, progress={progress_visible}")
        assert step1_visible and not step2_visible and progress_visible, "Step 1 initial state failed"

        # Capture Step 1 screenshot
        await page.screenshot(path='C:/Users/Mahendran K/.gemini/antigravity/brain/286be14e-9558-4fc1-b5d3-e5e458ba4ddc/pricing_step1_view.png', full_page=False)

        # 2. Click Continue to Step 2
        print("Clicking Continue to Step 2...")
        await page.click('#btnSubmitStep1')
        await page.wait_for_timeout(500)

        step1_visible = await page.is_visible('#pricingStep1Block')
        step2_visible = await page.is_visible('#pricingStep2Block')
        step2_active = await page.evaluate("() => document.getElementById('stepIndicator2').classList.contains('active')")
        step1_completed = await page.evaluate("() => document.getElementById('stepIndicator1').classList.contains('completed')")
        region_text = await page.inner_text('#step2SelectedRegion')
        print(f"After Step 1 submit: step1={step1_visible}, step2={step2_visible}, step2_active={step2_active}, step1_completed={step1_completed}, region='{region_text}'")
        assert not step1_visible and step2_visible and step2_active and step1_completed, "Advance to Step 2 failed"

        # Capture Step 2 screenshot
        await page.screenshot(path='C:/Users/Mahendran K/.gemini/antigravity/brain/286be14e-9558-4fc1-b5d3-e5e458ba4ddc/pricing_step2_view.png', full_page=False)

        # 3. Test Back to Step 1
        print("Testing Back to Step 1...")
        await page.click('#btnBackToStep1')
        await page.wait_for_timeout(300)
        step1_visible = await page.is_visible('#pricingStep1Block')
        step2_visible = await page.is_visible('#pricingStep2Block')
        assert step1_visible and not step2_visible, "Back to Step 1 failed"

        # Advance again to Step 2
        await page.click('#btnSubmitStep1')
        await page.wait_for_timeout(300)

        # 4. Test validation on empty submit
        print("Testing validation on empty submit...")
        await page.click('#pricingSubmitBtn')
        await page.wait_for_timeout(300)
        status_text = await page.inner_text('#pricingFormStatus')
        print(f"Status text on empty submit: '{status_text}'")
        assert "Please fill in all required fields" in status_text, "Validation failed"

        # 5. Fill out Form
        print("Filling form details...")
        await page.fill('#pricingCompanyName', 'TechInnovate Solutions')
        await page.fill('#pricingFullName', 'Alex Morgan')
        await page.fill('#pricingWorkEmail', 'alex@techinnovate.com')
        await page.fill('#pricingPhone', '+91 98765 43210')
        await page.select_option('#pricingTeamSize', '51-200')
        await page.select_option('#pricingInterest', 'All GroSuite Solutions')

        # 6. Submit form to reveal pricing
        print("Submitting Step 2 form...")
        await page.click('#pricingSubmitBtn')
        await page.wait_for_timeout(1000)

        banner_visible = await page.is_visible('#pricingSuccessBanner')
        pricing_visible = await page.is_visible('#pricingDetailsContainer')
        company_text = await page.inner_text('#summaryCompany')
        print(f"After Step 2 submit: banner={banner_visible}, pricing={pricing_visible}, company='{company_text}'")
        assert banner_visible and pricing_visible and company_text == 'TechInnovate Solutions', "Step 2 reveal pricing failed"

        # Capture Unlocked pricing screenshot
        await page.screenshot(path='C:/Users/Mahendran K/.gemini/antigravity/brain/286be14e-9558-4fc1-b5d3-e5e458ba4ddc/pricing_unlocked_view.png', full_page=False)

        print("ALL WORKFLOW STEPS PASSED SUCCESSFULLY!")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
