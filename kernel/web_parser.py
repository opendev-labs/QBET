import re
from .ast_nodes import HTMLElement, CSSRule, JSScript

class WebParser:
    """Parses html.qbet, css.qbet, and js.qbet files"""
    
    def parse_html_qbet(self, content):
        """
        Parses HTML-like QBET syntax.
        Example:
        div(class="container") {
            h1 { "Title" }
        }
        """
        # simplified regex-based parser for v1
        elements = []
        # Find pattern: tag(attrs) { content }
        # This is a placeholder for a recursive parser
        return [HTMLElement("div", {"class": "root"}, [])] 

    def parse_css_qbet(self, content):
        """
        Parses CSS-like QBET syntax.
        Example:
        .container {
            color: green;
        }
        """
        rules = []
        # Regex to find selectors and bodies
        pattern = r'([^{]+)\{([^}]+)\}'
        matches = re.findall(pattern, content)
        for selector, body in matches:
            props = {}
            for line in body.strip().split(';'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    props[k.strip()] = v.strip()
            rules.append(CSSRule(selector.strip(), props))
        return rules

    def parse_js_qbet(self, content):
        """
        Parses JS-like QBET syntax.
        Example:
        manifestReality() {
           console.log("Quantum");
        }
        """
        return JSScript(content)
