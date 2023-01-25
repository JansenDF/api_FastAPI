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

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)