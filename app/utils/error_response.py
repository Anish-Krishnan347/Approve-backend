
def error_response(message="Something went wrong", status_code=400, data=None):
    return {
        "status": "error",
        "status_code": status_code,
        "message": message,
        "data": data or []
    }, status_code