# Portfolio Site Generator 🛠️

This is a Python-powered static site generator that converts Markdown and JSON content into a clean, multi-page HTML portfolio — styled, navigable, and client-ready.

## 🔧 Features

- Converts `.md` and `.json` files into HTML pages
- Supports multiple content sections: Bio, Projects, Skills, Contact
- Automatically builds a navigation bar across all pages
- Includes dark mode and theme selector (Solarized, etc.)
- Renders project images if present, skips them if not
- Exports the entire site as a ZIP archive for deployment
- GitHub Pages ready

## 🧪 How to Use

1. Clone or download this repo.
2. Add your content in the `content/` folder:
   - `bio.md`, `projects.json`, `skills.md`, `contact.md`
3. Run the generator:
   ```bash
   python generator.py
   ```
4. Open the `output/` folder to view the generated site.
5. Upload it to GitHub Pages or zip it for deployment.

## 🧰 Dependencies

- `Jinja2`
- `markdown`

Install with:
```bash
pip install Jinja2 markdown
```

## 💡 Credits

Built by Daniel Jarvis as part of a Python developer portfolio.
Visit: [github.com/gandalf-ddj](https://github.com/gandalf-ddj)

## 📄 License

MIT
