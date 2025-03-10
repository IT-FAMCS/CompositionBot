user_create_responses = {
    201: {
        "description": "User successfully created",
        "content": {
            "application/json": {
                "example": {
                    "id": "uuid",
                    "username": "user123",
                    "email": "user@example.com",
                    "role": "member",
                    "status": "active",
                }
            }
        },
    },
    400: {
        "description": "Validation Error",
        "content": {"application/json": {"example": {"detail": {"message": "Invalid input data"}}}},
    },
    409: {
        "description": "User already exists",
        "content": {
            "application/json": {
                "example": {"detail": {"message": "User with this email already exists"}}
            }
        },
    },
}

user_find_responses = {
    200: {
        "description": "User details retrieved successfully",
        "content": {
            "application/json": {
                "example": {
                    "id": "uuid",
                    "username": "user123",
                    "email": "user@example.com",
                    "role": "member",
                    "status": "active",
                }
            }
        },
    },
    404: {
        "description": "User not found",
        "content": {"application/json": {"example": {"detail": {"message": "User not found"}}}},
    },
}

user_edit_responses = {
    200: {
        "description": "User updated successfully",
        "content": {
            "application/json": {
                "example": {
                    "id": "uuid",
                    "username": "user123",
                    "email": "user@example.com",
                    "role": "member",
                    "status": "active",
                }
            }
        },
    },
    400: {
        "description": "Validation Error",
        "content": {"application/json": {"example": {"detail": {"message": "Invalid update data"}}}},
    },
    404: {
        "description": "User not found",
        "content": {"application/json": {"example": {"detail": {"message": "User not found"}}}},
    },
}

user_delete_responses = {
    200: {
        "description": "User deleted successfully",
        "content": {
            "application/json": {"example": {"detail": {"message": "User deleted successfully"}}}},
    },
    400: {
        "description": "Invalid input data",
        "content": {"application/json": {"example": {"detail": {"message": "Invalid input data"}}}},
    },
}

user_filter_responses = {
    200: {
        "description": "Users filtered successfully",
        "content": {
            "application/json": {
                "example": {
                    "users": [
                        {
                            "id": "uuid",
                            "username": "user123",
                            "email": "user@example.com",
                            "role": "member",
                            "status": "active",
                        }
                    ]
                }
            }
        },
    },
    400: {
        "description": "Invalid parameters",
        "content": {"application/json": {"example": {"detail": {"message": "Invalid query parameters"}}}},
    },
}