
# How to create a new message handling plugin

Just add a new file and define the following function:

```
async def index(message):
    YOUR_CODE
    ...
    await message.reply("whatever you want to post", reply=False)

```

also, to register the trigger for your function, define any of these:

```
COMMANDS = ["telegram command that should call your function"]
REGEXP = "regexp for messages that are not commands but should trigger"
CONTENT_TYPES = ["aiogram content types that trigger it"]
```


