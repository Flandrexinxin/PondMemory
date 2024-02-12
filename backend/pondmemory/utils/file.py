from gridfs import *
from pondmemory.database.Mongo import Mongo
from pondmemory.utils.Logger import logger
from datetime import datetime
from bson import ObjectId


mongofs = Mongo(database="PondMemoryFS")
mongo = Mongo()

def uploadFileBinaryToDB(content: bytes) -> ObjectId:
    try:
        db = mongofs.get_db()
        fs = GridFS(db, collection='File')
        return ObjectId(str(fs.put(content)))

    except Exception as e:
        logger.logger.error(e)
        raise e


def getFileBinaryFromDB(query: dict) -> bytes:
    try:
        db = mongofs.get_db()
        fs = GridFS(db, collection="File")
        grid_out = fs.find_one(query)
        if grid_out is None:
            return None

        return grid_out.read()

    except Exception as e:
        logger.logger.error(e)
        raise e


def uploadFile(content: bytes, fileName: str, fileType: str, fileCategory: str) -> ObjectId:
    session = mongo.get_session()
    session.start_transaction()
    try:
        fileId = uploadFileBinaryToDB(content)
        _id = mongo.insert_one("File", {
            "fileId": fileId,
            "fileName": fileName,
            "fileType": fileType,
            "fileCategory": fileCategory,
            "createTime": datetime.now()
        })
        return _id
    except Exception as e:
        logger.logger.error(e)
        session.abort_transaction()
    finally:
        session.end_transaction()

def getFile(query:dict) -> dict:
    fileObj = mongo.find_one("File", query)
    if fileObj is None:
        return None
    content = getFileBinaryFromDB({"_id": fileObj['fileId']})
    fileObj["fileContent"] = content
    return fileObj



