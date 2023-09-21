import pickle
# import datetime


# def save_to_pickle(dir: str, model) -> None:
#     """
#     This function saves content to pickle file.
#     :param dir:
#     :param model:
#     :return:
#     """
#     pickle.dump(model, open(dir, 'wb'))


def load_from_pickle(dir: str) -> None:
    """
    This function loads content from pickle file.
    :param dir:
    :return:
    """
    return pickle.load(open(dir, 'rb'))


# def save_report(dir: str, report) -> None:
#     """
#     This function save model report to .txt with timestamp.
#     :param dir:
#     :param report:
#     :return:
#     """
#     timestamp = str(datetime.datetime.now()).replace('-', '').replace(':', '').replace(' ', '_')
#     file_name = dir.format(timestamp=timestamp)

#     with open(file_name, 'w') as f:
#         f.write(report)

#     return None