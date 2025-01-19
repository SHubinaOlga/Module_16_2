from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def Get_Main_Page():
    return "Главная страница"

@app.get("/user/admin")
async def Get_Admin_Page():
    return "Вы вошли как администратор"

@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(minimum=1, maximum=100,
                    description="Enter User ID", example='1')]) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def Get_User_Info(
        username: Annotated[str, Path(min_length = 5,
                            max_length = 20, description="Enter username", example = 'UrbanUser')],
        age: Annotated[int, Path(ge = 18, le =120, description = "Enter age", example='24')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
