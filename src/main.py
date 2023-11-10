import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import students

origins = [
    "*",
]

app = FastAPI()

app.include_router(students.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
