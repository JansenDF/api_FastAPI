from fastapi import FastAPI, HTTPException, status

from models import Curso


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

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id = {curso_id}')

@app.delete('/cursos/{curso_id}')
async def del_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return cursos
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com ID {curso_id}')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)