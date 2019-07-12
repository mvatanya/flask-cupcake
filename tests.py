from app import app
from models import db, connect_db, Cupcake
import unittest

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes-app-test'
db.create_all()

class AppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client and make new cupcake."""

        Cupcake.query.delete()

        self.client = app.test_client()

        self.cupcake = Cupcake(
            flavor='testing', size='small', rating=10)
        db.session.add(self.cupcake)
        db.session.commit()
    
    def test_all_cupcakes(self):
        """/cupcakes should show all cupcakes using GET method"""
        response = self.client.get("/cupcakes")
        response_data = response.json['cupcakes']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, [{'flavor': 'testing', 'size': 'small', 'rating': 10,'image': 'https://tinyurl.com/truffle-cupcake'}])

    def test_creating_cupcake(self):
        """test creating /cupcakes using POST method"""
        response = self.client.post(
            "/cupcakes", json={
                "flavor": "test2", "size": "large", "rating": 100,"image": ""
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['cupcake']['flavor'], "test2")
        self.assertEqual(response.json['cupcake']['size'], "large")
        self.assertEqual(response.json['cupcake']['rating'], 100)
        self.assertEqual(response.json['cupcake']['image'], "https://tinyurl.com/truffle-cupcake")
        self.assertEqual(Cupcake.query.count(), 2)
      
