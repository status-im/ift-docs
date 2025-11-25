This section describes the most common style elements and conventions in the Status user documentation. The goal is to simplify the writer's workflow using unambiguous guidelines that are easy to remember and follow.

For most of our style conventions, you can find both the *correct* and *incorrect* use examples in this guide. In many cases, the *incorrect* examples are valid and commonly used sentences in English. They're incorrect only in the context of this style guide and the Status technical documentation.

We prioritize simplicity over comprehensiveness. If you can't find a particular style convention, use the [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/). If you think a style convention is missing, you can contribute to this guide.

# Admonitions

- Logos documentation uses three different types of callouts:

    | Callout | Description |
    |:-----------|:------------|
    | **Tip**    | Helpful information that is not required for the task, such as a keyboard shortcut. |
    | **Note**   | Relevant information for completing the task, but does not affect the user's actions. |
    | **Important**| Information that may impact the user's actions or decisions about completing the task. |
    | **Caution**| Information that may impact the user's actions or decisions about completing the task. |

- Don't use *warning*, *error*, *danger*, *bug*, *important*, or *notes*.
- In procedural steps, place the callout after the procedure. If you need an admonition for a specific step, write the admonition after the step.
- For other content, add the callout after the relevant information.

### Admonition types

> ✨ **Tip:**
>
> The blockchain records transactions in blocks, hence the term "blockchain".

> 📒 **Note:**
>
> The blockchain records transactions in blocks, hence the term "blockchain".

> 🖐 **Important:**
>
> If you choose the CLI installation option, you must first export the API key as an environment variable.

> ⚠️ **Caution:** 
>
> The blockchain records transactions in blocks, hence the term "blockchain".

# Bullet lists

- Don't use a bullet list for actions that users should complete in an orderly manner; use numbered lists in procedures.
- Use a bullet list to improve the readability of sentences or paragraphs where you list or describe three or more items.

    | Usage      | Example                                                                                           |
    |:------------|:---------------------------------------------------------------------------------------------------|
    | **Correct**| You need a machine running Ubuntu Linux with the following minimum requirements:<br>- 4 GB memory<br>- 2 TB SSD<br>- Linux 64-bit |
    | Incorrect  | You need a machine running Ubuntu Linux with the following minimum requirements: 4 GB memory, 2 TB SSD, and Linux 64-bit. |
    | Incorrect  | You need a machine with 4 GB of memory, a 2 TB SSD, and a 64-bit Ubuntu Linux operating system.  |

- Use a colon (:) before the bullet list items.
- Use periods at the end of each sentence in a bullet list for [punctuation](./punctuation-and-symbols.md). Using periods on a bullet list can be tricky. Use the following guidelines:
    - When the list items are complete sentences, use a period at the end of each sentence.
    - Don't use a period when the list items are not complete sentences or sentences with three words or less.
    - In a list with elements of more and less than three words mixed, don't use a period.
    - If one item in a column is a complete sentence, all items in that column should end with a period, even if they are a single word.
<!--
- Don't use colons after each item on a list; type the item definition on a new line. Here are some examples of using punctuation on a list:

    | Usage      | Example                                                                 |
    |:------------|:-------------------------------------------------------------------------|
    | **Correct** | - **Dependency graph**<br>  A repository graph that shows the packages and projects that the repository depends on.<br>- **Dependents graph**<br>  A repository graph that shows the packages, projects, and repositories that depend on a public repository. |
    | Incorrect  | - **Dependency graph**:<br>  A repository graph that shows the packages and projects that the repository depends on.<br>- **Dependents graph**:<br>  A repository graph that shows the packages, projects, and repositories that depend on a public repository. |
    | Incorrect  | - **Dependency graph**: A repository graph that shows the packages and projects that the repository depends on.<br>- **Dependents graph**: A repository graph that shows the packages, projects, and repositories that depend on a public repository. |
-->

