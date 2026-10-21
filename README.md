# Mohammed Obaidul Hoque — Portfolio

A responsive front-end developer portfolio published on GitHub Pages. Built as a lightweight, single-file static site with no build step, package manager, external font dependency, or JavaScript framework.

## Live website

https://obaidhqbd.github.io/JUDO/

## Stack

- Semantic HTML5
- Responsive CSS with light/dark themes
- Vanilla JavaScript for theme toggle, mobile navigation, and scroll reveals
- GitHub Actions + GitHub Pages for automatic deployment

## Publish and update

The `Deploy portfolio to GitHub Pages` workflow runs on pushes to `main` and can also be started manually from the Actions tab. The page source is `index.html` at the repository root.

## Personalization checklist

- Verify the LinkedIn URL and social handles before sharing widely.
- Keep Obaid Web Lab labelled as in development until the project is ready.
- Update project descriptions as their status changes; do not add unverified client results or testimonials.

## Repository

https://github.com/obaidhqbd/JUDO

## Visitor analytics and privacy

- Google Analytics 4 uses Measurement ID `G-R8YP3TWCJN`.
- Analytics loads only after a visitor chooses **Accept analytics** in the privacy notice.
- Visitors can reject or change their selection using **Privacy choices** in the footer.
- The privacy policy is available at [privacy.html](https://obaidhqbd.github.io/JUDO/privacy.html).

### What visitor activity can be measured

With visitor consent, the site sends these custom GA4 events:

- `portfolio_section_view`: a portfolio or privacy-policy section was viewed.
- `portfolio_section_engagement`: approximate seconds that a section stayed visible while the browser tab was active (minimum 3 seconds; capped at 30 minutes per measurement).
- `portfolio_interaction`: a navigation link or button was used. The event stores a short label and internal/external/button classification, not the full destination URL.

The site does not collect names, form contents, or use hidden browser fingerprinting. Analytics measurement is pseudonymous and cannot identify a visitor by their real name on this static site.

In Google Analytics, check **Reports → Realtime** to test incoming events. For historical analysis, open **Reports → Engagement → Events**. To report custom event parameters in Explorations, register these event-scoped dimensions under **Admin → Data display → Custom definitions**: `section_id`, `element_label`, `destination_type`, and `placement`. Register `active_seconds` as a custom metric (integer/standard unit) so the section-time values can be examined. Custom definitions apply to data collected after registration and may take time to appear in reports.
