import re

def render_portal(qbet_file):
    """Translates index.qbet into a sovereign web portal"""
    
    # Defaults
    title = "QBET Universe"
    subtitle = "Manifesting Reality"
    theme = "void"
    
    if os.path.exists(qbet_file):
        with open(qbet_file, 'r') as f:
            content = f.read()
            
            # Simple extraction for v0.1
            title_match = re.search(r'title:\s*"([^"]+)"', content)
            if title_match: title = title_match.group(1)
            
            subtitle_match = re.search(r'subtitle:\s*"([^"]+)"', content)
            if subtitle_match: subtitle = subtitle_match.group(1)
            
            theme_match = re.search(r'theme:\s*"([^"]+)"', content)
            if theme_match: theme = theme_match.group(1)

    # Sovereign Template (Vanilla CSS, High-End)
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | QBET Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #000;
            --accent: #ff4d00;
            --text: #fff;
            --subtext: rgba(255,255,255,0.6);
            --glass: rgba(255,255,255,0.03);
            --border: rgba(255,255,255,0.1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Outfit', sans-serif;
            overflow-x: hidden;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .universe {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 50% 50%, rgba(255, 77, 0, 0.05), transparent 70%),
                linear-gradient(rgba(255, 77, 0, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 77, 0, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 50px 50px, 50px 50px;
            z-index: -1;
            animation: pulse 10s infinite alternate;
        }}

        @keyframes pulse {{
            from {{ opacity: 0.5; }}
            to {{ opacity: 1; }}
        }}

        .manifestation {{
            text-align: center;
            max-width: 800px;
            padding: 2rem;
            animation: emerge 1.5s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        @keyframes emerge {{
            from {{ opacity: 0; transform: translateY(20px); filter: blur(10px); }}
            to {{ opacity: 1; transform: translateY(0); filter: blur(0); }}
        }}

        .logo {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            letter-spacing: 0.5rem;
            color: var(--accent);
            margin-bottom: 2rem;
            text-transform: uppercase;
        }}

        h1 {{
            font-size: clamp(3rem, 10vw, 5rem);
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.1;
            background: linear-gradient(to bottom, #fff, #999);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        p {{
            font-size: 1.2rem;
            color: var(--subtext);
            margin-bottom: 3rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
        }}

        .action-container {{
            display: flex;
            gap: 1.5rem;
            justify-content: center;
        }}

        .button {{
            padding: 1rem 2.5rem;
            background: transparent;
            border: 1px solid var(--accent);
            color: var(--accent);
            font-family: 'JetBrains Mono', monospace;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }}

        .button:hover {{
            background: var(--accent);
            color: #000;
            box-shadow: 0 0 30px rgba(255, 77, 0, 0.4);
        }}

        .status {{
            position: fixed;
            bottom: 2rem;
            left: 2rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            color: var(--subtext);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .pulse-dot {{
            width: 6px;
            height: 6px;
            background: var(--accent);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--accent);
            animation: beacon 2s infinite;
        }}

        @keyframes beacon {{
            0% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.5); opacity: 0.5; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
    </style>
</head>
<body>
    <div class="universe"></div>
    
    <div class="manifestation">
        <div class="logo">opendev-labs // QBET</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
        
        <div class="action-container">
            <div class="button" onclick="alert('Collapsing potential...')">Enter the Field</div>
        </div>
    </div>

    <div class="status">
        <div class="pulse-dot"></div>
        <span>QUANUM FIELD: STABILIZED // CORE: NATIVE</span>
    </div>
</body>
</html>
    """
    return html_template

import os