> ✨ **Tip:**
>
> When you need to describe each element on a list and you have more than three elements, consider using a table instead.

# Capitalization

- Use sentence-style capitalization, including titles. That means everything is lowercase except the first word, proper nouns, like the Status product names.

    | Usage       | Example                       |
    |:------------|:------------------------------|
    | **Correct** | Configure system admin access |
    | Incorrect   | Configure System Admin Access |

- Don't capitalize words after colons, except when these words are proper nouns, acronyms, or bullet list items.

    | Usage       | Example                                                                                                                                         |
    |:------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Correct** | You can run the command-line application in several ways: using the binary, using Docker, or running as a service in Linux.                     |
    | Incorrect   | You can run the command-line application in several ways: Using the binary, using Docker, or running as a service in Linux.                     |
    | **Correct** | You can run the command-line application in several ways:<br>- Use the binary.<br>- Use Docker.<br>- Run as a service in Linux.                 |
    | Incorrect   | You can run the command-line application in several ways:<br>- use the binary<br>- use Docker<br>- run as a service in Linux.                   |
    | **Correct** | Many digital currencies use the ERC-20 standard: Status (STN), Basic Attention Token (BAT), MakerDAO (DAI), and others.                         |
    
# Checkbox lists

Use a [numbered list](./numbered-lists.md) for steps that the user can finish in one continuous session. Use a checkbox list for items that may be started, paused, and resumed later (for example, when you must wait days or weeks before the next action).

  ✅ Item 1<br>✅ Item 2<br>✅ Item 3

# Global language

- Don't use idioms, colloquial expressions, and culture-specific references. When writing examples to clarify a feature or concept, don't use historical references, brand names, social or political events, or any other topic that might be controversial or meaningless for a global audience.
- Observe the style rules for [numbers, date and time, currencies and units of measure](./14-numbers-date-and-time-currencies-and-units-of-measure.md).
- Use left and right carefully. Localized products in left-to-right (LTR) languages may have labels on the opposite side. Refer the reader to the specific UI element on the screen instead.
- Don't use pronouns like *Who*, *Whose*, or *Its*; replace the pronoun with the noun.
- Avoid using *(s)* for plural forms.

    | Usage       | Example                                                       |
    |:------------|:--------------------------------------------------------------|
    | **Correct** | Every file upload requires special permissions.               |
    | Incorrect   | The file(s) upload requires special permissions.              |
    | **Correct** | This option returns each token on your list alphabetically.   |
    | Incorrect   | This option returns the token(s) on your list alphabetically. |

# Links

Use links to other articles in the Logos documentation, but don't abuse links. For example, avoid making the topic resemble a Wikipedia article with a link in every sentence.

- Limit the links for sources outside the Logos documentation.
- Don't use links in procedural steps, except when you link to a subtask in the same article.
- In general, write the link without using the URL. If you must use the URL, omit the `https://` and the `www` parts of the URL (if the website allows this).
- Don't hide the linked content using the words _here_ or _this_. Instead, write out the content you link.

    | Usage       | Example                       |
    |:------------|:------------------------------|
    | **Correct** | For more details about tokens, check out **Understand Status tokens**. |
    | Incorrect   | For more details about tokens, check out **this** article. |

- When pointing the user to external sources, start you sentence with *For more details*.

    | Usage       | Example                       |
    |:------------|:------------------------------|
    | **Correct** | For more details about tokens, check out **Understand Status tokens**. |
    | **Correct** | For more details, check out **Understand Status tokens**. |
    | Incorrect   | To learn more about tokens, check out **this** article. |

