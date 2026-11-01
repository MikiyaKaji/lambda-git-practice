def lambda_handler(event, context):
    name = event.get("name","guest")

    return {
        "message": f"Hello from my dev branch, {name}!"
    }