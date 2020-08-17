import logging
from psycopg2.extras import RealDictCursor
import psycopg2

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def write_to_db(parsed_data):
    uri = os.environ["uri"]
    connection = psycopg2.connect(uri)

    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("CREATE TABLE IF NOT EXISTS monitoring  (id serial PRIMARY KEY, Content_Type text, Transfer_Encoding text, Connection text, Date text, Last_Modified text, ETag text, Server text, Content_Encoding text, Vary text, X_Cache text, Via text, X_Amz_Cf_Pop text, X_Amz_Cf_Id text, Age text, status_code text, response_time text);")
    insert_query = """ INSERT INTO monitoring (id, Content_Type, Transfer_Encoding, Connection, Date, Last_Modified, ETag, Server, Content_Encoding, Vary, X_Cache, Via, X_Amz_Cf_Pop, X_Amz_Cf_Id, Age, status_code, response_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values_to_insert = (parsed_data["id"], parsed_data["Content_Type"], parsed_data["Transfer_Encoding"], parsed_data["Connection"], parsed_data["Date"], parsed_data["Last_Modified"], parsed_data["ETag"], parsed_data["Server"], parsed_data["Content_Encoding"], parsed_data["Vary"], parsed_data["X_Cache"], parsed_data["Via"], parsed_data["X_Amz_Cf_Pop"], parsed_data["X_Amz_Cf_Id"], parsed_data["Age"], parsed_data["status_code"], parsed_data["response_time"])
    cursor.execute(insert_query, values_to_insert)
    connection.commit()
    count = cursor.rowcount
    logger.info(count)