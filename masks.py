import glob, os
def fetch_masks():
    all_masks = os.listdir('masks')
    names_only = []
    for item in all_masks:
        names_only.append(item[0:-4].capitalize())
    return names_only