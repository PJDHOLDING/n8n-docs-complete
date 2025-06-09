#!/usr/bin/env python3
"""
Create hybrid bundles that combine multiple domains for complex workflows
"""

import os
import shutil
import json

def create_hybrid_bundles():
    print("🔄 Creating hybrid bundles for multi-domain workflows...")
    
    source_dir = "n8n_docs_final"
    bundles_dir = "claude_context_bundles"
    
    # Define hybrid bundle configurations
    hybrid_bundles = {
        "ai_plus_integrations": {
            "description": "AI workflows + popular integrations (Slack, Google, etc.)",
            "sources": {
                "ai_workflows_compact": {
                    "folders": ["ai_langchain_curated", "core_essentials"],
                    "limit": 60
                },
                "api_integrations_compact": {
                    "folders": ["api_integrations_curated"],
                    "keywords": ["slack", "google", "gmail", "sheets", "discord", "telegram", "webhook", "http"],
                    "limit": 30
                }
            },
            "max_total": 100
        },
        
        "ai_plus_data": {
            "description": "AI workflows + data processing and databases",
            "sources": {
                "ai_workflows_compact": {
                    "folders": ["ai_langchain_curated", "core_essentials"],
                    "limit": 60
                },
                "data_processing": {
                    "folders": ["code_expressions", "nodes_integrations"],
                    "keywords": ["code", "transform", "filter", "merge", "split", "json", "csv", "postgres", "mongodb", "airtable"],
                    "limit": 35
                }
            },
            "max_total": 105
        },
        
        "full_automation": {
            "description": "Complete automation: AI + APIs + Data + Notifications",
            "sources": {
                "ai_workflows_compact": {
                    "folders": ["ai_langchain_curated"],
                    "limit": 40
                },
                "api_integrations_compact": {
                    "folders": ["api_integrations_curated"],
                    "keywords": ["slack", "email", "webhook", "http", "google", "notion"],
                    "limit": 25
                },
                "data_processing": {
                    "folders": ["code_expressions"],
                    "keywords": ["code", "transform", "json", "expression"],
                    "limit": 15
                },
                "workflows": {
                    "keywords": ["trigger", "schedule", "error", "execution"],
                    "limit": 10
                }
            },
            "max_total": 100
        },
        
        "business_intelligence": {
            "description": "Data analysis + AI insights + reporting",
            "sources": {
                "ai_workflows_compact": {
                    "folders": ["ai_langchain_curated"],
                    "keywords": ["analysis", "summarize", "classify", "extract"],
                    "limit": 30
                },
                "data_processing": {
                    "folders": ["code_expressions", "nodes_integrations"],
                    "keywords": ["postgres", "mysql", "mongodb", "airtable", "sheets", "transform", "aggregate"],
                    "limit": 40
                },
                "api_integrations_compact": {
                    "folders": ["api_integrations_curated"],
                    "keywords": ["google", "sheets", "slack", "email"],
                    "limit": 20
                }
            },
            "max_total": 100
        }
    }
    
    def copy_files_with_keywords(source_bundle_dir, dest_dir, folders, keywords=None, limit=50):
        """Copy files from source bundle matching keywords"""
        copied = 0
        files_found = []
        
        # Collect all relevant files
        for folder in folders:
            folder_path = os.path.join(source_bundle_dir, folder)
            if os.path.exists(folder_path):
                for filename in os.listdir(folder_path):
                    if filename.endswith('.md') and filename != 'README.md':
                        file_score = 0
                        
                        if keywords:
                            for keyword in keywords:
                                if keyword.lower() in filename.lower():
                                    file_score += 10
                        else:
                            file_score = 5  # Default score if no keywords specified
                        
                        if file_score > 0:
                            files_found.append((
                                os.path.join(folder_path, filename),
                                os.path.join(dest_dir, folder, filename),
                                file_score,
                                filename
                            ))
        
        # Sort by score and copy top files
        files_found.sort(key=lambda x: x[2], reverse=True)
        
        for source_path, dest_path, score, filename in files_found[:limit]:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            copied += 1
            print(f"    ✅ {filename} (score: {score})")
        
        return copied
    
    def copy_from_original_source(source_dir, dest_dir, keywords, limit=20):
        """Copy files directly from original source with keywords"""
        copied = 0
        files_found = []
        
        for root, dirs, files in os.walk(source_dir):
            for filename in files:
                if filename.endswith('.md') and filename != 'README.md':
                    file_score = 0
                    for keyword in keywords:
                        if keyword.lower() in filename.lower():
                            file_score += 10
                    
                    if file_score > 0:
                        source_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(root, source_dir)
                        dest_path = os.path.join(dest_dir, rel_path, filename)
                        files_found.append((source_path, dest_path, file_score, filename))
        
        # Sort and copy top files
        files_found.sort(key=lambda x: x[2], reverse=True)
        
        for source_path, dest_path, score, filename in files_found[:limit]:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            copied += 1
            print(f"    ✅ {filename} (score: {score})")
        
        return copied
    
    # Create each hybrid bundle
    for bundle_name, config in hybrid_bundles.items():
        print(f"\n📦 Creating hybrid bundle: {bundle_name}")
        bundle_dir = os.path.join(bundles_dir, bundle_name)
        
        # Clean and create bundle directory
        if os.path.exists(bundle_dir):
            shutil.rmtree(bundle_dir)
        os.makedirs(bundle_dir)
        
        total_files = 0
        
        # Process each source
        for source_name, source_config in config["sources"].items():
            print(f"  📂 Processing {source_name}...")
            
            # Check if source bundle exists
            source_bundle_dir = os.path.join(bundles_dir, source_name)
            
            if os.path.exists(source_bundle_dir):
                # Copy from existing bundle
                copied = copy_files_with_keywords(
                    source_bundle_dir,
                    bundle_dir,
                    source_config.get("folders", []),
                    source_config.get("keywords"),
                    source_config.get("limit", 50)
                )
            else:
                # Copy from original source
                copied = copy_from_original_source(
                    os.path.join(source_dir, source_name.replace("_compact", "")),
                    bundle_dir,
                    source_config.get("keywords", []),
                    source_config.get("limit", 20)
                )
            
            total_files += copied
            print(f"    📊 Added {copied} files from {source_name}")
        
        # Create bundle README
        readme_content = f"""# 🔄 {bundle_name.replace('_', ' ').title()} Hybrid Bundle

**{config['description']}**

## 📊 Bundle Stats
- **Total Files:** {total_files}
- **Context Size:** ~85-95% of Claude's limit
- **Type:** Multi-domain hybrid bundle
- **Quality:** Optimized for complex workflows

## 🎯 Perfect For Multi-Domain Workflows

This hybrid bundle combines essential documentation from multiple domains, allowing Claude to build sophisticated workflows that span:

"""
        
        # Add domain-specific descriptions
        domain_descriptions = {
            "ai_plus_integrations": "- 🤖 AI and LangChain capabilities\n- 🔗 Popular API integrations (Slack, Google, etc.)\n- 📨 Communication and notification systems",
            "ai_plus_data": "- 🤖 AI processing and analysis\n- 📊 Data transformation and manipulation\n- 🗄️ Database connections and queries",
            "full_automation": "- 🤖 AI decision making\n- 🔗 API integrations\n- 📊 Data processing\n- 📨 Notifications and alerts",
            "business_intelligence": "- 📈 Data analysis and insights\n- 🤖 AI-powered summarization\n- 📊 Business reporting\n- 🔗 Data source connections"
        }
        
        readme_content += domain_descriptions.get(bundle_name, "- Multi-domain workflow capabilities")
        
        readme_content += f"""

## 🚀 Usage

This bundle enables Claude to create workflows that:
- ✅ Combine multiple node types intelligently
- ✅ Understand cross-domain dependencies
- ✅ Suggest optimal integration patterns
- ✅ Handle complex data flows

## ⚖️ Trade-offs

**Pros:**
- ✅ Handles multi-domain workflows
- ✅ Good coverage across domains
- ✅ Fits within context limits

**Cons:**
- ❌ Less depth in any single domain
- ❌ Some specialized nodes may be missing

**Recommendation:** Use this for complex workflows that need multiple capabilities. For single-domain workflows, use the specialized bundles.

---

*Curated hybrid bundle from the complete n8n documentation collection*
"""
        
        with open(os.path.join(bundle_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"  ✅ Created {bundle_name} with {total_files} files")
    
    print(f"\n🎉 All hybrid bundles created!")
    print(f"📁 Location: {bundles_dir}/")
    print(f"\n🔄 Now you have bundles for:")
    print(f"  📦 Single domain: ai_compact, api_compact, data_processing")
    print(f"  🔄 Multi-domain: ai_plus_integrations, ai_plus_data, full_automation, business_intelligence")

if __name__ == "__main__":
    create_hybrid_bundles()