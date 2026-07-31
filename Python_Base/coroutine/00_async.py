async def hello_coroutine():
    print("The internal code was executed.")


coro = hello_coroutine()
print(type(coro))
