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

    # Sovereign Template (Matrix Premium v2 - High-End Minimalist)
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | QBET Sovereign Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #000000;
            --accent: #ff6b00; /* Sovereign Orange */
            --accent-glow: rgba(255, 107, 0, 0.4);
            --text: #ffffff;
            --subtext: rgba(255, 255, 255, 0.4);
            --border: rgba(255, 107, 0, 0.2);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: crosshair;
        }}

        body {{
            background: var(--bg);
            color: var(--text);
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
            opacity: 0.08;
            filter: blur(2px);
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
            color: var(--accent);
            margin-bottom: 5rem;
            text-transform: uppercase;
            opacity: 0.6;
        }}

        .heading-area {{
            margin-bottom: 5rem;
        }}

        h1 {{
            font-size: clamp(3.5rem, 12vw, 7.5rem);
            font-weight: 700;
            line-height: 0.95;
            letter-spacing: -0.05em;
            margin-bottom: 1.5rem;
            color: #fff;
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: var(--subtext);
            font-weight: 300;
            letter-spacing: 0.1rem;
        }}

        .action-area {{
            margin-bottom: 4rem;
        }}

        .button {{
            padding: 0.9rem 3.5rem;
            background: transparent;
            border: 1px solid var(--border);
            color: var(--accent);
            font-family: 'JetBrains Mono', monospace;
            font-weight: 400;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.4rem;
            transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
            border-radius: 2px;
            cursor: pointer;
            outline: none;
            position: relative;
        }}

        .button:hover {{
            border-color: var(--accent);
            background: rgba(0, 255, 65, 0.03);
            box-shadow: 0 0 30px rgba(0, 255, 65, 0.1);
            transform: translateY(-2px);
            letter-spacing: 0.45rem;
        }}

        .button:active {{
            transform: translateY(1px) scale(0.98);
            background: var(--accent);
            color: #000;
        }}

        /* Loading State */
        .button.loading {{
            pointer-events: none;
            color: transparent;
            border-color: var(--subtext);
        }}

        .button.loading::after {{
            content: "";
            position: absolute;
            width: 18px;
            height: 18px;
            top: 50%;
            left: 50%;
            margin: -9px 0 0 -9px;
            border: 1px solid var(--accent);
            border-top-color: transparent;
            border-radius: 50%;
            animation: spin 0.6s linear infinite;
        }}

        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}

        .terminal {{
            width: 100%;
            max-width: 500px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.65rem;
            color: var(--subtext);
            opacity: 0;
            transition: all 1s ease;
            text-align: left;
            border-left: 1px solid rgba(0, 255, 65, 0.1);
            padding-left: 1.5rem;
        }}

        .terminal.active {{ opacity: 1; }}

        .log-entry {{ margin-bottom: 0.4rem; display: flex; gap: 1rem; }}
        .log-entry.success {{ color: var(--accent); }}
        .log-entry .id {{ opacity: 0.3; width: 30px; }}

        .status-bar {{
            position: fixed;
            bottom: 3rem;
            left: 4rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.6rem;
            color: var(--subtext);
            letter-spacing: 0.2rem;
            display: flex;
            align-items: center;
            gap: 1.5rem;
            text-transform: uppercase;
        }}

        .pulse-dot {{
            width: 5px; height: 5px;
            background: var(--accent);
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 10px var(--accent);
            animation: pulse-glow 2.5s infinite ease-in-out;
        }}

        @keyframes pulse-glow {{ 
            0%, 100% {{ opacity: 0.3; transform: scale(0.9); }}
            50% {{ opacity: 1; transform: scale(1.1); }}
        }}

        .glitch-flash {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: var(--accent);
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
        <img src="assets/logo.png" style="width: 120px; margin-bottom: 2rem; filter: drop-shadow(0 0 15px rgba(0,255,65,0.3));">
        <div class="logo-area">OPENDEV-LABS // QBET</div>
        
        <div class="heading-area">
            <h1>{title}</h1>
            <div class="subtitle">{subtitle}</div>
        </div>

        <div class="action-area">
            <button class="button" onclick="manifestReality()">Enter the Field</button>
        </div>

        <div class="terminal" id="terminal"></div>
    </div>

    <div class="status-bar">
        <div class="status-item">
            <div class="pulse-dot"></div>
            <span>QUANTUM FIELD: STABILIZED // CORE: NATIVE</span>
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
            ctx.fillStyle = '#ff6b00';
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

import os
