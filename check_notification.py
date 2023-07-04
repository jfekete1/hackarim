notes = wasp.system.notifications
for key, value in list(notes.items()):
    if value['title'] == 'parancs':
        notes.pop(key)
        print("Success: Item removed from notes.")

