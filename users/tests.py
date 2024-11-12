from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user

class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        #Foydalanuvchini yaratamiz
        response = self.client.post(
            reverse('register'),
            data = {
            'username': 'riza',
            'first_name':'Rizamat',
            'last_name':'Khayrulloev',
            'email':'rizamat4@gmail.com',
            'password':'somepassword'
        }
        )
        #user bandligini tekshirish uchun ikkinchi userni yaratamiz
        response = self.client.post(
            reverse('register'),
             data = {
            'username': 'riza',
            'first_name':'Rizamat',
            'last_name':'Khayrulloev',
            'email':'rizamat@gmail.com',
            'password':'somepassword2'
        }
        )


        user = User.objects.get(username='riza')
        form = response.context['form']
        self.assertFormError(form, 'username', 'A user with that username already exists.')
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        self.assertEqual(response.status_code, 200) # Sahifa mavjudligin tekshiradi
        self.assertEqual(user.username, 'riza')
        self.assertEqual(user.first_name, 'Rizamat')
        self.assertEqual(user.last_name, 'Khayrulloev')
        self.assertEqual(user.email, 'rizamat4@gmail.com')
        self.assertNotEqual(user.password, 'somepassword')

    def test_required_fields(self):
        response = self.client.post(
            reverse('register'),
            data = {
                'first_name' : 'Madina',
                'last_name': 'Asadova',
                'email' : 'madina@gmail.com'                   
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        form = response.context['form']
        self.assertFormError(form, 'username', 'This field is required.')
        self.assertFormError(form, 'password', 'This field is required.')
    
    def test_invalid_email(self):
        #Foydalanuvchini yaratamiz
        response = self.client.post(
            reverse('register'),
            data = {
            'username': 'riza',
            'first_name':'Rizamat',
            'last_name':'Khayrulloev',
            'email':'rizamat4',# Noto'g'ri formatdagi email kiritdim
            'password':'somepassword'
        }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        form = response.context['form']
        self.assertFormError(form, 'email', 'Enter a valid email address.')

class LoginTestCase(TestCase):
    def test_success_logiding(self):
        db_user = User.objects.create(username='madina', first_name='Madina', last_name = 'Asadova', email='madina@gmail.com')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(
            reverse('login'),
            data={
                'username':'madina',
                'password':'somepass'
            }
        )

        db_user = get_user(self.client)
        self.assertTrue(db_user.is_authenticated)
    
    def test_wrong_username(self):
        db_user = User.objects.create(username='madina', first_name='Madina', last_name = 'Asadova', email='madina@gmail.com')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(
            reverse('login'),
            data={
                'username':'wrong-username',
                'password':'somepass'
            }
        )

        db_user = get_user(self.client)
        self.assertFalse(db_user.is_authenticated)  

        self.client.post(
            reverse('login'),
            data={
                'username':'madina',
                'password':'wrong-password'
            }
        )
        db_user = get_user(self.client)
        self.assertFalse(db_user.is_authenticated) 

        response=self.client.post(
            reverse('login'),
            data={
                'username':'',
                'password':''
            }
        )
        self.assertContains(response, 'This field is required.')
    
class BlockedUserTestCase(TestCase):
    def SetUp(self):
        #Bloklangan foydalanuvchi yaratish
        self.user = User.objects.create(username='blockeduser', password='password123')
        self.user.is_active=False
        self.user.save()
    
    def test_blocked_user_login(self):
        #Bloklangan foydalanuvchi bilan tizimga kirishga harakat qilish
        response = self.client.post(
            reverse('login'),
            data={
                'username':'blockeduser',
                'password':'password123'
            }
        )
        #Login muvaffaqiyatsiz bo'lishi va foydalanuvchu sahifaga yo'naltirilmasligi kerak
        self.assertNotIn('_auth_user_id', self.client.session)#Sessiyada foydalanuvchi ID bo'lmasligi kerak
        self.assertContains(response, 'Your account has been deactivated.')#Xato xabarini tekshirish