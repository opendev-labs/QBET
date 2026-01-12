# GitHub Pages Setup Instructions

## Enable GitHub Pages for TARS

To make the TARS landing page accessible at `https://opendev-labs.github.io/QBET/`, follow these steps:

### 1. Navigate to Repository Settings

Go to: https://github.com/opendev-labs/QBET/settings/pages

### 2. Configure GitHub Pages

Under **"Build and deployment"**:

- **Source**: Select "Deploy from a branch"
- **Branch**: Select `main`
- **Folder**: Select `/docs`
- Click **"Save"**

### 3. Wait for Deployment

GitHub will automatically build and deploy your site. This usually takes 1-2 minutes.

### 4. Access Your Site

Once deployed, your TARS landing page will be available at:

**https://opendev-labs.github.io/QBET/**

### 5. Verify Deployment

You can check the deployment status at:

https://github.com/opendev-labs/QBET/deployments

---

## What's Deployed

The GitHub Pages site includes:

- **Professional Landing Page** (`docs/index.html`)
  - TARS branding and description
  - Three layers of consciousness
  - Feature showcase
  - Quick start guide
  - Vercel deployment button
  - Links to QBET documentation

- **Documentation** (`docs/README.md`)
  - Overview of TARS
  - Local development instructions
  - Links to related docs

---

## Alternative: Deploy TARS to Vercel

For full TARS functionality (not just the landing page), deploy to Vercel:

1. Click the "Deploy to Vercel" button on the landing page
2. Or visit: https://vercel.com/new/clone?repository-url=https://github.com/opendev-labs/coding-super-agent
3. Configure environment variables:
   - `POSTGRES_URL`
   - `ANTHROPIC_API_KEY`
   - `GITHUB_TOKEN`
   - `VERCEL_TEAM_ID`
   - `VERCEL_PROJECT_ID`
   - `VERCEL_TOKEN`
   - `AI_GATEWAY_API_KEY`
4. Deploy and access your TARS instance

---

## Troubleshooting

### GitHub Pages not showing up?

1. Check that GitHub Pages is enabled in repository settings
2. Verify the `docs/` folder exists in the `main` branch
3. Wait a few minutes for the initial deployment
4. Check deployment status at: https://github.com/opendev-labs/QBET/deployments

### 404 Error?

- Make sure the source is set to `main` branch and `/docs` folder
- Verify `docs/index.html` exists in the repository

---

**Created by @iamyash.io | OpenDev Labs**
