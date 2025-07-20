def get_cheapest_product(products):
    """
    Filters out products that are 'out of stock', based on having zero or missing rating.count.
    Then returns the product with the lowest price.
    """
    filtered = [
        p for p in products 
        if p.get("rating", {}).get("count", 0) > 0
    ]
    return min(filtered, key=lambda p: p["price"]) if filtered else None


def get_lowest_rated_product(products):
    """
    Returns the product with the lowest customer rating.
    Defaults to 5 (maximum rating) if rating is missing.
    """
    return min(
        products,
        key=lambda p: p.get("rating", {}).get("rate", 5),
        default=None
    )
