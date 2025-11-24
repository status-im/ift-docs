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
    | **Correct** | In the content area, right-click your message and and click **Edit**.  |
    | Incorrect   | In the content panel, right-click your message and and click **Edit**. |
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
