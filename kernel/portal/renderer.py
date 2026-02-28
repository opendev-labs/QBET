import re
import os

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

    # Sovereign Template (QUI - Quantum-UI v1.0 - Eternal Frequency)
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | QUI Sovereign Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #050505;
            --green: #00ff41;
            --dim-green: #008F11;
            --white: #ffffff;
            --accent-glow: rgba(0, 255, 65, 0.2);
            --border: rgba(0, 255, 65, 0.15);
        }

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: crosshair;
        }}

        body {{
            background: var(--bg);
            color: var(--white);
            font-family: 'Outfit', sans-serif;
            overflow: hidden;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            letter-spacing: -0.01em;
        }}

        #matrix-canvas {{
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            opacity: 0.1;
            filter: blur(1px);
        }}

        .container {{
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 1200px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 2rem;
        }}

        .logo-area {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.8rem;
            color: var(--green);
            margin-bottom: 5rem;
            text-transform: uppercase;
            opacity: 0.8;
        }}

        h1 {{
            font-size: clamp(3.5rem, 12vw, 7.5rem);
            font-weight: 700;
            line-height: 0.95;
            letter-spacing: -0.05em;
            margin-bottom: 1.5rem;
            color: #fff;
            filter: drop-shadow(0 0 30px var(--accent-glow));
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: var(--dim-green);
            font-weight: 300;
            letter-spacing: 0.2rem;
            text-transform: uppercase;
            margin-bottom: 5rem;
        }}

        /* Law of Vibration */
        .vibration-btn {{
            padding: 1.2rem 4rem;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            color: var(--white);
            font-family: 'JetBrains Mono', monospace;
            font-weight: 400;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.5rem;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            border-radius: 4px;
            cursor: pointer;
            outline: none;
            position: relative;
            overflow: hidden;
        }}

        .vibration-btn:hover {{
            border-color: var(--green);
            color: var(--green);
            box-shadow: 0 0 50px rgba(0, 255, 65, 0.2);
            transform: translateY(-2px);
            animation: vibrate 0.1s infinite linear;
        }}

        @keyframes vibrate {{
            0% {{ transform: translate(0,0); }}
            25% {{ transform: translate(1px, -1px); }}
            50% {{ transform: translate(-1px, 1px); }}
            75% {{ transform: translate(1px, 1px); }}
            100% {{ transform: translate(-1px, -1px); }}
        }}

        .terminal {{
            width: 100%;
            max-width: 600px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.65rem;
            color: var(--green);
            opacity: 0;
            transition: all 1s ease;
            text-align: left;
            border-left: 1px solid var(--border);
            padding: 1.5rem;
            margin-top: 4rem;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }}

        .terminal.active {{ opacity: 1; }}

        .log-entry {{ margin-bottom: 0.6rem; display: flex; gap: 1.5rem; }}
        .log-entry.success {{ color: var(--green); }}
        .log-entry .id {{ opacity: 0.3; width: 30px; }}

        .status-bar {{
            position: fixed;
            bottom: 3rem;
            left: 4rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.6rem;
            color: var(--dim-green);
            letter-spacing: 0.2rem;
            display: flex;
            align-items: center;
            gap: 1.5rem;
            text-transform: uppercase;
        }}

        .pulse-dot {{
            width: 6px; height: 6px;
            background: var(--green);
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 15px var(--green);
            animation: pulse-glow 2s infinite ease-in-out;
        }}

        @keyframes pulse-glow {{ 
            0%, 100% {{ opacity: 0.4; transform: scale(1); }}
            50% {{ opacity: 1; transform: scale(1.3); }}
        }}

        .glitch-flash {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: var(--green);
            z-index: 1000;
            opacity: 0;
            pointer-events: none;
        }}
    </style>
