#!/usr/bin/env python3
import csv
import genanki
import random

# Create a unique model ID and deck ID
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID = random.randrange(1 << 30, 1 << 31)

# Define the Anki note model
ccrn_model = genanki.Model(
    MODEL_ID,
    'CCRN Hemodynamics Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Tags'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css='''
    .card {
        font-family: arial;
        font-size: 20px;
        text-align: left;
        color: black;
        background-color: white;
        white-space: pre-wrap;
    }
    '''
)

# Create the deck
deck = genanki.Deck(
    DECK_ID,
    'CCRN - Hemodynamics (Barron\'s)'
)

# Read cards from TSV
cards_added = 0
with open('ccrn_hemodynamics_cards.tsv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        # Create note with tags - ensure all fields are strings
        question = row.get('Question', '') or ''
        answer = row.get('Answer', '') or ''
        tags_str = row.get('Tags', '') or ''
        tags_list = tags_str.split() if tags_str else []
        note = genanki.Note(
            model=ccrn_model,
            fields=[question, answer, tags_str],
            tags=tags_list
        )
        deck.add_note(note)
        cards_added += 1

# Create the package
package = genanki.Package(deck)
package.write_to_file('CCRN - Hemodynamics (Barron\'s).apkg')

print(f"Successfully created Anki package with {cards_added} cards")
print(f"Deck name: CCRN - Hemodynamics (Barron's)")
print(f"Output file: CCRN - Hemodynamics (Barron's).apkg")
