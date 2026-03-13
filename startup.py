import os
import subprocess
import sys

# Change title in UI files
ui_path = "/opt/render/project/src/.venv/lib/python3.14/site-packages/autogenstudio/web/ui"

for root, dirs, files in os.walk(ui_path):
    for file in files:
        if file.endswith('.js') or file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'AutoGen Studio' in content:
                    content = content.replace('AutoGen Studio', 'AgentPilot Studio')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
            except:
                pass

# Start the actual server
os.execv(sys.executable, [sys.executable, '-m', 'autogenstudio.cli', 'ui', '--port', '8080', '--host', '0.0.0.0'])