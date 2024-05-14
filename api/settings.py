from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from modules.image_processor.router import image_rename_and_tag

tags = [
    {
        'name': 'Image Processing',
        'description': 'Image Processing API'
    },
]

origins = ["*"]
app = FastAPI(title="Just Some Tools Backend API",
              openapi_tags=tags,
              version="0.1.0",
              docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_rename_and_tag.router,
                   prefix="/api/image-processor", tags=["Image Processor"])
