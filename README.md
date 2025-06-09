# 🚀 Complete N8N Documentation Collection

A comprehensive, perfectly cleaned collection of the entire n8n documentation, optimized for AI assistants and Claude projects.

## 📊 Collection Stats

- **1,197 documentation files** with **474,007 words**
- **10/10 quality** - All navigation artifacts removed
- **99.8% success rate** from original scraping
- **10 organized categories** for easy navigation
- **AI-ready format** perfect for Claude context

## 📁 Documentation Categories

| Category | Files | Words | Description |
|----------|-------|-------|-------------|
| **Nodes & Integrations** | 774 | 222,548 | All available nodes, integrations, and credentials |
| **AI & LangChain** | 164 | 134,439 | AI features, LangChain, and advanced AI workflows |
| **Hosting & Deployment** | 72 | 29,644 | Self-hosting, configuration, and scaling |
| **Workflows** | 61 | 28,081 | Building, managing, and sharing workflows |
| **Development** | 44 | 26,764 | Creating custom nodes and contributing |
| **Code & Expressions** | 46 | 18,176 | Custom code, expressions, and functions |
| **API Reference** | 12 | 5,994 | REST API documentation and authentication |
| **Getting Started** | 7 | 4,539 | Basic concepts, tutorials, and first steps |
| **User Management** | 13 | 2,684 | Teams, permissions, and authentication |
| **Troubleshooting** | 4 | 1,138 | Common issues, debugging, and migration guides |

## 🎯 Perfect for Claude Projects

This collection is specifically optimized for use with Claude and other AI assistants:

✅ **Zero navigation clutter** - Only pure documentation content  
✅ **Consistent formatting** - Clean markdown throughout  
✅ **Logical organization** - Easy for AI to understand context  
✅ **Complete coverage** - Every aspect of n8n documented  
✅ **Source attribution** - Each file includes original URL  

## 🚀 How to Use

### For Claude Projects:
1. Download the `n8n_docs_final/` folder
2. Upload to your Claude project as context
3. Start building sophisticated n8n workflows with AI assistance

### For Reference:
- Browse categories in `n8n_docs_final/`
- Each category has its own README with file listings
- All files are clean markdown for easy reading

### For Developers:
- Use the scraping scripts to update the collection
- Modify categories in `organize_perfect.py` as needed
- All source code included for customization

## 🧠 Smart Context Bundles

### What are Smart Context Bundles?

Smart Context Bundles are intelligently selected subsets of the n8n documentation, tailored to your specific workflow needs. By describing your workflow, you can generate a focused documentation bundle that maximizes relevant context for Claude or other AI assistants, while staying within context size limits.

### How to Use the Smart Context Selector UI

1. Open `context_selector_ui.html` in your web browser (no server needed).
2. Describe your n8n workflow in the prompt box (e.g., "Create an AI chatbot that monitors Slack messages, analyzes them with OpenAI, stores conversations in Airtable, and sends daily summaries via email").
3. (Optional) Enter a custom bundle name and choose whether to auto-push to GitHub.
4. Click **Analyze & Create Command**.
5. Review the analysis and copy the generated command.
6. Run the command in your terminal to generate the bundle.

### How to Generate a Bundle from the Command Line

You can also generate a smart context bundle directly:

```bash
python3.11 smart_context_selector.py --prompt "<your workflow description>" [--name <bundle_name>] [--push]
```
- `--prompt` (required): Your workflow description.
- `--name` (optional): Custom name for the bundle.
- `--push` (optional): Automatically push the bundle to GitHub.

### Example Workflow

Suppose you want to build a workflow that syncs Salesforce data with Google Sheets and sends business reports via email. You would:

1. Enter this prompt in the UI or command line:
   > Sync Salesforce data with Google Sheets daily and generate business reports via email
2. The tool will analyze your needs and select the most relevant documentation files.
3. Run the generated command to create your bundle.
4. Upload the resulting bundle to Claude as context for your project.

Smart Context Bundles help you get the most out of AI-powered workflow building by providing only the most relevant n8n documentation for your use case.

## ⚠️ Important: Use Your Own GitHub Repository

By default, the smart context bundle tool will push to the GitHub remote configured in your local git repository. To ensure you do not push to the original author's repository, you must set up your own GitHub remote before using the `--push` option.

### How to Set Up Your Own GitHub Remote

1. **Remove the existing remote (if any):**
   ```sh
   git remote remove origin
   ```
2. **Add your own GitHub repository as the remote:**
   ```sh
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   ```
3. **(Optional) Set the default branch if needed:**
   ```sh
   git branch -M main
   ```
4. **Push the code to your own repo:**
   ```sh
   git push -u origin main
   ```

### Warning
- The tool will push to whatever remote is configured in your local git.
- Make sure you have permission to push to the repository you set as the remote.
- You will use your own GitHub authentication (SSH keys or personal access tokens).

## 🛠️ Scraping Scripts

The repository includes the complete scraping pipeline:

- `discover_urls.py` - Finds all documentation URLs
- `extract_content_perfect.py` - Downloads and cleans content  
- `organize_perfect.py` - Organizes into categories

To update the collection:
```bash
pip install requests beautifulsoup4 markdownify
python3 discover_urls.py
python3 extract_content_perfect.py  
python3 organize_perfect.py
```

## 📋 Quality Features

- **Comprehensive cleaning** removes navigation, ads, and artifacts
- **Smart categorization** based on content and URL structure
- **Duplicate handling** ensures no content conflicts
- **Metadata preservation** includes source URLs and word counts
- **Error handling** graceful failure recovery

## 📈 Original Source

Scraped from the complete [n8n documentation](https://docs.n8n.io/) with respect for robots.txt and rate limiting.

## 🤝 Contributing

Feel free to:
- Report issues with content quality
- Suggest category improvements  
- Submit pull requests for script enhancements
- Share usage examples

## 📄 License

This collection is for educational and development purposes. Original content belongs to n8n.io.

---

**Perfect for building n8n workflows with AI assistance! 🤖**