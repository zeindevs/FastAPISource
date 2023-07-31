from fastapi import FastAPI, Body, Depends

from app.models import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

app = FastAPI()


posts = [
    {
        'id': 1,
        'title': 'Pencake',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
]

users = []


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.get('/', tags=['root'])
async def root() -> dict:
    return {'message': 'Welcome to your blog!'}


@app.get('/posts', dependencies=[Depends(JWTBearer())],  tags=['posts'])
async def get_posts() -> dict:
    return {'data': posts}


@app.get('/posts/{id}', dependencies=[Depends(JWTBearer())], tags=['posts'])
async def get_single_post(id: int) -> dict:
    if id > len(posts) or id <= 0:
        return {'error': 'No such post with the supplied ID.'}

    for post in posts:
        if post['id'] == id:
            return {'data': post}


@app.post('/posts', dependencies=[Depends(JWTBearer())], tags=['posts'])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {'data': 'post added.'}


@app.post('/user/signup', tags=['user'])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


@app.post('/user/login', tags=['user'])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {'error': 'Wrong login details!'}
