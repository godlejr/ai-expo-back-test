from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from os import walk

app = FastAPI()

app.mount("/static", StaticFiles(directory="static",name="static"))

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],    
    allow_headers=["*"],	
)

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/tasks/{id}")
async def printHello(id:int):


	filePath ="./static/tasks/" + str(id)

	imageFiles = []
	for (dirpath, dirnames, filenames) in walk(filePath):
		
		for filename in filenames:

			imageFiles.append(dirpath +"/" + filename)

	return imageFiles