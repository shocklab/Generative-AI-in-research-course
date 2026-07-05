#!/usr/bin/env python3
import os, re, sys
import diagrams as D

ROOT = "/Users/jonathanshock/Cursor folders/Gen AI in research course/Course materials"
LA = "content/week-2/LLM Architecture Deep Dive.html"
TR = "content/week-2/Training Large Language Models.html"
FT = "content/week-2/Fine-Tuning RLHF and Alignment.html"

FIGS = [
    dict(fid="fig-w2-forward-pass", page=LA, loc=r'Transformer Architecture Fundamentals', mode="after_p",
         cap="A transformer's forward pass: text in, one next-token out — then the whole thing repeats to generate.",
         svg=D.vflow([
             ("Tokenise — split text into subword token IDs", 'neutral'),
             ("Embed — each token becomes a vector", 'accent'),
             ("Add positional encoding — mark word order", 'accent'),
             ("Stack of transformer layers — attention + feed-forward", 'accent'),
             ("Final layer norm", 'neutral'),
             ("Output projection — score every word in the vocabulary", 'accent'),
             ("Sample the next token", 'good'),
         ], "How a transformer turns text into the next token",
            "A seven-step vertical pipeline from tokenising text to sampling the next token.")),

    dict(fid="fig-w2-attention-variants", page=LA, loc=r'Attention Mechanisms in Detail', mode="after_p",
         cap="From multi-head to grouped-query attention — trading memory for a little quality, with GQA the modern compromise.",
         svg=D.columns([
             dict(title="Multi-head (MHA)", kind='alt', lines=["Each head has its own Q, K, V", "Most expressive", "Heaviest on memory"]),
             dict(title="Multi-query (MQA)", kind='neutral', lines=["Heads share one K and V", "Much lighter memory", "Small quality cost"]),
             dict(title="Grouped-query (GQA)", kind='accent', lines=["Groups share K and V", "Balance of both", "The modern default"]),
         ], "Three attention variants",
            "Multi-head, multi-query, and grouped-query attention compared by how they share keys and values.")),

    dict(fid="fig-w2-dense-vs-moe", page=LA, loc=r'Modern Architectural Innovations', mode="after_p",
         cap="Mixture-of-Experts models hold huge parameter counts but fire only a fraction per token — far more capacity per unit of compute.",
         svg=D.columns([
             dict(title="Dense", kind='alt', lines=["Every parameter runs for every token", "Simple and predictable", "All compute, all the time"]),
             dict(title="Mixture-of-Experts", kind='accent', lines=["A router picks a few experts per token", "Mixtral: 47B total, 13B active", "DeepSeek-V3: 671B total, 37B active"]),
         ], "Dense versus Mixture-of-Experts",
            "A dense model runs all parameters per token; a Mixture-of-Experts model activates only a few experts.")),

    dict(fid="fig-w2-data-pipeline", page=TR, loc=r'Training Data: Scale', mode="after_p",
         cap="The pre-training data pipeline: composition and cleaning matter as much as raw scale.",
         svg=D.vflow([
             ("Common Crawl and other raw web text", 'neutral'),
             ("Quality filtering — drop junk and spam", 'accent'),
             ("Deduplication — remove repeats", 'accent'),
             ("Tokenisation (BPE) — text into token IDs", 'accent'),
             ("Batching — feed the model", 'good'),
         ], "From raw web text to training tokens",
            "A pipeline from raw web text through filtering, deduplication, and tokenisation to training batches.")),

    dict(fid="fig-w2-scaling", page=TR, loc=r'Scaling Laws', mode="after_p",
         cap="The correction that reshaped training: balance tokens with parameters (about 20 to 1), not just bigger models. GPT-3 was undertrained.",
         svg=D.columns([
             dict(title="Kaplan (2020)", kind='alt', lines=["Scale model size for fixed data", "Bigger models, same tokens", "GPT-3: 175B params, 300B tokens"]),
             dict(title="Chinchilla (2022)", kind='accent', lines=["Scale data and size together", "About 20 tokens per parameter", "Same compute, better model"]),
         ], "The scaling shift: Kaplan to Chinchilla",
            "Two scaling recipes compared: scale model size alone, versus scale tokens and parameters together.")),

    dict(fid="fig-w2-parallelism", page=TR, loc=r'Parallelism: Training at Scale', mode="after_p",
         cap="Data, tensor, and pipeline parallelism combine — 16 × 8 × 8 = 1024 GPUs training one model.",
         svg=D.columns([
             dict(title="Data parallel", kind='alt', lines=["Split the batch across GPUs", "Each GPU holds a full copy", "16 ways in the example"]),
             dict(title="Tensor parallel", kind='accent', lines=["Split each layer's maths", "Across GPUs in a node", "8 ways"]),
             dict(title="Pipeline parallel", kind='good', lines=["Split layers into stages", "GPUs form an assembly line", "8 ways: 16×8×8 = 1024"]),
         ], "Three ways to split a model across GPUs",
            "Data, tensor, and pipeline parallelism, the three axes that distribute a model across many GPUs.")),

    dict(fid="fig-w2-rlhf", page=FT, loc=r'Reinforcement Learning from Human Feedback', mode="after_p",
         cap="RLHF in three stages — imitate good answers, learn what people prefer, then optimise toward it without drifting too far.",
         svg=D.vflow([
             ("Supervised fine-tuning on example answers", 'accent'),
             ("Train a reward model from human preferences", 'accent'),
             ("Optimise with RL (PPO), held close by a KL penalty", 'good'),
         ], "The three steps of RLHF",
            "Three stages: supervised fine-tuning, a reward model from human preferences, and reinforcement learning with a KL penalty.")),

    dict(fid="fig-w2-finetune-tree", page=FT, loc=r'Fine-Tuning for Researchers', mode="after_p",
         cap="Most research needs only prompting or a light LoRA — full fine-tuning is rarely worth the compute.",
         svg=D.tree("Adapting a model to your task", [
             dict(title="Prompt it", sub="few-shot examples", kind='good', action="Start here — no training"),
             dict(title="LoRA / PEFT", sub="some task data", kind='accent', action="Fine-tune a small model"),
             dict(title="Full fine-tune", sub="lots of data", kind='warn', action="Rarely worth the compute"),
         ], "Choosing how to adapt a model",
            "A decision tree from prompting through LoRA to full fine-tuning, by how much task data and change you need.")),
]


def dump():
    out = os.path.join(ROOT, "redesign", "_wk2_preview")
    os.makedirs(out, exist_ok=True)
    for f in FIGS:
        open(os.path.join(out, f['fid'] + ".svg"), "w", encoding="utf-8").write(f['svg'])
    print("dumped", len(FIGS))


def insert():
    for f in FIGS:
        path = os.path.join(ROOT, f['page'])
        src = open(path, encoding='utf-8').read()
        if f'id="{f["fid"]}"' in src:
            print("SKIP (present):", f['fid']); continue
        m = re.search(f['loc'], src)
        if not m:
            print("!! LOCATOR NOT FOUND:", f['fid']); continue
        if f['mode'] == 'before':
            idx = m.start()
        elif f['mode'] == 'after_p':
            c = src.find('</p>', m.end()); idx = c + 4 if c != -1 else m.end()
        else:
            idx = m.end()
        fig = f'\n<figure id="{f["fid"]}" class="diagram">{f["svg"]}<figcaption>{f["cap"]}</figcaption></figure>\n'
        open(path, 'w', encoding='utf-8').write(src[:idx] + fig + src[idx:])
        print("OK inserted:", f['fid'])


if __name__ == '__main__':
    (insert if '--insert' in sys.argv else dump)()
