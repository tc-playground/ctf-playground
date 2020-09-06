# HTTP - Web Fundamentals

* [Room - Web Fundamentals](https://tryhackme.com/room/webfundamentals)

## Loading Websites

1. Enter `url` into browser.

2. Browser performs ` DNS lookup` to find the `IP address`.

3. _IFF_ `https` `TLS (1.3)` is used to establish a `secure session`.

3. Browser performs `HTTP GET` to retrieve the resource (and further requests for any sub-resources).

4. A `webserver` will return the requested resources:

    1. `HTTP` runs on port `80`.
    
    2. `HTTPS` runs on port `443`.

5. The `browser` will parse the page:

    1. __Fetch__ any required `sub-resources`.

    2. __Construct__ the `DOM (Document Object Model)`.

    3. __Render__ the `DOM` as a page and apply any `CSS`.

    4. __Execute__ any `JavaScript`.



---

## HTTP - Verbs and Request formats

1. There are `9` different `HTTP` `verbs`, also known as `methods`, that act on `resources`.


    1. `GET` - Get the specified resource.

    2. `HEAD` - The HEAD method asks for a response identical to that of a GET request, but without the response body.

    3. `POST` -  __Updates__ resources. _Sends_ data to `web server` NB: Must be `idempotent`.

    4. `PUT` - * __Creates__ new resources.

    5. `DELETE` - The DELETE method deletes the specified resource.

2. GET request

    ```bash
    GET /main.js HTTP/1.1
    Host: 192.168.170.129:8081
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
    Accept: */*
    Referer: http://192.168.170.129:8081/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
    ```

3. GET Response



---

## Cookies

* `cookies` are small bit of `data` stored in the `browser`.

* `cookies` are __automatically__ sent with `every browser request` for defined `paths`.

* `cookies` are used for `session management`, `tracking`, etc.

    * `sessions token` can be stolen using `Cross Site scripting (XSS)` attacks.

* `cookies` are required because `HTTP is stateless`.

* `cookies` can be set by the `server` in the HTTP `Set-Cookie` response header.

* `cookies` can be set by client side JavaScript.

* `cookies` can be managed and manipulated in the browser.

* `HTML5` has `LocalStorage` and `SessionStorage` that can be used instead of `cookies`.

    * These are not automatically sent by the browser.

* __Anatomy__

    1. __Name__ - The name of the `cookie`.

    2. __Value__ - The associated value of the `cookie`,

    3. __Expiry Date__ - When the browser will clear the `cookie`.

    4. __Path__ - What `urls` the `cookie` will be sent with.

* [Cookies - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

---

## CTF

* `curl 10.10.14.136:8081`; echo

* `curl 10.10.14.136:8081/ctf/get`; echo

* `curl -X POST 10.10.14.136:8081/ctf/post -d 'flag_please'; echo`

* `curl -vvv -X GET 10.10.14.136:8081/ctf/getcookie; echo`

* `curl -b flagpls=flagpls 10.10.14.136:8081/ctf/sendcookie; echo`




