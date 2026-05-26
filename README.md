# MNS PTA — Jekyll site

Static replacement for the Neon-hosted version of [www.mnspta.org](https://www.mnspta.org).
Built with [Jekyll](https://jekyllrb.com/), deployable for free on
[GitHub Pages](https://pages.github.com/) or [Cloudflare Pages](https://pages.cloudflare.com/).

## What's here

```
.
├── _config.yml              ← site-wide settings, external URLs
├── _data/events.yml         ← upcoming events (edit YAML, not HTML)
├── _includes/               ← header & footer partials
├── _layouts/                ← page templates
├── assets/css/main.css      ← the only stylesheet
├── assets/images/           ← downloaded by scripts/download_assets.py
├── scripts/download_assets.py ← run once to grab images off Neon CDN
├── *.md                     ← one file per page
└── Gemfile                  ← pins to GitHub Pages gem versions
```

Each page is a markdown file with a small front-matter block. To edit a
page's text, open the `.md` file, change the words, commit. That's it.

## First-time setup

### 1. Download the images off the Neon CDN

```bash
python3 scripts/download_assets.py
```

Run this **before** cancelling Neon — once Neon is gone, the CDN URLs die.
The script is idempotent; re-running it skips files that already exist.

### 2. Install Jekyll locally (one-time)

Requires Ruby 3.1+ and Bundler. This project uses **modern Jekyll 4**, not
the legacy `github-pages` gem, so any current Ruby 3.x works.

**Important:** as of Dec 2025, `brew install ruby` installs Ruby 4.0, which
Jekyll's toolchain may not fully support yet. Pin a known-good Ruby with
rbenv instead of using the Homebrew default:

```bash
# if your computer isn't set up for ruby & rbenv already, run these 3 lines
# brew install rbenv
# echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
# source ~/.zshrc
rbenv init          # then add the printed line to ~/.zshrc and restart your shell
rbenv install 3.3.6
# cd /path/to/repo  # if you aren't in the repo already
rbenv local 3.3.6   # writes .ruby-version — pins ONLY this folder to 3.3.6
ruby -v             # confirm it shows 3.3.6 here
gem install bundler
bundle install
```

`rbenv local` leaves your system Ruby untouched everywhere else; the
pin applies only inside this directory. If a future Jekyll release supports
Ruby 4 cleanly, you can delete `.ruby-version` and skip rbenv entirely.

> Do **not** use the `github-pages` gem here. It locks the build to GitHub's
> legacy environment (old Jekyll, old Ruby) and breaks on new Ruby releases.
> Deployment is handled by GitHub Actions instead — see Deploying below.

### 3. Run locally

```bash
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>. Pages refresh automatically as you save.

## Editing common things

**Page text** — open the page's `.md` file, edit, save.

**Adding/removing an upcoming event** — edit `_data/events.yml`. The
`/upcoming-events/` page renders the list automatically.

**Updating the executive board for a new school year** — edit
`_data/board.yml`. The page renders from the data file, so changing a name,
adding a delegate, or rolling over the school year is just a YAML edit.

**Changing colors or fonts** — edit the CSS variables at the top of
`assets/css/main.css`.

**Adding a new page** — drop a new `.md` file at the repo root with this
front matter:

```yaml
---
layout: page
title: My new page
permalink: /my-new-page/
---
```

…then add a link to it in `_includes/nav.html`.

## Deploying

### Option A — GitHub Pages via Actions (recommended)

This repo ships a workflow at `.github/workflows/jekyll.yml` that builds
with modern Jekyll and deploys to Pages automatically.

1. Push this repo to GitHub.
2. **Settings → Pages → Source:** choose **"GitHub Actions"** (not "Deploy
   from a branch"). The included workflow handles the build.
3. Push to `main` (or use the Actions tab → "Run workflow"). Watch the build
   under the **Actions** tab; it builds then deploys.
4. **Settings → Pages → Custom domain:** `www.mnspta.org`.
5. At the DNS provider, create a CNAME record:
   `www → <your-github-username>.github.io`.
   For the apex `mnspta.org`, add an ALIAS / ANAME / forwarding record per
   [GitHub's docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
6. Enable "Enforce HTTPS" once the cert provisions (a few minutes).

Every push to `main` rebuilds and redeploys. Because the build runs the
Gemfile in CI, the published site matches exactly what you see locally —
no version drift between local and production.

### Option B — Cloudflare Pages

Connect the GitHub repo, set build command `bundle exec jekyll build`,
output directory `_site`. Free, fast, also issues TLS automatically.

## Cutover plan

1. Run `download_assets.py`, commit `assets/images/` to the repo.
2. Push to GitHub, deploy to Pages, point a temporary subdomain
   (`new.mnspta.org` or similar) at it. Verify visually.
3. Update DNS to point `www.mnspta.org` at GitHub Pages.
4. Wait ~24 hours for propagation, verify.
5. Cancel Neon Websites (keep the Neon CRM subscription — donations,
   events, member directory, login all still live there).

## Things to clean up before going live

These are flagged with `<!-- TODO -->` or in callouts in the relevant pages:

- **`after-school.md`** — the live page references Sept 2022 dates. Update
  to the current term.
- **`about-mns-pta.md`** — the "Read our bylaws" line has no link on the
  current site. Either drop the bylaws PDF in `assets/` and link it, or
  remove the line.
- **`_data/events.yml`** — currently empty/commented. Add this season's
  events when you're ready.
- **Old WordPress URLs** — the legacy site exposes `/wp-content/uploads/...`
  paths (e.g., the 2017 Parent Handbook PDF). If anything is still linked
  externally, copy those PDFs into `assets/docs/` and add `redirect_from`
  entries on a stub page, or set up redirects at the CDN.

## What stays external

These are kept as outbound links — none of them needs to live on the new
site:

| Service | Used for |
|---|---|
| Neon CRM (`ps290pta.app.neoncrm.com`) | Donations, event registration, parent directory, login |
| Square (`ps290.square.site`) | School store |
| Google Calendar | Calendar feed |
| Google Forms | Volunteer sign-up |
| Google Apps Scripts | Expense reimbursement, unpaid invoices forms |
| `api.neonemails.com` | Hosted welcome email |

All of these URLs are centralized in the `external:` block of
`_config.yml`, so if any change you only update one place.
