# 🗂️ Claude Context Bundles

Optimized documentation bundles for different types of n8n workflows. Each bundle is carefully curated to fit within Claude's context limits while maximizing workflow generation quality.

## 📦 Available Bundles

| Bundle | Files | Description | Best For |
|--------|-------|-------------|----------|
| **Core Essentials** | 20 | Essential n8n concepts - always include (small, high-impact) | Learning n8n basics, simple workflows |
| **Ai Workflows** | 170 | Everything for AI and LangChain workflows | AI assistants, chatbots, LangChain workflows |
| **Api Integrations** | 312 | API connections and data integrations | Connecting APIs, webhooks, data sync |
| **Data Processing** | 59 | Data manipulation and transformation | ETL, data transformation, analysis |
| **Hosting Deployment** | 87 | Self-hosting and production deployment | Production deployment, scaling |
| **Complete Reference** | 1207 | Complete documentation (use for complex workflows) | Complex multi-domain workflows |


## 🎯 How to Choose the Right Bundle

### **Starting Out?** 
→ Use `core_essentials` first

### **Building AI Workflows?**
→ Use `ai_workflows` 

### **Connecting APIs?**
→ Use `api_integrations`

### **Processing Data?** 
→ Use `data_processing`

### **Deploying to Production?**
→ Use `hosting_deployment`

### **Complex Multi-Domain Workflows?**
→ Use `complete_reference` (large context)

## 🚀 Usage Instructions

1. **Choose your bundle** based on workflow type
2. **Download the entire folder** 
3. **Upload to Claude project** as context
4. **Start building workflows!**

## 📊 Context Optimization

Each bundle is optimized for:
- ✅ **Claude's context limits**
- ✅ **Maximum relevance** for the workflow type  
- ✅ **Minimum noise** - only essential docs
- ✅ **Fast loading** - reasonable file counts

## 🔄 Updating Bundles

To refresh bundles with latest documentation:

```bash
python3 create_context_bundles.py
git add claude_context_bundles/
git commit -m "🔄 Update context bundles"
git push
```

---

**Perfect for building n8n workflows with Claude! 🤖**
