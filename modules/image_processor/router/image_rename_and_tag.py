
import zipfile

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from starlette.responses import FileResponse

from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/img-rename-and-tag", tags=["Image Processor"], summary="Upload images in zip file, rename images and add name as tag")
async def img_rename_and_tag(zip_file: UploadFile, tag_name: str):

    with zipfile.ZipFile(zip_file.file) as old_zip, zipfile.ZipFile("just_some_tools_cache/parsed.zip", "w") as new_zip:
        i = 0
        for f in old_zip.namelist():
            if "/" not in f:
                i += 1
                suffix = f.split(".")[-1]
                file = old_zip.open(f)
                new_name_short = f"{tag_name}_{i}"
                new_name = f"{tag_name}_{i}.{suffix}"

                with open(new_name, 'wb') as new_file:
                    new_file.write(file.read())
                    new_file.close()

                img = Image.open(new_name)
                img_draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(
                    font="font/simsun.ttc", size=65)
                img_draw.text((10, 10), new_name_short,
                              font=font, fill=(0, 0, 0), language='zh-TW')
                img.save(new_name)

                new_zip.write(new_name)

    return FileResponse("just_some_tools_cache/parsed.zip", media_type='application/octet-stream', filename="parsed_images_by_just_some_tools.zip")
