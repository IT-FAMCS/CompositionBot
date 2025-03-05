from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

add_markup = InlineKeyboardMarkup()
add = InlineKeyboardButton("Добавить", callback_data="add")
add_markup.add(add)

directions = [
    "IT-отдел", "Декораторка", "Научка", "Фандрайз", "Фото-видео", 
    "Креаторка", "Тик ток", "Медийка", "Рабочка", "Корпоратка"
]

# Функция для создания разметки с кнопками
def admin_get_directions_markup(page=0):
    markup = InlineKeyboardMarkup()
    per_page = 5  # Количество кнопок на странице
    start = page * per_page
    end = start + per_page
    buttons = [InlineKeyboardButton(text=dir, callback_data=f"admin_dir_{dir}") for dir in directions[start:end]]
    
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

add_admin_markup = InlineKeyboardMarkup()
add = InlineKeyboardButton("Добавить", callback_data="add_admin")
add_admin_markup.add(add)

edit_markup = InlineKeyboardMarkup()
edit = InlineKeyboardButton("Редактировать", callback_data="edit")
edit_markup.add(add)

edit_choise_markup = InlineKeyboardMarkup()
fio = InlineKeyboardButton("ФИОН", callback_data="fio")
course = InlineKeyboardButton("Курс", callback_data="course")
group = InlineKeyboardButton("Группа", callback_data="group")
direction = InlineKeyboardButton("Направление", callback_data="direction")
edit_choise_markup.add(fio, course, group, direction)

def edit_get_directions_markup(page=0):
    markup = InlineKeyboardMarkup()
    per_page = 5  # Количество кнопок на странице
    start = page * per_page
    end = start + per_page
    buttons = [InlineKeyboardButton(text=dir, callback_data=f"edit_dir_{dir}") for dir in directions[start:end]]
    
    for btn in buttons:
        markup.add(btn)

    # Кнопки "Назад" и "Далее"
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("<< Назад", callback_data=f"edit_dir_page_{page-1}"))
    if end < len(directions):
        nav_buttons.append(InlineKeyboardButton("Далее >>", callback_data=f"edit_dir_page_{page+1}"))
    
    if nav_buttons:
        markup.row(*nav_buttons)
    
    return markup

delete_markup = InlineKeyboardMarkup()
delete = InlineKeyboardButton("Удалить", callback_data="delete")
delete_markup.add(add)

export_markup = InlineKeyboardMarkup()
export = InlineKeyboardButton("Экспорт", callback_data="export")
export_markup.add(add)