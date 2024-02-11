from gridfs import *
from pondmemory.database.Mongo import Mongo
from pondmemory.utils.Logger import logger
def uploadFileToDB(content: bytes, filename: str, fileType: str) -> None:
    try:
        db = Mongo().get_db()
        fs = GridFS(db, collection='File')
        fs.put(content, filename=filename, fileType=fileType)
    except Exception as e:
        logger.logger.error(e)