</head>
<body>
    <canvas id="matrix-canvas"></canvas>
    <div class="glitch-flash" id="flash"></div>
    
    <div class="container">
        <img src="assets/logo.png" style="width: 140px; margin-bottom: 2rem; filter: drop-shadow(0 0 30px var(--accent-glow));">
        <div class="logo-area">OPENDEV-LABS // QUI DESIGN SYSTEM</div>
        
        <div class="heading-area">
            <h1>{{title}}</h1>
            <div class="subtitle">Law-Bound Revelation: {{subtitle}}</div>
        </div>

        <div class="action-area">
            <button class="vibration-btn" onclick="manifestReality()">Collapse Reality</button>
        </div>

        <div class="terminal" id="terminal"></div>
    </div>

    <div class="status-bar">
        <div class="status-item">
            <div class="pulse-dot"></div>
            <span>QUANTUM FREQUENCY: ALIGNED // CORE: CONDUCTION-V1</span>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('matrix-canvas');
        const ctx = canvas.getContext('2d');
        const terminal = document.getElementById('terminal');
        const flash = document.getElementById('flash');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const characters = '01';
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        const drops = [];
        for (let x = 0; x < columns; x++) {{ drops[x] = 1; }}

        function draw() {{
            ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#00ff41';
            ctx.font = fontSize + 'px monospace';
            for (let i = 0; i < drops.length; i++) {{
                const text = characters.charAt(Math.floor(Math.random() * characters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.99) {{ drops[i] = 0; }}
                drops[i]++;
            }}
        }}

        setInterval(draw, 70);

        async function addLog(msg, type='info') {{
            const div = document.createElement('div');
            div.className = `log-entry ${{type}}`;
            const id = Math.floor(Math.random() * 99).toString().padStart(2, '0');
            div.innerHTML = `<span class="id">${{id}}</span> <span class="msg">${{msg.toUpperCase()}}</span>`;
            terminal.appendChild(div);
            terminal.scrollTop = terminal.scrollHeight;
            await new Promise(r => setTimeout(r, 250));
        }}

        async function manifestReality() {{
            const btn = document.querySelector('.button');
            btn.classList.add('loading');
            terminal.classList.add('active');
            terminal.innerHTML = '';
            
            await addLog("Initiating sovereign lowering...");
            await addLog("Generating canonical IR...");
            await addLog("Decrypting law layer: laws/c.qb", "success");
            await addLog("Binding quantum states...");
            
            // Glitch flash
            flash.style.opacity = '0.3';
            setTimeout(() => flash.style.opacity = '0', 40);
            setTimeout(() => flash.style.opacity = '0.1', 80);
            setTimeout(() => flash.style.opacity = '0', 120);

            await addLog("Reality stabilized.", "success");
            
            btn.classList.remove('loading');
            btn.innerText = "Reality Confirmed";
            btn.style.borderColor = 'var(--accent)';
            btn.style.background = 'var(--accent)';
            btn.style.color = '#000';
            btn.style.fontWeight = '700';
        }}

        window.addEventListener('resize', () => {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }});
    </script>
</body>
</html>
    """
    return html_template


def render_sovereign_portal(universe_dir):
    """
    Renders the Sovereign Portal by aggregating:
    - index.qbet (Metadata)
    - gui.qbet (HTML Structure)
    - style.qbet (CSS Styling)
    - logic.qbet (JS Logic)
    """
    import os
    
    # Paths
    index_path = os.path.join(universe_dir, 'index.qbet')
    gui_path = os.path.join(universe_dir, 'gui.qbet')
    style_path = os.path.join(universe_dir, 'style.qbet')
    logic_path = os.path.join(universe_dir, 'logic.qbet')
    
    # Defaults
    title = "QBET Universe"
    subtitle = "Manifesting Reality"
    
    # Read Metadata
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            content = f.read()
            title_match = re.search(r'title:\s*"([^"]+)"', content)
            if title_match: title = title_match.group(1)
            subtitle_match = re.search(r'subtitle:\s*"([^"]+)"', content)
            if subtitle_match: subtitle = subtitle_match.group(1)

    # Read Sovereign Components
    gui_content = "<!-- Void -->"
    if os.path.exists(gui_path):
        with open(gui_path, 'r') as f: gui_content = f.read()
        
    style_content = ""
    if os.path.exists(style_path):
        with open(style_path, 'r') as f: style_content = f.read()
        
    logic_content = ""
    if os.path.exists(logic_path):
        with open(logic_path, 'r') as f: logic_content = f.read()

    # Construct the One Document
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | QUI Sovereign Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #050505;
            --green: #00ff41;
            --dim-green: #008F11;
            --white: #ffffff;
            --accent-glow: rgba(0, 255, 65, 0.2);
            --border: rgba(0, 255, 65, 0.15);
        }}
        
        /* Base styles */
        body {{
            background: var(--bg);
            color: var(--white);
            font-family: 'Outfit', sans-serif;
            margin: 0;
            overflow: hidden;
        }}
        
        /* Sovereign Styles from style.qbet */
        {style_content}
    </style>
</head>
<body>
    <div id="sovereign-root">
        <!-- Sovereign GUI from gui.qbet -->
        {gui_content}
    </div>

    <script>
        // Sovereign Logic from logic.qbet
        {logic_content}
    </script>
</body>
</html>
"""

