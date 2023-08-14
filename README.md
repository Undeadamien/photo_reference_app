# Magic Card Reference App

The Magic Card Reference App is a GUI application that provides users with an extensive collection of Magic card illustrations for drawing practice.
The app allows users to set a timer and interact with the Scryfall API to fetch card images online or choose images from their local computer.

## Features

-   **Built-in Timer:** The app comes with a timer feature, allowing users to set a specific duration for their drawing sessions. Users can adjust the timer to their preferred drawing time.
-   **Online and Local Image Selection:** Users have the option to fetch card images from the Scryfall API or choose images locally.
-   **Advanced Filtering Options:** The API enables users to apply filters to specify card attributes, such as the card artist. To use the filtering option, you just need to insert the query inside the config file or keep it empty to apply no filter.
    For more informations https://scryfall.com/docs/syntax

```json
"query": "(a:magali or a:john) and (art:warrior)"
```

![image](https://github.com/Undeadamien/photo_reference_app/assets/126392901/d9ddfd84-4336-42db-b5e1-65de4558889e)