- For links outside of the Logos documentation site, use the ↗ arrow symbol at the end of the link description. If the arrow symbol is at the end of a sentence, write a period after the symbol. 

    | Usage       | Example                       |
    |:------------|:------------------------------|
    | **Correct** | See [status.app/features ↗](https://status.app/features). |
    | Incorrect | [https://status.app/features ↗](https://status.app/features).|
    | Incorrect   | See 'Safely open apps on your Mac' at [https://support.apple.com/en-us/HT202491](https://support.apple.com/en-us/HT202491). |

# Modal verbs

Modal verbs are auxiliary verbs that modify the meaning of the main verb in a sentence. Modal verbs can be problematic in technical communication:

- Some modal verbs create a sense of uncertainty in readers.
- Using modal verbs like *should* or *must* can make your tone sound bossy and less helpful. In many cases, using the imperative is a better option. For example:

    | Tone          | Example                                      |
    |:--------------|:---------------------------------------------|
    | **Assertive** | Save your seed phrase in a secure location.  |
    | Bossy         | You should save your seed phrase in a secure location. |

- Use this reference for the most frequent modal verbs:

    | Modal verb           | Usage                                                                                                                                           |
    |:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
    | **can**              | Use to express the possibility for the user to do something, such as introducing a new concept or functionality.<br>Example: You can create multiple wallets for different purposes. |
    | **should**           | If possible, use the imperative form of the verb instead.                                                                                       |
    | **have to**          | Use *must* instead.                                                                                                                             |
    | **must**             | Use very selectively and only when it is strictly necessary for the user to do something to avoid data loss, data corruption, or unintended information disclosure. |
    | **could, would, might** | Don't use.                                                                                                                                   |
    
# Numbered lists

- When reading instructions, users understand numbered lists as actions to complete orderly. Because of this, limit the numbered lists to procedural instructions in procedure topics.
- If you must use a numbered list outside of a procedure, use the same rules described for bullet lists.
- Use "1." for all items in a Markdown numbered list. This ensures the Markdown list renders correctly and simplifies reordering.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | 1. Open the web page in your browser.<br>1. Click the "Sign In" button.<br>1. Enter your credentials. |
    | Incorrect   | 1. Open the web page in your browser.<br>2. Click the "Sign In" button.<br>3. Enter your credentials.  |

# Numbers, date and time, currencies, and units of measure

- In body text, always use numerals (for example, 2, 5, 21). Don't spell out whole numbers (two, five, twenty-one).
- For decimals, always begin with a zero before the decimal point and use a dot (.) as the decimal separator. Do not spell out decimals.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | 20.23   |
    | **Correct** | 0.13    |
    | Incorrect   | 0,13    |

- When writing in English, use a space as the thousand separator and a period (.) as the decimal separator to improve readability. For languages other than English, use the commonly accepted rule in the country or a comma if a common practice is unknown or controversial.

> 📒 **Note:** 
>
> There isn't a common notation for thousand and decimal separators and notation varies among different countries. In the United States, the decimal separator is a period (.) and the thousands separator is a comma (,). In Germany, the decimal separator is a comma (,) and the thousands separator is a period (.). In Sweden, the thousands separator is a space.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | 2 500     |
    | Incorrect   | 2500      |
    | **Correct** | 12 500    |
    | Incorrect   | 12.500    |
    | **Correct** | 2 500.46  |
    | Incorrect   | 2 500,46  |
    | **Correct** | 118 000   |
    | Incorrect   | 118,000   |
    | **Correct** | 118 000 000  |
    | Incorrect   | 118'000'000  |

- Don't use *rd.* or *th.* to express dates or indicate the order of things.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | Choose the options in rows 3 and 5.     |
    | Incorrect   | Choose the options in the 3rd and the 5th rows.      |

- Different countries use different ways of writing days as numerals. Write out the date to avoid confusion.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | The latest version was released on May 6, 2024.     |
    | Incorrect   | The latest version was released on 05/06/24.      |
    | Incorrect   | The latest version was released on the 6th of May, 2024.      |

- For writing decades, use two-digit numbers with an apostrophe (') before and the *s* letter after the number (for example, *'90s*).
- To describe a time, use the 12-hour clock with lowercase a.m./p.m. notation after the time. Don't write out the time.

    | Usage       | Example              |
    |:------------|:---------------------|
    | **Correct** | 1 p.m.               |
    | Incorrect   | 13 h.                |
    | Incorrect   | 1pm                  |
    | Incorrect   | 1 PM                 |
    | **Correct** | 8:30 p.m.            |
    | Incorrect   | half past eight      |

- Use the [UTC time standard](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) when writing for a global audience.
- For cryptocurrencies, NFTs, or DeFi tokens, use the symbol described on their website or use the symbol from [CoinMarketCap](https://coinmarketcap.com/) or [CoinGecko](https://www.coingecko.com/).
- For crypto amounts, place the symbol after the number.
- For fiat currencies, use the [ISO4217](https://www.iso.org/iso-4217-currency-codes.html) currency symbol after the amount. If you're using fiat to illustrate a concept, use [the most popular currencies](https://en.wikipedia.org/wiki/Template:Most_traded_currencies) like the US dollar (USD), Euro (EUR), or Japanese yen (JPY).
- For units of measure, use the [metric system](https://en.wikipedia.org/wiki/Metric_system) and, if necessary, include the [imperial units](https://en.wikipedia.org/wiki/Imperial_and_US_customary_measurement_systems#Comparison_of_imperial_and_US_customary_systems) conversion in parentheses immediately after.

# Other style conventions

- Use everyday language. Don't use jargon, technicalities, flowery or made-up words, or wordy constructions. Write as if you're talking to a client on a sync: don't be too casual but remember to sound human.
- Use verbs instead of nouns wherever possible. Rephrase the sentence if necessary. Verbs bring dynamics and help keep the reader engaged.
- It's OK to repeat important information throughout the text.
- Use gender-neutral language. Don't use _he_ and _she,_ _him_ or _her_, _he/she_ or similar. Instead, use _they_ and neutral nouns like _user_, _administrator_, or _content creator_. Use the plural form wherever possible.
- Use the same term for the same concept consistently. Avoid using synonyms to refer to the same idea or feature.
- Use _log in to_ and _sign in to_, not _log into_ or _sign into_.
- Treat the word _data_ as a plural noun. For example, "Your Status profile data are temporarily stored on the Waku network".
- Don't use _we recommend..._ or _Logos recommends..._. Recommendations create doubts in the reader's mind. Instead, explain to users what to do and, if necessary, the consequences of doing or not doing it.
- Don't use _please_ in technical documentation. Readers look for assertiveness when reading instructions.
- Don't try to be funny, express emotions with exclamation marks, or ask readers rhetorical questions. Users are not interested in reading prose but in getting things done.

    | Usage       | Example                                                       |
    |:------------|:--------------------------------------------------------------|
    | Incorrect   | Want to personalize and customize your profile for how it appears to other Community members? If so, follow these instructions below!              |

- It's OK to use prepositions at the end of sentences (for example, _the user you're searching for_).
- Don't use italics or quotes to introduce a new concept; in general, don't use them on any part of the text (except when writing about UI elements that use italics or quotes.)
- Use code formatting to distinguish parameters or options from the rest of your text when discussing them outside of procedure steps.

    | Usage       | Example                                                                                  |
    |:------------|:-----------------------------------------------------------------------------------------|
    | **Correct** | You can use the `Is Allowed` and `In options` to modify the permission scope.            |
    | Incorrect   | You can use the Is Allowed and In options to modify the permission scope.                |
    | Incorrect   | You can use the **Is Allowed** and **In** options to modify the permission scope.        |

- Avoid sentence connectors, such as _therefore_, _hence_, or _as a consequence_. Rephrase the sentence if necessary.
- Don't use adjectives to describe a task's difficulty or the time required to complete it.

    | Usage       | Example                                          |
    |:------------|:-------------------------------------------------|
    | **Correct** | You can easily set up your community.            |
    | Incorrect   | Using our app, you can mint your NFT in no time. |

- Keep phrasal verbs together.

    | Usage       | Example                                          |
    |:------------|:-------------------------------------------------|
    | **Correct** | Execute the command `shutdown -h now` to shut down the server. |
    | Incorrect   | Execute the command `shutdown -h now` to shut the server down. |

- Avoid referring to the document itself using _On this procedure_, _In this document_, _In the following list_, _In this section_, or similar expressions. Use _here_ instead.

    | Usage       | Example                                                                |
    |:------------|:-----------------------------------------------------------------------|
    | **Correct** | Here you can find the list of keyboard shortcuts.                      |
    | Incorrect   | In the following section, you can find the list of keyboard shortcuts. |

# Possessive form

- Use the possessive form with caution and avoid complex possessive forms like the [compound possessive](https://www.grammarly.com/blog/possessive-case/). Some non-native English readers may have problems understanding sentences with possessive forms.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | [...] your contact's status. |
    | Incorrect   | your contact's verified status.    |
    | **Correct** | [...] the verified status of the contact. |
    | **Correct** | [...] the picture shared by you and your trusted contact. |
    | Incorrect   | [...] you and your trusted contact's shared picture.    |

- Use a single straight quotation mark (') apostrophe. Don't use curly quotation marks (also known as smart quotes.)
- If you must use a passive form with a proper name ending with the possessive *s*, add the apostrophe at the end without an extra *s* letter.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | Check your contacts' list. |
    | Incorrect   | Check your contacts's list.    |

- If the possessor is not a person, you don't need to add an apostrophe to show possession.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | Verify the contact's ENS name on the Status details screen. |
    | Incorrect   | Verify the contact's ENS name on the Status' details screen.    |
    | **Correct** | Your profile information stays in your browser cache. |
    | Incorrect   | Your profile information stays in your browser's cache.    |

# Punctuation and symbols

- Avoid. Unnecessary. Punctuation.
- Use these guidelines for commas:
    - Use commas to separate main clauses.
    - Use a comma before *such as*.
    - Use a comma after *for example*.
    - Use the Oxford comma for *and* and *or* conjunctions.
    - In procedural steps, don't write a comma in sentences such as *click on cancel, and then...*
- Use these guidelines for periods:
    - Use a period at the end of a sentence, including sentences ending on a [URL](./links.mdx).
    - Observe the punctuation rules for items on a [bullet list](./bullet-lists.mdx).
    - Observe the punctuation rules for items on a [table](./tables.mdx).
- Don't use semicolons. Instead, use a period and write the text after the semicolon in a new sentence.
- Avoid preceding tables with colons. Instead, use a period.
- Don't use dashes (_em_ or _en_ dashes.) Instead, use parenthesis if you need to clarify information.
- Use parenthesis sparingly, and don't write essential information inside parenthesis.
- Don't use bold or italics with punctuation symbols.
- When you must use quotes, use double straight quotes. Don't use quotes with user interface elements.
- Observe the [bullet lists](./06-bullet-lists.md) punctuation rules.
- To spell out symbols and punctuations marks, use the [List of typographical symbols and punctuation marks](https://en.wikipedia.org/wiki/List_of_typographical_symbols_and_punctuation_marks) article from Wikipedia.

    | Usage       | Example                                                       |
    |:------------|:--------------------------------------------------------------|
    | **Correct** | To quote text inline, use the greater-than sign (`>`) before your text.  |
    | Incorrect   | To quote text inline, use the bigger-than sign (`>`) before your text.  |

# Sentences and paragraphs

- Write sentences of a maximum of 25 words and paragraphs of no more than 100 words. Rewrite the content and break sentences and paragraphs as necessary.
- Include *the* and *that* to clarify your sentence.

    | Usage      | Example                                         |
    |:-----------|:------------------------------------------------|
    | **Correct**   | Identify the chart settings that affect the layout.   |
    | Incorrect  | Identify chart settings affecting the layout.           |
    | **Correct**   | The database that is online syncs every 30 seconds.  |
    | Incorrect  | The online database syncs every 30 seconds.             |

- Don't use sentence connectors: *So*, *Thus*, *Therefore*, *Consequently*, *As a consequence*, *For this reason*, *Hence*, and so on.

    | Usage      | Example                                                                 |
    |:-----------|:------------------------------------------------------------------------|
    | **Correct**   | Your seed phrase provides access to your crypto assets. Keep your seed phrase safe. |
    | Incorrect  | Your seed phrase provides access to your crypto assets. Therefore, keep your seed phrase safe. |

- Avoid long [noun phrases](https://en.wikipedia.org/wiki/Noun_phrase). If you use a noun phrase, don't use more than one modifier. Use the *of* preposition to simplify noun phrases.

    | Usage      | Example                                      |
    |:-----------|:---------------------------------------------|
    | **Correct**   | The default lifetime of a token value is one year. |
    | Incorrect  | The default token value lifetime is one year.         |

- Keep adjectives and adverbs immediately before the word they modify. Pay close attention to *only* and *not*.

    | Usage      | Example                                 |
    |:-----------|:----------------------------------------|
    | **Correct**   | You can access your messages only after 30 days. |
    | Incorrect  | You can only access your messages after 30 days.    |

- In the first paragraph after a heading, avoid repeating the title information. For example, if the heading title is "Search for a contact using the Status display name," don't start the first paragraph with "To search for a contact using the Status display name [...]"
- Lookup for instances of the *which* word on your text; it's possible you can replace them with *that*. For more information about the differences between *which* and *that*, check out this [Grammarly article](https://www.grammarly.com/blog/which-vs-that/).

# Tables

Tables provide a simple way to summarize information. Use a table instead of [bullet lists](./06-bullet-lists.md) when you need to describe the elements on the list.

- Bullet list example (incorrect):

  There are four types of items:

  - **Item 1** <br>Item 1 description
  - **Item 2** <br>Item 2 description
  - **Item 3** <br>Item 3 description
  - **Item 4** <br>Item 4 description

- Table format example (**correct**):

    | Item   | Description          |
    |:-------|:---------------------|
    | Item 1 | Item 1 description |
    | Item 2 | Item 2 description |
    | Item 3 | Item 3 description |
    | Item 4 | Item 4 description |

You can also use tables to compare the available options across different elements.

    | Features   | Desktop | Mobile | Web |
    |:-----------|:--------|:-------|:----|
    | Feature A  |   ✅    |   ✅   |     |
    | Feature B  |   ✅    |        |     |
    | Feature C  |         |   ✅   | ✅  |

> ✨ **Tip:**
>
> You can use links in tables except if the table is part of a procedural step.

Use the following guidelines when using periods in a table for punctuation:

- End every complete sentence inside tables with a period.
- Use periods when there are multiple sentences in one table cell.
- Keep table columns parallel. If one item in a column is a complete sentence, all items in that column should end with a period, even if they are a single word. This rule applies to each column individually, not across the entire table.

# Titles

- Use the rules described in the [Structure the content](../10-structure-the-content/_index.md) section for each document type.
- Use meaningful titles that provide a precise idea of the article's content.

    | Usage     | Example |
    |:----------|:--------|
    | **Correct** | Upload a file using Codex  |
    | Incorrect   | Upload a file    |
    | Incorrect   | Uploading a file using Codex   |

- Adhere to the [capitalization convention](./capitalization.md).
- Don't use colons (:) in titles.
- The title of your article determines the Markdown file name:
    - Use the title of the article in all-lowercase letters for the Markdown file name.
    - Use a dash symbol ("-") to replace spaces.
    - Don't exclude articles, prepositions, or any other word in the Markdown file name.
    - If the name includes apostrophes, remove them from the Markdown file name. If the apostrophe is part of the possessive form with an extra *s* letter, separate the letter in the name (example: `transfer-you-community-s-ownership`).

    | Usage       | Article name                              | .md file name                           |
    |:------------|:------------------------------------------|:----------------------------------------|
    | **Correct** | Upload a file using Codex                 | upload-a-file-using-codex.md            |
    | **Correct** | Transfer your community's ownership       | transfer-your-community-s-ownership.md  |
    | Incorrect   | Transfer your community's ownership       | transfer-your-communitys-ownership.md   |
    | Incorrect   | Browse people and Communities in Status   | Browse-people-and-Communities-in-Status.md |
    | Incorrect   | Browse people and Communities in Status   | browse-people-communities-status.md     |
    | **Correct** | FAQ: Import data from Discord             | faq-import-data-from-discord.md         |
    | **Correct** | Do's and don'ts of Profile security       | dos-and-donts-of-profile-security.md    |

# UI elements

UI elements are screen components the user can interact with. A checkbox, a menu, or a button are all UI elements. An explanatory text with no user interaction is not considered a UI element in the context of this guide.

### General guidelines

- Don't write the type of the UI control (button, drop-down menu, radio button, etc.), except when it isn't clear you're referring to the UI control. The exceptions to this rule are *pop-up menu* and *check the [...] box.*

    | Usage       | Example                                                          |
    |:------------|:-----------------------------------------------------------------|
    | **Correct** | To publish your token, click **Publish**.                        |
    | Incorrect   | To publish your token, click the **Publish** button.             |
    | **Correct** | On the **Permission** pop-up menu, tap the **Write** permission. |
    | Incorrect   | On the **Permissions** pop-up, tap the **Write** permission.     |
    | Incorrect   | On **Permissions**, tap the **Write** permission.                |

- When describing actions across different screens or menu options, use angle brackets (>) to describe the sequence of UI elements.

    | Usage       | Example                                                            |
    |:------------|:-------------------------------------------------------------------|
    | **Correct** | Go to **Settings > Messages > Privacy**.                           |
    | Incorrect   | Go to **Settings**, then go to **Messages**, then tap **Privacy**. |

- Don't describe to users what's happening on the screen, unless the result is unexpected.

    | Usage       | Example                                                                                        |
    |:------------|:-----------------------------------------------------------------------------------------------|
    | **Correct** | 1. Select Change.</br>2. On the Options dialog, uncheck the Automatic box.                      |
    | Incorrect   | 1. Select Change. A new Options dialog opens.</br>2. On this dialog, uncheck the Automatic box. |

- When the action occurs in a specific menu or area in the user interface, write the location before the action.

- Write the result of the action first and then the condition for the result.

    | Usage      | Example                                             |
    |:-----------|:----------------------------------------------------|
    | **Correct**   | From the **Settings** option, change your profile picture.      |
    | Incorrect     | Change your profile picture in the Settings option.             |
    | **Correct**   | In **Available tokens**, tap **Change token**.           |
    | Incorrect     | Tap **Change token** in the **Available tokens** menu.   |

- To describe menus or buttons in a particular user interface area, follow the order of the interface itself, going from left to right and from top to bottom. This means that if the user has the option to choose between *save* and *cancel* buttons, and the *save* button appears first, you should describe them in that order.

### Format guidelines

- Format the UI element as seen on the screen, even if it contradicts the style conventions in this guide.
- Write out the entire UI label, as seen on the screen.

    | Usage       | Example                                                                                |
    |:------------|:---------------------------------------------------------------------------------------|
    | **Correct** | Check **I understand this is the only time I can see my recovery phrase in the app**. |
    | Incorrect   | Check **I understand this is ...**.                                                    |

- Use a bold typeface to write UI controls in procedural steps (1, 2, 3, and so on). Don't use the bold typeface outside of the procedural steps.

    | Usage | Example |
    |:---|:---|
    | **Correct** | You can use the Share action to send pictures or documents:</br>1. Tap **Messages**.</br>2. Tap the picture and tap **Share**. |
    | Incorrect | You can use the **Share** action to send pictures or documents:</br>1. Tap on the **Messages** button.</br>2. Choose the picture and tap **Share**. |

- When you write UI areas or sidebars, use a bold typeface only for the visible part in the UI.

    | **Usage**   | **Example**                                                      |
    |:------------|:-----------------------------------------------------------------|
    | **Correct** | From the navigation sidebar, click your profile picture.         |
    | Incorrect   | From the **navigation sidebar**, click your **profile picture**. |
    | **Correct** | From the **Settings** sidebar, click **Network Settings**.       |
    | Incorrect   | From the Settings sidebar, click **Network Settings**.           |
    | Incorrect   | From the **Settings sidebar**, click **Network Settings**.       |

### Name conventions

- Use *screen* (unbolded) to refer to the current screen in an app. Don't use *window*, *option*, or *dialog*.

    | Usage       | Example                                                       |
    |:------------|:--------------------------------------------------------------|
    | **Correct** | On the **Wallet** screen, tap **New** to create a new wallet. |
    | Incorrect   | On the **Wallet** window, tap **New** to create a new wallet. |

- Use *area* or *sidebar* (unbolded) to describe a particular group of elements on the current screen. Don't use *section*, *panel*, or *pane*.

    | Usage       | Example                                                                |
    |:------------|:-----------------------------------------------------------------------|
    | **Correct** | In the content area, right-click your message and click **Edit**.  |
    | Incorrect   | In the content panel, right-click your message and click **Edit**. |
    | **Correct** | From the navigation sidebar, click your profile picture.               |
    | Incorrect   | From the navigation section, click your profile picture.               |
    | Incorrect   | From the **navigation** sidebar, click your profile picture.           |

### User actions

When you describe a UI interaction, use these action verbs:

| Action | Style convention (desktop, web, and mobile) |
|:---|:---|
| Go to a menu or screen | Use *go to*. |
| Click a URL | Use *check out*. |
| Select a single UI element | Select. |
| Select one or more user-preferred options from a list | *choose* </br>Example: *Choose a name and highlight colour for your group chat*. |
| Select one or more specific option from a list / select text | *select* </br>Example: *Select the channel with a lock icon from the channel list*. |
| Action on checkboxes | *check* the [UI label] box (to enable) / *uncheck* the [UI label] box (to disable). |
| Action on switches | *turn on*/*turn off* |
| Go to previous screen | Use *return to*. |
| Swipe element | Use *swipe* [left or right]. |
| Long press | *long press* for mobile interactions, when required. |
| Right click | *right click* for desktop and web interactions, when required. |
| Start session | *log in* (verb) or *login* (noun). |
| End session | *log out* (verb) or *logout* (noun). |

# Writing style

- Address the user using *you* or *your*.
- Use the active voice to emphasize that the action is on the user, not the software. Sometimes a passive sentence is unavoidable, and that's OK.

    | Usage       | Example                                                                 |
    |:------------|:------------------------------------------------------------------------|
    | **Correct** | Click Block User to block messages from the user.                      |
    | Incorrect   | The Block User option must be selected to block messages from the user. |

- Write in the present tense. Avoid using the future tense or variations of the present tense, such as the present perfect tense.

    | Usage       | Example                                                                     |
    |:------------|:----------------------------------------------------------------------------|
    | **Correct** | If you tap Untrust, you should complete a mutual verification again.       |
    | Incorrect   | If you tap Untrust, you will need to complete a mutual verification again.  |
    | **Correct** | You can see the new badge after you complete the mutual verification.       |
    | Incorrect   | You will see the new badge once you have completed the mutual verification. |
