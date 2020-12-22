# Burp Suite (HTTP PRoxy)

* [Room - BurpSuite](https://tryhackme.com/room/rpburpsuitex)

* [Room - OWASP Juice Shop](https://tryhackme.com/room/owaspjuiceshop)

* [Juice Shop - Github](https://github.com/bkimminich/juice-shop)

## Burp Suite Installation

* [Burp Suite - Installation](https://portswigger.net/burp/communitydownload)

* [Burp Suite - Docs](https://portswigger.net/burp/documentation/desktop/getting-started)

* `curl -L https://portswigger.net/burp/releases/download?product=community&version=2020.9.1&type=Linux -o burpsuite.sh`

* __Configure CA Certificate__

    * Start `BurpSuite`.

    * Install `FoxyProxy`

    * Add `FoxyProxy Proxy` - `BurpSuite`, `127.0.0.1`, `8080`.

    * In `Firefox` navigate to `127.0.0.1:8080`.

    * Select `CA certificate` and select the certificate.

    * Import the `PortSwigger CA` into Firefox.

* __Dark Mode__

    * `User Options` -> `Display` -> `Dark Mode`.

---

## Burp Suite Features

* __Proxy__ - What allows us to funnel traffic through Burp Suite for further analysis.

* __Target__ - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing.

* __Intruder__ - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more.

* __Repeater__ - Allows us to 'repeat' requests that have previously been made with or without modification. Often used in a precursor step to fuzzing with the aforementioned Intruder.

* __Sequencer__ - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for testing session cookies.

* __Decoder__ - As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding.

* __Comparer__ - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.

* __Extender__ - Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more!

* __Scanner__ - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible exploitation with another section of Burp. This feature, while not in the community edition of Burp Suite, is still a key facet of performing a web application test.

---

## Proxy

1. __Proxy Mode__

    1. `Ctrl+I` - Forward request to Repeater.

    3. `Ctrl+R` - Forward request to Intruder.

---

## Target Definition

1. `Target -> Site Map` - Site structure.

    * Browse site to generate `site map`. 

2. `Target -> Scope`

    * Add the domain of the site to reduce scope.

    * Can also set scope from `Proxy -> Request History` 

3. `Target -> Issue Definitions` - To view issues with explored site.

    * web cache poisoning

---

## Repeater

* `Repeater` best handles experimentation or `ad-hoc` testing and investigation.

* Attempt login

    * Can send to repeater from `Proxy -> Request History`

    * Send `'` to look for SQLi vulnerabilities.

---

## Intruder

* `Intruder` best handles experimentation or `programmatic` testing and investigation.

* `Intruder` _automates_ `enumeration`, `harvesting`, `fuzzing`.

    * __Sniper__ - Cycles through positions and uses a single dictionary of payloads.

    * __Battering Ram__ - Puts every payload into every selected position.

    * __Pitchfork__ - Allows multiple positions and payloads then tries every combination.

    * __Cluster__ 

* [Docs](https://portswigger.net/burp/documentation/desktop/tools/intruder/using)










