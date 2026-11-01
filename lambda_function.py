def lambda_handler(event, context):
    name = event.get("name", "guest")
    age = event.get("age", 0)

    return {
        "message": f"Hello, {name}!",
        "age": age
    }