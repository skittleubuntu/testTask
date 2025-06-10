import logging

logging.basicConfig(filename='manager_report.log', level=logging.INFO)

def log_result(dialog_id, summary):
    logging.info(f"Dialog: {dialog_id}\n{summary}\n{'='*50}\n")
