#start to create smart notes app
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
app = QApplication([])
note = QWidget()
note.setWindowTitle('Smart Notes')
list_tags = QListWidget()
label1 = QLabel('List of notes')
label2 = QLabel('List of tags')
box1 = QTextEdit()
box2 = QListWidget()
box3 = QListWidget()
box4 = QLineEdit()
box4.setPlaceholderText('Enter tag...')
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
b_create = QPushButton('Create note')
b_delete = QPushButton('Delete note')
b_set = QPushButton('Save note')
b_add = QPushButton('Add to note')
b_untag = QPushButton('Untag from note')
b_search = QPushButton('Search notes by tag')
line1.addWidget(box1)
line2.addWidget(label1)
line2.addWidget(box2)
line3.addWidget(b_create)
line3.addWidget(b_delete)
line2.addLayout(line3)
line2.addWidget(b_set)
line2.addWidget(label2)
line2.addWidget(box3)
line2.addWidget(box4)
line4.addWidget(b_add)
line4.addWidget(b_untag)
line2.addLayout(line4)
line2.addWidget(b_search)

notes = {
    'Welcome!' : {
        'text' : 'This is the best note taking app in the world!' ,
        'tags' : ['good','instructions']
    }
}
with open('notes_data.json','w') as file:
    json.dump(notes,file)
box2.addItems(notes)
def show_note():
    name = box2.selectedItems()[0].text()
    box1.setText(notes[name]['text'])
    box3.clear()
    box3.addItems(notes[name]['tags'])
box2.itemClicked.connect(show_note)
def add_note():
    note_name, result = QInputDialog.getText(note, 'Add note', 'Notename:')
    if note_name != '' :
        notes[note_name] = {'text': '','tags' : []}
        box2.addItem(note_name)
        box3.addItems(notes[note_name]['tags'])
    else :
        pass
def del_note():
    if box2.selectedItems():
        Notename = box2.selectedItems()[0].text()
        del(notes[Notename])
        with open('notes_data.json','w') as file:
            json.dump(notes,file)
        box1.clear()
        box2.clear()
        box3.clear()
        box2.addItems(notes)
def save_note():
    if box2.selectedItems():
        Notename = box2.selectedItems()[0].text()
        text_note = box1.toPlainText()
        notes[Notename]['text'] = text_note
        with open('notes_data.json','w') as file:
            json.dump(notes,file)
def add_tag():
    if box2.selectedItems():
        tag = box4.text()
        Notename = box2.selectedItems()[0].text()
        if(tag !='') and (tag not in notes[Notename]['tags']):
            notes[Notename]['tags'].append(tag)
            box3.addItem(tag)
            box4.clear()
            with open('notes_data.json','w') as file:
                json.dump(notes,file)
def del_tag():
    if box2.selectedItems():
        Notename = box2.selectedItems()[0].text()
        tag = box3.selectedItems()[0].text()
        notes[Notename]['tags'].remove(tag)
        box3.clear()
        box3.addItems(notes[Notename]['tags'])
        with open('notes_data.json','w') as file:
            json.dump(notes,file)
def search_tag():
    if b_search.text() == 'Search notes by tag':
        tag = box4.text()
        note_filtered = {}
        for i in notes:
            if tag in notes[i]['tags']:
                note_filtered[i] = notes[i]
        box2.clear()
        box3.clear()
        box2.addItems(note_filtered)
        b_search.setText('Clear search')
    elif b_search.text() == 'Clear search':
        box1.clear()
        box2.clear()
        box3.clear()
        box4.clear()
        box2.addItems(notes)
        b_search.setText('Search notes by tag')
b_search.clicked.connect(search_tag)
b_untag.clicked.connect(del_tag)
b_add.clicked.connect(add_tag)
b_set.clicked.connect(save_note)
b_delete.clicked.connect(del_note)
b_create.clicked.connect(add_note)
main_line = QHBoxLayout()
main_line.addLayout(line1, stretch = 2)
main_line.addLayout(line2, stretch = 1)
note.setLayout(main_line)
note.resize(900,600)
note.show() 
app.exec_()