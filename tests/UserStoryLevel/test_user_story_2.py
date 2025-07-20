import pytest
import uuid

def test_add_multiple_unique_clothing_products(session, base_url):
    """
    User Story 2:
    As a store manager, I want to add 3 new clothing items with unique names to the catalogue.

    Acceptance Criteria:
    - Each product has a unique title and should be accepted.
    - Products with duplicate titles should be rejected.
    - Each new product should appear in the product listing after creation.
    """
    #TO DO: Randomly generate the payload for products (random price, description etc)
    new_products = [
        {
            "title": f"Test Jacket {uuid.uuid4()}",
            "price": 49.99,
            "description": "A lightweight test jacket",
            "category": "men's clothing"
        },
        {
            "title": f"Test T-Shirt {uuid.uuid4()}",
            "price": 19.99,
            "description": "A test t-shirt",
            "category": "men's clothing"
        },
        {
            "title": f"Test Jeans {uuid.uuid4()}",
            "price": 39.99,
            "description": "Test denim jeans",
            "category": "men's clothing"
        },
    ]

    for product in new_products:
        response = session.post(f"{base_url}/products", json=product)
        assert response.status_code in (200, 201)

        created = response.json()
        assert created["title"] == product["title"]

        # Confirm product appears in listing (failing as API is stateless)
        products = session.get(f"{base_url}/products").json()
        assert any(p["title"] == product["title"] for p in products)

# NOTE:
# I have written the test as per the AC — it is failing due to the following:
# Adding a product via POST /products returns 200/201
# But when you do a follow-up GET /products, the newly added item is not there, therefore the test fails.
# In a real testing situation this wouldn't be an issue, as the record would persist and be assertable.


def test_duplicate_product_should_be_rejected(session, base_url):
    """
    Simulates adding a duplicate product and verifies that it should be rejected.
    """
    product = {
        "title": "Duplicate Test Product",
        "price": 29.99,
        "description": "This product is used to test duplicates",
        "category": "men's clothing"
    }

    # First attempt — should succeed
    response_1 = session.post(f"{base_url}/products", json=product)
    assert response_1.status_code in (200, 201)

    # Second attempt — should fail as duplicate name
    response_2 = session.post(f"{base_url}/products", json=product)

    assert response_2.status_code == 400 or response_2.status_code == 400

# NOTE:
# FakeStore API does not actually enforce title/ID uniqueness,
# so this test will not behave as expected
# In a real-world application, this check would be valid and critical.
