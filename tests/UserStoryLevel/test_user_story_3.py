from utils.api_helpers import get_lowest_rated_product

def test_delete_lowest_rated_product(session, base_url):
    """
    User Story 3:
    As a store admin, I want to delete the product with the lowest rating.

    Acceptance Criteria:
    - Product is selected based on lowest 'rate' value.
    - After deletion, it no longer appears in product list.
    - Retrieving it directly returns a 404.
    """
    products = session.get(f"{base_url}/products").json()
    target = get_lowest_rated_product(products)
    assert target is not None

    delete_resp = session.delete(f"{base_url}/products/{target['id']}")
    assert delete_resp.status_code == 200

    updated_products = session.get(f"{base_url}/products").json()
    assert not any(p["id"] == target["id"] for p in updated_products)

    fetch_resp = session.get(f"{base_url}/products/{target['id']}")
    assert fetch_resp.status_code == 404


#NOTE:
#I have written the test as per the AC - it is failing due to the following --
#Delete a product via DELETE /products/{id} returns 200 (mocked).
#But the same product still shows up in GET /products, because the API is stateless, therefore that part of the test fails.
#In a real testing situation this shouldn't be an issue as the record would actually be deleted and we could assert that