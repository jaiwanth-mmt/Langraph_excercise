from ast import Num
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import functools
import operator

app = FastAPI()

class NumberList(BaseModel):
    numbers: List[int]

class MultiplicationResult(BaseModel):
    product: int

class AdditionResult(BaseModel):
    total: int

class SubtractionResult(BaseModel):
    difference: List[int]

@app.post("/multiply" , response_model=MultiplicationResult)
async def multpily_numbers(data: NumberList):
    if not data.numbers:
        return MultiplicationResult(product=0)
    result = functools.reduce(operator.mul ,data.numbers)
    return MultiplicationResult(product=result)

@app.post("/add",response_model=AdditionResult)
async def add_numbers(data: NumberList):
    if not data.numbers:
        return AdditionResult(total=0)
    result = functools.reduce(operator.add, data.numbers)
    return AdditionResult(total=result)

@app.post("/subtract" ,response_model=SubtractionResult)
async def subtract_numbers(data:NumberList):
    if not data.numbers:
        return SubtractionResult(difference=[])
    total = sum(data.numbers)
    result = [i-total for i in data.numbers]
    return SubtractionResult(difference=result)

@app.get("/")
async def root():
    return {"message":"Multiplication API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)