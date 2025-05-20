#!/usr/bin/env python3
# We're now approaching enterprise grade.
# This script generates random job titles. The lists of title components
# have been expanded to include a mix of serious, creative, and zany options
# to enhance the variety and fun of the generated titles.
from random import seed, choice

seed()

def ofprefix():
    # List of prefixes for titles using 'of' (e.g., Viceroy of Engineering)
    # Expanded for more variety (serious, creative, zany).
    l = ['Viceroy', 'Commandant', 'Grand Poo-Bah', 'Archon', 'Duke', 'Chancellor', 'President', 'Marquis',
            'Earl', 'Director', 'Chair', 'Head', 'Senior Director', 'Vice President', 'Dark Lord',
            'Dread Lord', 'Czar', 'Emperor', 'Baron', 'Guru', 'Supreme Commander', 'Galactic Overlord',
            'Chief Visionary Officer', 'Master of Coin', 'Head Honcho', 'The Big Cheese', 'Captain']
    return choice(l)

def prefix():
    # List of general prefixes (e.g., Principal Solutions Architect)
    # Expanded for more variety (serious, creative, zany).
    l = ['Principal', 'Master Chief', 'Chief', 'Head', 'Lead', 'Senior', 'Master', 'Premier', 'Scrum Certified',
            'Distinguished', 'Elite', 'Galactic', 'Cyber', 'Quantum', 'Supreme', 'Ninja']
    return choice(l)

def job():
    # List of job areas or focuses (e.g., Cloud, DevOps)
    # Expanded for more variety (serious, creative, zany).
    l = ['Solutions', 'Systems', 'Network', 'Security', 'Compliance', 'Information', 'Scalability',
            'Database', 'Platform', 'Storage', 'Cloud', 'DevOps', 'Blockchain', 'Serverless', 'Reliability',
            'Innovation', 'Synergy', 'Cybersecurity', 'Digital Transformation', 'Meme Curation',
            'Cat Herding', 'Quantum Entanglement']
    return choice(l)

def ofpostfix():
    # List of postfixes for titles using 'of' (e.g., Viceroy of Engineering)
    # Expanded for more variety (serious, creative, zany).
    l = ['Engineering',
            'Management', 'Development', 'Deployment', 'Technical Training', 'Operations', 'Architecture',
            'Infrastructure', 'Technology', 'Administration', 'Thought Leadership', 'Shiny Things', 'Agility',
            'Strategy', 'Global Dominance', 'Creative Solutions', 'Advanced Shenanigans', 'Future Planning',
            'Resource Allocation', 'Mischief Management']
    return choice(l)

def postfix():
    # List of general postfixes (e.g., Principal Solutions Architect)
    # Expanded for more variety (serious, creative, zany).
    l = ['Engineer', 'Architect', 'Designer', 'Consultant', 'Manager', 'Officer', 'Leader', 'Janitor', 'Plumber',
            'Specialist', 'Evangelist', 'Wizard', 'Ninja Rockstar', 'Overlord', 'Sensei', 'Visionary']
    return choice(l)

def ofornot():
    l = ['1', '0']
    return choice(l)

print("Congratulations! Your new title is:")
if ofornot() == '1':
    print(ofprefix() + ' of ' + job() + ' ' + ofpostfix())
else:
    print(prefix() + ' ' + job() + ' ' + postfix())
