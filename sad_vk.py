import vk_api



from vk_api.longpoll import VkLongPoll, VkEventType

from random import randint

key ="2767b6f40dd752513111457a96caa1980352446dda9e1ec34ba844bae28a9a84149e305d06f4d0b2f192c" 
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
    from random import randint
    vk.method('messages.send',
              {'user_id': user_id,
               "random_id":randint(1,1000) ,
               'message': message,}
              )
WHAT = """what?
    supported commands:
    hello
            game
кот
"""
dev_id = 632098697
send_message(dev_id,' hi i am alive')
debug = False
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            if user_id == dev_id:
                if text == 'debug':
                    debug = not debug
                    send_message(dev_id,'debug is now '+str(debug))
                if debug:
                    text = ''
                    for i in dir(event):
                        if i[0]!='_':
                            send_message(dev_id,i+' : '+str(eval('event.'+i)))
                    continue
            if text == "hello":
                send_message(user_id, "hello")
                
            elif text == "game":
                game_mode = True
                chislo = randint(1,100)
                send_message(user_id, "lets go!")

            elif game_mode:
                x = int(text)
                if chislo < x:
                    send_message(user_id, "моё число меньше (-) ")
                elif chislo > x:
                    send_message(user_id, "моё число больше (+) ")
                elif chislo == x:
                    send_message(user_id, "You are winner! I lose  :(")
                    game_mode = False
            
                
            elif "кот" in text:
                send_message(user_id, "мяу")
                
            elif "пока" in text:
                send_message(user_id, "пока")

            elif "ranster" in text:
                send_message(user_id, "Error999999999999999999999999")

            elif "почему ошибки" in text:
                send_message(user_id, "Откуда мне знать?")

            elif "спроси меня" in text:
                send_message(user_id, "ок, как посмотреть мне на небо?")

            elif "" in text:
                send_message(user_id, "")

                
                
            else:
                send_message(user_id, WHAT)
                
            
