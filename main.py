from schemes import create_schemes
from data_load import load_data_into_db, get_running_session, close_session
from connection import create_session
import query

if __name__ == "__main__":
    # U can comment create_sechemes() and load_data_into_db() if u dont want the data to upload again
    print('Creating scheme...')
    # create_schemes()
    print('Loading data...')
    # load_data_into_db()
    print('Running queries...')

    running_session = get_running_session()

    # Check it there is a running mysql session and uses it, otherwise it creates a new session
    query.set_running_session(
        running_session if running_session != None else create_session())
    query.run_all_queries()
    close_session()
