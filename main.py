from fastapi import FastAPI, status, HTTPException
from database import Base, engine
from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
import schemas

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return "cust"

@app.post("/Customer", status_code=status.HTTP_201_CREATED)
def create_Customer(todo: schemas.Customer):

    session = Session(bind=engine, expire_on_commit=False)

    tododb = models.Customer(firstname = todo.firstname,lastname=todo.lastname,email=todo.email,customer_type=todo.customer_type,created_on=todo.created_on)

    session.add(tododb)
    session.commit()
    id = tododb.id
    session.close()
    return f"created todo item with id {id}"


@app.get("/Customer/{id}", response_model=schemas.Customer)
def read_Customer(id: int):

    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(models.Customer).get(id)
    session.close()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.put("/Customer/{id}")
def update_Customer(id: int, firstname: str,lastname:str,email: str,customer_type: str,created_on: str):

    session = Session(bind=engine, expire_on_commit=False)

    todo = session.query(models.Customer).get(id)

    # update todo item with the given task (if an item with the given id was found)
    if todo:
        todo.firstname = firstname
        todo.lastname = lastname
        todo.email=email
        todo.customer_type= customer_type
        todo.created_on= created_on
        session.commit()

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.delete("/Customer/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Customer(id: int):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(models.Customer).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None

@app.get("/Customer")
def read_Cust_list():
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all todo items
    todo_list = session.query(models.Customer).all()

    # close the session
    session.close()

    return todo_list