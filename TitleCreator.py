#!/usr/bin/env python3
# We're now approaching enterprise grade.
# This script generates random job titles. The lists of title components
# have been expanded to include a mix of serious, creative, and zany options
# to enhance the variety and fun of the generated titles.
from random import seed, choice
from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)
seed()

# HTML template with embedded CSS
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title Creator</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #fff;
            min-height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            max-width: 600px;
            width: 90%;
            animation: fadeIn 0.5s ease-in;
        }
        h1 {
            color: #4ecca3;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .title {
            font-size: 2em;
            color: #ffd700;
            margin: 30px 0;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .refresh-btn {
            background: #4ecca3;
            color: #1a1a2e;
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-top: 20px;
        }
        .refresh-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(78, 204, 163, 0.4);
        }
        .refresh-btn:active {
            transform: translateY(0);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Your New Title 🎉</h1>
        <div class="title">{{ title }}</div>
        <button class="refresh-btn" onclick="window.location.reload()">Generate Another Title</button>
        <div class="footer">
            Inspired by a salesperson who would always introduce me with a new title on every call
        </div>
    </div>
</body>
</html>
'''

def ofprefix():
    # List of prefixes for titles using 'of' (e.g., Viceroy of Engineering)
    l = ['Viceroy', 'Commandant', 'Grand Poo-Bah', 'Archon', 'Duke', 'Chancellor', 'President', 'Marquis',
            'Earl', 'Director', 'Chair', 'Head', 'Senior Director', 'Vice President', 'Dark Lord',
            'Dread Lord', 'Czar', 'Emperor', 'Baron', 'Guru', 'Supreme Commander', 'Galactic Overlord',
            'Chief Visionary Officer', 'Master of Coin', 'Head Honcho', 'The Big Cheese', 'Captain',
            'AI Whisperer', 'Prompt Engineer', 'Neural Network Navigator', 'Quantum Computing Conductor',
            'Machine Learning Maestro', 'Deep Learning Diva', 'Algorithm Alchemist', 'Data Science Druid',
            'Cloud Computing Conjurer', 'DevOps Demigod', 'Code Whisperer', 'Stack Overflow Sage',
            'Git Guru', 'Docker Docker', 'Kubernetes Keeper', 'Microservices Monarch']
    return choice(l)

def prefix():
    # List of general prefixes (e.g., Principal Solutions Architect)
    l = ['Principal', 'Master Chief', 'Chief', 'Head', 'Lead', 'Senior', 'Master', 'Premier', 'Scrum Certified',
            'Distinguished', 'Elite', 'Galactic', 'Cyber', 'Quantum', 'Supreme', 'Ninja',
            'AI-Powered', 'ML-Enhanced', 'Neural', 'Deep', 'Quantum', 'Blockchain', 'Web3',
            'Cloud-Native', 'Serverless', 'Edge', 'IoT', 'AR/VR', 'Metaverse', 'Crypto',
            'Prompt', 'LLM', 'GPT', 'Transformer', 'Tensor', 'PyTorch', 'TensorFlow',
            'Vibe', 'Chill', 'Zen', 'Mindful', 'Agile', 'Lean', 'DevOps', 'SRE']
    return choice(l)

def job():
    # List of job areas or focuses (e.g., Cloud, DevOps)
    l = ['Solutions', 'Systems', 'Network', 'Security', 'Compliance', 'Information', 'Scalability',
            'Database', 'Platform', 'Storage', 'Cloud', 'DevOps', 'Blockchain', 'Serverless', 'Reliability',
            'Innovation', 'Synergy', 'Cybersecurity', 'Digital Transformation', 'Meme Curation',
            'Cat Herding', 'Quantum Entanglement',
            'AI', 'Machine Learning', 'Deep Learning', 'Neural Networks', 'Natural Language Processing',
            'Computer Vision', 'Reinforcement Learning', 'Prompt Engineering', 'LLM Operations',
            'AI Ethics', 'AI Safety', 'AI Alignment', 'AI Governance', 'AI Infrastructure',
            'Vibe Engineering', 'Code Vibes', 'Developer Experience', 'Developer Relations',
            'Technical Writing', 'Documentation', 'Open Source', 'Community Management',
            'Web3', 'DeFi', 'NFT', 'Smart Contracts', 'Blockchain Infrastructure',
            'Edge Computing', 'IoT', 'AR/VR', 'Metaverse', 'Digital Twins',
            'Quantum Computing', 'Quantum Algorithms', 'Quantum Security']
    return choice(l)

def ofpostfix():
    # List of postfixes for titles using 'of' (e.g., Viceroy of Engineering)
    l = ['Engineering',
            'Management', 'Development', 'Deployment', 'Technical Training', 'Operations', 'Architecture',
            'Infrastructure', 'Technology', 'Administration', 'Thought Leadership', 'Shiny Things', 'Agility',
            'Strategy', 'Global Dominance', 'Creative Solutions', 'Advanced Shenanigans', 'Future Planning',
            'Resource Allocation', 'Mischief Management',
            'AI', 'Machine Learning', 'Deep Learning', 'Neural Networks', 'Natural Language Processing',
            'Computer Vision', 'Reinforcement Learning', 'Prompt Engineering', 'LLM Operations',
            'AI Ethics', 'AI Safety', 'AI Alignment', 'AI Governance', 'AI Infrastructure',
            'Vibe Engineering', 'Code Vibes', 'Developer Experience', 'Developer Relations',
            'Technical Writing', 'Documentation', 'Open Source', 'Community Management',
            'Web3', 'DeFi', 'NFT', 'Smart Contracts', 'Blockchain Infrastructure',
            'Edge Computing', 'IoT', 'AR/VR', 'Metaverse', 'Digital Twins',
            'Quantum Computing', 'Quantum Algorithms', 'Quantum Security']
    return choice(l)

def postfix():
    # List of general postfixes (e.g., Principal Solutions Architect)
    l = ['Engineer', 'Architect', 'Designer', 'Consultant', 'Manager', 'Officer', 'Leader', 'Janitor', 'Plumber',
            'Specialist', 'Evangelist', 'Wizard', 'Ninja Rockstar', 'Overlord', 'Sensei', 'Visionary',
            'AI Engineer', 'ML Engineer', 'Data Scientist', 'AI Researcher', 'Prompt Engineer',
            'LLM Engineer', 'AI Ethicist', 'AI Safety Engineer', 'AI Alignment Researcher',
            'Vibe Engineer', 'Code Vibes Specialist', 'Developer Experience Engineer',
            'Developer Relations Engineer', 'Technical Writer', 'Documentation Engineer',
            'Open Source Maintainer', 'Community Manager', 'Web3 Developer', 'Smart Contract Engineer',
            'Blockchain Developer', 'Quantum Computing Engineer', 'Edge Computing Specialist',
            'IoT Engineer', 'AR/VR Developer', 'Metaverse Architect', 'Digital Twin Engineer']
    return choice(l)

def ofornot():
    l = ['1', '0']
    return choice(l)

def generate_title():
    if ofornot() == '1':
        return ofprefix() + ' of ' + job() + ' ' + ofpostfix()
    else:
        return prefix() + ' ' + job() + ' ' + postfix()

@app.route('/', methods=['GET'])
def get_title():
    title = generate_title()
    if os.environ.get('WEB_MODE', 'false').lower() == 'true':
        return render_template_string(HTML_TEMPLATE, title=title)
    return jsonify({
        'title': title,
        'message': 'Congratulations! Your new title is:'
    })

def print_title():
    print("Congratulations! Your new title is:")
    print(generate_title())

if __name__ == '__main__':
    # Check if we should run as a web service
    if os.environ.get('WEB_MODE', 'false').lower() == 'true':
        port = int(os.environ.get('PORT', 8080))
        app.run(host='0.0.0.0', port=port)
    else:
        # Run in CLI mode
        print_title()
