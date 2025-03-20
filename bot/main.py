import telebot 
import os
import actions
from markups.filter_markup import filter_markup, get_group_markup, course_markup, get_directions_markup
from markups.admin_markups import (
    add_markup, 
    admin_get_directions_markup, 
    add_admin_markup, 
    edit_markup, 
    edit_choise_markup, 
    edit_get_directions_markup, 
    delete_markup,
    export_markup
)
from functools import partial
from dotenv import load_dotenv
from responses import *

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"), parse_mode="HTML")

@bot.message_handler(commands=['start'])
def StartSession(message):
    bot.send_message(message.chat.id, START_MESSAGE)

@bot.message_handler(commands=['help'])
def HelpMessage(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['find'])
def FindUser(message):
    bot.send_message(message.chat.id, FIND_MESSAGE)
    bot.register_next_step_handler(message, FindUserInput)

@bot.message_handler(commands=['filter'])
def FilterUsers(message):
    bot.send_message(message.chat.id, FILTER_MESSAGE, reply_markup=filter_markup)

@bot.message_handler(commands=['add'])
def AddUser(message):
    sent = bot.send_message(message.chat.id, ADD_MESSAGE)
    if actions.CheckAdmin(message.chat.username):
        bot.edit_message_text("✅ Проверка пройдена!", sent.chat.id, sent.message_id, reply_markup=add_markup)
    else:
        bot.edit_message_text("❗️ Проверка не пройдена", sent.chat.id, sent.message_id,)

@bot.message_handler(commands=['add_admin'])
def AddAdmin(message):
    sent = bot.send_message(message.chat.id, ADD_MESSAGE)
    if actions.CheckAdmin(message.chat.username):
        bot.edit_message_text("✅ Проверка пройдена!", sent.chat.id, sent.message_id, reply_markup=add_admin_markup)
    else:
        bot.edit_message_text("❗️ Проверка не пройдена", sent.chat.id, sent.message_id,)

@bot.message_handler(commands=['edit'])
def EditUser(message):
    sent = bot.send_message(message.chat.id, ADD_MESSAGE)
    if actions.CheckAdmin(message.chat.username):
        bot.edit_message_text("✅ Проверка пройдена!", sent.chat.id, sent.message_id, reply_markup=edit_markup)
    else:
        bot.edit_message_text("❗️ Проверка не пройдена", sent.chat.id, sent.message_id,)

@bot.message_handler(commands=['delete'])
def DeleteUser(message):
    sent = bot.send_message(message.chat.id, ADD_MESSAGE)
    if actions.CheckAdmin(message.chat.username):
        bot.edit_message_text("✅ Проверка пройдена!", sent.chat.id, sent.message_id, reply_markup=delete_markup)
    else:
        bot.edit_message_text("❗️ Проверка не пройдена", sent.chat.id, sent.message_id,)

@bot.message_handler(commands=['export'])
def ExportData(message):
    sent = bot.send_message(message.chat.id, ADD_MESSAGE)
    if actions.CheckAdmin(message.chat.username):
        bot.edit_message_text("✅ Проверка пройдена!", sent.chat.id, sent.message_id, reply_markup=export_markup)
    else:
        bot.edit_message_text("❗️ Проверка не пройдена", sent.chat.id, sent.message_id,)



#/find
def FindUserInput(message):
    sent_msg = bot.send_message(message.chat.id, "🔎 Ищу пользователя...")
    result = actions.FindUser(message)
    bot.edit_message_text(result, sent_msg.chat.id, sent_msg.message_id)



#/add
User = []

def AddUserFIO(message):
    Fio = message.text
    bot.send_message(message.chat.id, "Введите курс")
    bot.register_next_step_handler(message, partial(AddUserCourse, Fio))

def AddUserCourse(Fio, message):
    Course = message.text
    bot.send_message(message.chat.id, "Введите группу")
    bot.register_next_step_handler(message, partial(AddUserGroup, Fio, Course))

def AddUserGroup(Fio, Course, message):
    Group = message.text
    User.append[Fio]
    User.append[Course]
    User.append[Group]
    bot.send_message(message.chat.id, "Выберите направление", reply_markup=admin_get_directions_markup())    

@bot.callback_query_handler(func=lambda call: call.data == "add")
def AddUser(call):
    bot.edit_message_text("Введите ФИО", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, AddUserFIO)

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_dir_page_"))
def handle_admin_directions_callback(call):
    page = int(call.data.split("_")[3]) 
    bot.edit_message_text("Выберите группу:", call.message.chat.id, call.message.message_id,
                          reply_markup=admin_get_directions_markup(page))

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_dir_"))
def GroupSelected(call):
    direction = call.data.split("_")[2]
    User.append[direction]
    bot.edit_message_text("🕗 Добавление участника...", call.message.chat.id, call.message.message_id)
    result = actions.AddUser(User)
    User.clear()
    bot.edit_message_text(result, call.message.chat.id, call.message.message_id)



#/export
def ExportDataFile(MessageId, message):
    bot.edit_message_text("🕗 Обрабатываю данные...", message.chat.id, MessageId)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_path = f"/data/{message.document.file_name}"
    with open(file_path, "wb") as f:
        f.write(downloaded_file)
    result = actions.ExportData(file_path)
    bot.edit_message_text(result, message.chat.id, MessageId)


