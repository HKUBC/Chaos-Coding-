from app.model.item import Item

class ItemService:
    """
    A simple service to fetch Item objects from item IDs.

    """
    
    # Returns the item for a given id
    def get_item(self, item_id: str) -> Item | None:
        return self.items.get(item_id)