from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, notes 
from dotenv import load_dotenv
import os




load_dotenv()

os.getenv("OPENAI_API_KEY")


app = FastAPI()  

# CORS middleware for frontend-backend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root():
    return {"message": "📝 AI Note-Taking Backend is running!"}

# Include your auth routes
app.include_router(auth.router)
app.include_router(notes.router)
