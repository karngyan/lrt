from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

  def test_create_user_with_email_successful(self):
    """Test creating a new user with an email is successful"""
    email = 'mail@karngyan.com'
    password = '123456'
    user = get_user_model().objects.create_user(
      email=email,
      password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_normalized(self):
    """Test the email for a new user is normalized"""
    email = 'test@KARNgyan.com'
    user = get_user_model().objects.create_user(email, '123456')

    self.assertEqual(user.email, email.lower())
  
  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, '1234')

  def test_create_new_super_user(self):
    """Test creating a new super user"""
    user = get_user_model().objects.create_superuser(
      'super@karngyan.com',
      '123456'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
    