@bot.callback_query_handler(func=lambda call: call.data == "export")
def ExportData(call):
    bot.edit_message_text("Отправьте файл для экспорта", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(call.message, partial(ExportDataFile, call.message.message_id))




#/edit
EditUserList = []

def EditUserId(message):
    EditUserList.append(message.text)
    bot.send_message(message.chat.id, "👀 Что хотите изменить?", reply_markup=edit_choise_markup)

def EditDataUser(MessageId, message):
    EditUserList.append(message.text)
    bot.edit_message_text("🕗 Изменяю данные...", message.chat.id, MessageId)
    result = actions.EditUser(EditUser)
    EditUser.clear()
    bot.edit_message_text(result, message.chat.id, MessageId)

@bot.callback_query_handler(func=lambda call: call.data == "edit")
def EditUser(call):
    bot.edit_message_text("Введите id пользователя", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(call.message, partial(EditUserId, call.message.message_id))

@bot.callback_query_handler(func=lambda call: call.data == "fio")
def EditFio(call):
    EditUserList.append("fio")
    bot.edit_message_text("Введите новое ФИО", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(call.message, partial(EditUserId, call.message.message_id))

@bot.callback_query_handler(func=lambda call: call.data == "course")
def EditCourse(call):
    EditUserList.append("course")
    bot.edit_message_text("Введите новый курс", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(call.message, partial(EditUserId, call.message.message_id))

@bot.callback_query_handler(func=lambda call: call.data == "group")
def EditGroup(call):
    EditUserList.append("group")
    bot.edit_message_text("Введите новую групу", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, partial(EditUserId, call.message.message_id))

@bot.callback_query_handler(func=lambda call: call.data == "direction")
def EditDirection(call):
    EditUserList.append("direction")
    bot.edit_message_text("Выберите новое направление", call.message.chat.id, call.message.message_id, reply_markup=edit_get_directions_markup())


@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_dir_page_"))
def PaginateEdit(call):
    page = int(call.data.split("_")[3]) 
    bot.edit_message_text("Выберите новое направление", call.message.chat.id, call.message.message_id,
                          reply_markup=edit_get_directions_markup(page))

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_dir_"))
def EditSelected(call):
    direction = call.data.split("_")[2]
    EditUserList.append(direction)
    bot.edit_message_text("🕗 Изменяю направление...", call.message.chat.id, call.message.message_id)
    result = actions.EditUser(EditUser)
    EditUser.clear()
    bot.edit_message_text(result, call.message.chat.id, call.message.message_id)



#/delete
def DeleteUserId(MessageId, message):
    bot.edit_message_text("🕗 Удаляю участника...", message.chat.id, MessageId)
    result = actions.DeleteUser(message.text)
    bot.edit_message_text(result, message.chat.id, MessageId)

@bot.callback_query_handler(func=lambda call: call.data == "delete")
def DeleteUser(call):
    bot.edit_message_text("Введите id пользователя", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, partial(DeleteUserId, call.message.message_id))



#/add_admin
@bot.callback_query_handler(func=lambda call: call.data == "add_admin")
def AddAdmin(call):
    bot.edit_message_text("Введите имя пользователя", call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(message, AddAdminUsername)

def AddAdminUsername(message):
    sent_msg = bot.send_message(message.chat.id, "🕗 Добавляю админа...")
    result = actions.AddAdmin(message)
    bot.edit_message_text(result, sent_msg.chat.id, sent_msg.message_id)



#/filter Напраление
@bot.callback_query_handler(func=lambda call: call.data == "direction")
def FilterDirection(call):
    bot.edit_message_text("Выберите направление", call.message.chat.id, call.message.message_id, reply_markup=get_directions_markup())

@bot.callback_query_handler(func=lambda call: call.data.startswith("dir_page_"))
def handle_directions_callback(call):
    page = int(call.data.split("_")[2]) 
    bot.edit_message_text("Выберите группу:", call.message.chat.id, call.message.message_id,
                          reply_markup=get_directions_markup(page))

@bot.callback_query_handler(func=lambda call: call.data.startswith("dir_"))
def GroupSelected(call):
    direction = call.data.split("_")[1]
    bot.edit_message_text("🔎 Поиск пользователей по направлению...", call.message.chat.id, call.message.message_id)
    result = actions.FilterDirectionFind(direction)
    bot.edit_message_text(result, call.message.chat.id, call.message.message_id)



#/filter Курс
@bot.callback_query_handler(func=lambda call: call.data == "course")
def FilterCourse(call):
    bot.edit_message_text("Выберите курс", call.message.chat.id, call.message.message_id, reply_markup=course_markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
def CourseSelected(call):
    course_number = call.data.split("_")[1]
    bot.edit_message_text("🔎 Поиск пользователей по курсу...", call.message.chat.id, call.message.message_id)
    result = actions.FilterCourseFind(course_number)
    bot.edit_message_text(result, call.message.chat.id, call.message.message_id)



#/filter Группа
@bot.callback_query_handler(func=lambda call: call.data == "group")
def FilterGroup(call):
    bot.edit_message_text("Выберите группу", call.message.chat.id, call.message.message_id, reply_markup=get_group_markup())

@bot.callback_query_handler(func=lambda call: call.data.startswith("page_"))
def PaginateGroups(call):
    page = int(call.data.split("_")[1]) 
    bot.edit_message_text("Выберите группу:", call.message.chat.id, call.message.message_id,
                          reply_markup=get_group_markup(page))

@bot.callback_query_handler(func=lambda call: call.data.startswith("group_"))
def GroupSelected(call):
    group_number = call.data.split("_")[1]
    bot.edit_message_text("🔎 Поиск пользователей по группе...", call.message.chat.id, call.message.message_id)
    result = actions.FilterGroupFind(group_number)
    bot.edit_message_text(result, call.message.chat.id, call.message.message_id)



bot.polling()