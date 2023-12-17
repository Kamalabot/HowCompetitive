from django.test import TestCase
from django.urls import reverse
from .models import Customer, Products

# Create your tests here.

class ProductIndexViewTests(TestCase):
    def test_product_customer_index(self):
        """Tests Index view by looking at the data. Initially there will be nothing"""
        response = self.client.get(reverse('index'))
        # status code has to be 200
        self.assertEqual(response.status_code, 200)
        # response should return empty list of lists
        self.assertEqual(response.json(), [[], []])

    def test_add_customer(self):
        """Tests by adding customer to the data, and checking the output"""
        response = self.client.post(reverse('add_customer'),
                                    data={"name": "maru", "location": "bozo"})
        self.assertEqual(response.status_code, 200)
        # get the customer objects
        customers = Customer.objects.all() 
        # assert that there is only single customer data
        self.assertEqual(len(customers), 1)

    def test_add_product(self):
        """Tests by adding producte to the data, and checking the output"""
        response = self.client.post(reverse('add_product'),
                                    data={"name": "lego", "cost": 57, "qty": 7})
        self.client.post(reverse('add_product'),
                         data={"name": "lego", "cost": 57, "qty": 7})

        self.assertEqual(response.status_code, 200)
        # get the customer objects
        products = Products.objects.all()
        # assert that there is only single customer data
        self.assertEqual(len(products), 2)
 
    def test_update_product(self):
        """Tests the product data update in the database"""
        self.client.post(reverse('add_product'),
                         data={"name": "lego", "cost": 57, "qty": 7})
        # print(reverse("update_product", kwargs={'pk': 1}))
        response = self.client.put(reverse("update_product", kwargs={'pk': 1}),
                                    data={"name": "Arduino", "cost": 57,
                                         "qty": 2})
        self.assertEqual(response.status_code, 200)
        product = Products.objects.filter(pk=1)
        print(product)
        self.assertEqual(product.name == 'arduino')
        self.assertEqual(product.cost == 57)
        self.assertEqual(product.quantity == 2)

    def test_delete_product(self):
        """Tests the product data is deleted in the database"""
        self.client.post(reverse('add_product'),
                         data={"name": "lego", "cost": 57, "qty": 7})
        # print(reverse("update_product", kwargs={'pk': 1}))
        response = self.client.delete(reverse("delete_product", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 204)
        product = Products.objects.all()
        self.assertEqual(len(product), 0)
    