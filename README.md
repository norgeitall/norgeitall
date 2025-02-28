[![CI](https://github.com/norgeitall/norgeitall/actions/workflows/ci.yml/badge.svg)](https://github.com/norgeitall/norgeitall/actions) [![Netlify Status](https://api.netlify.com/api/v1/badges/de5a3ecd-f354-43e0-82bd-53f9555a0f16/deploy-status)](https://app.netlify.com/sites/norgeitall/deploys)

# Norge i tall

_Norge i tall_ is built on [Evidence - Business Intelligence as Code](https://evidence.dev/). In addition, we use Python to build data sources.

To get started:

```bash
uv sync
source .venv/bin/activate
pre-commit run --all-files
./main.py
npm install
npm run sources
npm run dev -- --host 0.0.0.0
```

See [the CLI docs](https://docs.evidence.dev/cli/) for more command information.

## Learning More

- [Docs](https://docs.evidence.dev/)
- [Github](https://github.com/evidence-dev/evidence)
- [Slack Community](https://slack.evidence.dev/)
- [Evidence Home Page](https://www.evidence.dev)
