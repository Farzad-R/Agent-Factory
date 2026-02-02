# LLM Tool Management: A Practical Comparison

Managing 70+ tools for LLM agents? This project shows you what actually works.

We tested 4 approaches with GPT-4o-mini and found that **semantic retrieval beats throwing all tools at the model** - achieving better accuracy while using 82% fewer tokens.

## 🎯 The Problem

When building LLM agents, you quickly accumulate dozens of tools. Passing all 70 tools to the LLM:
- Costs 4x more per query
- Uses 3,600+ tokens just for tool schemas  
- Still fails on 18% of queries

There's got to be a better way.

## 🧪 What We Tested

1. **Naive** - Pass all 70 tools (the baseline)
2. **Category-Based** - Route to category, use ~15 tools
3. **Retrieval-Based** - ChromaDB finds top 10 relevant tools
4. **Hybrid** - Category routing + retrieval

## 📊 Results

| Approach | Accuracy | Tokens | Cost | Speed |
|----------|----------|--------|------|-------|
| Naive | 92.4% | 3,663 | $0.0064 | 2.02s |
| Category | 74.2% | 848 | $0.0017 | 1.72s |
| **Retrieval** | **93.9%** | **646** | **$0.0014** | **1.76s** |
| Hybrid | 77.3% | 564 | $0.0013 | 1.68s |

**Winner: Retrieval** - Best accuracy, 78% cheaper than naive, handles cross-category queries.

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd llm-tool-management
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key
```bash
export OPENAI_API_KEY='your-key-here'
# On Windows: set OPENAI_API_KEY=your-key-here
```

### 5. Run the comparison notebook
```bash
jupyter notebook tool_management_comparison.ipynb
```

The notebook will:
- Initialize ChromaDB with 70 e-commerce tools
- Run 11 test scenarios through all 4 approaches
- Generate comparison charts
- Export results to CSV

**Expected cost:** ~$0.01 total (using GPT-4o-mini)  
**Expected time:** 5-10 minutes

## 📁 What's Included
```
├── ecommerce_tools.py              # 70 tools with Pydantic schemas
├── tool_manager.py                 # ChromaDB integration
├── tool_management_comparison.ipynb # Main notebook
├── setup_demo.py                   # Quick demo script
├── test_system.py                  # Verify everything works
├── requirements.txt                # Dependencies
└── README.md                       # You are here
```

## 🎓 Key Findings

1. **More tools ≠ better performance**  
   Retrieval with 10 tools beat naive with 70 tools (93.9% vs 92.4%)

2. **Routing is a bottleneck**  
   Simple keyword routing failed 27% of the time

3. **Semantic search wins**  
   ChromaDB handles cross-category queries that routing can't

4. **Cost matters**  
   At scale, 78% cost reduction = real savings

## 💡 Recommendations

**Use Retrieval-Based when:**
- You want best accuracy (our winner)
- Queries span multiple categories
- You can set up ChromaDB

**Use Category-Based when:**
- Queries fit neatly into domains
- You need simple architecture
- 74% accuracy is acceptable

**Use Hybrid when:**
- You have a very accurate router
- Every token counts
- Categories are well-separated

**Avoid Naive in production** - It's expensive and not even the most accurate.

## 🛠️ Customization

### Add your own tools
Edit `ecommerce_tools.py` and add functions with Pydantic schemas:
```python
def your_tool(param: str) -> Dict[str, Any]:
    """Your tool description"""
    return {"status": "success"}

class YourToolInput(BaseModel):
    param: str = Field(description="Parameter description")
```

### Test with different models
In the notebook, change:
```python
model = "gpt-4o-mini"  # Try gpt-4o, claude-3-5-sonnet, etc.
```

### Adjust number of tools retrieved
```python
N_TOOLS_TO_RETRIEVE = 10  # Try 5, 15, 20
```

## 📈 Example Use Case

The notebook tests real e-commerce scenarios:
- Process refund + send notification
- Check stock + set alert
- Generate report + show top products
- Cross-category analytics

All with proper parallel actions (no conditional logic).

## 🐛 Troubleshooting

**"ChromaDB collection not found"**  
Run `python setup_demo.py` first to initialize the database

**"OpenAI API key not set"**  
Make sure you exported the key in your terminal

**Tests failing**  
Run `python test_system.py` to verify everything is set up correctly

## 📊 Output Files

After running the notebook:
- `tool_management_results.csv` - Detailed results
- `tool_management_summary.csv` - Aggregated metrics
- `chroma_db/` - ChromaDB database (auto-created)

## 🤝 Contributing

Found a better approach? Have more tools to test? PRs welcome!

## 📄 License

MIT License - use it however you want

## 🙏 Acknowledgments

Built to answer the question: "How do I manage 70+ tools for my LLM agent?"

Turns out: semantic search with 10 tools > naive approach with 70 tools.

---

**Questions?** Open an issue or check the notebook comments.

**Star this repo** if it helped you build better agents! ⭐