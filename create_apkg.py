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
    'CCRN Cardiovascular Model',
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
    'CCRN - Cardiovascular (Barron\'s)'
)

# Read cards from TSV
cards_added = 0
with open('ccrn_cardio_cards.tsv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        # Create note with tags
        tags_list = row['Tags'].split()
        note = genanki.Note(
            model=ccrn_model,
            fields=[row['Question'], row['Answer'], row['Tags']],
            tags=tags_list
        )
        deck.add_note(note)
        cards_added += 1

# Create the package
package = genanki.Package(deck)
package.write_to_file('CCRN - Cardiovascular (Barron\'s).apkg')

print(f"Successfully created Anki package with {cards_added} cards")
print(f"Deck name: CCRN - Cardiovascular (Barron's)")
print(f"Output file: CCRN - Cardiovascular (Barron's).apkg")
