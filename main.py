import argparse
import logging
import asyncio
from aiopath import AsyncPath
from aioshutil import copy, move
from pathlib import Path

FOLDER_EXTENSIONS = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".svg": "images",
    ".doc": "docs",
    ".txt": "docs",
    ".docx": "docs",
    ".rtf": "docs",
    ".pdf": "docs",
    ".mp3": "audio",
}

FOLDER_EXTENSIONS_OTHER = "uknown"


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


async def path_parser():
    logger.info("Start parsing")
    parser = argparse.ArgumentParser(description="Files sorting")
    parser.add_argument("--in_folder", type=str, help="source folder", required=True)
    parser.add_argument("--out_folder", type=str, help="output folder", required=True)
    return parser


async def path_creator(folder: str):
    logger.info(f"Start path creation for {folder} folder")
    apath = AsyncPath(folder)
    if not await apath.exists():
        await apath.mkdir(exist_ok=True, parents=True)
    return apath


async def read_folder(source_folder: AsyncPath, output_folder: AsyncPath):
    async for object in source_folder.iterdir():
        if await object.is_dir():
            await read_folder(object, output_folder)
        else:
            file_extension = Path(object).suffix
            to_folder = output_folder / FOLDER_EXTENSIONS.get(
                file_extension, FOLDER_EXTENSIONS_OTHER
            )
            await copy_file(object, to_folder)


async def copy_file(object, to_folder):
    logger.info(f"Start copying file for {object} to {to_folder} folder")
    new_path = await path_creator(to_folder)
    await copy(object, new_path)


async def main():
    logger.info("Start copying")
    parser = await path_parser()
    args = parser.parse_args()
    source_folder = await path_creator(args.in_folder)
    output_folder = await path_creator(args.out_folder)
    await read_folder(source_folder, output_folder)
    logger.info("Finish copying")


if __name__ == "__main__":
    asyncio.run(main())
