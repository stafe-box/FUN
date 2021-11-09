from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id


login, password = '89227617166', 'aap:%5D84A*jsN:qt'
vk_session = VkApi('login', 'password')
vk_session.auth(token_only=True)

vk = vk_session.get_api()

vk.messages.send(user_id=202148794, message='Сообщение', random_id=get_random_id())

