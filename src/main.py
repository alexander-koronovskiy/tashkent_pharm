from fastapi import FastAPI
from api.router import router
import uvicorn


app = FastAPI(title='Pharmacy')

app.include_router(router, prefix='api')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings_app.SERVER_HOST,
        port=settings_app.SERVER_PORT,
        debug=True,
        reload=True
    )
