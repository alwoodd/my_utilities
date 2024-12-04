import logging

def init_log(log_file_name = None, logging_level=logging.DEBUG, truncate_log=True):
    '''
    Initialize logging. Logging is written to log_file_name and to stdout.
    Args:
        logging_level (int): Logging level as defined in logging
        truncate_log (bool): True to truncate log file, False to append.
    '''
    if truncate_log:
        file_mode = "w"
    else:
        file_mode = "a"

    file_handlers = [logging.StreamHandler()]
    if log_file_name is not None:
        file_handlers.append(logging.FileHandler(log_file_name, file_mode))

    logging.basicConfig(handlers=file_handlers,
            level=logging_level, format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")