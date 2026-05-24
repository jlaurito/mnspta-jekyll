source "https://rubygems.org"

# Modern Jekyll 4 — NOT the github-pages gem.
# The github-pages gem locks you to GitHub's legacy build environment
# (old Jekyll, old Ruby) and lags badly behind new Ruby releases. We build
# with GitHub Actions instead (see .github/workflows/jekyll.yml), so we're
# free to run current Jekyll and a modern Ruby locally.

ruby ">= 3.1"

gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-redirect-from", "~> 0.16"
end

# Required for Ruby 3.0+ (no longer bundled with Ruby)
gem "webrick", "~> 1.9"
gem "csv"
gem "base64"
gem "bigdecimal"

# Windows / JRuby timezone data
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Faster file watching on Windows
gem "wdm", "~> 0.2", :platforms => [:mingw, :x64_mingw, :mswin]
