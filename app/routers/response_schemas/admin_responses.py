admin_create_responses = {
    201: {
        "description": "Admin successfully created",
        "content": {
            "application/json": {
                "example": {
                    "id": "uuid",
                    "username": "admin_user",
                    "email": "admin@example.com",
                    "role": "superadmin",
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
        "description": "Admin already exists",
        "content": {
            "application/json": {
                "example": {"detail": {"message": "Admin with this email already exists"}}
            }
        },
    },
}

admin_detail_responses = {
    200: {
        "description": "Admin details retrieved successfully",
        "content": {
            "application/json": {
                "example": {
                    "id": "uuid",
                    "username": "admin_user",
                    "email": "admin@example.com",
                    "role": "superadmin",
                    "status": "active",
                }
            }
        },
    },
    404: {
        "description": "Admin not found",
        "content": {"application/json": {"example": {"detail": {"message": "Admin not found"}}}},
    },
}