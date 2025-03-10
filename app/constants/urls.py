from enum import Enum

class Urls(Enum):
    #find
    finduser = "/api/find_user/{fio}"

    #filter
    filter_group = "/api/filter/group/{data}"
    filter_course = "/api/filter/course/{data}"
    filter_direction = "/api/filter/direction/{data}"

    #admin
    admin_check = "/api/check_admin/{data}"
    add_admin = "/api/add_admin"
    add_user = "/api/add_user"
    edit_user = "/api/edit_user/{fio}"
    delete_user = "/api/delete/{id}"

    