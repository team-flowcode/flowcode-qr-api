## Create and bulk manage Flowcodes (dynamic QR codes) at scale! 🚀

<p align="center">
  <img width="300px"src="https://i.imgur.com/Dsw0Gml.png"/>
</p>

The **Flowcode API** is a **RESTful API** that lets you programmatically leverage the Flowcode platform:

* 🚀 Create and manage (dynaymic QR) Flowcodes at scale
* 📈 Extract real-time analytics data from your Flowcodes and Flowpages
* ♾️ Seamlessly integrate the API into your application

Please visit our 🛠️ [Developer Portal ➜](https://developer.flowcode.com/) for more information about each API endpoint and try our interactive test environment.

### Flowcode (dynamic QR) API Endpoints

| API               | Endpoint URL                                        | Type  | Description                                          |
| ----------------- | --------------------------------------------------- | ----- | ---------------------------------------------------- |
| Create a Flowcode | `https://gateway.flowcode.com/v4/codes`           | POST  | Creates a Flowcode                                   |
| Get All Flowcodes | `https://gateway.flowcode.com/v4/codes`           | GET   | Returns a list of Flowcodes accessible by this user  |
| Fetch Flowcode    | `https://gateway.flowcode.com/v4/codes/{code_id}` | GET   | Returns metadata for a specified Flowcode            |
| Update Flowcode   | `https://gateway.flowcode.com/v4/codes/{code_id}` | PATCH | Updates a Flowcode according to specified parameters |

### Flowcode Image Generation API Endpoints

| API                         | Endpoint URL                                                  | Type | Description                                                                                              |
| --------------------------- | ------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------- |
| Generate static code image  | `https://gateway.flowcode.com/v3/codes/generator/static`    | GET  | Generate a static Flowcode image that scans to a specific destination, specified by url                  |
| Generate dynamic code image | `https://gateway.flowcode.com/v3/codes/generator/{code_id}` | GET  | Generate a dynamic Flowcode image that scans to the short_url of an existing code, specified by code_id. |

### Flowcode Code Templates API Endpoints

| API                     | Endpoint URL                                       | Type | Description                                                             |
| ----------------------- | -------------------------------------------------- | ---- | ----------------------------------------------------------------------- |
| List Flowcode Templates | `https://gateway.flowcode.com/v3/code-templates` | GET  | Returns a list of code template configurations accessible by this user. |
| Fetch Flowcode Template | `https://gateway.flowcode.com/v3/{template_id}`  | GET  | Returns metadata for a specified Flowcode template.                     |

### Analytics API Endpoints

| API                 | Endpoint URL                                                  | Type | Description                                                                                              |
| ------------------- | ------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------- |
| Get Flowcode Events | `https://gateway.flowcode.com/analytics/v2/events/flowcode` | GET  | Get events for all of your Flowcodes                                                                     |
| Get Flowpage Events | `https://gateway.flowcode.com/analytics/v2/events/flowpage` | GET  | Generate a dynamic Flowcode image that scans to the short_url of an existing code, specified by code_id. |
| Get Contacts (CRM)  | `https://gateway.flowcode.com/analytics/v2/contacts`        | GET  | Get contact info submitted on flowpages for a specific date range.                                       |

[**Full List of Analytics API Endpoints ➜**](https://developer.flowcode.com/)

---

#### 🤝 Get in Touch / Help : `help-api@flowcode.com`

#### 💡 Rate Limiting

The Flowcode API sets a limit of 100 API requests per second. Once this limit is reached the API will start returning errors with HTTP status code 429.

#### 💫 More Flowcode Platform Features

* Create, manage, and share innovative artist designed Flowcodes
* Develop Flowpages for mobile-first online destinations and digital experiences
* Real-time data and analytics, including advanced Geolocation tracking
* Enterprise-grade security and features, GDPR and CCPA compliant.
* Integrations with Zapier, Klaviyo, Hubspot, Mailchimp, and Salesforce

Learn more at [Flowcode.com ➜](https://www.flowcode.com/)
