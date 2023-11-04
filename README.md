# Description
RIM, which stands for RPG Inventory Manager, is a small app designed to assist RPG Game Masters and players in managing character inventories. With RIM, users can easily add or remove items, track the states of items, and perform other inventory-related tasks.

This app provides a convenient and organized way to keep track of the various items that characters possess in the game. Whether it's weapons, armor, potions, or any other items, RIM allows Game Masters and players to efficiently manage and update the inventory as the game progresses.

By using RIM, Game Masters can easily create, modify, and assign items to specific characters. They can also track the availability and status of items, such as whether an item is equipped, stored, or consumed. This helps to streamline the gameplay experience and ensures that all players have a clear understanding of their characters' inventories.

Furthermore, RIM offers features that allow users to categorize items, search for specific items, and even generate reports and summaries of a character's inventory. This makes it easier for Game Masters to keep track of the overall game progression and helps players to make informed decisions about their characters' equipment and resources.

Overall, RIM is a valuable tool for RPG Game Masters and players, simplifying the management of character inventories and enhancing the gaming experience.
# Backend endpoints
- `/` returns dict with app version.
- `/item/`**`{item_id}`** returns item by it's _id field (exact match).
- `/item/search/`**`{regex}`** returns items by regex match in _id field (case sensitive).
- `/items` returns list of all items.
- `/items/`**`{category_id}`** returns all items in category.
- `/categories` returns category list
- `/categories/flat` returns flattened category list only with names.