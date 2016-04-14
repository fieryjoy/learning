from django.test import TestCase
from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from tank.models import Room, Visitor, Reservation, RoomReservation

# testing models
class RoomTestCase(TestCase):
    data = {
        "capacity": 4,
        "floor_number": 1,
        "price": "35.50",
        "reserved": False,
        "room_number": 1,
        "room_type": "QUEEN",
        "smoking": False
    }

    def setUp(self):
        Room.objects.create(**self.data)

    def test_room_was_created(self):
        rooms = Room.objects.all()
        self.assertEqual(len(rooms), 1)
        room = rooms[0]
        self.assertEqual(room.price, 35.50)
        self.assertEqual(room.reserved, False)
    
    def test_reserve(self):
        room = Room.objects.get(room_number=1)
        room.reserve()
        self.assertEqual(room.reserved, True)

    def test_unreserve(self):
        room = Room.objects.get(room_number=1)
        room.unreserve()
        self.assertEqual(room.reserved, False)


class VisitorTestCase(TestCase):
    data = {
            "address": "St. Ploiesti 1C, Timisoara, Timis, Romania",
            "email": "ion@rabdare.com",
            "first_name": "Ion",
            "last_name": "Rabdare",
            "title": "Mr"
    }
 
    def setUp(self):
       Visitor.objects.create(**self.data)

    def test_visitor_was_created(self):
        visitors = Visitor.objects.all()
        self.assertEqual(len(visitors), 1)
        visitor = visitors[0]
        self.assertEqual(visitor.first_name, "Ion")
        self.assertEqual(visitor.title, "Mr")

    def test_visitor_display(self):
        visitor = Visitor.objects.get(email="ion@rabdare.com")
        self.assertEqual(str(visitor), "{}. {} {}".format(
                self.data['title'], 
                self.data['first_name'], 
                self.data['last_name']))


class ReservationTestCase(TestCase):
    data = {
            "adults": 1,
            "check_in": "2015-05-24",
            "check_out": "2015-05-25",
            "children": 0,
            "confirmed": True,
            "number_of_rooms": 1,
            "room_type": "DOUBLE",
            "smoking": False,
            "visitor": None
    }

    def setUp(self):
        Reservation.objects.create(**self.data)

    def test_reservation_was_created(self):
        reservations = Reservation.objects.all()
        self.assertEqual(len(reservations), 1)

    def test_reservation_confirm(self):
        reservation = Reservation.objects.all()[0]
        reservation.confirm()
        self.assertEqual(reservation.confirmed, True)

    def test_reservation_unconfirm(self):
        reservation = Reservation.objects.all()[0]
        reservation.unconfirm()
        self.assertEqual(reservation.confirmed, False)
    
    def test_reservation_add_visitor(self):
        reservation = Reservation.objects.all()[0]
        visitor_data = {
            "address": "St. Ploiesti 1C, Timisoara, Timis, Romania",
            "email": "ion@rabdare.com",
            "first_name": "Ion",
            "last_name": "Rabdare",
            "title": "Mr"
        }
        visitor = Visitor.objects.create(**visitor_data)
        reservation.add_visitor(visitor)
        self.assertTrue(reservation.visitor is not None)
        

class RoomReservationTestCase(TestCase):
    room_data = {
        "capacity": 4,
        "floor_number": 1,
        "price": "35.50",
        "reserved": False,
        "room_number": 1,
        "room_type": "QUEEN",
        "smoking": False
    }
    reservation_data = {
        "adults": 1,
        "check_in": "2015-05-24",
        "check_out": "2015-05-25",
        "children": 0,
        "confirmed": False,
        "number_of_rooms": 1,
        "room_type": "DOUBLE",
        "smoking": False,
        "visitor": None
    } 
    def setUp(self):
        self.room = Room.objects.create(**self.room_data)
        self.reservation = Reservation.objects.create(**self.reservation_data)
        self.room_reservation = RoomReservation.objects.create(room=self.room, reservation=self.reservation)

    def test_room_reservation_exists(self):
        room_reservations = RoomReservation.objects.all()
        self.assertTrue(len(room_reservations) > 0)
        
    def test_post_save_link_changes_fields_in_room_and_reservation(self):
        self.room_reservation.save()
        self.assertEqual(self.room.reserved, True)
        self.assertEqual(self.reservation.confirmed, True)
    
    def test_pre_delete_link_changes_fields_in_room_and_reservation(self):
        self.room_reservation.delete()
        self.assertEqual(self.room.reserved, False)
        self.assertEqual(self.reservation.confirmed, False)


class IndexViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")
        
class SuccessViewTests(TestCase):
    def test_success_view(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "mail")




class MySeleniumTests(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('alice')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('fr33mys3lf')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


