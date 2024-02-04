from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


<<<<<<< HEAD
@app.get("/")
async def say_hello():
    return "I love u"


=======
>>>>>>> c0946524a359dd872d2670922f8cf76bcf47483a
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
<<<<<<< HEAD


@app.put("/items/{model_name}")
def update_model(model_name: str, model: ModelName):
    return {"model_name": model_name}
=======
>>>>>>> c0946524a359dd872d2670922f8cf76bcf47483a
