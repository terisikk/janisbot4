# QuoteAPI

To develop new applications that utilize QuoteAPI, request API key and swagger ui location from admin. Provide authorization header with Authorize-button and you can test the read-only queries. 

API documentation can be found from swagger, and also a link to PostgREST documentation. 

For developing your own applications, especially this bot, remember to add Authorization header to your request. 

For developing new features to JanisBot that use QuoteAPI, you can use `quote_api.py` as an example. You can use the provided token for testing in local dev env, but keep in mind that the bot uses a production API key that has full CRUD permissions. 

> :warning: Please do not commit API keys or endpoint urls directly to this public repository!

Use configuration files instead. The production config has for example the following useful items:

* QUOTE_API_TOKEN
* QUOTE_API_URL

You can use them in code for example this way: `QUOTE_API_TOKEN = cfg.get('QUOTE_API_TOKEN')`.

# LorremAPI

LorremAPI does not currently have swagger documentation, and it uses basic authentication instead of JWT tokens. However, the usage from code works about the same way. You provide the Authorization header and add the basic auth token requested from admin to it. Admin can also provide you the api endpoint for development purposes. 

The following options are in production configuration:

* LORREM_API_URL
* LORREM_API_TOKEN
