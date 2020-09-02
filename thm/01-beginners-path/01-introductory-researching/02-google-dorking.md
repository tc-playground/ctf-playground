# Google Dorking

* [Room - Google Dorking](https://tryhackme.com/room/googledorking)

---

## Web Crawling and Indexing

* Web crawlers, indexing, keywords.

---

## Search Engine Optimisation (SEO)

* Search engines will “prioritise” those domains that are easier to index.

    * How responsive your website is to the different browser types.

    * How easy it is to crawl your website ("Sitemaps")

    * What kind of keywords your website has

* `SEO Optimisation Tools` are basically `linters` for `websites`.

* [SEO Site Checkup](https://seositecheckup.com/) - Analyse a specific site and provide a ranking based on criteria.

* [SEO Analyser](https://neilpatel.com/seo-analyzer/)

    * Finding Profitable Keywords
    * SEO Site Audit
    * Creating Sharable Content
    * Advanced Tracking
    * Link Building
    * Branding & Experience
    * Advanced Content Marketing

---

## robots.txt

* `robots.txt` is first thing indexed by "Crawlers" when visiting a website.

* `robots.txt`must be served at the root directory (specified by the webserver).

* __Example__

    ```txt
    # Group 1
    User-agent: Googlebot
    Disallow: /nogooglebot/

    # Group 2
    User-agent: *
    Allow: /

    Sitemap: http://www.example.com/sitemap.xml
    ```

* __Rule Definitions__ - (regex paths permitted)

    * `User-agent`	Specify the type of "Crawler" that can index your site.
    * `Allow`	Whitelist path and files hat the "Crawler" cannot index.
    * `Disallow` - Blacklist path and files hat the "Crawler" cannot index.

    * `Sitemap` - SiteMap path.

* __References__

    * [https://www.robotstxt.org/](https://www.robotstxt.org/)

    * [Mozilla robots.txt](https://moz.com/learn/seo/robotstxt)

    * [Google robots.txt](https://support.google.com/webmasters/answer/6062596?hl=en)

---

## Sitemaps

* `sitemaps` are a map of the site.

* `sitemaps` are indicative resources that specify the necessary routes to find content on the domain.

* `Sitemaps` are XML formatted.

* __References__

    * [XXE Room](https://tryhackme.com/room/xxe)

---

## Google Dorking / Hacking

* `google dorking` uses `advanced google search terms` to search the `index` of a specific website.

* __Google Search Query Filter Syntax__

    * `'xyz 123'` - Search exact string.

    * `site: "example.com"` - Search and exact site.

    * `filetype: "some-file-extension"` - Search for a specific filetype by extension. e.g. pdf.
	
    * `cache "some-url"`:	View Google's Cached version of a specified URL.

    * `intitle: some-phrase` - The specified phrase MUST appear in the title of the page.

    * `inurl: some-phrase`

    * etc.

* __Examples__

    * `site:bbc.co.uk filetype:pdf` - PDFs on the BBC website.

    * `intitle: index.of` - Files.

    * `intitle: login` - look for login pages.

* __Resources__

    * [Cheat Sheet](https://www.sans.org/security-resources/GoogleCheatSheet.pdf)

    * [Gist](https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06)

    * [Dorks List](https://gbhackers.com/latest-google-dorks-list/)

