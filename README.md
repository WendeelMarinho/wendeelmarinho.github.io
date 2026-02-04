# Wendeel Marinho — Static portfolio (GitHub Pages)

This is a lightweight, 100% static one-page portfolio/resume intended for publish on GitHub Pages.

Quick publish steps

- Create a repository named `username.github.io` (replace `username` with your GitHub username).
- Push the contents of this folder to the `main` branch (or `master` if you prefer).
- In the repository Settings > Pages: set Source to `main` branch and root (`/`). Save.
- The site will be available at `https://username.github.io/` within a few minutes.

Files included

- `index.html` — single page with sections and anchors.
- `styles.css` — theme, layout, responsive styles.
- `main.js` — minimal interactions (theme toggle, active nav highlight, copy email, back-to-top).
- `robots.txt` — simple allow + sitemap pointer.
- `sitemap.xml` — basic sitemap for the site root.
- `assets/` — (optional) place images, `Wendeel-Marinho-CTO-Resume.pdf`, `og.png` here.

Notes

- The site is pure HTML/CSS/JS and does not require Node or a build step.
- If you host under a GitHub Pages project page (not `username.github.io`), you may need to update paths or the sitemap URL.
- To change the sitemap/og URLs, edit `index.html`, `robots.txt` and `sitemap.xml`.

Accessibility & SEO

- Includes keyboard focus styles, aria labels and visible focus states.
- OpenGraph meta tags are in `index.html` (replace `og:image` if you add a custom image).

Customizing

- Replace the placeholder resume in `assets/Wendeel-Marinho-CTO-Resume.pdf`.
- Add images to `assets/` and update `index.html` as needed.

If you want I can:
- commit these files to the repository and open a PR, or
- add a small `assets/README` with recommended image sizes and an example `og.png`.
# wendeelmarinho.github.io