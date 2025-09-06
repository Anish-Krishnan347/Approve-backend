def success_response(data=None, message="Success", status_code=200):
    return {
        "status": "success",
        "status_code": status_code,
        "message": message,
        "data": data or []
    }, status_code