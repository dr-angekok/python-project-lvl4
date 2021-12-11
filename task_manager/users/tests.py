from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

USER_NAMES = ('Igor', 'Oboev', 'Nadoev')

TEST_CASE = (
    (('/users/', '/login/',
      {'username': 'Igor', 'password': 'password!@#$123'}), ('"success">Вы залогинены<',)),
    (('/users/', None,
      None), USER_NAMES,),
    (('/users/', '/users/2/delete/',
     None), (USER_NAMES[1], '>У вас нет прав для изменения другого пользователя.<')),
    (('/users/', '/users/2/update/',
     None), ('>У вас нет прав для изменения другого пользователя.<',)),
    (('/users/', '/logout/',
     None), ('>Вы разлогинены<',)),
    (('/users/', '/login/',
      {'username': USER_NAMES[1], 'password': 'password!@#$123'}), ('>Вы залогинены<',)),
    (('/users/', '/users/2/delete/',
      None), ('>Пользователь успешно удалён<',)),
)


class UserTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        for name in USER_NAMES:
            self.user = User.objects.create_user(
                username=name,
                password='password!@#$123',)
        self.client = Client()

    def get_page(self, get_link, post_link=None, post_data=None):
        if post_link:
            self.client.post(post_link, post_data)
        response = self.client.get(get_link)
        return response.content.decode("utf-8")

    def test_users(self):
        client = Client()
        response = client.post('/login/', {'username': 'Igor', 'password': 'password!@#$123'})
        self.assertEqual(response.status_code, 302)

        for prepear_data, cases in TEST_CASE:
            get_link, post_link, post_data = prepear_data
            content = self.get_page(get_link, post_link, post_data)
            for case in cases:
                self.assertTrue(content.__contains__(case))
