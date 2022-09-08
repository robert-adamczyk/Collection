from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth import authenticate

from .models import Movie, Director


class TestMovieModel(TestCase):
    def setUp(self) -> None:
        """ This function inserts
        dummy data into database
        to check during testing """
        test_client = User.objects.create(username="user5", email="user5@gmail.com", password="user5account")
        self.client.force_login(test_client)
        director = Director.objects.create(director_name="Wes Ball")
        self.Movie = Movie.objects.create(title="The Maze Runner",
                                          gender="2",
                                          youtube_trailer_url="https://www.youtube.com/watch?v=AwwbhhjQ9Xk",
                                          director=director,
                                          user=test_client)

    def test_Movie_model(self):
        movie_object = Movie.objects.get(pk=1)
        expected_object_title = f'{movie_object.title}'
        expected_object_gender = f'{movie_object.gender}'
        expected_object_youtube_trailer_url = f'{movie_object.youtube_trailer_url}'
        expected_object_director = f'{movie_object.director}'
        expected_object_user = f'{movie_object.user}'
        self.assertEqual(expected_object_title, 'The Maze Runner')
        self.assertEqual(expected_object_gender, '2')
        self.assertEqual(expected_object_youtube_trailer_url, 'https://www.youtube.com/watch?v=AwwbhhjQ9Xk')
        self.assertEqual(expected_object_director, 'Wes Ball')
        self.assertEqual(expected_object_user, "user5")

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies_collection/movie_list.html')

    def test_movie_details(self):
        response = self.client.get('/movie/1/')
        no_response = self.client.get('/movie/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'movies_collection/movie_detail.html')

    def test_new_movie_view(self):
        response = self.client.post(reverse('movie-create'),
                                    {
                'title': 'New title',
                'gender': '1',
                'youtube_trailer_url': 'https://www.youtube.com/watch?v=zc8XXv3pl10',
                'director': 'Dir_tester',
                'user': 'Tester'
            })
        self.assertEqual(response.status_code, 200)

    def test_movie_update_view(self):
        response = self.client.post(reverse('movie-edit', args='1'),
                                    {
                'title': 'Update title',
                'gender': '2',
                'youtube_trailer_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0',
                'director': 'Dir_tester_update',
            })
        self.assertContains(response, 'title')
        self.assertContains(response, 'director')
        self.assertEqual(response.status_code, 200)

    def test_movie_delete_view(self):
        response = self.client.get(reverse('movie-delete', args='1'))
        self.assertEqual(response.status_code, 200)


class RegisterTests(TestCase):
    def setUp(self) -> None:
        """ This function inserts
        dummy data into database
        to check during testing """
        self.user = get_user_model().objects.create_user(
            username='testuser1',
            email='testuser@email.com',
            password='testuser1account',
        )
        self.user.save()

    def test_register_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/register.html')

    def test_register_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/register.html')

    def test_user_is_sign_up(self):
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_user_is_authenticated(self):
        user = authenticate(
            username='testuser1',
            email='testuser@email.com',
            password='testuser1account',
        )
        self.assertEqual(user.is_authenticated, True)

    def test_delete_user(self):
        self.user.delete()
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 0)

    def test_wrong_username_log_in(self):
        user = authenticate(
            username='te',
            email='testuser@email.com',
            password='testuser1account',
        )
        self.assertTrue(user is None)

    def test_wrong_password_log_in(self):
        user = authenticate(
            username='testuser1',
            email='testuser@email.com',
            password='test',
        )
        self.assertTrue(user is None)

    def test_correct_log_in(self):
        user = authenticate(
            username='testuser1',
            email='testuser@email.com',
            password='testuser1account',
        )
        self.assertTrue((user is not None) and user.is_authenticated)


