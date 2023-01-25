from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 67,
    },
    2: {
        "titulo": "Algoritmos e lógicas de programação",
        "aulas": 67,
        "horas": 47,
    },
}
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)