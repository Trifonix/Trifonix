from fastapi import FastAPI, HTTPException
from models import Note, NoteSchema

app = FastAPI()

notes = []

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def create_note(note: NoteSchema):
    new_note = Note(note.title, note.content)
    notes.append(new_note)
    return {"message": "Заметка создана!", "note": new_note.__dict__}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if 0 <= note_id < len(notes):
        removed = notes.pop(note_id)
        return {"message": f"Заметка '{removed.title}' удалена!"}
    else:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
