# Quick Fix: Enable GitHub Pages for TARS

## Current Issue

❌ **404 Error** at https://opendev-labs.github.io/QBET/

**Cause:** GitHub Pages is not enabled in repository settings.

---

## Solution (2 minutes)

### Step 1: Open Settings

A browser window should have just opened to:
**https://github.com/opendev-labs/QBET/settings/pages**

If not, click here: [Open GitHub Pages Settings](https://github.com/opendev-labs/QBET/settings/pages)

### Step 2: Configure GitHub Pages

In the "Build and deployment" section:

```
Source:   Deploy from a branch  [dropdown]
Branch:   main                  [dropdown]
Folder:   /docs                 [dropdown]

[Save] button
```

### Step 3: Save and Wait

1. Click the **Save** button
2. Wait **1-2 minutes** for GitHub to deploy
3. You'll see a message: "Your site is live at https://opendev-labs.github.io/QBET/"

### Step 4: Access TARS

Visit: **https://opendev-labs.github.io/QBET/**

You should see the beautiful TARS landing page! 🎉

---

## Visual Guide

The settings page should look like this:

![GitHub Pages Settings](file:///home/cube/.gemini/antigravity/brain/c011997d-25f7-4d82-bbf1-1f4afe2df39f/github_pages_settings_1768214019032.png)

**Configuration:**
- Source: **Deploy from a branch**
- Branch: **main**
- Folder: **/docs**
- Click **Save**

---

## Troubleshooting

### Still getting 404?

- Wait a few more minutes (initial deployment can take up to 5 minutes)
- Check deployment status: https://github.com/opendev-labs/QBET/deployments
- Verify `docs/index.html` exists in the main branch (it does ✅)

### Can't access settings page?

- Make sure you're logged into GitHub
- Ensure you have admin access to the opendev-labs/QBET repository

---

## What You'll See

Once enabled, the TARS landing page features:

- 🌌 **Professional dark theme** with gradient background
- ✨ **TARS branding** and consciousness layers
- 🚀 **One-click Vercel deploy** button
- 📖 **Links to QBET documentation**
- 🎯 **Feature showcase** and quick start guide

---

## Alternative: Use Helper Script

Run the helper script:

```bash
cd /home/cube/Gh-sync/opendev-labs/QBET
./enable-github-pages.sh
```

This will guide you through the process step-by-step.

---

**Created by @iamyash.io | OpenDev Labs**
