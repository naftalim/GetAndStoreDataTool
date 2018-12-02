import dropbox, private

def getDropbox():
    dbx = dropbox.Dropbox(private.DROPBOX_KEY)
    return dbx



