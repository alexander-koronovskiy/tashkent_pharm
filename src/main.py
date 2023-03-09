from fastapi import FastAPI
import uvicorn

from api.router import router
from settings import settings_app

app = FastAPI(title='Pharmacy')
app.include_router(router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings_app.SERVER_HOST,
        port=settings_app.SERVER_PORT,
        reload=True
    )
