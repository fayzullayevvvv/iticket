from fastapi import FastAPI


app = FastAPI(title="Iticket API")


@app.get("/")
async def root_view():
    return {"message": "project is running..."}
