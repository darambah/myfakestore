# FakeStore API Test Suite (Cox Automotive QA Tech Test)

This project contains an automated test suite written in Python using `pytest`.  
The tests validate user workflows against the [FakeStore API](https://github.com/keikaavousi/fake-store-api), which simulates a fictitious online store.

# Requirements

- Python 3.8+
- `pytest`
- `requests`

Install dependencies:

```bash
pip install -r requirements.txt
```

# Run test
pytest


pytest test/

# Notes

The FakeStore API is stateless:
Products added via POST /products do not persist in subsequent GET /products requests.
This causes some listing checks to fail, though they are written correctly as per real-world expectations.

# Future Improvements

To keep the tests clean and DRY (Don't Repeat Yourself), I would extract reusable functions (e.g., add_product, get_product_by_title) into a separate module such as utils/api_helpers.py. These helper methods would:

- Accept parameters for product data
- Encapsulate the logic for interacting with the API
- Improve test readability and reduce repetition
- 

# Performance test with Jmeter

To test for performance and to make sure the store meets performance targets I would run the following test;
- GET/products, Ger/products/{ID}
- Adding to car: POST/carts
- Checkout flow: Post/orders
- stress test ramping users from 100+ observe what point errors start to occur
- soak test with about 50 request for  1-2 hours and observe how the system behaves

# Security test with OWASP ZAP & Burp Suite
- OWASP ZAP Scan to uncover injection, XSS, broken auth, and insecure configurations.
- Proxy via Burp Suite: Intercept all API calls, enable Burp’s Active Scanner, and fuzz parameters to detect input‐validation and session management flaws 

From my findings I would document all medium to high-risk issues
