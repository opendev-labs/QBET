#!/bin/bash

# GitHub Pages Enabler Script for QBET/TARS
# This script helps you enable GitHub Pages for the QBET repository

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║              GitHub Pages Setup for TARS                 ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if we're in the right directory
if [ ! -d "docs" ]; then
    echo "❌ Error: docs/ directory not found"
    echo "   Please run this script from the QBET repository root"
    exit 1
fi

if [ ! -f "docs/index.html" ]; then
    echo "❌ Error: docs/index.html not found"
    echo "   The GitHub Pages site files are missing"
    exit 1
fi

echo "✅ Found docs/index.html"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "⚠️  GitHub CLI (gh) is not installed"
    echo ""
    echo "To enable GitHub Pages, you have two options:"
    echo ""
    echo "Option 1: Manual (Recommended)"
    echo "  1. Open: https://github.com/opendev-labs/QBET/settings/pages"
    echo "  2. Under 'Build and deployment':"
    echo "     - Source: Deploy from a branch"
    echo "     - Branch: main"
    echo "     - Folder: /docs"
    echo "  3. Click 'Save'"
    echo "  4. Wait 1-2 minutes"
    echo "  5. Visit: https://opendev-labs.github.io/QBET/"
    echo ""
    echo "Option 2: Install GitHub CLI"
    echo "  Run: sudo snap install gh"
    echo "  Then run this script again"
    echo ""
    exit 0
fi

echo "✅ GitHub CLI is installed"
echo ""

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "⚠️  Not authenticated with GitHub"
    echo "   Run: gh auth login"
    exit 1
fi

echo "✅ Authenticated with GitHub"
echo ""

# Try to enable GitHub Pages using gh CLI
echo "🚀 Attempting to enable GitHub Pages..."
echo ""

# Note: gh CLI doesn't have direct GitHub Pages enable command
# We'll open the settings page in browser
echo "Opening GitHub Pages settings in your browser..."
echo ""

xdg-open "https://github.com/opendev-labs/QBET/settings/pages" 2>/dev/null || \
    echo "Please manually open: https://github.com/opendev-labs/QBET/settings/pages"

echo ""
echo "📋 Manual Steps Required:"
echo ""
echo "  1. In the browser window that just opened:"
echo "     (or go to: https://github.com/opendev-labs/QBET/settings/pages)"
echo ""
echo "  2. Under 'Build and deployment':"
echo "     ┌─────────────────────────────────────┐"
echo "     │ Source: Deploy from a branch        │"
echo "     │ Branch: main                        │"
echo "     │ Folder: /docs                       │"
echo "     │ [Save]                              │"
echo "     └─────────────────────────────────────┘"
echo ""
echo "  3. Wait 1-2 minutes for deployment"
echo ""
echo "  4. Your TARS site will be live at:"
echo "     🌐 https://opendev-labs.github.io/QBET/"
echo ""
echo "✨ Done! Follow the steps above to complete setup."
