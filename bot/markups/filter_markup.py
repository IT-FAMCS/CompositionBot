from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

filter_markup = InlineKeyboardMarkup()
direction = InlineKeyboardButton("Направление", callback_data="direction")
course = InlineKeyboardButton("Курс", callback_data="course")
group = InlineKeyboardButton("Группа", callback_data="group")
filter_markup.add(direction, course, group)

direction_markup = InlineKeyboardMarkup()

direction_markup.add()

course_markup = InlineKeyboardMarkup()
_1 = InlineKeyboardButton("1", callback_data="course_1")
_2 = InlineKeyboardButton("2", callback_data="course_2")
_3 = InlineKeyboardButton("3", callback_data="course_3")
_4 = InlineKeyboardButton("4", callback_data="course_4")
course_markup.add(_1, _2, _3, _4)

groups = [str(i) for i in range(1, 14)] 
groups_per_page = 5 


def get_group_markup(page=0):
    """Генерирует разметку с кнопками для текущей страницы"""
    markup = InlineKeyboardMarkup()

    start = page * groups_per_page
    end = start + groups_per_page
    group_buttons = [InlineKeyboardButton(g, callback_data=f"group_{g}") for g in groups[start:end]]

    for btn in group_buttons:
        markup.add(btn)
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("<< Назад", callback_data=f"page_{page - 1}"))
    if end < len(groups):
        nav_buttons.append(InlineKeyboardButton("Далее >>", callback_data=f"page_{page + 1}"))

    if nav_buttons:
        markup.row(*nav_buttons)

    return markup

directions = [
    "IT-отдел", "Декораторка", "Научка", "Фандрайз", "Фото-видео", 
    "Креаторка", "Тик ток", "Медийка", "Рабочка", "Корпоратка"
]

# Функция для создания разметки с кнопками
def get_directions_markup(page=0):
    markup = InlineKeyboardMarkup()
    per_page = 5  # Количество кнопок на странице
    start = page * per_page
    end = start + per_page
    buttons = [InlineKeyboardButton(text=dir, callback_data=f"dir_{dir}") for dir in directions[start:end]]
    
    for btn in buttons:
        markup.add(btn)

    # Кнопки "Назад" и "Далее"
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("<< Назад", callback_data=f"dir_page_{page-1}"))
    if end < len(directions):
        nav_buttons.append(InlineKeyboardButton("Далее >>", callback_data=f"dir_page_{page+1}"))
    
    if nav_buttons:
        markup.row(*nav_buttons)
    
    return markup