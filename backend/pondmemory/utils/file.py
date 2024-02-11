from gridfs import *
from pondmemory.database.Mongo import Mongo
from pondmemory.utils.Logger import logger

mongo = Mongo(database="PondMemoryDB_GRIDFS")

def uploadFileToDB(content: bytes, fileName: str, fileType: str, fileCategory: str) -> None:
    try:
        db = mongo.get_db()
        fs = GridFS(db, collection='File')
        fs.put(content, fileName=fileName, fileType=fileType, fileCategory=fileCategory)
    except Exception as e:
        logger.logger.error(e)


def getFileFromDB(query: dict) -> dict:
    try:
        db = mongo.get_db()
        fs = GridFS(db, collection="File")
        grid_out = fs.find_one(query)
        if grid_out is None:
            return None
        res = {
            "fileName": grid_out["fileName"],
            "fileType": grid_out["fileType"],
            "fileCategory": grid_out["fileCategory"],
            "fileContent": grid_out.read(),
            "md5": grid_out.md5,
            "length":grid_out.length
        }
        return res

    except Exception as e:
        logger.logger.error(e)